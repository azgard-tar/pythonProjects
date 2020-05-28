from app import app
import mysql.connector 
import json

context = mysql.connector.connect(
    user = "pyuser",password="user",
    host="127.0.0.1",database="DB_for_learning"
) # connect to db

cursor = context.cursor()

@app.route('/')
@app.route('/index')
def index():
    cursor.execute("SELECT Login,RealName,Email FROM Users")
    retArr = []
    for (Login,RealName,Email) in cursor:
        retArr.append({
            "Login" : Login,
            "RealName" : RealName,
            "Email" : Email
        })
    return json.dumps( retArr )

    cursor.close()
    context.close()

@app.route('/asd')
def asd():
    return "dsa"
