from assemblyline_v4_p2compat.common import forge


def test_get_config():

    config = forge.get_config()
    assert 'logging' in config
