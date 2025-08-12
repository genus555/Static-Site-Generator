import os
import shutil
def wipe_public(files, dst):
    for file in files:
        path = f"{dst}/{file}"
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)

def find_source_path(source):
    if os.path.exists(f"./{source}"):
        source_path = f"./{source}"
        return source_path
    else:
        raise Exception(f"Error finding source path. Found path [{source_path}] doesnt exist")

def dir_file_list(dir_path):
    return os.listdir(dir_path)

def source_to_public_path(source, source_path, new_item, dst):
    new_path = source_path[2:]
    new_path = new_path[len(source):]
    if new_path != "":
        new_path = f"/{new_path}"
    new_path = f"{dst}{new_path}/{new_item}"
    return new_path

def copy_dir(source_path, source_files, source, dst):
    for file in source_files:
        new_dst = source_to_public_path(source, source_path, file, dst)
        path = f"{source_path}/{file}"
          
        if os.path.isdir(path):
            os.mkdir(new_dst)
            path_files = dir_file_list(path)
            copy_dir(path, path_files, source, dst)
        else:
            shutil.copy(path, new_dst)

def source_to_public(source, dst):
    if not os.path.exists(dst):
        os.mkdir(dst)
    else:
        public_files = os.listdir(dst)
        wipe_public(public_files, dst)
    
    source_path = find_source_path(source)
    source_files = dir_file_list(source_path)

    copy_dir(source_path, source_files, source, dst)
