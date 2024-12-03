import os
import subprocess
import logging
from .config import Config
import mkpj.ansi_colors as ansi_colors

TEMPLATES_REPO = Config.GIT_REMOTE_REPO
TEMPLATES_DIR = os.path.expanduser(Config.ROOT_FOLDER_NAME + "/templates")

def update_templates():
    """goes to root folder and pulls the latest version of the templates"""
    logging.info(f"{ansi_colors.AnsiColors.CYAN}Updating templates...{ansi_colors.AnsiColors.RESET}")
    if not os.path.exists(TEMPLATES_DIR):
        # error if the templates folder does not exist, the installation is probably incomplete
        logging.error(f"{ansi_colors.AnsiColors.RED}Templates folder not found. Did you install mkpjp properly?{ansi_colors.AnsiColors.RESET}")
    else:
        os.chdir(TEMPLATES_DIR)
        result = subprocess.run(["git", "pull"], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info(f"{ansi_colors.AnsiColors.GREEN}Templates successfully updated.{ansi_colors.AnsiColors.RESET}")
            print(f"{ansi_colors.AnsiColors.GREEN}Templates successfully updated.{ansi_colors.AnsiColors.RESET}")
        else:
            logging.error(f"{ansi_colors.AnsiColors.RED}Failed to update templates.{ansi_colors.AnsiColors.RESET}")
    logging.info("Templates updated.")