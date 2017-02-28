# HTML5-Scanner-3rd

##Summary
This application is for people who want to know that web pages have vulnerabilities.
The main purpose of this application is scanning (obfuscated) Javascript and HTML5 script.

##Server
Please make sure that your Ubuntu version is 16.04 or higher. If you want to install the service, please run the script below,

\# scanner_server/install.sh 

This script will install the following libraries automatically:
- libpcap-dev
- pkg-config
- python-dev
- libgtk2.0-dev
- libnet1-dev
- python-pip
- python-tornado

Once the installation is successful, run the script below to listen requests from the client,

$ listener

##Client
Please download the scanner_client.crx and visit the "Settings" page in your Chrome. Then drag-drop the *.crx file. Chrome will ask if you want to add the extension to your browser. Click on "Add" to manually install the extention.

To reconfigure the IP address and Port number of server, right click on the extension icon so that you can config the extension.

1) Visit a web page you want to check

2) Click on the extension icon and wait a moment (generally the task is completed within 3 seconds.).

Check the server is working correctly if there is something wrong.
