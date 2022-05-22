import subprocess
import sys


def build_module():
    print("Installing local module ce2-0.0.0...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", "."],
                          stdout=subprocess.DEVNULL)
    print("Installed ce2-0.0.0")


try:
    from app.main import main as app_main
except:
    print('REQUIRED: Local module ce2 is not installed!')
    build_module()
    from app.main import main as app_main


def main(file_name):
    return app_main(file_name)
