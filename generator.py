import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def create_passport_sheet(input_image_path):
    DPI = 300
    
    # Standard Passport Size: 35mm x 45mm
    PHOTO_W = int((35 / 25.4) * DPI) 
    PHOTO_H = int((45 / 25.4) * DPI) 
    
    # A4 Paper Size
    A4_W = int((210 / 25.4) * DPI)   
    A4_H = int((297 / 25.4) * DPI)   

    try:
        img = Image.open(input_image_path)
        img = img.resize((PHOTO_W, PHOTO_H), Image.Resampling.LANCZOS)

        sheet = Image.new('RGB', (A4_W, A4_H), 'white')

        margin_x, margin_y = 100, 100
        spacing = 40
        current_x, current_y = margin_x, margin_y

        while current_y + PHOTO_H < A4_H - margin_y:
            while current_x + PHOTO_W < A4_W - margin_x:
                sheet.paste(img, (current_x, current_y))
                current_x += PHOTO_W + spacing
            current_x = margin_x 
            current_y += PHOTO_H + spacing

        # Save to Desktop for easy finding
        output_path = os.path.join(os.path.expanduser("~"), "Desktop", "Passport_Sheet_Ready.jpg")
        sheet.save(output_path, quality=95)
        print(f"--- SUCCESS! ---\nYour sheet is saved on your Desktop as: Passport_Sheet_Ready.jpg")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # This creates a hidden window so the file dialog looks clean
    root = tk.Tk()
    root.withdraw() 

    print("Please select your photo in the pop-up window...")
    
    # Opens the Windows/Mac file selector
    file_path = filedialog.askopenfilename(
        title="Select your portrait photo",
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )

    if file_path:
        create_passport_sheet(file_path)
    else:
        print("No file selected. Exiting.")
