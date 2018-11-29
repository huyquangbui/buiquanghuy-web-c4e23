import mlab
from flask import Flask, render_template, request
from data import CusInfo
from gmail import GMail, Message

# gmail = GMail("f.lampard263@gmail.com","tubqut-7nybny-cufzEf")
mlab.connect()
app = Flask(__name__)

@app.route("/registry", methods = ["GET","POST"])
def registry():
    if request.method == "GET":
        return render_template("registry.html")
    elif request.method == "POST":
        form = request.form
        username = form["USERNAME"]
        password = form["PASSWORD"]
        info = CusInfo(username = username, password = password)
        user_data = CusInfo.objects(username = username).first()
        while user_data != None:
            return "existing user name"
        else:
            info.save()
            # email = form["email"]

        # message = Message("Congrats", to="email", text="You are in!")
        # gmail.send(message)

        return "Welcome!  " + username
if __name__  == "__main__":
    app.run(debug=True)