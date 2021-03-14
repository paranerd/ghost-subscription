"""Cache helper."""

import os

from . import util
from .config import ConfigHelper

class Cache(ConfigHelper):
    """Cache helper."""
    def __init__(self):
        """
        Constructor
        """
        # Determine cache location
        location = os.path.join(util.get_project_path(), 'config', 'cache.json')

        super().__init__(location=location)