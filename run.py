from cProfile import run
import os
import sys

sys.path.insert(0, os.path.join(os.getcwd(), 'frontend'))
sys.path.insert(1, os.path.join(os.getcwd(), 'backend'))

# Execute the application
def run_app():
    from backend.core.start import launch_app
    launch_app()

if __name__ == '__main__':
    run_app()