from dotenv import load_dotenv
import os 
import mysql.connector 

load_dotenv(".env")

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    passwd=os.getenv("DB_PASS"),
    user=os.getenv("DB_USER")
)

conn.autocommit = True

cursor = conn.cursor(buffered=True)

cursor.execute("CREATE DATABASE IF NOT EXISTS ssis")
cursor.execute("USE ssis")

cursor.execute("CREATE TABLE IF NOT EXISTS students (id VARCHAR(9) PRIMARY KEY,last_name VARCHAR(100) NOT NULL,first_name VARCHAR(100) NOT NULL,middle_name VARCHAR(100),gender VARCHAR(100),year_level INT NOT NULL,program VARCHAR(20))")
cursor.execute("CREATE TABLE IF NOT EXISTS programs (id VARCHAR(20) PRIMARY KEY,name VARCHAR(100) NOT NULL)")

cursor.execute("update students set program = null")