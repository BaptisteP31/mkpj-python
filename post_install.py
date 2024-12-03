import os
import subprocess
import sys
from setuptools.command.install import install

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        self._post_install()

    def _post_install(self):
        config_dir = os.path.expanduser("~/.mkpjp")
        git_repo = "https://github.com/BaptisteP31/mkpj-python-templates.git"

        if not os.path.exists(config_dir):
            os.makedirs(config_dir)

        if not self._is_git_installed():
            print("Git is not installed. Please install Git and try again.")
            sys.exit(1)

        self._clone_repo(git_repo, config_dir)

    def _is_git_installed(self):
        try:
            subprocess.run(["git", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True
        except subprocess.CalledProcessError:
            return False

    def _clone_repo(self, repo_url, clone_dir):
        if not os.path.exists(os.path.join(clone_dir, ".git")):
            subprocess.run(["git", "clone", repo_url, clone_dir], check=True)
        else:
            subprocess.run(["git", "-C", clone_dir, "pull"], check=True)