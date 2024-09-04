import sys
from PIL import Image

ASCII_CHARS = ".'`^\",:;Il!i<>~+_-?][}{1\\|/ftjxrnvuczYUJLCQ0OMwbkdoah*#MW&%8B@$"

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ''.join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return ascii_str

def image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    image = resize_image(image, new_width)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img)

    print("ASCII art written to ascii_image.txt")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    image_to_ascii(image_path)
