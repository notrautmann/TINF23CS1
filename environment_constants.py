"""Collection of relevant environment constants (e.g. relevant paths)
    """
from pathlib import Path

PROJECT_ROOT = Path(".")
"""Path to the project root
"""

API_BLUEPRINTS_PATH = Path.joinpath(PROJECT_ROOT, "app/api/blueprints")
"""Path to the API blueprints
"""
