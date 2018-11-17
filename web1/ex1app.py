from flask import Flask, render_template

app = Flask(__name__)

@app.route("/bmi/<int:weight>/<int:height>")
def BMI(weight, height):
    # ---------------------------------------------
    BMI = weight / (height/100 * height/100)
    # if BMI < 16:
    #     return "Severly downweight"
    # elif BMI < 18.5:
    #     return "Underweight"
    # elif BMI < 25:
    #     return "Normal"
    # elif BMI < 30:
    #     return "Overweight"
    # else:
    #     return "Obsese"
    # ----------------------------------------------
    return render_template("bmi.html", BMI = BMI)
if __name__ == "__main__":
    app.run(debug=True)