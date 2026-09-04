"""Tests for onset_detect"""

import numpy as np
import pytest

from lightning.dsp.onset import onset_detect
from tests.fixtures.signals import make_synthetic_signal

def test_onset_detect_with_spike():
    """Test that the onset detect is working as expected with simulated thunder.
    """
    sample_rate = 44100
    signal = make_synthetic_signal(onset_idx=sample_rate, sample_rate=sample_rate, noise_level=0.5)
    onset_idx = onset_detect(signal, sample_rate, threshold=0.15)
    onset_time = onset_idx / sample_rate
    assert onset_time > 0.5
    assert onset_time < 1.5

def test_onset_detect_with_silence():
    """Test that the onset detect is working as expected with a silent signal.
    """
    sample_rate = 44100
    signal = np.zeros(sample_rate * 2)
    onset_time = onset_detect(signal, sample_rate, threshold=0.15)
    assert onset_time is None