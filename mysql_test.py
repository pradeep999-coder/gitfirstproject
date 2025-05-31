import os
import mysql.connector
from mysql.connector import Error

def main():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST', 'localhost'),
            user=os.getenv('MYSQL_USER', 'root'),
            password=os.getenv('MYSQL_PASSWORD', ''),
            database=os.getenv('MYSQL_DATABASE', ''),
            port=3306  # inside container network
        )
        if connection.is_connected():
            print("Connected to MySQL database!")

            cursor = connection.cursor()

            # Optional: Drop existing table
            cursor.execute("DROP TABLE IF EXISTS users")

            # Create table
            cursor.execute("""
            CREATE TABLE users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                age INT
            );
            """)

            # Insert data
            cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Alice", 25))
            connection.commit()

            # Read and print all rows
            cursor.execute("SELECT * FROM users")
            for row in cursor.fetchall():
                print(row)

            # Clean up
            cursor.close()
            connection.close()

    except Error as e:
        print(f"Error connecting to MySQL: {e}")

if __name__ == "__main__":
    main()
