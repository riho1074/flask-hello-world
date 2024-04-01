import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Riley in 3308'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgres://database_example_lff5_user:64t2vX6bUfBZ0f6XMZZTZzkyzYjgn0F5@dpg-co5en5fsc6pc7385cnvg-a/database_example_lff5")
    conn.close()
    return "Database Connection Successful"

