from ligotools import utils as ut
from ligotools import readligo as rl
import numpy as np
import pytest

@pytest.fixture(autouse=True)
def change_test_dir(request, monkeypatch):
    monkeypatch.chdir(request.fspath.dirname)

@pytest.fixture
def load_test_data() :
	rl.loaddata("testdata/H-H1_LOSC_4_V2-1126259446-32.hdf5")

def test_reqshift() :
	x = np.random.randn(131072)
	assert (x.shape == ut.reqshift(x).shape)

def test_numbers() :
	assert (2022 == 2022)