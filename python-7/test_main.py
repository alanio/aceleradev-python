import main

def get_temperature_substitute_function(lat, lng):
    return 16


def test_get_temperature_by_lat_lng(monkeypatch):

    lat = -14.235004
    lng = -51.92528
    expected = 16

    monkeypatch.setattr(main, 'get_temperature', get_temperature_substitute_function)
    assert main.get_temperature(lat, lng) == expected
