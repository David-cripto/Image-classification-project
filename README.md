# Image-classification-project

Create a `.env` inside the `services` directory file with the following content:
```
IMGS_ROOT=<PATH_TO_YOUR_IMAGES_DIRECTORY>
IMG_PATH=/root/images
```

For run a script inside the docker you should go to `services` directory
```
cd services
```
and run
```
sudo IMG=<IMAGE_NAME> docker compose up
```
