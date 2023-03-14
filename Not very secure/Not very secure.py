def alphanumeric(password):
    if len(password) == 0:
        return False
    else:
        for i in password:
            if i.isalnum():
                continue
            else:
                return False
    return True