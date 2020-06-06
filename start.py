from flask import Flask,redirect, render_template, request, jsonify, url_for
import json
from collections import defaultdict
from itertools import islice

app = Flask("Bagpacker")
neue_reise = {}

def schreibe_daten_in_json(pfad, daten):
    with open(pfad, 'w') as datei:
        # dump()-Methode stellt Schreiben von Daten in Dateien zur Verfügung.
        json.dump(daten, datei)


def lade_daten_aus_json(pfad, standard_wert=[]):
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
        # erstelle dict für json
        neue_reise = {
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
        aktivitaeten = request.form.getlist("aktivitaet")
        return redirect(url_for("result", aktivitaeten=aktivitaeten))

    return render_template("holiday.html")


@app.route("/working/", methods=["GET", "POST"])
def working():
    if request.method == "POST":
        aktivitaeten = request.form.getlist("aktivitaet")
        return redirect(url_for("result", aktivitaeten=aktivitaeten))

    return render_template("working.html")


@app.route("/result/<aktivitaeten>", methods=["GET", "POST"])
def result(aktivitaeten):
    global neue_reise
    print(neue_reise["reisedauer_in_tagen"])
    items = {
        "Unterlagen": ["Fahrausweis", "Visa/Passport/ID", "Impfausweis", "Flug-/Bahn-/Reiseticket", "Karte", "Reiseführer"],
        "Hygieneartikel": ["Zahnbürste & Zahnpaste", "Gesichtsreiniger", "Tagescreme", "Nachtcreme", "Wattestäbchen", "Pinzette", "Deodorant", "Shampoo und Duschgel", "Wäschesack", "Badetuch", "Nastücher"],
        "Elektronik": ["Handy & Ladegerät", "Kamera & Ladegerät", "Kopfhörer", "Adapter"],
        "Kleider": [neue_reise["reisedauer_in_tagen"] + "x Unterhosen", neue_reise["reisedauer_in_tagen"] + "x Socken", "Pyjama", "Gürtel", neue_reise["reisedauer_in_tagen"] + "x Bikini/Badehose", "Regenjacke"]
    }

    if "Joggen" in aktivitaeten:
        items["Joggen"] = ["Laufschuhe", "Laufhosen", "Lauf Shirt",
                           "Jacke / Windstopper", "Trinkflasche", "Sporttuch"]
    if "Wandern" in aktivitaeten:
        items["Wandern"] = ["Wanderschuhe", "Wanderhose", "Wander Shirt", neue_reise["reisedauer_in_tagen"] + "x Wandersocken",
                            "Jacke / Windstopper", "Mütze / Stirnband", "Trinkflasche", "Rucksack", "erste Hilfe Ausrüstung", "Taschenlampe"]
    if "Biken" in aktivitaeten:
        items["Biken"] = ["Bikehose / Bikeshirt", "Bikeschuhe", "Bike / Ort zum Mieten raussuchen",
                          "Trinkflasche", "Bike Handschuhe", "Rucksack", "Sportbrille"]
    if "Camping" in aktivitaeten:
        items["Camping"] = ["Zelt", "Schlafmatte", "Feuerzeug", "Taschenlampe", "Trinkflasche",
                            "Rucksack", "Trainer", "Jacke / Windstopper / Regenjacke", "Besteck / Teller", "Schlafsack"]
    if "Strand" in aktivitaeten:
        items["Strand"] = ["Badetuch", neue_reise["reisedauer_in_tagen"] + "x Bikini / Badehose",
                           "Sonnenbrille", "Strandtuch", "Sonnencreme", "Flipflops", "Tasche", "Buch / Spiel", "Lockere Kleidung"]
    if "Nachtessen" in aktivitaeten:
        items["Nachtessen"] = ["Hemd", "Kleid",
                               "Schöne Schuhe", "Schmuck", "Uhr", "Mantel"]
    if "Fitness" in aktivitaeten:
        items["Fitness"] = ["Sporthose", "Sportshirt", "Sportschuhe", "Trinkflasche",
                            "Sporttuch", neue_reise["reisedauer_in_tagen"] + "x Sportsocken", "Kopfhörer"]
    if "Fotografie" in aktivitaeten:
        items["Fotografie"] = ["Kamera", "Speicherkarte", "Fototasche",
                               "Ladegerät", "Kamera Linsen", "Putztzch für Kamera", "Stativ"]
    if "Business Formal" in aktivitaeten:
        items["Business Formal"] = ["Anzug", "Hemd", "Anzugshose", "Anzugsschuhe",
                                    "Mantel", "Aktentasche", "Schmuck / Uhr", "Laptop & Ladegerät"]
    if "Arbeit" in aktivitaeten:
        items["Arbeit"] = ["Dokumente", "Schreibzeug", "Aktentasche",
                           "Laptop & Ladegerät", "Kreditkarten", "Visitenkarten", "Notizpapier"]
    if "International" in aktivitaeten:
        items["International"] = ["Visa", "Adapter", "Wörterbuch",
                                  "wichtigsten App herunterladen", "offline Karte auf Handy speichern"]

    # "Trip Speichern" löst POST request aus
    if request.method == "POST":
        ausgewaehlte_eintrage = request.form.getlist("eintrag")
        neue_reise["packliste"] = ausgewaehlte_eintrage
        meine_trips = lade_daten_aus_json("backpacker.json")
        meine_trips.append(neue_reise)
        schreibe_daten_in_json("backpacker.json", meine_trips)
        return redirect(url_for("start"))

    return render_template("result.html", items=items)


@app.route("/gespeicherte_trips/", methods=["GET", "POST"])
def gespeicherte_trips():
    meine_trips = lade_daten_aus_json("backpacker.json")

    return render_template("gespeicherte_trips.html", trips=meine_trips)


def get_items(elements, items):
        items = []
        # Get all items from json
        for elements in items:
            print(elements)
            items = items + elements.items

        return items

def get_items_count(elements, items):
    # We return a list which holds the count for each item given (we assume they are already unique)
        counts = []
        for item in items:
            current_item_count = None
            for element in elements:
                if item in element.items:
                    current_item_count = current_item_count + 1
            counts.append(current_item_count)
        return counts

@app.route("/analyse/", methods=["GET", "POST"])
def analyse():
    return render_template("analyse.html")

@app.route("/analyse/data", methods=["GET", "POST"])
def process_analyse():
    # Variable that will container the json data from file
    backpacker = None

    # Open file and set json data to backpacker
    with open('backpacker.json') as json_file:
        backpacker = json.load(json_file)

    # Get packliste in json data and store in new list
    default_dict = defaultdict(int)
    packliste_in_json = []
    for item in backpacker:
        packliste_in_json.append(item["packliste"])


    # Transform each list in a set to avoid false positives like [[1,1],[2,2]]
    for packlist in packliste_in_json:
        packliste_set = set(packlist)
        for v in packliste_set:
            default_dict[v] += 1

    # Create a dictionary that contains items with multiple occurence
    chart_dict = {}
    for value,number in default_dict.items():
        if number > 1:
            chart_dict[value] = number

    # Creates a list of tuples containing sorted values in descending order (Biggest to smallest) 
    sorted_highest = sorted(chart_dict.items(), key=lambda x: x[1], reverse=True)

    sorted_to_dict = dict(sorted_highest)

    # Get the first 5 items with highest occurence
    highest_occured_items = dict(islice(sorted_to_dict.items(), 5))

    return jsonify(highest_occured_items)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
