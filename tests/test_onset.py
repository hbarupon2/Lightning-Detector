"""Tests for onset_detect"""

import numpy as np
import pytest

from lightning.dsp.onset import onset_detect

def make_synthetic_signal(onset_idx: int, sample_rate: int):
    """Create a synthetic signal with a spike for testing.
    """
    signal = np.zeros(sample_rate * 2)
    rng = np.random.default_rng(42)
    signal[onset_idx:] = 0.5 * rng.normal(0, 1, sample_rate * 2 - onset_idx)
    return signal


def test_onset_detect_with_spike():
    """Test that the onset detect is working as expected with simulated thunder.
    """
    sample_rate = 44100
    signal = make_synthetic_signal(onset_idx=sample_rate, sample_rate=sample_rate)
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