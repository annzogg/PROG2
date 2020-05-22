## Bagpacker - Projektidee

# Ausgangslage
Es kennt wohl jeder: Man geht in die Ferien und hat bestimmt noch etwas vergessen, was nun nachgekauft werden muss und damit nur unnötig Geld ausgegeben wird. Dies sollte mit meiner App vermieden werden. 


# Ideevorschlag
Die App "Bag Packer" stellt anhand der, von der Person ausgewählten Kriterien, eine Liste der Dinge zusammen, die im Urlaub nicht vergessen werden sollten und auf jeden Fall in den Koffer/Rucksack müssen. Die Grundausstattung für das Gepäck wird zurückgegeben und die ausgewählten Aktivitäten berücksichtigt. Danach kann die Reise mit all den Dingen, die bereits gepackt wurden, gespeichert werden. 

# Enthaltene Auswahlkritierien in der App

* Reiseort
* Datum der Reise
* Dauer der Reise
* Geschäftlich oder Urlaub
* Aktivitäten

# Workflow 
* Zu Beginn gibt der Nutzer den Reiseort, Reisedaten, Zeitdauer der Reise sowie Urlaub oder Geschäftlich an. 
* Aufgrund der Auswahl Urlaub oder Geschäftlich kann er die gewünschten Zusätze der Art der Reise / Aktivitäten auswählen 
* Daraus resultiert eine Packliste mit den Basics und den ausgewählten Aktivitäten, wobei die Anzahl Tag berücksichtig wurden
* Schlussendlich kann er die Sachen packen und abhacken. Die abgehackten Dinge werden zusammen mit dem Reiseort und Datum gespeichert


# Datenverarbeitung
Als Datenspeicherung wird eine JSON Datei verwendet

* Berechnung Anzahl Packsachen für die Dauer der Reise
* Berücksichtigung der Aktivitäten
* Neue Artikel hinzufügen 
* Angecklickte (gepackte) Sachen speichern
* Reise speichern 

# Ausgabe
* Packliste aufgrund der Auswahlkriterien der Aktivitäten
* Packliste mit den bereits gepackten Sachen

# Szenaorios 
[scenarios](../scenarios/scenarios.png)

