import os

def process_user_image(image_filename):
    # CRITICAL FLAW: Directly passing user input to the system shell
    # An attacker could pass "image.jpg; rm -rf /" to delete the server
    os.system(f"convert {image_filename} output.png")
    return "Image processed!"
