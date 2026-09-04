"""Signal helper functions for testing."""

import numpy as np

def make_synthetic_signal(
    onset_idx: int,
    sample_rate: int,
    noise_level: float = 0.5,
) -> np.ndarray:
    """Create a synthetic signal with a spike for testing.
    """
    signal = np.zeros(sample_rate * 2)
    rng = np.random.default_rng(42)
    signal[onset_idx:] = noise_level * rng.normal(0, 1, sample_rate * 2 - onset_idx)
    return signal


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
