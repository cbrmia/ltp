import argparse, sys
from MyApp import MyApp


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', help='4-letters name')
    return parser.parse_args(args)

def main(parsed_args):
    if parsed_args.name and len(parsed_args.name) > 4:
        sys.exit('Name too long')

    app = MyApp(parsed_args.name) if parsed_args.name else MyApp()
    return app

if __name__ == '__main__':
    parsed = parse_args(sys.argv[1:])
    print(main(parsed))
