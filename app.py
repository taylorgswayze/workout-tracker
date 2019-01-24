from flask import Flask, render_template, request
import datetime
import pymongo




app = Flask(__name__)
x = datetime.datetime.now()
today = x.strftime("%m"+"-"+"%d"+"-"+"%Y")
workout = {}


print(today)
@app.route('/', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':

        myclient = pymongo.MongoClient("mongodb://tgsbs:614Nmain@ds115931.mlab.com:15931/tgsbs")
        mydb = myclient["tgsbs"]
        mycol = mydb["workouts"]
        workout['date'] = today
        workout['press'] = request.form['press']
        workout['pressreps'] = request.form['pressreps']
        workout['standingrow'] = request.form['standingrow']
        workout['standingrowreps'] = request.form['standingrowreps']
        workout['curls'] = request.form['curls']
        workout['curlsreps'] = request.form['curlsreps']
        workout['flys'] = request.form['flys']
        workout['flyreps'] = request.form['flyreps']
        workout['time'] = request.form['time']
        workout['distance'] = request.form['distance']
        print(workout)
    return render_template('template.html')
    mycol.insert_one(workout)

if __name__ == '__main__':
    app.run(debug=True)