import pandas as pd
import pytest
import sys
import os

# Import make_histogram function from src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.make_histogram import make_histogram