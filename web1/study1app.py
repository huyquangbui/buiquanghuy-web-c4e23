from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/about-me")
def aboutme():
    me = {
        "name":"Huy QB",
        "work":"employed",
        "school":"FLSS",
        "hobbies":"football",
        "dog or crush":"dont exist",    }
    return render_template("personal_info.html", me = me)

@app.route("/school")
def school():
    return redirect("http://techkids.vn", code=302)

if __name__ == "__main__":
    app.run(debug=True)