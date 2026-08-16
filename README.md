# 🔐 Python Auth System

A simple and secure authentication system built with Python.  
The project supports user registration, login, logout, password changes, and input validation.

## ✨ Features

- 👤 User registration
- 🔑 User login and logout
- 🔄 Password change functionality
- 🔒 SHA-256 password hashing
- 👤 Username validation
- 🔐 Password validation
- 🪪 National ID validation
- 📱 Phone number validation
- 📧 Email validation
- 👋 Welcome message after login
- 🧪 Unit testing with `unittest`

## 🛠️ Technologies

- Python 3
- Object-Oriented Programming (OOP)
- Decorators
- Regular Expressions (`re`)
- SHA-256 Hashing (`hashlib`)
- Unit Testing (`unittest`)

## 📁 Project Structure

```text
python-auth-system/
│
├── main.py
├── tests/
│   └── test_account_site.py
│
└── README.md
```

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/amirreza-pourdehghan/python-auth-system.git
```

### Navigate to the project directory

```bash
cd python-auth-system
```

### Run the project

```bash
python main.py
```

## 🧪 Running Tests

This project includes unit tests written using Python's built-in `unittest` framework.

Run all tests with:

```bash
python -m unittest discover -s tests
```

## 💻 Usage

```python
from main import Account, Site


# Create a new account
user = Account(
    "amir_reza",
    "StrongPass1",
    "1234567890",
    "09123456789",
    "amir@example.com",
)


# Create a site
site = Site("https://example.com")


# Register the user
site.register(user)


# Login
site.login(
    username="amir_reza",
    password="StrongPass1",
)
```

## 📋 Validation Rules

| Field | Validation Rule | Example |
| :--- | :--- | :--- |
| 👤 Username | `firstname_lastname`, letters only | `amir_reza` |
| 🔐 Password | At least 8 characters, uppercase, lowercase, and digit | `StrongPass1` |
| 🪪 National ID | 10 digits with checksum validation | `1234567890` |
| 📱 Phone | `09xxxxxxxxx` or `+989xxxxxxxxx` | `09123456789` |
| 📧 Email | Standard email format | `amir@example.com` |

## 🔒 Security

Passwords are not stored as plain text.  
They are hashed using the **SHA-256 algorithm** before being stored.

## 🧪 Testing

The project uses Python's built-in `unittest` framework to test the initialization and behavior of the main classes.

```text
tests/
└── test_account_site.py
```

## 📌 Future Improvements

- Add persistent data storage
- Add database support
- Implement password reset functionality
- Improve test coverage
- Add a command-line interface (CLI)

---

⭐ If you found this project useful, feel free to star the repository!
```text
python-auth-system/
│
├── auth_system.py
└── README.md
