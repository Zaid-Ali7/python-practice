def is_palindrom(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False
    
print(is_palindrom(1331))