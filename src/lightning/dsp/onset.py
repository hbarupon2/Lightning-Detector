"""Thunder onset detection.

Finds the index of the first instance of thunder in the audio stream.
"""

from __future__ import annotations

import numpy as np


def onset_detect(
    samples: np.ndarray,
    sample_rate: int,
    threshold: float = 0.15,
    onset_window_s: float = 0.02,
) -> int | None:
    """Find the index of the first instance of thunder in the audio stream.

    Args:
        samples: 1-D array, values roughly in [-1, 1]
        sample_rate: Hz (e.g. 44100)
        threshold: envelope level that counts as a strike

    Returns:
        Index of the first instance of thunder in the audio stream, or None if no thunder was detected
    """
    if samples.ndim != 1:
        raise ValueError("samples must be 1-D")

    # First we rectify the samples.
    # AC signals have negative and positive values, so we take the absolute value to get a signal that is always positive.
    samples = np.abs(samples)

    # Next, we apply a moving average filter to the samples.
    # This is a simple filter that averages the samples over a window of time.
    # The window size is determined by the envelope_window_s parameter.
    # This is needed to smooth out the signal and remove noise/instantaneous spikes.
    window_samples = max(1, int(onset_window_s * sample_rate))
    window_samples = min(window_samples, samples.shape[0])
    envelope = np.convolve(samples, np.ones(window_samples) / window_samples, mode='same')

    # Finally, we find the index of the first instance of thunder in the audio stream.
    indices = np.where(envelope > threshold)[0]
    if len(indices) == 0:
        return None
    return indices[0]
