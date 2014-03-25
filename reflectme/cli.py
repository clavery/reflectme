import argparse
import os
from os import path
from appdirs import user_data_dir

from reflectme.app import create_app

def main(argv=None, prog=None, **kwargs):
    """reflectme main entry point"""

    database_location = path.join(user_data_dir('reflectme', 'clavery'), 'database.db')

    parser = argparse.ArgumentParser(description='Create an HTTP server to record and\
                                     respond to requests.')
    parser.add_argument('host', type=str, default='0.0.0.0', nargs='?',
                        help='host to listen on')
    parser.add_argument('port', type=int, default=5000, nargs='?',
                        help='host to listen on')
    parser.add_argument('--database', dest='database', help='sqlite database location (default: {0})'
                        .format(database_location), type=str, default=database_location)
    args = parser.parse_args()

    norm_path = path.abspath(args.database)
    if not path.exists(path.dirname(norm_path)):
        os.makedirs(path.dirname(norm_path))

    app = create_app(database=norm_path)
    app.run(host=args.host, port=args.port)

if __name__ == '__main__':
    main()
