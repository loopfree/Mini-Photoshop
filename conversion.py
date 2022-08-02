import io
import base64 
import numpy as np
from PIL import Image

# Take in base64 string and return PIL image in ndarray
def base64_to_arr(base64_string):
    imgdata = base64.b64decode(base64_string)
    return np.array(Image.open(io.BytesIO(imgdata)))

#Take in ndarray and convert into PIL image
def arr_to_pil(arr):
    result = Image.fromarray(arr.astype(np.uint8))
    return result

def pil_to_base64(image):
    output_buffer = io.BytesIO()

    image.save(output_buffer, format='PNG')

    byte_data = output_buffer.getvalue()

    encoded_input_string  = base64.b64encode(byte_data)

    base64_string = encoded_input_string.decode("utf-8")

    return base64_string