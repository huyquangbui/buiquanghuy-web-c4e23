from flask import Flask, render_template

app = Flask(__name__)

@app.route("/user/<username>")
def user(username):
    userdata = {
        "alex":{
            "age":10,
            "hobbies":"basketball",
            "school":"CIC",
        },
        "ted":{
            "age":34,
            "hobbies":"robin",
            "school":"nyu",
        },
        "specter":{
            "age":"no idea",
            "hobbies":"winning by settling cases",
            "school":"harvard",
        }
    }
    if username in userdata.keys():
        return render_template("user.html", user_name = username, personal_info = userdata[username])
    else:
        return "User not found"
if __name__ == "__main__":
    app.run(debug=True)