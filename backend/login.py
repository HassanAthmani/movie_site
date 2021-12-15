import mysql.connector
import sys



def login(email,password):
    try:
        conn = mysql.connector.connect(host="localhost", user="root", passwd="")
        cursor = conn.cursor()
        print("connection is on.")

    except:
        sys.exit("Error connecting to the database. Please check your inputs. ")


    cursor.execute("SELECT * FROM `movie_site`.`user` WHERE email= %s AND password= %s;",(email,password))
    res=cursor.fetchall()

    if len(res)>0:
        cursor.close()
        conn.close()
        return str(email)

    else:

        cursor.close()
        conn.close()
        return "0"





























