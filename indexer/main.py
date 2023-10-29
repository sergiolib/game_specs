from indexer import Indexer
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("db_host")
parser.add_argument("db_user")
parser.add_argument("db_password")
parser.add_argument("db_name")
parser.add_argument("db_port")

if __name__ == "__main__":
    args = parser.parse_args()
    indexer = Indexer(args.db_host, args.db_user, args.db_password, args.db_name, args.db_port)
    indexer.run(".")
