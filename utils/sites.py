"""Sites helper."""

import os

from . import util
from .config import ConfigHelper

class Sites(ConfigHelper):
    """Sites helper."""
    def __init__(self):
        """
        Constructor
        """
        # Determine sites location
        location = os.path.join(util.get_project_path(), 'config', 'sites.json')

        super().__init__(location=location)