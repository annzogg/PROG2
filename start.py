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
	items = {
	"unterlagen": ["Fahrausweis", "Visa/Passport/ID", "Impfausweis", "Flug-/Bahn-/Reiseticket", "Karte", "Reiseführer"],
	"hygieneartikel": ["Zahnbürste & Zahnpaste", "Gesichtsreiniger", "Tagescreme", "Nachtcreme", "Wattestäbchen", "Pinzette", "Deodorant", "Shampoo und Duschgel", "Wäschesack", "Badetuch", "Nastücher"],
	"elektronik": ["Handy & Ladegerät", "Kamera & Ladegerät", "Kopfhörer", "Adapter"],
	"kleider": ["Unterhosen", "Socken", "Pyjama", "Gürtel", "Bikini/Badehose", "Regenjacke"],
	"bformal": ["Anzug", "Hemd", "Anzugshose", "Anzugsschuhe", "Mantel", "Aktentasche", "Schmuck / Uhr", "Laptop & Ladegerät"],
	"arbeit": ["Dokumente", "Schreibzeug", "Aktentasche", "Laptop & Ladegerät", "Kreditkarten", "Visitenkarten", "Notizpapier"],
	"international": ["Visa", "Adapter", "Wörterbuch", "wichtigsten App herunterladen", "offline Karte auf Handy speichern"],
	"wandern": ["Wanderschuhe", "Wanderhose", "Wander Shirt", "Wandersocken", "Jacke / Windstopper", "Mütze / Stirnband", "Trinkflasche", "Rucksack", "erste Hilfe Ausrüstung", "Taschenlampe"],
	"joggen": ["Laufschuhe", "Laufhosen", "Lauf Shirt", "Jacke / Windstopper", "Trinkflasche", "Sporttuch"],
	"biken": ["Bikehose / Bikeshirt", "Bikeschuhe", "Bike / Ort zum Mieten raussuchen", "Trinkflasche", "Bike Handschuhe", "Rucksack", "Sportbrille"],
	"camping": ["Zelt", "Schlafmatte", "Feuerzeug", "Taschenlampe", "Trinkflasche", "Rucksack", "Trainer", "Jacke / Windstopper / Regenjacke", "Besteck / Teller", "Schlafsack"],
	"strand": ["Badetuch", "Bikini / Badehose", "Sonnenbrille", "Strandtuch", "Sonnencreme", "Flipflops", "Tasche", "Buch / Spiel", "Lockere Kleidung"],
	"nachtessen": ["Hemd", "Kleid", "Schöne Schuhe", "Schmuck", "Uhr", "Mantel"],
	"fitness": ["Sporthose", "Sportshirt", "Sportschuhe", "Trinkflasche", "Sporttuch", "Sportsocken", "Kopfhörer"],
	"foto": ["Kamera", "Speicherkarte", "Fototasche", "Ladegerät", "Kamera Linsen", "Putztzch für Kamera", "Stativ"],
	}
	
	return render_template("result.html", items = items)




if __name__ == "__main__":
	app.run(debug=True, port=5000)
