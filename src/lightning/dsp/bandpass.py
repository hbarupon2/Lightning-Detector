"""Bandpass filter for audio signals.

Microphones will pickup a wide range of frequencies,
but we only care about the frequencies in the range of thunder rumbles,
so we can apply a bandpass filter to the signal to remove the frequencies outside of the range.
"""

from __future__ import annotations

import numpy as np

def bandpass_filter(
    samples: np.ndarray,
    sample_rate: int,
    low_hz: float,
    high_hz: float,
) -> np.ndarray:
    """Apply a bandpass filter to the signal.

    Args:
        samples: 1-D array, values roughly in [-1, 1]
        sample_rate: Hz (e.g. 44100)
        low_hz: low frequency cutoff in Hz
        high_hz: high frequency cutoff in Hz

    Returns:
        1-D array of filtered samples
    """
    if samples.ndim != 1:
        raise ValueError("samples must be 1-D")

    raise NotImplementedError("Not implemented yet")