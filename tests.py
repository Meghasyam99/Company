# import sys

# sys.stdout.reconfigure(encoding='utf-8')

# s='Hello Guys'

# encode=s.encode('utf-8')

# decode=encode.decode('utf-8')

import bcrypt


p='password@123'

encode=p.encode('utf-8')

salt=bcrypt.gensalt(rounds=12)

hashed_pass=bcrypt.hashpw(encode,salt).decode('utf-8')

print(hashed_pass)

login_pass='password@123'

encoded1=login_pass.encode('utf-8')
print(encoded1)
print(hashed_pass.encode('utf-8'))

if bcrypt.checkpw(encoded1,hashed_pass.encode('utf-8')):
    print('login successfull')
else:
    print('login failed')