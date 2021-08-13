import jwt
import datetime

_encode = jwt.encode(
    {
        'hello': 'wow',
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=0.1)
    },
    '1',
    algorithm='HS256'
)

print(_encode)

import time

time.sleep(1)

decode_ = jwt.decode(_encode, '1')

print(decode_)