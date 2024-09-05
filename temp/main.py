""" List all compressed files """
import os
import re
import shutil
from typing import List
from zipfile import ZipFile


def list_zip_file(input_file_path: str) -> List:
    """ List all directory files """
    files = os.listdir(input_file_path)

    """ Filter only zip files """
    return [os.path.join(input_file_path, zip_file) for zip_file in files if zip_file.endswith('.zip')]


def unpack_file(compressed_file: str) -> str:
    """ Load zip file and create a zip handler object """
    with ZipFile(compressed_file, 'r') as zip_file_handle:
        """ Identify output path based on input file path """
        output_file_path = compressed_file.replace('.zip', '')

        """ Extract all the members of the zip into a specific location"""
        zip_file_handle.extractall(path=output_file_path)

    return "Success"


def find_scripts_through(input_file_path: str) -> List:
    """ Given a source path find all script files """
    """
        root -> String that represents the root file path
        dirs -> List of directories that were traversed
        file -> list of files that were traversed
    """
    script_files = []
    for root, dirs, files in os.walk(input_file_path):
        script_files.extend([os.path.join(root, file) for file in files if file.endswith('.pl')])

    return script_files


def get_file_name_id(script_file_path: str) -> str:
    result = re.search(r"(\bCodeTask-[A-Za-z0-9]+\b)", script_file_path)

    return result.groups()[0]


def copy_file_to_output_file_path(script_file_path: str, output_file_path: str) -> None:
    script_file_path_input = "CodeTask-kakhafahjfJJ9109/start/middle/end/code.pl"
    file_name_id = get_file_name_id(script_file_path=script_file_path_input)

    output_file_name_path_id = os.path.join(output_file_path, f"{file_name_id}.pl")

    shutil.copy(script_file_path, output_file_name_path_id)


if "__main__" == __name__:
    file_path = "/Users/fernandoferreira/temp"
    zip_files = list_zip_file(input_file_path=file_path)
    script_list = []
    for zip_file in zip_files:
        status = unpack_file(compressed_file=zip_file)
        if status != "Success":
            raise Exception(f'Not possible to uncompress file {zip_file}')
        script_list = find_scripts_through(input_file_path=str(zip_file).replace('.zip', ''))

    for script_file_found in script_list:
        print(f"Script file found {script_file_found}")
        copy_file_to_output_file_path(script_file_path=script_file_found, output_file_path=file_path)
    # print(f"File Id {file_id}")

