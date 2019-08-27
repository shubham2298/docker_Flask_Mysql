FROM python:3.6

EXPOSE 5000

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

COPY app.py /app
CMD python app.py