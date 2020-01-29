import re
from assemblyline_v4_p2compat.common import isotime


def test_epoch():
    epoch = isotime.now()

    assert isinstance(epoch, float)
    assert int(isotime.local_to_epoch(isotime.iso_to_local(isotime.epoch_to_iso(epoch)))) == int(epoch)


def test_local():
    local_format = re.compile(r'[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{6}.*')

    local = isotime.now_as_local()

    assert isinstance(local, str)
    assert local_format.match(local)
    assert isotime.epoch_to_local(isotime.local_to_epoch(local)) == local


def test_iso():
    now = isotime.now_as_iso()

    iso_format = re.compile(r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{6}Z')

    assert isinstance(now, str)
    assert iso_format.match(now)
    assert isotime.epoch_to_iso(isotime.iso_to_epoch(now)) == now


