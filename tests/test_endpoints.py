import ge.endpoints as endpoints

def test_timeseries():
	timestep = endpoints.Timestep.FIVE_MIN.value
	res = endpoints.get_timestep("4151", timestep)
	assert res.status_code == 200 