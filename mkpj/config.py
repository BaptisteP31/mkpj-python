
class Config:
    ROOT_FOLDER_NAME = "~/.mkpjp"
    BUILD_FOLDER_NAME = "build"
    LICENSES_FOLDER_NAME = "licenses"
    PROJECT_TEMPLATE_FOLDER_NAME = "project"
    GIT_REMOTE_REPO = "https://github.com/BaptisteP31/mkpj-python.git"

    @staticmethod
    def get_build_folder_name():
        return Config.BUILD_FOLDER_NAME

    @staticmethod
    def get_git_remote_repo():
        return Config.GIT_REMOTE_REPO