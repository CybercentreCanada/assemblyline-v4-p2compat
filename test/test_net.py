from assemblyline_v4_p2compat.common import net


def test_get_ip():
    ip = net.get_hostip()

    assert isinstance(ip, basestring)


def test_get_hostname():
    hostname = net.get_hostname()

    assert isinstance(hostname, basestring)
