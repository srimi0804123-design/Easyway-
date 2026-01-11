from PIL import Image

def preprocess_image(image: Image.Image) -> Image.Image:
    return image.convert("L")
