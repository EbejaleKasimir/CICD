FROM python:3.9

COPY . /app 
WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip cache purge && \
    pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "jobs_api.py" ]