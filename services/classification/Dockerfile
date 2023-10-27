FROM pytorch/pytorch as base

RUN mkdir project_dir

WORKDIR project_dir

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY scripts/predict.py predict.py

CMD python3 predict.py $IMG_PATH/$IMG
