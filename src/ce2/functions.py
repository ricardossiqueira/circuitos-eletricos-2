def file_handler(file_name):
    file = open(file_name)
    file_contents = file.read()
    contents_split = file_contents.splitlines()
    file.close()
    return file, contents_split
