import os
import mysql.connector
from mysql.connector import Error
import time

def wait_for_mysql(max_attempts=10, delay=3):
    for attempt in range(max_attempts):
        try:
            connection = mysql.connector.connect(
                host=os.getenv('MYSQL_HOST'),
                user=os.getenv('MYSQL_USER'),
                password=os.getenv('MYSQL_PASSWORD'),
                database=os.getenv('MYSQL_DATABASE'),
                port=3306
            )
            if connection.is_connected():
                print("✅ Connected to MySQL!")
                return connection
        except Error as e:
            print(f"Attempt {attempt + 1}: Waiting for MySQL - {e}")
            time.sleep(delay)
    raise Exception("❌ Could not connect to MySQL after retries.")

def main():
    try:
        connection = wait_for_mysql()
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS users")
        cursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), age INT)")
        cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Alice", 25))
        connection.commit()
        cursor.execute("SELECT * FROM users")
        for row in cursor.fetchall():
            print(row)
        cursor.close()
        connection.close()
    except Error as e:
        print(f"❌ Final MySQL error: {e}")

if __name__ == "__main__":
    main()
