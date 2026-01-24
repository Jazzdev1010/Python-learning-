import os 
from PIL import Image 

base_path = "images/" 

def is_allowed_file_type(file_path):
    allowed_filetypes=["jpg","png","jpeg"]
    file_type = file_path.split(".")[-1]
    if file_type.lower() in allowed_filetypes:
        return True
    return False
    
def get_dime(img_obj):
    return img_obj.size

for file_name in os.listdir("images/"): 
    if is_allowed_file_type(file_name):
        full_path = os.path.join(base_path, file_name)
        img = Image.open(full_path)
        print(get_dime(img))
        print(full_path)
    else:
        print(f"Found not-allowed file type : {file_name}")
