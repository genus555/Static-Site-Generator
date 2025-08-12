import os
import shutil
def wipe_public(files):
    for file in files:
        path = f"./public/{file}"
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)

def source_to_public():
    if not os.path.exists("./public"):
        return("No Public file found")
    else:
        print("Public found\n_______________")
        public_files = os.listdir("./public")
        wipe_public(public_files)
    return("No Errors")
    