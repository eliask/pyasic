# ------------------------------------------------------------------------------
#  Copyright 2022 Upstream Data Inc                                            -
#                                                                              -
#  Licensed under the Apache License, Version 2.0 (the "License");             -
#  you may not use this file except in compliance with the License.            -
#  You may obtain a copy of the License at                                     -
#                                                                              -
#      http://www.apache.org/licenses/LICENSE-2.0                              -
#                                                                              -
#  Unless required by applicable law or agreed to in writing, software         -
#  distributed under the License is distributed on an "AS IS" BASIS,           -
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.    -
#  See the License for the specific language governing permissions and         -
#  limitations under the License.                                              -
# ------------------------------------------------------------------------------

import logging

from pyasic.settings import PyasicSettings


def init_logger():
    if PyasicSettings().logfile:
        logging.basicConfig(
            filename="logfile.txt",
            filemode="a",
            format="%(pathname)s:%(lineno)d in %(funcName)s\n[%(levelname)s][%(asctime)s](%(name)s) - %(message)s",
            datefmt="%x %X",
        )
    else:
        logging.basicConfig(
            format="%(pathname)s:%(lineno)d in %(funcName)s\n[%(levelname)s][%(asctime)s](%(name)s) - %(message)s",
            datefmt="%x %X",
        )

    _logger = logging.getLogger()

    if PyasicSettings().debug:
        _logger.setLevel(logging.DEBUG)
        logging.getLogger("asyncssh").setLevel(logging.DEBUG)
    else:
        _logger.setLevel(logging.WARNING)
        logging.getLogger("asyncssh").setLevel(logging.WARNING)

    return _logger


logger = init_logger()
