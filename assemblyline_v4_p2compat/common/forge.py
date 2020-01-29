# This file contains the loaders for the different components of the system
import easydict
import os
import yaml

from assemblyline_v4_p2compat.common.dict_utils import recursive_update


def get_config():
    yml_config = "/etc/assemblyline/config.yml"

    # Initialize a default config
    config = {
        "logging": {
            'log_level': 'INFO',
            'log_to_console': True,
            'log_to_file': False,
            'log_directory': '/var/log/assemblyline/',
            'log_to_syslog': False,
            'syslog_host': 'localhost',
            'export_interval': 5,
            'log_as_json': True
        }
    }

    # Load modifiers from the yaml config
    if os.path.exists(yml_config):
        with open(yml_config) as yml_fh:
            yml_data = yaml.safe_load(yml_fh.read())
            if yml_data:
                config = recursive_update(config, yml_data)

    if 'AL_LOG_LEVEL' in os.environ:
        config['logging']['log_level'] = os.environ['AL_LOG_LEVEL']

    return easydict.EasyDict(config)
