import os
import sys
from backend.core.api import launch

sys.path.insert(0, os.path.join(os.getcwd(), 'frontend'))
sys.path.insert(1, os.path.join(os.getcwd(), 'backend'))

if __name__ == '__main__':
    launch()