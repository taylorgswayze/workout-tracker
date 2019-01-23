from flask import Flask, render_template, request
import datetime
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["mydatabase"]


app = Flask(__name__)
x = datetime.datetime.now()
today = x.strftime("%m"+"-"+"%d"+"-"+"%Y")
workout = {}

@app.route('/', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        workout['date'] = today
        workout['press'] = request.form['press']
        workout['pressreps'] = request.form['pressreps']
        workout['standingrow'] = request.form['standingrowreps']
        workout['curls'] = request.form['curls']
        workout['curlsreps'] = request.form['curlsreps']
        workout['flys'] = request.form['flys']
        workout['flyreps'] = request.form['flyreps']
        workout['time'] = request.form['time']
        workout['distance'] = request.form['distance']

        print(workout)

    return render_template('template.html')

if __name__ == '__main__':
    app.run(debug=True)