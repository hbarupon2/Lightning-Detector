"""Tests for bandpass_filter"""

import numpy as np
import pytest

from lightning.dsp.bandpass import bandpass_filter

def test_bandpass_filter():
    """Test that the bandpass filter is working as expected.
    """

    # We start by creating a signal that contants two tones, one at 100 Hz and one at 500 Hz.
    sample_rate = 44100
    n = sample_rate # 1 second of audio
    t = np.arange(n) / sample_rate
    tone_100 = np.sin(2 * np.pi * 100 * t)
    tone_500 = np.sin(2 * np.pi * 500 * t)
    signal = tone_100 + tone_500

    # We then apply the bandpass filter to the signal and check that the energy of the 100 Hz tone is greater than 0.4
    # and the energy of the 500 Hz tone is less than 0.01.
    filtered = bandpass_filter(signal, sample_rate, low_hz=20, high_hz=300)
    energy_100 = np.mean(filtered * tone_100)
    energy_500 = np.mean(filtered * tone_500)
    assert energy_100 > 0.4
    assert energy_500 < 0.01