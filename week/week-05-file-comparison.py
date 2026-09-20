"""File content comparison using Sha256"""

import hashlib


def hash_file(filepath):
    """Creates a hash for the file content"""

    hasher = hashlib.sha256()
    with open(filepath, "rb") as file:
        while chunk := file.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()


def verify_hash(file_one, file_two):
    """Compares two file hash and return true when they are the same"""

    first_hash = hash_file(file_one)
    second_hash = hash_file(file_two)

    return first_hash == second_hash


def perform_comparison(first_file, second_file):
    """Returns true if file is"""

    if verify_hash(first_file, second_file):
        return "File is still the same"

    else:
        return "File has changed"


print(perform_comparison("../resources/text1.txt", "../resources/text2.txt"))
print(perform_comparison("../resources/text2.txt", "../resources/text3.txt"))
