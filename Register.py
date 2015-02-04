#!/usr/bin/python
import json
import thread
import httplib
import urllib
'''
def registerURL (unamer):
    for j in range(2):
        email = unamer + '_' + str(j) + '@test.com'
        registerJsonString = "{\"email\": \"" + email + "\",\"password\": \"098f6bcd4621d373cade4e832627b4f6\",\"tenant\": \"fp\"}"
        postSender(registerJsonString)
    thread.exit_thread()  
    
def postSender(regJsonString):
    data = urllib.urlencode(regJsonString)
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection("ums.beta.homestyler.com:8080")
    conn.request("POST", "/v1.0/user", data, headers)
    response = conn.getresponse()
    print response.status, response.reason


def run():
    for i in range(3):
        userName = 'test_' + str(i);
        thread.start_new_thread(registerURL, (userName,))
'''

def registerURL (uname):
    for j in range(2):
        email = uname + '_' + str(j) + '@test.com'
        registerJsonString = "{\"email\": \"" + email + "\",\"password\": \"098f6bcd4621d373cade4e832627b4f6\",\"tenant\": \"fp\"}"
        postSender(registerJsonString)
    
def postSender(regJsonString):
    #data = urllib.urlencode(regJsonString)
    headers = {"Content-type": "application/json", "Accept": "application/json","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"}
    conn = httplib.HTTPConnection("ums.beta.homestyler.com:8080")
    conn.request("POST", "/v1.0/user", regJsonString, headers)
    response = conn.getresponse()
    print response.status, response.reason
    
def run():
    for i in range(3):
        userName = '_test_' + str(i);
        thread.start_new_thread(registerURL, (userName,))
        
if __name__ == '__main__':
    run()