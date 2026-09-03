"""RF sferic envelope detection.

Lightning produces a sharp EM pulse. On an AM radio you hear it as a crackle.
This module finds those spikes in a mono audio stream.
"""

from __future__ import annotations

import numpy as np


def envelope_detect(
    samples: np.ndarray,
    sample_rate: int,
    threshold: float = 0.15,
    envelope_window_s: float = 0.0009,
) -> np.ndarray:
    """Find spike times in a mono float32/float64 signal.

    Args:
        samples: 1-D array, values roughly in [-1, 1]
        sample_rate: Hz (e.g. 44100)
        threshold: envelope level that counts as a strike
        envelope_window_s: window size seconds for the moving average filter

    Returns:
        1-D array of sample indices where spikes were detected
    """
    if samples.ndim != 1:
        raise ValueError("samples must be 1-D")


    """First we rectify the samples. 
    AC signals have negative and positive values, so we take the absolute value to get a signal that is always positive.
    """
    samples = np.abs(samples)

    """Next, we apply a moving average filter to the samples.
    This is a simple filter that averages the samples over a window of time.
    The window size is determined by the envelope_window_s parameter.
    This is needed to smooth out the signal and remove noise/instantaneous spikes.
    """
    window_samples = max(1, int(envelope_window_s * sample_rate))
    window_samples = min(window_samples, samples.shape[0])
    envelope = np.convolve(samples, np.ones(window_samples) / window_samples, mode='same')

    """Finally, we find the indices where the envelope exceeds the threshold.
    """
    indices = np.where(envelope > threshold)[0]
    return indices