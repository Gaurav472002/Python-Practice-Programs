


SECURE = (('s', '$'), ('and', '&'), 
            ('a', '@'), ('o', '0'), ('i', '1'),
            ('I', '|'))


def secure_password(password):
    for a,b in SECURE:
        password=password.replace(a,b)
    return password

if __name__=="__main__":
    password=input("Please Enter your Password to get it's Secured version:")
    password=secure_password(password)
    print(f"Your Secured password is :{password}")