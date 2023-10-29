# Image-classification-project

## Discription of our project

Our team is currently working on developing an app that utilizes a pre-trained neural network for the purpose of classifying images into two categories: dogs and cats. 
The machine learning model ([vit-base-cats-vs-dogs](https://huggingface.co/akahana/vit-base-cats-vs-dogs)) was used for classification.
To ensure the reproducibility and scalability of our app, we wraped it with Docker. 
This technology allows for a deployment and configuration across multiple platforms. 
For testing and integration our team also created configuration files, such as Makefiles, that provide instructions on how to build, deploy and test the app.
The final product is an app that can be easily set up within the Docker environment. 
By providing just one image as input, users are able to rapidly classify whether it contains a dog or a cat. 


## Short discription of the code

Next engineering staff was done:

- The public git repository with all source and engineering files, as well as README file with description for a successful run of the project
- Docker container to build docker image locally ("Dockerfile")
- Build system in form of Makefiles ("Makefile") by which:
    - installation of requirements ("requirements")
    - build: obtain external data, perform data preprocessing, training and model optimization ("predict", "build")
    - test: check the critical functionality ("test") 
        parts are done



Clone repository

```
git clone https://github.com/David-cripto/Image-classification-project.git
```


Change directory

```
cd Image-classification-project/
```



To run the code you need package requirements. Run commands inside docker container

```
sudo pip install -r requirements.txt 
```

Ubuntu 22.04.3 LTS must be used to run this project.


## Get started

1. To make engineering stuff working follow the instructions:

a)  You need to download "Dockerfile" from the current repository or you can clone the repository by 
```
git clone https://github.com/David-cripto/Image-classification-project.git
``` 

and build "Dockerfile" by:

```
docker build -t _____
```

If you use git clone then apply 
```
cd Image-classification-project
```

2. Install requirements and then run main calculations

Add dependencies
```
./prepeqs.sh
```

3. Build the code
```
./build.sh
```

4. After it you can make testing by
```
./test.sh
```
or
```
make test
```

5. Workflow: you can also try created workflows on GitHub 

6. Our team also tried to develop an app for the project



## Developers

[David Li](https://github.com/David-cripto)

[Kneniia Petrushina](https://github.com/pkseniya)

[Arina Chumachenko](https://github.com/arina-chumachenko)

[Irina Lebedeva](https://github.com/swnirk)
