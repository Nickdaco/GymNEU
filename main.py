from flask import Flask
from flask.templating import render_template
import json
from datetime import datetime

f = open('gym_percents.json')
gym_data = json.load(f)

app = Flask(__name__)

@app.route('/')
def index():
    context = gym_data
    date_time = datetime.now()
    date_time = date_time.strftime("%d/%m/%Y %H:%M:%S")
    return render_template('home.html', context=context, date_time=date_time)


if __name__ == "__main__":
    app.run(debug=True)

f.close()