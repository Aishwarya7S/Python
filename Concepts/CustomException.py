class PasswordError(Exception):
    pass

def check_password(password):
    if len(password) < 6:
        raise PasswordError("Password too short! Must be at least 6 characters.")
    elif password.isalpha() or password.isdigit():
        raise PasswordError("Password must include both letters and numbers.")
    else:
        return "Password is strong."

try:
    pwd = "abc12"  
    print(check_password(pwd))
except PasswordError as e:
    print("Custom Exception:", e)
