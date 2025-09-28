import re

# -------------------------------
# Name regex
# -------------------------------
# Rules:
# - Must start with an uppercase letter
# - Allows letters, apostrophes, and hyphens
# - Names separated by exactly one space
name = r"^[A-Z][a-zA-Z'-]*(?: [A-Z][a-zA-Z'-]*)*$"
name_regex = re.compile(name)

# -------------------------------
# Phone regex
# -------------------------------
# Rules:
# - Matches 10 digits: 5555555555
# - Or format xxx-xxx-xxxx
# - Or format (xxx) xxx-xxxx
phone_number = r"^(?:\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$"
phone_regex = re.compile(phone_number)

# -------------------------------
# Email regex
# -------------------------------
# Rules:
# - Must start with a letter
# - Local part: letters, digits, single dots allowed
# - Domain: letters only before the dot
# - TLD: 2–6 letters
email_address = r"^[A-Za-z][A-Za-z0-9]*(?:\.[A-Za-z0-9]+)*@[A-Za-z]+\.[A-Za-z]{2,6}$"
email_regex = re.compile(email_address)

