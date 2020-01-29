
hostname = 'unknownhost'
# noinspection PyBroadException
try:
    from assemblyline_v4_p2compat.common.net import get_hostname
    hostname = get_hostname()
except Exception:
    pass

ip = 'x.x.x.x'
# noinspection PyBroadException
try:
    from assemblyline_v4_p2compat.common.net import get_hostip
    ip = get_hostip()
except Exception:
    pass

AL_SYSLOG_FORMAT = '{ip} AL %(levelname)8s %(process)5d %(name)20s | %(message)s'.format(ip=ip)
AL_LOG_FORMAT = '%(asctime)-16s %(levelname)8s {hostname} %(process)d %(name)30s | %(message)s'.format(
    hostname=hostname)
AL_JSON_FORMAT = '{{' \
    '"@timestamp": "%(asctime)s", ' \
    '"event.module": "assemblyline", ' \
    '"event.dataset": "%(name)s", ' \
    '"host.ip": "{ip}", ' \
    '"host.hostname": "{hostname}", ' \
    '"log.level": "%(levelname)s", ' \
    '"log.logger": "%(name)s", ' \
    '"process.pid": "%(process)d", ' \
    '"message": %(message)s}}'.format(ip=ip, hostname=hostname)
