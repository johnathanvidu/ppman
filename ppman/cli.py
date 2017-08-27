import sys


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    print('entry point - it worked')

if __name__ == "__main__":
    sys.exit(main())
