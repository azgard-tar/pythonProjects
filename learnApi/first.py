import mysql.connector
import json

context = mysql.connector.connect(
    user = "pyuser",password="user",
    host="127.0.0.1",database="DB_for_learning"
) # connect to db

cursor = context.cursor()

cursor.execute("SELECT Login,RealName,Email FROM Users where Id = " + str(1) )
obj = cursor.fetchone()
ret = {
    "Login" : obj[0],
    "RealName" : obj[1],
    "Email" : obj[2]
}
print( json.dumps( ret ) )

cursor.close()
context.close()
