FROM ubuntu:23.04 as load

WORKDIR /classification

COPY . .

RUN ./prereqs.sh

RUN python3 scripts/load_model.py

FROM load as predict

RUN ./build.sh

CMD make run img=$IMG_PATH/$IMG