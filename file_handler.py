import os
import json

def read_file(filepath):
    f = open(filepath, 'r')
    content = f.read()
    # File not closed - resource leak
    return content

def write_file(filepath, content)  # Missing colon
    with open(filepath, 'w') as f:
        f.write(content)

def delete_file(filepath):
    os.remove(filepath)
    # No check if file exists

def count_lines(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    return len(lines)
    # No error handling for file not found

def parse_json_file(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data
    # No error handling for invalid JSON

class FileManager:
    def __init__(self, directory):
        self.directory = directory
    
    def list_files(self):
        files = os.listdir(self.directory)
        return files
        # No check if directory exists
    
    def get_file_size(self, filename):
        filepath = os.path.join(self.directory, filename)
        size = os.path.getsize(filepath)
        return size / 1024  # Convert to KB
        # No error handling, potential division issues
