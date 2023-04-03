import sys
from os import environ
import os

def show_files():
    path = environ.get('PATH')

    if len(sys.argv) > 1:
        dir = sys.argv[1]
        print(dir)
        print("zad 2 b --------------------------------")

        if os.path.isdir(dir):
            files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))
                     and os.access(os.path.join(dir, f), os.X_OK)]
            print(dir)

            for file in files:
                print("\t" + file)
            print()

        else:
            print("The arguemnt is not a directory!")
    else:
        paths = path.split(os.pathsep)
        print("zad 2 a --------------------------------")

        for path in paths:

            if path != "":
                print(path)
                files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))
                         and os.access(os.path.join(path, f), os.X_OK)]

                for file in files:
                    print("\t" + file)
                print()


if __name__ == "__main__":
    show_files()