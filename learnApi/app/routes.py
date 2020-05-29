from app import app
import mysql.connector 
import json

def mysqlOn( query ):
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

@app.route('/')
@app.route('/index')
def index():
    data = mysqlOn( "SELECT Login,RealName,Email FROM Users" )
    retArr = []
    for (Login,RealName,Email) in data:
        retArr.append({
            "Login" : Login,
            "RealName" : RealName,
            "Email" : Email
        })
    
    return json.dumps( retArr )   

@app.route('/<int:user_id>')
def getById(user_id):
    obj = mysqlOn("SELECT Login,RealName,Email FROM Users where Id = " + str( user_id ) )[0]
    if obj != None:
        ret = {
            "Login" : obj[0],
            "RealName" : obj[1],
            "Email" : obj[2]
        }
    else:
        return None
    return json.dumps( ret )