#!/usr/bin/python
# coding: utf-8

import datetime
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import re
import os
import script_scanner

os.chdir('/etc/jsunpack-n')
p = re.compile('(<html|<HTML)')

class WSHandler(tornado.websocket.WebSocketHandler):
    clients = []

    def check_origin(self, origin):
        return True

    def open(self):
        print '[%s] new connection' % str(datetime.datetime.now()).split('.')[0]
        WSHandler.clients.append(self)

    def on_message(self, message):
        print '[%s] Analysis Start' % str(datetime.datetime.now()).split('.')[0]
        msg = message.encode("utf-8")

        # URL
        if p.match(msg) == None:
            pass

        # HTML
        elif p.match(msg) != None:
            f = open('/tmp/tmp.html', 'wb')
            f.write(msg)
            f.close()
            cmd = './jsunpackn-single.py -V %s' % '/tmp/tmp.html'
            jsunpack_result = os.popen(cmd).read()
            jsunpack_list = []
            for line in jsunpack_result.splitlines():
                if line.strip()[:5] != 'error':
                    jsunpack_list.append(line.strip())
            jsunpack_list[0] = jsunpack_list[0][:jsunpack_list[0].rfind(']')+1]

            jsunpack_flag = 0
            for line in jsunpack_list:
                if line.find('malicious') >= 0:
                    jsunpack_flag = 1
                    break
                elif line.find('suspicious') >= 0:
                    jsunpack_flag = 0.5
                    break

            scanner_result = script_scanner.scan(msg)
            for i in range(len(scanner_result)):
                 scanner_result[i] = str(scanner_result[i])
            scanner_result = ','.join(scanner_result)
            self.write_message(scanner_result + '\n' + str(jsunpack_flag) + '\n' + '\n'.join(jsunpack_list))

        print '[%s] Analysis End' % str(datetime.datetime.now()).split('.')[0]


    def on_close(self):
        print '[%s] connection closed' % str(datetime.datetime.now()).split('.')[0]
        WSHandler.clients.remove(self)

    @classmethod
    def write_to_clients(cls):
        print "[%s] Writing to clients" % str(datetime.datetime.now()).split('.')[0]


application = tornado.web.Application([(r'/ws', WSHandler),])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().add_timeout(datetime.timedelta(seconds=120), WSHandler.write_to_clients)
    tornado.ioloop.IOLoop.instance().start()
