import requests

from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image


def get_image(path): 
    if path.startswith("http"):
        try:
            image_path = requests.get(path, stream=True).raw
        except requests.exceptions.MissingSchema:
            print("Invalid URL")
            return None
    else:
        image_path = path

    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print(f"Can't open image on the {path}")
        return None
    except PIL.UnidentifiedImageError:
        print(f"URL f{path} doesn't lead to image")
        return None

    return image


def main():
    labels = ["cat", "dog"]

    while True:
        try:
            path = input("Enter image path/url: ")
            image = get_image(path)
            if image is None:
                continue

            feature_extractor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224-in21k')
            model =  ViTForImageClassification.from_pretrained('akahana/vit-base-cats-vs-dogs')
            inputs = feature_extractor(images=image, return_tensors="pt")

            outputs = model(**inputs)
            print(f"This is a {labels[outputs.logits.argmax()]}!")

        except KeyboardInterrupt:
            print("\nSystem shutdown")
            break

if __name__ == "__main__":
    main()

