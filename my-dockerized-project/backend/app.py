from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        conn = psycopg2.connect(
            dbname=os.environ['POSTGRES_DB'],
            user=os.environ['POSTGRES_USER'],
            password=os.environ['POSTGRES_PASSWORD'],
            host='db'
        )
        return 'Успешна връзка с базата данни!'
    except Exception as e:
        return f'Грешка при връзка: {e}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
