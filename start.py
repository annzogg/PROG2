from flask import Flask
from flask import request
from flask import render_template

app = Flask("Demo")

@app.route("/start/", methods=['GET', 'POST'])
def start():
	if request.method == 'POST':
		ziel_person = request.form['vorname']
		rueckgabe_string = "Hello " + ziel_person + "!"
		return rueckgabe_string

	return render_template("start.html")

@app.route("/holiday/")
def holiday(): 

	return render_template("holiday.html")


@app.route("/working/")
def working():

	return render_template("working.html")

@app.route("/result/")
def result(): 
	unterlagen = ["Fahrausweis", "Visa/Passport/ID", "Impfausweis"]
	return render_template("result.html", unterlagen = unterlagen)




if __name__ == "__main__":
	app.run(debug=True, port=5000)
