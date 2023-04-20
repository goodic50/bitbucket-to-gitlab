import requests
import os

GITLAB_TOKEN = os.getenv("GITLAB_TOKEN") 

BITBUCKET_SERVER_URL = os.getenv("BITBUCKET_SERVER_URL")
BITBUCKET_SERVER_USERNAME = os.getenv("BITBUCKET_SERVER_USERNAME")
PERSONAL_ACCESS_TOKEN = os.getenv("PERSONAL_ACCESS_TOKEN")
BITBUCKET_SERVER_PROJECT = os.getenv("BITBUCKET_SERVER_PROJECT")
BITBUCKET_SERVER_REPO = os.getenv("BITBUCKET_SERVER_REPO")

NEW_NAME = os.getenv("NEW_NAME")
PREFIX = os.getenv("PREFIX")
LAYER = os.getenv("LAYER")
TEAM = os.getenv("TEAM")
PROJECT = os.getenv("PROJECT")

GITLAB_DOMAIN = os.getenv("GITLAB_DOMAIN")

target_namespace = f"{PREFIX}/{LAYER}/{TEAM}/{PROJECT}"
project_path = f"{target_namespace}/{NEW_NAME}"

# --------------------------------------------------- sync repos ---------------------------------------------------

headers = {
    "content-type" : "application/json",
    "PRIVATE-TOKEN": GITLAB_TOKEN
}


data = {
    "bitbucket_server_url": BITBUCKET_SERVER_URL,
    "bitbucket_server_username": BITBUCKET_SERVER_USERNAME,
    "personal_access_token": PERSONAL_ACCESS_TOKEN,
    "bitbucket_server_project": BITBUCKET_SERVER_PROJECT,
    "bitbucket_server_repo": BITBUCKET_SERVER_REPO,
    "new_name": NEW_NAME,
    "target_namespace": target_namespace,
}

url = f"https://{GITLAB_DOMAIN}/api/v4/import/bitbucket_server"

response = requests.post(url=url, headers=headers, json=data)

if response.status_code != 201:
    print("Error sync bitbucket repo")
    print("Status Code", response.status_code)
    print("JSON Response ", response.json())
    exit(1)


