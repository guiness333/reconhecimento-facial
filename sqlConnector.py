import mysql.connector
def login(login='walber', senha='1234'):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="APS"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT UserID FROM users where Login='"+login+"' AND Passwd='"+senha+"'")

    myresult = mycursor.fetchone()
    mycursor.close()
    mydb.close()

    return myresult
