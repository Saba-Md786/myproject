FROM python:3.9
WORKDIR /app
COPY ./requirements.txt /app
COPY src/ src/
RUN pip install -r requirements.txt
RUN python3 --version
ENTRYPOINT ["python3","/app/src/app.py"]
