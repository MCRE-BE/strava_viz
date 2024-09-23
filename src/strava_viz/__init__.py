# module level doc-string
# isort: skip_file
__version__ = "0.0.1"
__doc__ = """
Welcome to Strava_viz API Documentation !
=========================================

The API documentation is built automatically using sphinx and a couple
of different extensions. Please read carefully the settings in docs
Each module is described at all stages.

See Also
--------
The package uses lazy loading to speed up the loading process and only
load the needed information. See info : https://peps.python.org/pep-0562/
"""

import importlib
import logging
from environs import Env

env = Env()
env.read_env()  # Read current .env
