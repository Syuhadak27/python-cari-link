from os import path
from subprocess import run as srun

UPSTREAM_REPO = "https://github.com/Syuhadak27/python-cari-link"
UPSTREAM_BRANCH = "update"

# Clone atau reset repo dari GitHub
if path.exists(".git"):
    srun(["rm", "-rf", ".git"])

update = srun(
    [
        f"git init -q \
         && git config --global user.email support@zee-mirror.in \
         && git config --global user.name zee \
         && git add . \
         && git commit -sm update -q \
         && git remote add origin {UPSTREAM_REPO} \
         && git fetch origin -q \
         && git reset --hard origin/{UPSTREAM_BRANCH} -q"
    ],
    shell=True,
)

if update.returncode == 0:
    print("Successfully updated...")
else:
    print("Error while getting latest updates. Check if UPSTREAM_REPO is valid!")