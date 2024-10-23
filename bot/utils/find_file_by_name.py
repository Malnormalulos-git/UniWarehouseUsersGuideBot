import os
from aiogram.types import FSInputFile
from typing import Optional


def find_file_by_name(directory: str, filename: str) -> Optional[FSInputFile]:
    """Searches for a file in a specified directory and subdirectories by name and returns FSInputFile or None"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    directory_path = os.path.join(current_dir, f"../{directory}")

    for root, _, files in os.walk(directory_path):
        if filename in files:
            file_path = os.path.join(root, filename)
            return FSInputFile(file_path, filename=filename)
    return None
