import mysql.connector
from flask import Flask, request


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    connection = mysql.connector.connect(user ='misf', password='misf',host='db',port="3306",database='db_main')
    cursor = connection.cursor()
    cursor.execute('Select * FROM VM')
    VM = cursor.fetchall()
    cursor.execute('SELECT * FROM SITES')
    SITES =  cursor.fetchall()
    connection.close()

    

    return str(f"{VM}\n\n{SITES}")

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port = '80')

