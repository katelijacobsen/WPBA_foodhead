import mysql.connector

#_____CONNECT TO DB_____##############################
def db():
    try:
        db = mysql.connector.connect(
            host = "mariadb",
            user = "root",
            password = "password",
            database = "foodhead"
        )
        cursor = db.cursor(dictionary=True)
        return db, cursor
    except Exception as e:
        print(e, flush=True)
        raise Exception("Database under maintenance", 500)


def close(db, cursor):
    if cursor: cursor.close()
    if db: db.close()
##############################_____CONNECT TO DB_____#