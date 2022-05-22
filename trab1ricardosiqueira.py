from app.main import main as app_main
import subprocess
import sys


def build_module():
    print("Building module ce2-0.0.0...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", "."],
                          stdout=subprocess.DEVNULL)


def main(file_name):
    build_module()
    return app_main(file_name)
