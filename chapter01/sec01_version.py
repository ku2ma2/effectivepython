"""
sysモジュールから Pythonバージョンを取得

# python version.py
"""
import sys


def print_version():
    """
    Pythonバージョンを出力
    """
    print(sys.version_info)
    print(sys.version)


if __name__ == "__main__":
    print_version()
