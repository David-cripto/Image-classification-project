# Image classification with pretrain Neural Network

## Discription of our project

Our team is currently working on developing an app that utilizes a pre-trained neural network for the purpose of classifying images into two categories: dogs and cats. 
The machine learning model ([vit-base-cats-vs-dogs](https://huggingface.co/akahana/vit-base-cats-vs-dogs)) was used for classification.
To ensure the reproducibility and scalability of our app, we wraped it with Docker. 
This technology allows for a deployment and configuration across multiple platforms. 
For testing and integration our team also created configuration files, such as Makefiles and yaml config for GitHUb workflows, that provide instructions on how to build, deploy and test the app.
The final product is an app that can be easily set up within the Docker environment. 
By providing just one image as input, users are able to rapidly classify whether it contains a dog or a cat. 


## Short discription of the code

Next engineering staff was done:

- The public git repository with all source and engineering files, as well as README file with description for a successful run of the project
- Docker container to build docker image locally `Dockerfile`
- Installation of requirements `prereqs.sh`
- Build system in form of Makefiles `build.sh`
- Check the critical functionality `test.sh`

## Quickstart with Dockerfile

1. Clone the repository with project to your local machine:

```
git clone https://github.com/David-cripto/Image-classification-project.git
cd Image-classification-project
```

2. Go to `services` directory:
```
cd services
```
And Create a `.env` file inside the `services` directory with the following content:
```
IMGS_ROOT=<PATH_TO_YOUR_IMAGES_DIRECTORY>
IMG_PATH=/root/images
```
where `<PATH_TO_YOUR_IMAGES_DIRECTORY>` &mdash; path to your directory with image to classify

3. Run the following command to classify the image:

```
sudo IMG=<IMAGE_NAME> docker compose up
```
where `<IMAGE_NAME>` &mdash; name of your image to classify


## Quickstart with `.sh` scripts

1. Create an empty `ubuntu:latest` docker container: 

```
docker pull ubuntu:latest
docker run -ti --name fse_2023 ubuntu:latest
apt-get update
apt-get install -y git
```

2. Clone repository with project: 

```
git clone https://github.com/David-cripto/Image-classification-project.git
cd Image-classification-project
```


3. Run the following shell scripts: 
```
chmod u+x ./prereqs.sh
./prereqs.sh
chmod u+x ./build.sh
./build.sh
chmod u+x ./test.sh
./test.sh   
```

4. After it you can make testing by:
```
./test.sh
```
or
```
make test
```

5. And also you car run the Neural network with the following command:
```
make run img="PATH_TO_YOUR_IMAGE"
```


## Developers

[David Li](https://github.com/David-cripto)

[Kseniia Petrushina](https://github.com/pkseniya)

[Arina Chumachenko](https://github.com/arina-chumachenko)

[Irina Lebedeva](https://github.com/swnirk)
