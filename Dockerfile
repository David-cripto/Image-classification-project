FROM pytorch/pytorch as base

ARG IMG

ARG IMG_PATH

ENV IMG_P=$IMG_PATH
ENV IM=$IMG

RUN mkdir project_dir

WORKDIR project_dir

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN apt-get update

RUN apt-get install -y git

RUN git clone https://github.com/David-cripto/Image-classification-project.git 

COPY predict.py predict.py

CMD python3 predict.py $IMG_P/$IM

