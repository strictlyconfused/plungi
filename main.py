import os

GITHUB_TOKEN = os.environ["GITHUB_TOKEN_2"]
print(GITHUB_TOKEN)
os.system("git config --list")
