import streamlit as st
import cv2
import numpy as np
from PIL import Image
import os

#it is used to give title of an app
st.title("Image Processing App")

#it is folder path
image_folder = "/Users/coding/ResoluteAI Tasks/Task 3/Images"

#storing images in directory into a list,consits only image names
image_files = [f for f in os.listdir(image_folder) 
               if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

#here a list of images is passed to selectbox(),so we can store that image into selected_image
selected_image = st.selectbox("Select an Image", image_files)

#if image is selected by user ,it will join the directory with image name
if selected_image:
    image_path = os.path.join(image_folder, selected_image)

    #image is read using opencv
    img = cv2.imread(image_path)

    # Resize image to 1080x720
    resized_img = cv2.resize(img, (1080, 720))

    # Convert BGR to RGB for Streamlit display
    resized_img_rgb = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)

    #it is uesd to display image on web ,and if use_column_width is False image spread all over page 
    # else: image is adjusted properly if it is true
    st.image(resized_img_rgb, caption="Resized Image (1080x720)", use_column_width=True)

    st.write("### Apply Filters")

    #slider creates a slider into a web which is used to pass input to a variable
    
    blur_kernel = st.slider("Blur Kernel Size (Odd Only)", 1, 25, 5, step=2) #(label,min_value,max_value,Default_value,step)

    #0-255 because Canny Edge Detection works on grayscale image

    #If gradient(intensity of pixel) < threshold1 → Ignore
    threshold1 = st.slider("Canny Threshold 1", 0, 255, 100)

    #If gradient(intensity of pixel) > threshold2 → Strong edge
    threshold2 = st.slider("Canny Threshold 2", 0, 255, 200)
    
    #Streamlit returns a list of 3 column containers
    #st.columns(3) Divide the page into 3 equal columns
    col1, col2, col3 = st.columns(3)
    
    #in column 1 there is gray button if it is pressed image gets converted into grey
    
    with col1: #Whatever is written inside this block, put it inside column 1.
        
        if st.button("Gray"): #This creates a button labeled ,If user clicks this button, run the code inside.
            
            gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
            
            st.image(gray, caption="Gray Scaled Image", use_column_width=True)


    with col2:
        if st.button("Blur"):
            blur = cv2.GaussianBlur(resized_img, (blur_kernel, blur_kernel), 0)
            blur_rgb = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)
            st.image(blur_rgb, caption="Blurred Image", use_column_width=True)

    with col3:
        if st.button("Edge"):
            gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, threshold1, threshold2)
            st.image(edges, caption="Edge Detection Image", use_column_width=True)





