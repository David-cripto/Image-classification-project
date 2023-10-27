from transformers import ViTImageProcessor, ViTForImageClassification

def main():
    feature_extractor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224-in21k')
    model =  ViTForImageClassification.from_pretrained('akahana/vit-base-cats-vs-dogs')

if __name__ == "__main__":
    main()