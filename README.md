## Password Generator (Python)

### Overview

This project is a **Python-based password generator** that creates strong, random passwords using cryptographically secure randomness.
It allows users to select a security level before generating a password.

## Educational Use Only

> **This project is intended for educational purposes only.**

It was created to:

* Learn how password generation works
* Understand randomness and entropy
* Practice writing Python code

While the passwords generated are strong, this project:

* Has not been security audited
* Is not intended for production or commercial systems
* Should not be relied upon as a full security solution
* Do not rely on it for securing sensitive accounts or systems. The author is
not responsible for any loss, damage, or security breach resulting from its use.


---

## Features

* Cryptographically secure randomness for password generation using Python’s `secrets` module
* Multiple password security levels


---

## 🔢 Security Levels

| Level        | Description                       |
| ------------ | ----------------------------------|
| Basic        | Strong random password            |
| Secure       | Longer password                   |
| Ultra Secure | Very long, high-entropy password  |

> All levels generate **random, high-entropy passwords**.
> The difference between levels is primarily password length.

---

## Requirements

* Python 3.8+
* No external libraries required (standard library only)


---

## How to Run

```bash
python password_generator.py
```

Follow the on-screen prompts to choose a security level.
---

## Clone

```bash
git clone https://github.com/dzenan-dzizic/password-generator.git
```
