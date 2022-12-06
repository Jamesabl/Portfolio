from pathlib import Path
from PIL import Image


def convert_to_webp(source):

    destination = source.with_suffix(".webp")
    image = Image.open(source)  # Open image
    image.save(destination, format="webp")  # Convert image to webp

    return destination


def main():
    paths = Path(r'C:\Users\nadul\Desktop\image change').glob("**/*.jpg")
    for path in paths:
        webp_path = convert_to_webp(path)
        print(webp_path)
    paths = Path(r'C:\Users\nadul\Desktop\image change').glob("**/*.jpeg")
    for path in paths:
        webp_path = convert_to_webp(path)
        print(webp_path)
    paths = Path(r'C:\Users\nadul\Desktop\image change').glob("**/*.png")
    for path in paths:
        webp_path = convert_to_webp(path)
        print(webp_path)

main()
