from app import app
from flask import request
import mysql.connector 
import json

def mysqlGetSmth( query ):
    context = mysql.connector.connect(
        user = "pyuser",password="user",
        host="127.0.0.1",database="DB_for_learning"
    ) # connect to db
    cursor = context.cursor()
    cursor.execute( query )
    ret = cursor.fetchall()
    cursor.close()
    context.close()
    return ret

@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        data = mysqlGetSmth( "SELECT Login,RealName,Email FROM Users" )
        retArr = []
        for (Login,RealName,Email) in data:
            retArr.append({
                "Login" : Login,
                "RealName" : RealName,
                "Email" : Email
            })
        
        return json.dumps( retArr )  
    else:
        # Login, Registered, Email, RealName
        context = mysql.connector.connect(
            user = "pyuser",password="user",
            host="127.0.0.1",database="DB_for_learning"
        ) # connect to db
        cursor = context.cursor()
        cursor.execute( """ INSERT INTO Users 
                            ( Login,RealName,Email,Registered )
                            VALUES( %s, %s, %s, %s )
        """, (request.form['Login'],request.form['RealName'],request.form['Email'],request.form['Registered']) )
        id = cursor.lastrowid
        context.commit()
        
        cursor.close()
        context.close()
        return "User added with id = " + str( id )

@app.route('/<int:user_id>')
def getById(user_id):
    obj = mysqlGetSmth("SELECT Login,RealName,Email FROM Users where Id = " + str( user_id ) )[0]
    if obj != None:
        ret = {
            "Login" : obj[0],
            "RealName" : obj[1],
            "Email" : obj[2]
        }
    else:
        return None
    return json.dumps( ret )