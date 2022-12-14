import sys
import os
from time import sleep
from github import Github


def listen_for_updates():
    g = Github()
    path = sys.argv[1]
    port = sys.argv[2]
    repo = g.get_repo("KaitoKunTatsu/KMesRework")
    last_commit_counter = repo.get_commits().totalCount
    path_to_this_dir = os.path.dirname(os.path.abspath(__file__))
    os.system(f'bash {path_to_this_dir}/kmes_updater.sh {path} {port}')

    while True:
        sleep(180)
        repo = g.get_repo("KaitoKunTatsu/KMesRework")
        print("Checking for updates...")
        if repo.get_commits().totalCount > last_commit_counter:
            last_commit_counter = repo.get_commits().totalCount
            os.system(f'bash {path_to_this_dir}/kmes_updater.sh {path} {port}')
        else:
            print("Already up to date")


if __name__ == '__main__':
    listen_for_updates()
