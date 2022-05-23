import sys

if 'unittest' in sys.modules.keys():
    from app.main import main as app_main
else:
    from src.app.main import main as app_main


def main(file_name):
    return app_main(file_name)
