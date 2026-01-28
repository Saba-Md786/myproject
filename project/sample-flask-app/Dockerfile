FROM python:3.9
WORKDIR /app
COPY ./requirements.txt /app
COPY src/ src/
RUN pip install -r requirements.txt
EXPOSE 8084
CMD ["python3","src/app.py"]
