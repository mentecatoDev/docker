import os
import yaml

def get_sorted_file_dict(directory):
    """
    Recursively creates a dictionary of lists of files for the given directory and its subdirectories,
    sorted by key.

    Parameters:
    directory (str): The directory for which the file dictionary will be generated.

    Returns:
    A dictionary of lists of files in the given directory and its subdirectories, sorted by key.

    Example:
    >>> get_sorted_file_dict('/home/user/Documents')
    {'Documents': ['file1.txt', 'file2.txt'], 'Subdirectory': {'file3.txt': [], 'file4.txt': []}}
    """
    file_list = []
    direct = os.path.basename(directory)
    # Iterate over the contents of the current directory
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        # If it's a directory, recursively call get_sorted_file_dict on the subdirectory
        if os.path.isdir(path):
            subdirectory_dict = get_sorted_file_dict(path)
            if subdirectory_dict:
                # Sort the subdirectory dictionary by key before adding it to the parent dictionary
                file_dict.append(sorted(subdirectory_dict.items()))
            else:
                # If there are no files in the subdirectory, skip it
                continue
        # If it's a file, add it to the file list for the current directory
        elif os.path.isfile(path):
            # If the directory isn't in the file_dict yet, add an empty list
            file_dict.append(name)

    # Sort the file list for the current directory by key
    if direct in file_dict:
        file_dict[direct] = sorted(file_dict[direct])

    print('Gigante :', file_dict)
    return file_dict

def write_file_structure_yaml(directory, filename):
    """
    Writes the file structure of the given directory and its subdirectories to a file in YAML format,
    sorted by key.

    Parameters:
    directory (str): The directory for which the file structure will be generated.
    filename (str): The name of the file to write the file structure to.

    Returns:
    None.

    Side Effects:
    Creates or overwrites the file specified in 'filename' and writes the file structure in YAML format.

    Raises:
    May raise an IOError if there is a problem writing to the file.

    Important Note:
    This function uses yaml.dump with the 'allow_unicode' parameter set to True and the 'encoding' parameter set to 'utf-8'
    to properly encode any non-ASCII characters in the YAML file.

    Example:
    >>> write_file_structure_yaml('/home/user/Documents', 'documents.yaml')
    """
    file_dict = get_sorted_file_dict(directory)
    with open(filename, 'w', encoding="utf-8") as f:
        yaml.dump(file_dict, f, allow_unicode=True, encoding="utf-8")

write_file_structure_yaml('../borrame', 'file_structure.yaml')
