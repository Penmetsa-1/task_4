Task - 4 User Management REST API with Flask
The goal of this task is to build a **RESTful API using Flask** that manages user data.

---

## 📌 Objective

Create a simple REST API that performs CRUD (Create, Read, Update, Delete) operations for managing users.

---

## 🧰 Tools & Technologies

- **Python**
- **Flask**
- **Postman** or **Curl** for API testing

---

## 📁 Features / API Endpoints

| Method | Endpoint          | Description                  |
|--------|-------------------|------------------------------|
| GET    | `/`               | Welcome message              |
| GET    | `/users`          | Fetch all users              |
| GET    | `/users/<id>`     | Fetch a user by ID           |
| POST   | `/users`          | Add a new user               |
| PUT    | `/users/<id>`     | Update an existing user      |
| DELETE | `/users/<id>`     | Delete a user                |

---

## 🧪 Sample Request Payloads

### POST `/users`
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
{
  "name": "John Updated",
  "email": "john.updated@example.com"
}
pip install flask
python task4_flask_api.py

