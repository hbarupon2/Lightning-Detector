"""Tests for envelope_detect"""

import numpy as np
import pytest

from lightning.dsp.envelope import envelope_detect


def make_synthetic_spike(
    duration_s: float = 2.0,
    sample_rate: int = 44100,
    spike_at_s: float = 1.0,
    spike_amplitude: float = 0.9,
) -> np.ndarray:
    """Quiet noise floor + one sharp crackle (like an AM sferic)."""
    n = int(duration_s * sample_rate)
    rng = np.random.default_rng(42)
    signal = rng.normal(0, 0.01, n).astype(np.float64)

    spike_idx = int(spike_at_s * sample_rate)
    width = 50  # samples — short burst
    burst = spike_amplitude * np.exp(-np.linspace(0, 8, width))
    signal[spike_idx : spike_idx + width] += burst

    return signal


def test_finds_single_spike():
    sample_rate = 44100
    spike_at_s = 1.0
    signal = make_synthetic_spike(spike_at_s=spike_at_s, sample_rate=sample_rate)

    peaks = envelope_detect(signal, sample_rate, threshold=0.15)

    assert len(peaks) >= 1, "Should detect at least one spike"
    # Peak should land near the injected spike (within ~20 ms)
    peak_time_s = peaks[0] / sample_rate
    assert abs(peak_time_s - spike_at_s) < 0.02, f"Expected ~{spike_at_s}s, got {peak_time_s:.3f}s"


def test_quiet_signal_no_peaks():
    sample_rate = 44100
    signal = np.zeros(int(2.0 * sample_rate))

    peaks = envelope_detect(signal, sample_rate, threshold=0.15)

    assert len(peaks) == 0


def test_rejects_multichannel():
    signal = np.zeros((2, 1000))
    with pytest.raises(ValueError, match="1-D"):
        envelope_detect(signal, 44100)
