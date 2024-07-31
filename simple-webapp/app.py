'''
Author: 0xSchnappi 952768182@qq.com
Date: 2024-07-31 11:40:30
LastEditors: 0xSchnappi 952768182@qq.com
LastEditTime: 2024-07-31 15:21:45
FilePath: /simple-webapp/simple-webapp/app.py
Description: 

Copyright (c) 2024 by github.com/0xSchnappi, All Rights Reserved. 
'''


import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    provider = str(os.environ.get('PROVIDER', 'World'))
    return 'Hello ' + provider+ '!'

if __name__ == "__main__":
    
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)