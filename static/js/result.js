// Müssen mit keys in start.py übereinstimmen
const keys = ["Unterlagen", "Hygieneartikel", "Elektronik", "Kleider", "Joggen", "Biken", "Wandern", "Camping", "Strand", "Nachtessen", "Fitness", "Fotografie", "Busniess Formal", "Arbeit", "International"];

keys.forEach(key => {
	const button = document.getElementById(`${key}-button`);
	button.addEventListener("click", () => {
		const text = document.getElementById(`${key}-input`);

		const liste = document.getElementById(`${key}-liste`);
		const liElement = document.createElement("li")
		liElement.className = "list-group-item"

		const inputElement = document.createElement("input");
		inputElement.type = "checkbox";
		inputElement.id = "listitem";
		inputElement.value = text.value;
		inputElement.name = "eintrag";

		const label = document.createElement("label");
		label.class="form-check-label";
		label.for = "listitem";
		label.innerHTML = text.value;

		liElement.appendChild(inputElement);
		liElement.appendChild(label);
		liste.appendChild(liElement);
	})

})