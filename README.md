# Flask RESTful API for Coffee and Farms

## Overview
This project is a Flask-based RESTful API designed to manage **coffee varieties** and their associated **farms**. It employs SQLite for data storage, SQLAlchemy ORM for database interaction, and Flask-RESTful for creating API endpoints. The API supports CRUD operations for farms and coffee varieties, ensuring seamless management of coffee-related data.

---

## Key Features
1. **Farm Management**:
   - Add new farms with details such as name, location, and description.
   - Retrieve a list of all farms.

2. **Coffee Management**:
   - Add coffee varieties associated with specific farms.
   - Retrieve a list of all coffee varieties.
   - Automatically generate `url_name` for coffee entries based on farm name, coffee variety, and process.

3. **Database**:
   - SQLite database for persistent storage.
   - SQLAlchemy ORM for intuitive database interactions.

---

## Prerequisites
- Python 3.7 or higher
- Flask
- Flask-RESTful
- Flask-SQLAlchemy

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/polinashamokhina/coffee_flask_project.git
   ```

2. **Install Dependencies**:

Use `pip` to install the required dependencies:

  ```bash
  pip install -r requirements.txt
```
3. **Set Up the Database**:

To initialize the SQLite database and create the necessary tables, run the following in a Python shell:

```python
with app.app_context():
  db.create_all()
```
3. **Run the application**:
```bash
  python main.py
```



