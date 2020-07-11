FROM joyzoursky/python-chromedriver

WORKDIR /code
ENV FLASK_APP MainScores.py
ENV FLASK_RUN_HOST 0.0.0.0

COPY requirements.txt requirements.txt
RUN  pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8777
COPY . .
CMD ["flask", "run"]
