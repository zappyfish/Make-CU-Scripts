import json
import os


def sendURL():
    os.system("curl  http://localhost:4040/api/tunnels > tunnels.json")

    with open('tunnels.json') as data_file:
        datajson = json.load(data_file)



    for i in datajson['tunnels']:
      msg = i['public_url']
      break

    #msg variable contains URL
    return msg
