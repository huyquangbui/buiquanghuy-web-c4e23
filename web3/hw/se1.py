import mlab
from flask import Flask, render_template, request
from data import VehicleInfo

mlab.connect()
app = Flask(__name__)

@app.route("/new_bike", methods = ["GET","POST"])
def new_bike():
    if request.method == "GET":
        return render_template("holybike.html")
    elif request.method == "POST":
        form = request.form
        model = form["model"]
        fee = form["fee"]
        image = form["image"]
        year = form["year"]

        new_bike = VehicleInfo(model = model, fee = fee, image = image, year= year)
        new_bike.save()

        return "SUBMITED"
if __name__ == "__main__":
    app.run(debug=True)