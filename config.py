from flask import request, make_response
from functools import wraps # use decorator so the function knows automatically not to cache
import mysql.connector
import re # Regex
import regex

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

##############################_____CONNECT TO DB_____#