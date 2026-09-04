"""Generalized Cross-Correlation with Phase Transform (GCC-PHAT)

Uses uses differences in thunder arrivales between microphones to estimate
the bearing.
"""

from __future__ import annotations

import numpy as np


def gcc_phat(
    signal1: np.ndarray,
    signal2: np.ndarray,
) -> float:
    """Calculate the GCC-PHAT between two signals.
    """

    if signal1.ndim != 1 or signal2.ndim != 1:
        raise ValueError("Signals must be 1-dimensional")

    n = len(signal1) + len(signal2)

    spec1 = np.fft.rfft(signal1, n=n)
    spec2 = np.fft.rfft(signal2, n=n)

    cc = spec1 * np.conj(spec2)
    cc /= np.abs(cc) + 1e-15

    corr = np.fft.irfft(cc, n=n)

    peak = int(np.argmax(np.abs(corr)))

    if peak > n // 2:
        peak -= n

    return peak
