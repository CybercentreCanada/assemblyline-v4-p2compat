import logging
import os

from assemblyline_v4_p2compat.common.log import init_logging
from assemblyline_v4_p2compat.common import forge


def test_logger():
    config = forge.get_config()
    config.logging.log_to_file = True
    config.logging.log_directory = '/tmp'

    init_logging("bob", config=config)
    log = logging.getLogger("assemblyline.bob")
    log.info("test")

    assert os.path.exists('/tmp/bob.log')
    assert os.path.exists('/tmp/bob.err')
