import urllib
import urllib2

class Server:

    def __init__(self):
        self.url = "https://pingfyp.herokuapp.com/api/persons"
        self.tname=""
    def send_to_server(self,name, faculty):
        value = dict()
        url = self.url
        value['name'] = name
        value['faculty'] = faculty
        # This urlencodes your data (that's why we need to import urllib at the top)
        try:
            data = urllib.urlencode(value)
        # Send HTTP POST reques
            request = urllib2.Request(url, data)
        #print "Error: Sending Data to Server"
            response = urllib2.urlopen(request)
            html = response.read()
            if html['tname'] != None:
                self.tname= html['tname']

        except:
            print "Error: Sending Data to Server"
        else:
            print html