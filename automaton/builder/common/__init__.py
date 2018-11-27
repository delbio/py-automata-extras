import sys
import os
import importlib


def add_dir_to_path_from_file(file_path):
    abs_config_file_path = os.path.abspath(file_path)
    abs_config_dir_path = os.path.dirname(abs_config_file_path)
    sys.path.append(abs_config_dir_path)


def allow_local_module_if_requested(file_path, element, attribute='local-module-enabled'):
    try:
        # if local-module-enabled is not present
        # parse raise exception
        element.attrib[attribute]
        # local-module-enabled present, skip value
        # Allow Modules that are in config file folder
        add_dir_to_path_from_file(file_path)
        print("Local Module enabled\n")
    except KeyError:
        print("No local modules enabled.\n")
    pass


def getClassFromElement(element):
    """
    Return class definition from xml element:

    <tag module="module.name" name="ClassName" />

    :param element:
    :return:
    """
    return getclass(element.attrib['module'], element.attrib['name'])


def getclass(module_name, class_name):
    """
    inspired by:
    https://stackoverflow.com/questions/4821104/python-dynamic-instantiation-from-string-name-of-a-class-in-dynamically-imported

    :param module_name:
    :param class_name:
    :return:
    """
    module = importlib.import_module(module_name)
    return getattr(module, class_name)

