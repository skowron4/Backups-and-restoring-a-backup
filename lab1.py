import sys
from os import environ


def show_Environment_Variables(env_vars):

    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            env_vars = [var for var in env_vars if arg in var[0]]
    for var in env_vars:
        print(var[0], var[1])
        print()

if __name__ == "__main__":
    show_Environment_Variables(sorted(environ.items()))