import socket
import subprocess
import sys

import netifaces as nif


def get_hostname():
    return socket.gethostname()


def get_hostip():
    return get_default_gateway_ip()


def get_default_gateway_ip():
    # fetch the nic serving up the default gateway
    if_default = nif.gateways().get('default')
    (ip, nic) = if_default.get(nif.AF_INET)
    # Fetch the IP of that nic
    try:
        ip = nif.ifaddresses(nic).get(nif.AF_INET)[0].get('addr')
    except (IndexError, KeyError):
        subnet = ip.split(".")[0]
        if sys.platform.startswith('win'):
            proc = subprocess.Popen('ipconfig', stdout=subprocess.PIPE)
            output = proc.stdout.read()
            for line in output.split('\n'):
                if "IP Address" in line and ": %s" % subnet in line:
                    ip = line.split(": ")[1].replace('\r', '')
                    break

        else:
            proc = subprocess.Popen('ifconfig', stdout=subprocess.PIPE)
            output = proc.stdout.read()

            for line in output.split('\n'):
                if "addr:%s" % subnet in line:
                    ip = line.split("addr:")[1].split(" ")[0]
                    break

    return ip
