import os
import sys

# Add root directory to system path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_DIR = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
sys.path.append(SOURCE_DIR)
