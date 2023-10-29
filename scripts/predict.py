import argparse
import requests
import torch

from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
from pathlib import Path
import PIL


def configure_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path", type=str, help="Path for image to classify")
    return parser


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


def return_prediction(logits, thr=0.95):
    probs = torch.exp(logits) / torch.exp(logits).sum()
    if probs[0, 0] > thr:
        return "a cat"
    elif probs[0, 1] > thr:
        return "a dog"
    else:
        return "an unidentified thing"


def main(path_2_img):

    image = get_image(path_2_img)

    feature_extractor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224-in21k')
    model =  ViTForImageClassification.from_pretrained('akahana/vit-base-cats-vs-dogs')

    if image is not None:
        inputs = feature_extractor(images=image, return_tensors="pt")
        outputs = model(**inputs)
        prediction = return_prediction(outputs.logits)

        FIFO = "/tmp/trans"
        res = f"This is {prediction}!"
        fifo = open(FIFO, 'w')
        fifo.write(res + " " * (100 - len(res)))
        fifo.close()

if __name__ == "__main__":
    args = configure_arg_parser().parse_args()
    main(args.image_path)

