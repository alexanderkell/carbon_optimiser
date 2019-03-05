FROM python:3.6

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY . /app

WORKDIR /app

ENV PYTHONPATH "${PYTHONPATH}:/src/"

ENTRYPOINT [ "python", "src/models/carbon_optimiser_northern_ireland.py" ]