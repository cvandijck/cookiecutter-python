import sys
from pathlib import Path
from typing import Union
from artifactory import ArtifactoryPath

APP_ARTIFACTORY_PATH = None


def upload_file_to_artifactory(file_path: Union[str, Path], target_path: ArtifactoryPath):
    """ Upload a file to artifactory

    Args:
        file_path (str or Path): the file to upload
        target_path (ArtifactoryPath): the location on Artifactory to store to

    """

    target_path.deploy_file(file_path)


def main(args):
    root_folder = Path(__file__).resolve().parents[1]
    # TODO


if __name__ == '__main__':
    exit_code = main(sys.argv[1:])
    sys.exit(exit_code)
