import re

def usr(s):
    p = r'^[a-zA-Z][a-zA-Z0-9_]{2,15}$'
    return bool(re.match(p, s))

def get(s):
   
    if usr(s):
        return s
    else:
        raise ValueError("Invalid username, bro.")


try:
    u = "1Valid_User123"
    x = get(u)
    print(f"Username '{x}' is cool.")
except ValueError as e:
    print(e)