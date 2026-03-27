import streamlit as st
from PIL import Image, ImageDraw
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="Passport Photo Generator", layout="centered")

st.title("📸 Passport Photo Sheet Generator")
st.write("Upload a photo, and I'll create a perfectly aligned A4 sheet for you.")

# --- SIDEBAR SETTINGS ---
st.sidebar.header("Settings")
spacing = st.sidebar.slider("Spacing between photos", 10, 100, 40)
line_color = st.sidebar.color_picker("Cut Line Color", "#D3D3D3")

# --- CORE LOGIC ---
def generate_sheet(uploaded_file, spacing, line_color):
    DPI = 300
    PHOTO_W = int((35 / 25.4) * DPI) 
    PHOTO_H = int((45 / 25.4) * DPI) 
    A4_W = int((210 / 25.4) * DPI)   
    A4_H = int((297 / 25.4) * DPI)   

    img = Image.open(uploaded_file).convert("RGB")
    img = img.resize((PHOTO_W, PHOTO_H), Image.Resampling.LANCZOS)

    sheet = Image.new('RGB', (A4_W, A4_H), 'white')
    draw = ImageDraw.Draw(sheet)

    margin_x, margin_y = 150, 150
    current_x, current_y = margin_x, margin_y

    while current_y + PHOTO_H < A4_H - margin_y:
        while current_x + PHOTO_W < A4_W - margin_x:
            sheet.paste(img, (current_x, current_y))
            # Draw cut lines
            shape = [current_x - 1, current_y - 1, current_x + PHOTO_W + 1, current_y + PHOTO_H + 1]
            draw.rectangle(shape, outline=line_color, width=2)
            current_x += PHOTO_W + spacing
        
        current_x = margin_x 
        current_y += PHOTO_H + spacing

    return sheet

# --- UI LAYOUT ---
uploaded_file = st.file_uploader("Choose a portrait photo...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Show a small preview of the original
    st.image(uploaded_file, caption="Original Photo", width=150)
    
    if st.button("Generate A4 Sheet"):
        with st.spinner("Arranging photos..."):
            final_sheet = generate_sheet(uploaded_file, spacing, line_color)
            
            # Show a preview of the A4 sheet (scaled down for web view)
            st.success("Sheet Generated Successfully!")
            st.image(final_sheet, caption="Print Preview (A4 Size)", use_column_width=True)

            # --- DOWNLOAD BUTTON ---
            # Convert PIL image to bytes for download
            buf = io.BytesIO()
            final_sheet.save(buf, format="JPEG", quality=95)
            byte_im = buf.getvalue()

            st.download_button(
                label="📥 Download Printable JPG",
                data=byte_im,
                file_name="passport_sheet.jpg",
                mime="image/jpeg"
            )
          to run this in terminal we print this  streamlit run app.py
