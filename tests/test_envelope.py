"""Tests for envelope_detect"""

import numpy as np
import pytest

from lightning.dsp.envelope import envelope_detect
from tests.fixtures.signals import make_synthetic_spike


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
