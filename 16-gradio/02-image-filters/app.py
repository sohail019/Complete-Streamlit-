import numpy as np
import gradio as gr
from scipy.ndimage import gaussian_filter

def sepia(input_img):
    sepia_filter = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img

def black_and_white(input_img):
    gray_img = np.dot(input_img[..., :3], [0.2989, 0.5870, 0.1140])
    gray_img = np.clip(gray_img, 0, 255)  
    return np.stack((gray_img,)*3, axis=-1).astype(np.uint8)  

def negative(input_img):
    return 255 - input_img

def blur(input_img):
    return gaussian_filter(input_img, sigma=1)

def sharpen(input_img):
    blurred_img = gaussian_filter(input_img, sigma=1)
    sharpened_img = input_img + (input_img - blurred_img)
    sharpened_img = np.clip(sharpened_img, 0, 255)
    return sharpened_img.astype(np.uint8)

def apply_filter(input_img, filter_type):
    if filter_type == "Sepia":
        return sepia(input_img)
    elif filter_type == "Black and White":
        return black_and_white(input_img)
    elif filter_type == "Negative":
        return negative(input_img)
    elif filter_type == "Blur":
        return blur(input_img)
    elif filter_type == "Sharpen":
        return sharpen(input_img)
    else:
        return input_img

demo = gr.Interface(
    fn=apply_filter,
    inputs=[gr.Image(), gr.Dropdown(["Sepia", "Black and White", "Negative", "Blur", "Sharpen"], label="Filter Type")],
    outputs="image"
)

if __name__ == "__main__":
    demo.launch()
