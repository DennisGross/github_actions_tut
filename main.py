import requests
import os
import time
try:
    SOME_SECRET = os.environ['SOME_SECRET']
except KeyError:
    SOME_SECRET = 'default'



# Add Hello World with secret and time to file
with open('hello.txt', 'a') as f:
    f.write('Hello World' + str(SOME_SECRET) +str(time.time()))

