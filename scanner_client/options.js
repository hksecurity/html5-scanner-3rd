var defaultColor = "blue";

var default_IP_Address = "192.168.44.135";
var default_Port_Number = "8888";

function loadOptions() {
	var IP_Address;
	var Port_Number;
	chrome.storage.sync.get('IP_Address', function(data){
		IP_Address = data['IP_Address'];

		if (IP_Address == undefined) {
			IP_Address = default_IP_Address;
		}
		document.getElementById("IP_Address").value = IP_Address;
	});
	console.log(chrome.storage);
	chrome.storage.sync.get('Port_Number', function(data){
		Port_Number = data['Port_Number'];

		if (Port_Number == undefined) {
			Port_Number = default_Port_Number;
		}
		document.getElementById("Port_Number").value = Port_Number;
		
	});

	// Valid IP Address Check
	if (IP_Address == undefined) {
		IP_Address = default_IP_Address;
	}
	
	//Valid Port Number Check
	if (Port_Number == undefined) {
		Port_Number = default_Port_Number;
	}
}
function save() {
	var data = {};
	data['IP_Address'] = document.getElementById("IP_Address").value;
	data['Port_Number'] = document.getElementById("Port_Number").value;

	chrome.storage.sync.set(data, function() {
	});

}

window.onload = loadOptions;
document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('button').addEventListener('click', save);
});
/*
function loadOptions() {
	var favColor = localStorage["favColor"];

	// valid colors are red, blue, green and yellow
	if (favColor == undefined || (favColor != "red" && favColor != "blue" && favColor != "green" && favColor != "yellow")) {
		favColor = defaultColor;
	}

	var select = document.getElementById("color");
	for (var i = 0; i < select.children.length; i++) {
		var child = select.children[i];
			if (child.value == favColor) {
			child.selected = "true";
			break;
		}
	}
}

function saveOptions() {
	var select = document.getElementById("color");
	var color = select.children[select.selectedIndex].value;
	localStorage["favColor"] = color;
}

function eraseOptions() {
	localStorage.removeItem("favColor");
	location.reload();
}
*/