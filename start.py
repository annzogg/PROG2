from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
import json

app = Flask("Demo")
neue_reise = {}

def schreibe_daten_in_json(pfad, daten):
	with open(pfad, 'w') as datei:
		json.dump(daten, datei)

def lade_daten_aus_json (pfad, standard_wert = []):
	try:
		with open(pfad, 'r') as datei:
			return json.load(datei)
	except Exception:
		return standard_wert

@app.route("/", methods=["GET", "POST"])
@app.route("/start/", methods=["GET", "POST"])
def start():
	if request.method == "POST":
		ort = request.form["ort"]
		tag = request.form["tag"]
		monat = request.form["monat"]
		reisedauer_in_tagen = request.form["reisedauer_in_tagen"]
		art_der_reise = request.form["art_der_reise"]
		global neue_reise
		neue_reise = { #schreibe Daten in Jason 
			"ort": ort, 
			"tag": tag,
			"monat": monat,
			"reisedauer_in_tagen": reisedauer_in_tagen,
			"art_der_reise": art_der_reise
		}

		if art_der_reise == "urlaub":
			return redirect(url_for("holiday"))
		else:
			return redirect(url_for("working"))

	return render_template("start.html")

@app.route("/holiday/", methods=["GET", "POST"])
def holiday():
	if request.method == "POST":
		aktivitäten = request.form.getlist("aktivität")
		return redirect(url_for("result", aktivitaeten = aktivitäten))

	return render_template("holiday.html")


@app.route("/working/", methods=["GET", "POST"])
def working():
	if request.method == "POST":
		aktivitäten = request.form.getlist("aktivität")
		return redirect(url_for("result", aktivitaeten = aktivitäten))

	return render_template("working.html")

@app.route("/result/<aktivitaeten>", methods=["GET", "POST"])
def result(aktivitaeten):
	global neue_reise
	print(neue_reise["reisedauer_in_tagen"])
	items = {
	"unterlagen": ["Fahrausweis", "Visa/Passport/ID", "Impfausweis", "Flug-/Bahn-/Reiseticket", "Karte", "Reiseführer"],
	"hygieneartikel": ["Zahnbürste & Zahnpaste", "Gesichtsreiniger", "Tagescreme", "Nachtcreme", "Wattestäbchen", "Pinzette", "Deodorant", "Shampoo und Duschgel", "Wäschesack", "Badetuch", "Nastücher"],
	"elektronik": ["Handy & Ladegerät", "Kamera & Ladegerät", "Kopfhörer", "Adapter"],
	"kleider": [neue_reise["reisedauer_in_tagen"] + "x Unterhosen", neue_reise["reisedauer_in_tagen"] + "x Socken", "Pyjama", "Gürtel", neue_reise["reisedauer_in_tagen"]  + "x Bikini/Badehose", "Regenjacke"]
	}

	if "joggen" in aktivitaeten:
		items["joggen"] = ["Laufschuhe", "Laufhosen", "Lauf Shirt", "Jacke / Windstopper", "Trinkflasche", "Sporttuch"]
	if "wandern" in aktivitaeten:
		items["wandern"] = ["Wanderschuhe", "Wanderhose", "Wander Shirt", neue_reise["reisedauer_in_tagen"] + "x Wandersocken", "Jacke / Windstopper", "Mütze / Stirnband", "Trinkflasche", "Rucksack", "erste Hilfe Ausrüstung", "Taschenlampe"]
	if "biken" in aktivitaeten:
		items["biken"] = ["Bikehose / Bikeshirt", "Bikeschuhe", "Bike / Ort zum Mieten raussuchen", "Trinkflasche", "Bike Handschuhe", "Rucksack", "Sportbrille"]
	if "camping" in aktivitaeten:
		items ["camping"] = ["Zelt", "Schlafmatte", "Feuerzeug", "Taschenlampe", "Trinkflasche", "Rucksack", "Trainer", "Jacke / Windstopper / Regenjacke", "Besteck / Teller", "Schlafsack"]
	if "strand" in aktivitaeten:
		items ["strand"] = ["Badetuch", neue_reise["reisedauer_in_tagen"] + "x Bikini / Badehose", "Sonnenbrille", "Strandtuch", "Sonnencreme", "Flipflops", "Tasche", "Buch / Spiel", "Lockere Kleidung"]
	if "nachtessen" in aktivitaeten:
		items ["nachtessen"] = ["Hemd", "Kleid", "Schöne Schuhe", "Schmuck", "Uhr", "Mantel"]
	if "fitness" in aktivitaeten:
		items ["fitness"] = ["Sporthose", "Sportshirt", "Sportschuhe", "Trinkflasche", "Sporttuch", neue_reise["reisedauer_in_tagen"] + "x Sportsocken", "Kopfhörer"]
	if "fotografie" in aktivitaeten:
		items ["fotografie"] = ["Kamera", "Speicherkarte", "Fototasche", "Ladegerät", "Kamera Linsen", "Putztzch für Kamera", "Stativ"]
	if "bformal" in aktivitaeten:
		items ["bformal"] = ["Anzug", "Hemd", "Anzugshose", "Anzugsschuhe", "Mantel", "Aktentasche", "Schmuck / Uhr", "Laptop & Ladegerät"]
	if "arbeit" in aktivitaeten: 
		items ["arbeit"] = ["Dokumente", "Schreibzeug", "Aktentasche", "Laptop & Ladegerät", "Kreditkarten", "Visitenkarten", "Notizpapier"]
	if "international" in aktivitaeten: 
		items ["international"] = ["Visa", "Adapter", "Wörterbuch", "wichtigsten App herunterladen", "offline Karte auf Handy speichern"]

	# "Trip Speichern" löst POST request aus
	if request.method == "POST":
		ausgewaehlte_eintrage = request.form.getlist("eintrag")
		neue_reise["packliste"] = ausgewaehlte_eintrage
		meine_trips = lade_daten_aus_json("backpacker.json")
		meine_trips.append(neue_reise)
		schreibe_daten_in_json("backpacker.json", meine_trips)
		return redirect(url_for("start"))

	return render_template("result.html", items = items)


@app.route("/gespeicherte_trips/")
def gespeicherte_trips():
  meine_trips = lade_daten_aus_json("backpacker.json")
  return render_template("gespeicherte_trips.html", trips = meine_trips)

if __name__ == "__main__":
	app.run(debug=True, port=5000)
