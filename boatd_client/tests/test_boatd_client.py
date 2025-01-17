from httpretty import HTTPretty, httprettified

from boatd_client import Boat

@httprettified
class TestBoatdClient(object):
    def setup(self):
        self.boat = Boat()

    def test_root(self):
        HTTPretty.register_uri(HTTPretty.GET, 'http://localhost:2222/',
                               body='{"boatd": {"version": "0.1mock"}}')
        assert self.boat.version

    def test_heading(self):
        HTTPretty.register_uri(HTTPretty.GET, 'http://localhost:2222/heading',
                               body='{"result": 2.43}')
        assert self.boat.heading == 2.43

    def test_wind(self):
        HTTPretty.register_uri(HTTPretty.GET, 'http://localhost:2222/wind',
                               body='{"direction": 8.42}')
        assert self.boat.wind.direction == 8.42
