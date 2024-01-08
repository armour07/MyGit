import sys
import os

PLUIN_DIR = "a"


def test():
    global PLUIN_DIR
    PLUIN_DIR = "b"
    print(PLUIN_DIR)


if __name__ == '__main__':

    tool_path = "./" if os.path.exists("LearnEBuild") else "../"
    print(tool_path)
