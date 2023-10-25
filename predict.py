import argparse

from transformers import ViTImageProcessor, ViTModel, ViTForImageClassification
from PIL import Image

def configure_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path", type=str, help="Path for image to classify")
    return parser

def main(image_path: str):
    labels = ["cat", "dog"]
    image = Image.open(image_path)

    feature_extractor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224-in21k')
    model =  ViTForImageClassification.from_pretrained('akahana/vit-base-cats-vs-dogs')
    inputs = feature_extractor(images=image, return_tensors="pt")

    outputs = model(**inputs)
    print(f"This is a {labels[outputs.logits.argmax()]}!")

if __name__ == "__main__":
    _args = configure_arg_parser().parse_args()
    main(**vars(_args))

