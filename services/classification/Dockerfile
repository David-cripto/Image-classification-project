FROM pytorch/pytorch as load

RUN mkdir project_dir

WORKDIR project_dir

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY scripts/load_model.py load_model.py

RUN python3 load_model.py

FROM load as predict

COPY scripts/predict.py predict.py

CMD python3 predict.py $IMG_PATH/$IMG
