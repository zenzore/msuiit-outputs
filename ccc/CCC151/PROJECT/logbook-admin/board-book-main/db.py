import mysql.connector 
from dotenv import load_dotenv
from os import getenv

load_dotenv(".env")

conn = mysql.connector.connect(
    host=getenv("DB_HOST"),
    passwd=getenv("DB_PASS"),
    user=getenv("DB_USER")
)

conn.autocommit = True 

cursor = conn.cursor(buffered=True)

cursor.execute("CREATE DATABASE IF NOT EXISTS logbook")

cursor.execute("USE logbook")

cursor.execute("""CREATE TABLE IF NOT EXISTS room (
    room_number INT PRIMARY KEY
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS boarder (
    id INT AUTO_INCREMENT,
    room_number INT,
    last_name VARCHAR(100) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    middle_name VARCHAR(100),
    phone_number VARCHAR(11),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY (room_number, id),
    FOREIGN KEY (room_number) REFERENCES room(room_number) ON DELETE CASCADE
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS visitor (
    id INT PRIMARY KEY AUTO_INCREMENT,
    last_name VARCHAR(100) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    middle_name VARCHAR(100),
    phone_number VARCHAR(11)
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS visitor_logs (
    visitor INT NOT NULL,
    boarder INT NOT NULL,
    log_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (visitor) REFERENCES visitor(id) ON DELETE CASCADE,
    FOREIGN KEY (boarder) REFERENCES boarder(id) ON DELETE CASCADE
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS boarder_bills (
    boarder INT NOT NULL,
    bill_date DATETIME,
    bill_amount INT NOT NULL,
    FOREIGN KEY (boarder) REFERENCES boarder(id) ON DELETE CASCADE
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS boarder_logs (
    boarder INT,
    log_type ENUM('in', 'out'),
    log_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (boarder, log_date),
    FOREIGN KEY (boarder) REFERENCES boarder(id) ON DELETE CASCADE
)""")