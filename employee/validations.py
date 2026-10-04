import bcrypt

def password_hash(ip_pass):
    encoded=ip_pass.encode('utf-8')
    salt=bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(encoded,salt).decode('utf-8')



def password_check(login_pass,db_pass):
    return bcrypt.checkpw(login_pass.encode('utf-8'),db_pass.encode('utf-8'))