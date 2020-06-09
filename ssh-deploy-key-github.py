import os
import sys
import argparse
from dotenv import load_dotenv
from github import Github

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--pulic-key",
        type=str,
        dest="public_key",
        default=None,
        required=True,
        help="deploy this ssh public key FILE",
    )
    parser.add_argument(
        "-r",
        "--repo",
        type=str,
        default=None,
        required=True,
        help="add ssh deploy key to this target github repo",
    )
    parser.add_argument(
        "-u",
        "--user",
        type=str,
        default="alta3",
        help="target repos owner (org or user)",
    )
    parser.set_defaults(stdout=False, annotate=False)
    return parser.parse_args()

if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("GITHUB_USER_TOKEN")


    if token == None or token == "":
       sys.stderr.write("GITHUB_USER_TOKEN not provided. Exiting!\n")
       sys.exit(1)
    

    args = parse_args()
    # TODO: handle auth/org/repo exceptions
    g = Github(token)
    username = g.get_user().name
    alta3 = g.get_organization(args.user)
    repo = alta3.get_repo(args.repo)


    #TODO: handle file exceptions
    with open(args.public_key) as f:
        # TODO: validate public key format
        public_key = f.read()
        key_title = f"{username}_api-added-deploy-key"
        read_only = True
        
        # TODO: check if public key is already installled as deploy key
        
        # TODO: handle public key adding exceptions
        repo.create_key(
            title = key_title,
            key = public_key,
            read_only = read_only,
        )

    print(f"{username} modifying {repo.full_name}")
    for k in repo.get_keys():
        print(f"\ttitle={k.title} read_only={k.read_only}")
