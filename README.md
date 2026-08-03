```markdown
# Python Auth System

A secure Python authentication system for managing user registration, login, logout, and password changes with input validation and SHA-256 password hashing.

## Features

- User registration
- User login and logout
- Password change functionality
- Password hashing with SHA-256
- Username validation
- Password validation
- National ID validation
- Phone number validation
- Email validation
- Welcome message after login

## Technologies

- Python 3
- Object-Oriented Programming
- Decorators
- SHA-256 hashing
- Regular expressions

## Project Structure
```text
python-auth-system/
│
├── auth_system.py
└── README.md
```

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/amirreza-pourdehghan/python-auth-system.git
   ```
2. Run the script:
   ```bash
   python auth_system.py
   ```

## Usage

```python
from auth_system import Account, Site

# Create a new account
user = Account("amir_reza", "StrongPass1", "1234567890", "09123456789", "amir@example.com")

# Create a site and register
site = Site("https://example.com")
site.register(user)

# Login
site.login(username="amir_reza", password="StrongPass1")
```

## Validation Rules

Field Rule Example
Username firstname_lastname, letters only amir_reza
Password Min 8 chars, uppercase, lowercase, digit StrongPass1
National ID 10 digits, official checksum 1234567890
Phone 09xxxxxxxxx or +989xxxxxxxxx 09123456789
Email Standard email format amir@example.com

```
```text
python-auth-system/
│
├── auth_system.py
└── README.md
