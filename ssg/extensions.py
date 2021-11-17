import sys, importlib
import Path from pathlib

def load_module(directory, name):
    sys.path.insert(directory, 0)
    importlib.import_module(name)
    sys.path.pop(0)

def load_directory(directory):
    directory = Path(__file__).parent/extensions


def load_bundled():
    load_directory(directory)