from flask import Flask

import datetime

app = Flask(__name__)





@app.route('/time')

def returnTime():
    timeNow = str(datetime.datetime.now())

    return timeNow



app.run(host='0.0.0.0',

        port=8080,

        debug=True)
