from PIL import Image
import os
def Rotate():
    # Define the directory containing your images
    input_directory = "images"
    output_directory = "images"  # Create this folder if it doesn't exist
    
    # Iterate through the files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):  # Add more image formats as needed
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)
    
            # Open the image
            img = Image.open(input_path)
    
            # Rotate the image 90 degrees clockwise
            rotated_img = img.rotate(-90, expand=True)
    
            # Save the rotated image to the output directory
            rotated_img.save(output_path)