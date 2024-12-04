import os
from InquirerPy import prompt
import mkpj.project as project
import mkpj.ansi_colors as ansi_colors
import mkpj.config as config

def get_choices(directory, only_files=True):
    if only_files:
        return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    else:
        return [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]

def main():
    project_name = prompt([{
        "type": "input",
        "message": "Enter Project Name:",
        "name": "project_name"
    }])["project_name"]

    licenses = get_choices(os.path.expanduser(config.Config.ROOT_FOLDER_NAME + "/templates/licenses"))
    build_systems = get_choices(os.path.expanduser(config.Config.ROOT_FOLDER_NAME + "/templates/build"))

    if not licenses:
        print("No licenses found.")
        return

    # Prioritize GPL license
    if "GPL" in licenses:
        licenses.remove("GPL")
        licenses.insert(0, "GPL")

    license_choice = prompt([{
        "type": "list",
        "message": "Choose License:",
        "choices": licenses,
        "name": "license_choice"
    }])["license_choice"]

    if not build_systems:
        print("No build systems found.")
        return
    
    # Prioritize CMake
    if "cmake" in build_systems:
        build_systems.remove("cmake")
        build_systems.insert(0, "cmake")

    build_choice = prompt([{
        "type": "list",
        "message": "Choose Build System:",
        "choices": build_systems,
        "name": "build_choice"
    }])["build_choice"]

    create_project((project_name, license_choice, build_choice))

def create_project(choices):
    project_name, license_choice, build_choice = choices
    project.create_project(project_name, build_choice, license_choice)
    # if visual studio code is installed, prompt to open the project
    ret = os.system(f"code --version > /dev/null 2>&1")
    if ret == 0:
        open_project = prompt([{
            "type": "confirm",
            "message": "Open project in Visual Studio Code?",
            "name": "open_project"
        }])["open_project"]
        if open_project:
            os.system(f"code {project_name}")

if __name__ == "__main__":
    main()