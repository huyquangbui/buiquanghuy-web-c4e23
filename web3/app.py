import mlab
from flask import render_template, Flask, request
from data import Movie

app = Flask(__name__)
mlab.connect()

@app.route("/add_movie", methods = ["GET","POST"])
def add_movie():
    if request.method == "GET":
        # user requests form
        return render_template("add_movie.html")
    elif request.method == "POST":
        # user submits form
        form = request.form #unpack the shit from GET
        t = form["title"]
        img = form["image"]
        yr = form["year"]
        
        m = Movie(title = t, image = img, year = yr)
        m.save()
        
        return "Gotcha!"
    
if __name__ == "__main__":
    app.run(debug=True)