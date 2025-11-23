"""
Módulo de configuración del proyecto
"""

from .colors import SPOTIFY, CATEGORICAL, EXPLICIT, get_palette
from .settings import (
    IMAGES_DIR, 
    INTERACTIVE_DIR, 
    CLEAN_DATA_FILE,
    RAW_DATA_FILE,
    MESSAGES,
    MPL_CONFIG
)

__all__ = [
    'SPOTIFY',
    'CATEGORICAL', 
    'EXPLICIT',
    'get_palette',
    'IMAGES_DIR',
    'INTERACTIVE_DIR',
    'CLEAN_DATA_FILE',
    'RAW_DATA_FILE',
    'MESSAGES',
    'MPL_CONFIG'
]