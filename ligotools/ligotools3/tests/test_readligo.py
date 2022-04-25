from ligotools import readligo as rl
import pytest

@pytest.fixture(autouse=True)
def change_test_dir(request, monkeypatch):
    monkeypatch.chdir(request.fspath.dirname)

def test_load_data() :
	try :
		rl.loaddata("testdata/H-H1_LOSC_4_V2-1126259446-32.hdf5")
	except Exception as e:
		assert (0 == e)
	assert (1 == 1)

def test_read_hdf5() :
	try :
		rl.read_hdf5("testdata/H-H1_LOSC_4_V2-1126259446-32.hdf5")
	except Exception as e:
		assert (0 == e)
	assert (1 == 1)

def test_dq_channel_to_seglist() :
	try : 
		a, b, c = rl.loaddata("testdata/H-H1_LOSC_4_V2-1126259446-32.hdf5")
		rl.dq_channel_to_seglist(c)
	except Exception as e :
		assert(0 == e)
	assert (1 == 1)