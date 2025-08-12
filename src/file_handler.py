import os
import shutil
def wipe_public(files):
    for file in files:
        path = f"./public/{file}"
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

def source_to_public_path(source, source_path, new_item):
    new_path = source_path[2:]
    new_path = new_path[len(source):]
    if new_path != "":
        new_path = f"/{new_path}"
    new_path = f"./public{new_path}/{new_item}"
    return new_path

def copy_dir(source_path, source_files, source):
    for file in source_files:
        new_dst = source_to_public_path(source, source_path, file)
        path = f"{source_path}/{file}"

        #debug
        print(f"Old Path: {path}\nNew Path:{new_dst}\n--------------")
        
        if os.path.isdir(path):
            os.mkdir(new_dst)
            path_files = dir_file_list(path)
            copy_dir(path, path_files, source)
        else:
            shutil.copy(path, new_dst)

def source_to_public(source):
    if not os.path.exists("./public"):
        os.mkdir("public")
    else:
        public_files = os.listdir("./public")
        wipe_public(public_files)
    
    source_path = find_source_path(source)
    source_files = dir_file_list(source_path)

    copy_dir(source_path, source_files, source)
