# app.py
import streamlit as st
import qrcode
import base64

def generate_qr_code(data, output_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save(output_path)

st.title("QR Code Generator")

data = st.text_input("Enter the data to encode in the QR code", key="data_input")
output_image = st.empty()

if st.button("Generate QR Code"):
    if data:
        # Generate the plain QR code
        qr_code_path = "qr_code.png"
        generate_qr_code(data, qr_code_path)
        output_image.image(qr_code_path, use_column_width=True)

        # Create a download link
        st.markdown(f'[Download QR Code](data:file/png;base64,{base64.b64encode(open(qr_code_path, "rb").read()).decode()})', unsafe_allow_html=True)

    else:
        st.warning("Please enter data to generate a QR code.")
