function addItem():
	var input = document.getElementById("userinput");
	var ul = document.querySelector("ul");

button.addEventListener("click", function() {
  var li = document.createElement("li");
  li.className = 'list-group-item';
  li.textContent = input.value;
  ul.appendChild(li);
})