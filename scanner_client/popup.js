chrome.extension.onMessage.addListener(function (request, sender) {
    if (request.action == "getSource") {
        document.body.innerText = request.source;
    }
});

function ps1() {
    // url : current tab url
    // ps1 : current html
    // window.alert(url + "\n" + ps1);

    chrome.tabs.executeScript(
	{
	    code: "document.getElementsByTagName('html')[0].outerHTML;"
	},
	function (ps1) {
	    // url : current tab url
	    // ps1 : current html
	    // window.alert(url + "\n" + ps1);

	    
		var address;
		var setting_Info = ['IP_Address', 'Port_Number'];

		chrome.storage.sync.get(setting_Info, function(data){
			// Setting load
			address = "ws://"+data['IP_Address']+":"+data['Port_Number']+"/ws";
			console.log(address);
			var ws = new WebSocket(address);
			
			//start
			ws.onopen = function (e) {
				ws.send(ps1);
				ws.onmessage = function (event) {
					document.body.innerText = event.data;
					var event_log = event.data.split('\n');

					//Title
					document.write("<B><center><font size=6>Web Page Vulnerability Analyzer</font></center></B>");
					document.write("<table width='100%' height='50%' border='0' cellspacing='0' cellpadding='0'")
					
					//Table
					document.write("<tr>")
					document.write("<td align='center'>")
	 
					document.write("<table border='1' cellspacing='1' cellpadding='0' bgcolor='#000000'>");

					var functions_id = new Array('CookieSniffing', 'Cors', 'CrossDocumentMessaging', 'Csrf', 'FileApi', 'FileDownload', 'GeolocationApi', 'Localdb', 'NewTagAbusing', 'ProtocolScheme', 'ScriptDDoS', 'Websocket', 'Webstorage', 'Webworker');
					var functions_name = new Array('Cookie Sniffing', 'CORS', 'Cross Document Messaging', 'CSRF', 'File Api', 'File Download', 'Geolocation Api', 'Local DB', 'New Tag Abusing', 'Protocol Scheme', 'Script DDoS', 'Websocket', 'Webstorage', 'Webworker');
					var result = event_log[0].split(',');

					for (i = 0; i < 3; i++) {
						colspan = '4'
						if (i == 2)
							colspan = '5'
						document.write("<tr>");
						for (j = 0; j < 5; j++) {
							if (i * 5 + j == 14)
								break;
							if (result[i * 5 + j] == '0')
								color = '#3498DB';
							else {
								color = '#E74C3C';
							}
							tmp = "<td id=" + functions_id[i * 5 + j] + " colspan='" + colspan + "' width='100' height='50' bgcolor='" + color + "' align=center><b>" + functions_name[i * 5 + j] + "</b></td>";
							document.write(tmp);
						}
						document.write("</tr>");
					}	            

					
					if (event_log[1] == '0')
						color = '#3498DB';
					else if(event_log[1] == '0.5') {
						color = '#FE9903';
					}
					else {
						color = '#E74C3C';
					}

					
					document.write("<tr>");
					document.write("<td id=jsunpack_ana colspan='20' width='500' height='50' bgcolor='" + color + "' align=center><b>");
					
					document.write('<button style="height:100%;width:100%;background-color:Transparent;outline:none;border: none;" type="button" id="analysisBtn" onclick="func123"><b><font size="4">Javascript Vulnerability Analysis<br/>(Click)</font></b></button>');
					
					
					document.write("</b></td>");
					document.write("</tr>");
					
					
					document.write("</table>");
	 
					document.write("</td>");
					document.write("</tr>");
					document.write("</table>");

					//var button = document.createElement("button");
					
					//button.innerHTML = "Detail";
					
					// 2. Append somewhere
					var body = document.getElementById("analysisBtn");
					//body.appendChild(button);
					var flag = 0;
					// 3. Add event handler
					body.addEventListener ("click", function() {
						if(flag == 0){
							var tmp = "\n";
							for (var i = 2; i < event_log.length; i++) {
								tmp = tmp + event_log[i] + "<br/><br/>";
							}
							//label.innerHTML = tmp;
							
							document.write("<table width='100%'")
							document.write("<tr>")
							document.write('<td style="word-wrap:break-word;">')
							document.write('<div style="overflow-y:scroll; width:500px; height:180px; border: 3px solid;">')
							document.write(tmp);
							document.write('</div>')
							
							document.write("</td>");
							document.write("</tr>");
							document.write("</table>");
							
							flag = 1;
						}
						
					});
					document.write();
				}
			}
		});
	}
    );
}

window.onload = ps1;



