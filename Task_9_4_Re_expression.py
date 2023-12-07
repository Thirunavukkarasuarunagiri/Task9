import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def validate_bangladeshi_mobile(mobile):
    pattern = r'^\+8801[1-9]\d{8}$'
    return bool(re.match(pattern, mobile))

def validate_usa_telephone(telephone):
    pattern = r'^\+\d{1,2}\s?\(\d{3}\)\s?\d{3}-\d{4}$'
    return bool(re.match(pattern, telephone))

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'
    return bool(re.match(pattern, password))

email = "example@email.com"
mobile = "+8801712345678"
telephone = "+1 (123) 456-7890"
password = "Abcd1234@5678901"

print("Email validation:", validate_email(email))
print("Bangladeshi mobile validation:", validate_bangladeshi_mobile(mobile))
print("USA telephone validation:", validate_usa_telephone(telephone))
print("Password validation:", validate_password(password))