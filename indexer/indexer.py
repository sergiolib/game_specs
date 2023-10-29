import json
import os
import git

from db import IndexerDatabase


class Indexer:
    def __init__(self, db_host, db_user, db_password, db_name, db_port):
        self.db = IndexerDatabase(db_host, db_user, db_password, db_name, db_port, "game_specs")

    def run(self, directory):
        files = self.get_files("json")
        print(files)
        for f in files:
            content = self.read_file(f)
            self.index(f, content)

    def get_files(self, extension):
        contents = os.listdir()
        contents = list(filter(lambda x: x.endswith(extension), contents))
        return contents

    def read_file(self, file_name):
        with open(file_name, "r") as f:
            contents = f.read()
            return contents

    def index(self, file_name, file_contents):
        game_specs = json.loads(file_contents)
        last_commit = get_last_commit_from_file(file_name)
        self.db.insert(
            {
                "original_file_name": file_name,
                "version": last_commit,
                "name": game_specs["name"],
            }
        )

    def get_last_commit_from_file(self, file_path):
        repo = git.Repo(".")
        commits = list(repo.iter_commits(paths=file_path, max_count=1))

        if commits:
            latest_commit = commits[0]
            commit_hash = latest_commit.hexsha
            print(f"Latest commit hash for {file_path}: {commit_hash}")
        else:
            print(f"No commits found for {file_path}")

