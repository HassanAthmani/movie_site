import mysql.connector
import sys



def register(email,password):
    try:
        conn = mysql.connector.connect(host="localhost", user="root", passwd="")
        cursor = conn.cursor()
        print("connection is on.")

    except:
        sys.exit("Error connecting to the database. Please check your inputs. ")


    cursor.execute("SELECT * FROM `movie_site`.`user` WHERE email= %s;",(email,))
    res=cursor.fetchall()

    if len(res)>0:
        cursor.close()
        conn.close()
        return "0"

    else:
        cursor.execute("INSERT INTO `movie_site`.`user` (`email`, `password`) VALUES (%s, %s);",(email,password))
        conn.commit()

        cursor.close()
        conn.close()
        return str(email)




























