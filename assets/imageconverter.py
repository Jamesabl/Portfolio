from pathlib import Path
from PIL import Image


def convert_type(source):

    destination = source.with_suffix(".webp")
    image = Image.open(source)  # Open image
    image.save(destination, format="webp")  # Convert image to webp

    return destination


def main():
    paths = Path(r'filepath\folderOfImages').glob("**/*.jpg")
    for path in paths:
        type_path = convert_type(path)
        print(type_path)
    paths = Path(r'filepath\folderOfImages').glob("**/*.jpeg")
    for path in paths:
        type_path = convert_type(path)
        print(type_path)
    paths = Path(r'filepath\folderOfImages').glob("**/*.png")
    for path in paths:
        type_path = convert_type(path)
        print(type_path)

main()
