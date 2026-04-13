import google.generativeai as genai
import streamlit as st
from PIL import Image
from dotenv import load_dotenv
import os
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

def give_response(input , image):
    model = genai.GenerativeModel("gemini-1.5-pro")
    if input!="":
        response = model.generate_content([input,image])
        return response.text
    else:
        response = model.generate_content(image)
        return response.text


# streamlit application
st.title("Prompt and Image Input Application")

# Prompt input
prompt = st.text_input("Enter your prompt:", placeholder="Type something here...")

uploaded_image = st.file_uploader(
    "Upload an image",
    type=["png", "jpeg", "jpg", "webp", "heic", "heif"],
    accept_multiple_files=False
    
)

# Display the prompt and image
if prompt:
    st.write("Your prompt is:")
    st.write(prompt)

if uploaded_image:
    try:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image")
        st.write(f"Image format: {image.format}")
    except Exception as e:
        st.error(f"Error processing image: {e}")



button = st.button("generate response :")

if button:
    response = give_response(prompt,image)
    st.write(response)