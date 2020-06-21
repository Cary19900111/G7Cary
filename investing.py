#!/usr/bin/env python
# -*- coding:utf-8 -*- 

import websocket
import requests
import re
import random
import string
import ssl
import certifi
import json
import _thread
import time


class Investing(object):

    subscribeChannel = []

    def __init__(self, subscribeChannel):
        websocket.enableTrace(True)
        self.subscribeChannel = subscribeChannel

    def __onWebsocketOpen(self):
        print("open")
        pass
    
    def __onWebsocketMessage(self, m):
        print("reviced message : " + m)
        if (m == "o") :
            subs = {"_event": "bulk-subscribe", "tzID": self.timeZoneId, "message": "%%".join(self.subscribeChannel)}
            subsjson = json.dumps(subs)
            subsjson = json.dumps([subsjson])
            
            print(subsjson)
            self.ws.send(subsjson)

            uids = {"_event": "UID", "UID":0}
            uidsjson = json.dumps(uids)
            uidsjson = json.dumps([uidsjson])
           
            print(uidsjson)
            self.ws.send(uidsjson)

            _thread.start_new_thread(self.__heartbeat, ())
            
        
    def __heartbeat(self):
        time.sleep(5)

        heartbeatObj = {
            "_event": "heartbeat",
            "data": "h"
        }
        heartbeat = json.dumps(heartbeatObj)
        heartbeat = json.dumps([heartbeat])
        # heartbeat = '["{"_event":"heartbeat","data":"h"}"]'
        print(heartbeat)
        self.ws.send(heartbeat)
        

    def __onWebsocketError(self, exception):
        print("error : " + str(exception))
        pass

    def __onWebsocketClose(self):
        print("close")
        pass

    def __onWebsocketPing(self,  m):
        print("ping " + m)
        pass

    def __onWebsocketPong(self,  m):
        print("pong " + m)
        pass

    def __onWebsocketData(self,  m, t, c):
        print("data " + m + " " + str(t) + " " + str(c))
        pass

    def __onWebsocketContMsg(self,  m, c):
        print("contmsg " + m + " " + str(c))
        pass

    def __predo(self):
        pageResp = requests.request("get", "https://cn.investing.com/commodities/", headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"})
        if (pageResp.status_code != 200) :
            raise RuntimeError("status code illegal")
        self.timeZoneId = re.findall(r'var\ TimeZoneID\ =\ .\"(\d+)\"', pageResp.text)[0]
        streamUrl = re.findall(r';window\.stream\ =\ \"(http.*)\";', pageResp.text)[0]
        streamUrl = "wss" + streamUrl[5:] if streamUrl[5:] != "https" else "ws" + streamUrl[4:]
        random8Str = ''.join(random.sample(string.ascii_lowercase + string.digits, 8))
        server = random.randint(100, 999)
        self.websocketUrl = streamUrl + "/echo/" + str(server) + "/" + random8Str + "/websocket"

    def connWebsocket(self):
        self.__predo()


        ws = websocket.WebSocketApp(self.websocketUrl, 
            on_open=self.__onWebsocketOpen, 
            on_message=self.__onWebsocketMessage,
            on_error=self.__onWebsocketError,
            on_close=self.__onWebsocketClose,
            on_ping=self.__onWebsocketPing,
            on_pong=self.__onWebsocketPong,
            on_data=self.__onWebsocketData,
            on_cont_message=self.__onWebsocketContMsg,
            header={
                "Origin": "https://cn.investing.com",
                "User-Agant": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                "Cache-Control": "no-cache"})

        self.ws = ws

    def close(self):
        self.ws.close()

    def forever(self):
        self.ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
        

if __name__ == "__main__":
    inv = Investing(subscribeChannel=[
        "pid-1:",
            "pid-2:",
            "pid-3:",
            "pid-5:",
            "pid-7:",
            "pid-146:",
            "pid-8:",
            "pid-2111:",
            "pid-1486:",
            "pid-10027:",
            "pid-40820:",
            "pid-28930:",
            "pid-179:",
            "pid-178:",
            "pid-8873:",
            "pid-8839:",
            "pid-8827:",
            "pid-9:",
            "pid-10:",
            "pidTechSumm-1:",
            "pidTechSumm-2:",
            "pidTechSumm-3:",
            "pidTechSumm-5:",
            "pidTechSumm-7:",
            "pidTechSumm-9:",
            "pidTechSumm-10:",
            "isOpenExch-54:",
            "isOpenExch-21:",
            "isOpenExch-20:",
            "isOpenPair-8873:",
            "isOpenPair-8839:",
            "isOpenPair-8827:"
    ])
    inv.connWebsocket()
    inv.forever()

    while (True):
        pass

    # ws = websocket.create_connection('wss://stream138.forexpros.com/echo/072/7w51txmq/websocket', timeout=10)

    # # {"_event":"bulk-subscribe","tzID":28,"message":"pid-8833:%%pid-44634:%%pid-985364:%%pid-40820:%%pid-28930:%%pid-179:%%pid-942630:%%pid-8873:%%pid-8839:%%pid-8827:%%pid-1055949:%%pid-1:%%pid-2:%%pid-3:%%pid-5:%%pid-7:%%pid-9:%%pid-10:%%pidTechSumm-1:%%pidTechSumm-2:%%pidTechSumm-3:%%pidTechSumm-5:%%pidTechSumm-7:%%pidTechSumm-9:%%pidTechSumm-10:%%pidExt-8833:%%isOpenExch-1:%%isOpenExch-97:%%isOpenExch-54:%%isOpenExch-21:%%isOpenExch-103:%%isOpenExch-1004:%%isOpenPair-8833:%%isOpenPair-8873:%%isOpenPair-8839:%%isOpenPair-8827:%%cmt-6-5-8833:%%domain-6:"}
    # # {"_event":"bulk-subscribe","tzID":28,"message":"pid-40820:%%pid-100634:%%pid-100541:%%pid-942827:%%pid-100933:%%pid-100448:%%pid-996084:%%pid-100736:%%pid-100907:%%pid-953917:%%pid-102952:%%pid-100468:%%pid-101094:%%pid-100425:%%pid-100530:%%pid-100883:%%pid-28930:%%pid-179:%%pid-942630:%%pid-8873:%%pid-8839:%%pid-8827:%%pid-1055949:%%pid-1:%%pid-2:%%pid-3:%%pid-5:%%pid-7:%%pid-9:%%pid-10:%%pid-8833:%%pidTechSumm-1:%%pidTechSumm-2:%%pidTechSumm-3:%%pidTechSumm-5:%%pidTechSumm-7:%%pidTechSumm-9:%%pidTechSumm-10:%%pidExt-40820:%%isOpenExch-54:%%isOpenExch-21:%%isOpenExch-103:%%isOpenExch-1004:%%isOpenPair-8873:%%isOpenPair-8839:%%isOpenPair-8827:%%cmt-6-5-40820:%%domain-6:"}
    # # ws.send('[{"_event":"bulk-subscribe","tzID":28,"message":"pid-40820"}]')
    # ws.send('[{"_event":"UID","UID":0}]')
    # data = ws.recv()
    # print(data)


    """



    <script>var TimeZoneID = +"28";window.timezoneOffset = +"28800";window.stream = "https://stream229.forexpros.com:443";</script>



    base_url = https://stream225.forexpros.com:443/echo
    random = random_string(8)
    server = random_number_string(1e3)


    url = base_url + server + random

is open pair 是开放的
isOpenExch 公开交换

		$(window).trigger('appendNewData',[[
            "pid-1:",
            "pid-2:",
            "pid-3:",
            "pid-5:",
            "pid-7:",
            "pid-146:",
            "pid-8:",
            "pid-2111:",
            "pid-1486:",
            "pid-10027:",
            "pid-40820:",
            "pid-28930:",
            "pid-179:",
            "pid-178:",
            "pid-8873:",
            "pid-8839:",
            "pid-8827:",
            "pid-9:",
            "pid-10:",
            "pidTechSumm-1:",
            "pidTechSumm-2:",
            "pidTechSumm-3:",
            "pidTechSumm-5:",
            "pidTechSumm-7:",
            "pidTechSumm-9:",
            "pidTechSumm-10:",
            "isOpenExch-54:",
            "isOpenExch-21:",
            "isOpenExch-20:",
            "isOpenPair-8873:",
            "isOpenPair-8839:",
            "isOpenPair-8827:"]]);



tzID = windows.tz
message = json("%%")

    < o
    > ["{\"_event\":\"bulk-subscribe\",\"tzID\":28,\"message\":\"pid-8849:%%pid-44794:%%pid-14218:%%pid-1014132:%%pid-14208:%%pid-44793:%%pid-1075589:%%pid-996464:%%pid-1159065:%%pid-40820:%%pid-28930:%%pid-179:%%pid-178:%%pid-8873:%%pid-8839:%%pid-8827:%%pid-1:%%pid-2:%%pid-3:%%pid-5:%%pid-7:%%pid-9:%%pid-10:%%pidTechSumm-1:%%pidTechSumm-2:%%pidTechSumm-3:%%pidTechSumm-5:%%pidTechSumm-7:%%pidTechSumm-9:%%pidTechSumm-10:%%pidExt-8849:%%isOpenExch-1:%%isOpenExch-95:%%isOpenExch-54:%%isOpenExch-21:%%isOpenExch-20:%%isOpenPair-8849:%%isOpenPair-8873:%%isOpenPair-8839:%%isOpenPair-8827:%%cmt-6-5-8849:%%domain-6:\"}"]
    > ["{\"_event\":\"UID\",\"UID\":0}"]
    
    ...
    < a["{\"message\":\"pid-7::{\\\"pid\\\":\\\"7\\\",\\\"last_dir\\\":\\\"greenBg\\\",\\\"last_numeric\\\":1.419,\\\"last\\\":\\\"1.4190\\\",\\\"bid\\\":\\\"1.4189\\\",\\\"ask\\\":\\\"1.4191\\\",\\\"high\\\":\\\"1.4208\\\",\\\"low\\\":\\\"1.4152\\\",\\\"last_close\\\":\\\"1.4169\\\",\\\"pc\\\":\\\"+0.0021\\\",\\\"pcp\\\":\\\"+0.15%\\\",\\\"pc_col\\\":\\\"greenFont\\\",\\\"turnover\\\":\\\"57.81K\\\",\\\"turnover_numeric\\\":\\\"57807\\\",\\\"time\\\":\\\"9:02:29\\\",\\\"timestamp\\\":1585645348}\"}"]
    ...

    < a["{\"_event\":\"heartbeat\",\"data\":\"h\"}"]
    > ["{\"_event\":\"heartbeat\",\"data\":\"h\"}"]
    """