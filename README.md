# PhotoPro
PhotoPro is a website where we can just upload a photo and it  will enhance clear background and make photosheet which we can download and Print 
Navigation Menu
Sign in
deepakguptabca
/
InstantPhotos
Public
Code
Issues
Pull requests
1
deepakguptabca/InstantPhotos
Name	
deepakguptabca
deepakguptabca
2 weeks ago
.gitignore
4 months ago
templates
3 weeks ago
venv
3 weeks ago
README.md
2 weeks ago
app.py
3 weeks ago
requirements.txt
3 weeks ago
Repository files navigation
README
📸 Passport Photo Pro
A web-based tool to generate print-ready passport photo sheets from uploaded images. Supports multiple photos, per-photo copy counts, AI background removal, image enhancement, and multi-page PDF export — all on an A4 layout at 300 DPI.

🚀 Features
Multi-photo upload — drag & drop or click to upload one or more photos at once
Per-photo copy count — set how many copies of each photo you need (1–54)
In-browser cropper — crop each photo to the correct passport aspect ratio before processing
AI background removal — powered by remove.bg
AI image enhancement — restored and sharpened via Cloudinary's gen_restore
A4 print layout — photos are automatically arranged in a grid at 300 DPI
Multi-page PDF — if photos exceed one A4 page, additional pages are created automatically
Advanced options — customize photo width, height, spacing, and border size
Feedback system — built-in bug report form powered by EmailJS
Animated particle background — via Particles.js
🧰 Tech Stack
Layer	Technology
Frontend	HTML, Tailwind CSS, Vanilla JS
Cropping	Cropper.js
Backend	Python, Flask
Image AI	remove.bg API, Cloudinary AI
PDF gen	Pillow (PIL)
Email	EmailJS
📦 Prerequisites
Python 3.8+
pip
A remove.bg API key
A Cloudinary account (free tier works)
🛠️ Installation

 Create a virtual environment (recommended)
python -m venv venv



# On Windows
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Set up environment variables
Create a .env file in the project root:

REMOVE_BG_API_KEY=your_remove_bg_api_key_here
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_cloudinary_api_key
CLOUDINARY_API_SECRET=your_cloudinary_api_secret
⚠️ Never commit your .env file. Add it to .gitignore.

5. Run the app
python app.py
The server will start at http://localhost:8086.


Make sure your requirements.txt includes:

flask
pillow
requests
python-dotenv
cloudinary
Generate it automatically with:

pip freeze > requirements.txt

🖼️ How It Works
Upload
Open the app in your browser at http://localhost:8086
Drag and drop one or more photos onto the upload zone, or click to browse
Each photo appears as a card with a thumbnail
Crop (Optional but Recommended)
Click Crop on any photo card
A modal cropper opens with a fixed passport aspect ratio (384×472)
Adjust the crop area and click Crop & Save
Set Copies
Each photo card has a Copies input (default: 6)
Change it per photo to control how many times it appears on the sheet
Advanced Options (Optional)
Click Advanced Options to customize:
Width / Height — passport photo dimensions in pixels
Spacing — gap between rows of photos
Border — black border thickness around each photo
Generate
Click Generate Sheet
The backend processes each photo:
Removes the background via remove.bg
Uploads to Cloudinary and applies AI restoration
Resizes and adds a border
All photos are arranged on A4 pages (2480×3508 px at 300 DPI)
If photos overflow one page, new pages are added automatically
Download
Once generated, a PDF preview appears in the browser
Click Download PDF to save the print-ready file
