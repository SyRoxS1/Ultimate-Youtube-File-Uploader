from PIL import Image
import os
def Rotate():
    
    input_directory = "images"
    output_directory = "images"  
    
    
    for filename in os.listdir(input_directory):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):  
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)
            img = Image.open(input_path)      
            rotated_img = img.rotate(-90, expand=True)
            rotated_img.save(output_path)