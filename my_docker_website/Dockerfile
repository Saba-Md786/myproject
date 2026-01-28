FROM python:3.10
WORKDIR /dockerapp
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python" , "app.py"]	
