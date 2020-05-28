import mysql.connector
import json

context = mysql.connector.connect(
    user = "pyuser",password="user",
    host="127.0.0.1",database="DB_for_learning"
) # connect to db

cursor = context.cursor()

cursor.execute("SELECT Login,RealName,Email FROM Users")
tempArr = []
for (Login,RealName,Email) in cursor:
    tempArr.append({
        "Login" : Login,
        "RealName" : RealName,
        "Email" : Email
    })
    #print("Login: {Login}, RealName: {RealName}, Email: {Email}".format(Login=Login,RealName=RealName,Email=Email) )

print( json.dumps( tempArr ) )

cursor.close()
context.close()
