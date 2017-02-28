function get_source(document_body) {
    chrome.tabs.executeScript(
    {
        code: "document.getElementsByTagName('html')[0].outerHTML;"
    },
    function (ps1) {
        // url : current tab url
        // ps1 : current html
        // window.alert(url + "\n" + ps1);

        // Info Send
        var ws = new WebSocket("ws://192.168.254.130:8888/ws");
        ws.onopen = function (e) {
            // ws.send(url);
            ws.send(ps1);
            ws.onmessage = function (event) {
                window.alert(event.data);
                document.body.innerText = event.data;
                return event.data;
            }
        }

    });

}

function psl() {
        // url : current tab url
        // ps1 : current html
        // window.alert(url + "\n" + ps1);

        // Info Send
        var ws = new WebSocket("ws://192.168.254.130:8888/ws");
        ws.onopen = function (e) {
            // ws.send(url);
            ws.send(ps1);
            ws.onmessage = function (event) {
                window.alert(event.data);
                document.body.innerText = event.data;
                return event.data;
            }
        }

    });

window.onload = psl();
chrome.extension.sendMessage({
    action: "getSource",
    source: get_source(document)
});