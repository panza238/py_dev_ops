"""
Simple script to show how the molotov library works.
This is a minimal example of how molotov works.
"""
from molotov import scenario

BASE_API_URL = "http://worldtimeapi.org/"


@scenario(weight=80)
async def _test1(session):
    """Success load test scenario definition"""
    async with session.get(BASE_API_URL) as resp:
        assert resp.status == 200, resp.status


# Let's write a test that fails
@scenario(weight=20)
async def _test2(session):
    """Failure load test scenario definition"""
    async with session.get(BASE_API_URL) as resp:
        assert resp.status == 201, resp.status
        # By asserting == 201, the test will fail. This is because the server will respond with 200 (as in _test1)
