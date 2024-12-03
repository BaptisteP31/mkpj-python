import os
import subprocess
import logging

TEMPLATES_REPO = "https://github.com/ton-username/create-project-templates"
TEMPLATES_DIR = os.path.expanduser("~/.create-project/templates")

def update_templates():
    """Update the templates repository."""
    if not os.path.exists(TEMPLATES_DIR):
        logging.info("Cloning templates repository...")
        subprocess.run(["git", "clone", TEMPLATES_REPO, TEMPLATES_DIR], check=True)
    else:
        logging.info("Updating templates...")
        subprocess.run(["git", "-C", TEMPLATES_DIR, "pull"], check=True)