<div style="display: flex; justify-content: center; align-items: center; height: 100vh; width: 100vw; margin: auto;">
  <img src="https://yosbel.pages.dev/assets/myEcommerce-BUxOKSiA.png" alt="Ecommerce pic" style="width: 100%; margin: auto;">
</div>


 # myEcommerce

## Project Overview

**myEcommerce** is a Django-based eCommerce application designed to provide a seamless online shopping experience. The project is structured to demonstrate Django's capabilities in managing an eCommerce platform, including product listing, user authentication, and cart management.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Project Structure](#project-structure)
5. [Contributing](#contributing)
6. [License](#license)
7. [References](#references)

## Installation

### Prerequisites

- Python 3.x
- Django 3.x
- SQLite (default database)

### Steps

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yosbelm/myEcommerce.git
    cd myEcommerce
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations and run the server:**

    ```sh
    python manage.py migrate
    python manage.py runserver
    ```

5. **Access the application:**

    Open your browser and go to `http://127.0.0.1:8000/`.

## Usage

### Admin Panel

To access the admin panel:

1. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

2. Log in to the admin panel at `http://127.0.0.1:8000/admin`.

### Adding Products

Products can be added via the admin panel. Navigate to the `Products` section and add new products with their details.

## Features

- User authentication (registration, login, logout)
- Product listing
- Shopping cart
- Order management

## Project Structure

```plaintext
myEcommerce/
│
├── ecommerceApp/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── ecommerceProject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── requirements.txt
```


## Contributing
### We welcome contributions! Please follow these steps:

Fork the repository.  
Create a new branch:
```sh
git checkout -b feature-branch
```
Commit your changes:  
```sh
git commit -am 'Add new feature'
```
Push to the branch.  
```sh
git push origin feature-branch
```
Create a new Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


## References
[Django Documentation](https://docs.djangoproject.com/en/5.0/)  

[Django Admin Interface](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/)  

[Django Models](https://docs.djangoproject.com/en/5.0/topics/db/models/)
