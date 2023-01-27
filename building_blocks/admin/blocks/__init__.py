"""
Admin blocks hold values for django admin fields for various models. As we follow a compositions model for defining our
data models, we have created a parallel system to build django admin panels for the composition models. Optimized for
mixing, matching and combining django admin config for various models.
"""

from .base import *
from .extra import *
