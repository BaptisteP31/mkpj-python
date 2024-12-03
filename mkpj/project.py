import os
import logging
import mkpj.ansi_colors as ansi_colors
import shutil
from .config import Config

TEMPLATES_DIR = os.path.expanduser(Config.ROOT_FOLDER_NAME + "/templates")

def create_project(name, build_system, license_type):
    """Create a new project with the given name, build system, and license type."""
    try:
        project_path = os.path.join(os.getcwd(), name)
        
        # Check if project directory already exists
        if os.path.exists(project_path):
            logging.warning(f"Project directory {project_path} already exists. Skipping project creation.")
            print(f"\n{ansi_colors.AnsiColors.RED}A directory with the name \"{name}\" already exists. Skipping project creation.{ansi_colors.AnsiColors.RESET}")
            return False
        
        os.makedirs(os.path.join(project_path, "src"), exist_ok=True)
        os.makedirs(os.path.join(project_path, "include"), exist_ok=True)
        
        # Copy the file structure of the template project
        template_project_path = os.path.join(TEMPLATES_DIR, Config.PROJECT_TEMPLATE_FOLDER_NAME)
        if os.path.exists(template_project_path):
            # Copy the template project to the new project directory
            for item in os.listdir(template_project_path):
                logging.info(f"Copying {item}...")
                s = os.path.join(template_project_path, item)
                d = os.path.join(project_path, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, dirs_exist_ok=True)
                else:
                    shutil.copy2(s, d)
            logging.info(f"Copied template project to project directory.")
        else:
            logging.warning(f"Template project directory {template_project_path} does not exist.")
            return False

        # Copy the build system template
        template_file = os.path.join(TEMPLATES_DIR, Config.BUILD_FOLDER_NAME, build_system, "CMakeLists.txt" if build_system == "cmake" else "Makefile")
        if os.path.exists(template_file):
            # Read template file and replace project name
            with open(template_file) as f:
                content = f.read().replace("{{PROJECT_NAME}}", name)
            # Write to project directory
            with open(os.path.join(project_path, "CMakeLists.txt" if build_system == "cmake" else "Makefile"), "w") as f:
                f.write(content)
            # Log and print success message
            logging.info(f"Copied {template_file} to project directory.")
        else:
            # Log and print warning message
            logging.warning(f"Template file {template_file} does not exist.")
            return False

        # Copy license
        license_file = os.path.join(TEMPLATES_DIR, Config.LICENSES_FOLDER_NAME, f"{license_type}.txt")
        if os.path.exists(license_file):
            # Read license file and write to project directory
            with open(license_file) as f:
                license_content = f.read()
            # Write to project directory
            with open(os.path.join(project_path, "LICENSE"), "w") as f:
                f.write(license_content)
            logging.info(f"Copied {license_file} to project directory.")
        else:
            logging.warning(f"License file {license_file} does not exist.")
            return False

        logging.info(f"Project \"{name}\" created successfully at {project_path}")
        print(f"\n{ansi_colors.AnsiColors.GREEN}Project \"{name}\" created successfully at {project_path}{ansi_colors.AnsiColors.RESET}")
        return True
    except Exception as e:
        logging.error(f"An error occurred while creating the project: {e}")
        return False