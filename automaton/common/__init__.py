import sys
import os


def add_dir_to_path_from_file(file_path):
    abs_config_file_path = os.path.abspath(file_path)
    abs_config_dir_path = os.path.dirname(abs_config_file_path)
    sys.path.append(abs_config_dir_path)

