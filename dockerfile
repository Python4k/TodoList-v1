FROM python:3.12

RUN mkdir /todoapi

WORKDIR /todoapi

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r /todoapi/requirements.txt

COPY . .

RUN chmod a+x /todoapi/docker/*.sh

CMD ["uvicorn", "app.run:app", "--host", "0.0.0.0", "--port", "80"]
