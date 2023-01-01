FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN pip install -U scikit-learn
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
