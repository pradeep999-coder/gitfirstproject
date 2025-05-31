# 🐍 Python + 🐬 MySQL Dockerized App

This project demonstrates how to connect a Python application to a MySQL database using **Docker** and **Docker Compose**. It automates the setup of the MySQL service and runs a Python script to interact with the database.

---

## 📁 Project Structure

```
python-mysql-app/
│
├── mysql_test.py           # Python script to interact with MySQL
├── requirements.txt        # Python dependencies
├── Dockerfile              # Dockerfile to build the Python app
├── docker-compose.yml      # Docker Compose file to manage both containers
└── README.md               # You are here!
```

---

## 🔧 Prerequisites

- Install [Docker](https://www.docker.com/products/docker-desktop)
- Install [Docker Compose](https://docs.docker.com/compose/install/) (if separate)
- Optional: [MySQL Workbench](https://dev.mysql.com/downloads/workbench/) (for GUI)

---

## 🐋 Step-by-Step Using Docker Compose (Recommended)

### 1. Clone this repository
```bash
git clone https://github.com/veera-collab/python-mysql-app.git
cd python-mysql-app
```

### 2. Run the project
```bash
docker-compose up --build
```

### 3. See the output
You should see:
```bash
(1, 'Alice', 25)
```

This means Python successfully connected to MySQL and fetched data.

---

## 🐳 Dockerfile Manual Setup (Alternative)

### 1. Build Python App Image
```bash
docker build -t python-mysql-app .
```

### 2. Create Docker Network
```bash
docker network create app-network
```

### 3. Run MySQL Container
```bash
docker run -d \
  --name mysql-container \
  --network app-network \
  -e MYSQL_ROOT_PASSWORD=root \
  -e MYSQL_DATABASE=testdb \
  -p 3307:3306 \
  mysql:latest
```

### 4. Run Python Container
```bash
docker run --rm --name python-mysql-app --network app-network python-mysql-app
```

---

## ⚙️ `docker-compose.yml` Explained

```yaml
version: "3.8"

services:
  mysql:
    image: mysql:latest
    container_name: mysql-container
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: testdb
    ports:
      - "3307:3306"
    networks:
      - app-network

  python:
    build: .
    container_name: python-mysql-app
    depends_on:
      - mysql
    networks:
      - app-network

networks:
  app-network:
    driver: bridge
```

---

## 🐍 Sample `mysql_test.py`

```python
import mysql.connector

conn = mysql.connector.connect(
    host='mysql-container',
    user='root',
    password='root',
    database='testdb'
)

cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT, name VARCHAR(255), age INT)")
cursor.execute("INSERT INTO users (id, name, age) VALUES (1, 'Alice', 25)")
conn.commit()
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
```

---

## 📦 `requirements.txt`

```
mysql-connector-python
```

---

## 🧠 Why Use Docker?

- Reproducible environment across all systems
- No need to install MySQL or Python dependencies manually
- Easily test, deploy, or share your setup with others
- Portable: works the same on your system, cloud, or teammate's laptop

---

## 🛠 Useful Docker Commands

| Command | Description |
|--------|-------------|
| `docker build -t <name> .` | Build image from Dockerfile |
| `docker run ...` | Run container manually |
| `docker ps -a` | List all containers |
| `docker-compose up` | Start all services |
| `docker-compose down` | Stop and remove services |
| `docker network create <name>` | Create a custom network |

---

## 🧪 Testing MySQL from Workbench

You can connect using:
- **Host:** `localhost`
- **Port:** `3307`
- **Username:** `root`
- **Password:** `root`

> Make sure the MySQL container is running.

---

## ✅ Output Example

```bash
(1, 'Alice', 25)
```

This confirms the connection and query execution was successful.

---

## 📃 License

MIT License - Free to use and modify.
