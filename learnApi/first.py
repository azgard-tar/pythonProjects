import mysql.connector

context = mysql.connector.connect(
    user = "pyuser",password="user",
    host="127.0.0.1",database="DB_for_learning"
) # connect to db

cursor = context.cursor()

cursor.execute("SELECT Login,RealName,Email FROM Users")
for (Login,RealName,Email) in cursor:
    print("Login: {Login}, RealName: {RealName}, Email: {Email}".format(Login=Login,RealName=RealName,Email=Email) )

cursor.close()
context.close()
