import sys
import importlib

def check_system():
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}")

def check_library(library_name):
    try:
        lib = importlib.import_module(library_name)
        print(f"{library_name} version: {lib.__version__}")
        if library_name == 'torch':
            print(f"CUDA available: {lib.cuda.is_available()}")
    except ImportError:
        print(f"{library_name} is not installed")

def check_dependencies():
    check_system()
    check_library('numpy')
    check_library('torch')
    check_library('whisper')