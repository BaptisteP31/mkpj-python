import argparse
import logging
import os
from mkpj.templates import update_templates
from mkpj.project import create_project
from mkpj.logging_config import configure_logging
import mkpj.cli_menu as cli_menu
from .config import Config

LOGGING = False
configure_logging(LOGGING)

def main():
    parser = argparse.ArgumentParser(description="Create a new C++ project.")
    parser.add_argument("--update", action="store_true", help="Update templates repository.")
    parser.add_argument("name", nargs="?", help="Name of the project (not required for update).")
    parser.add_argument("--build", choices=["makefile", "cmake"], default="cmake", help="Build system to use")
    parser.add_argument("--license", choices=["MIT", "GPL"], default="GPL", help="License type")

    args = parser.parse_args()

    if args.update:
        update_templates()
    elif args.name:
        create_project(args.name, args.build, args.license)
    else:
        cli_menu.main()

if __name__ == "__main__":
    main()