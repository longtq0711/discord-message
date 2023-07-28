import requests
import json


def retrieve_message(channelId):
    headers= {
        'authorization': 'NDg2NTI4NDQyMDg3NzY4MDY0.G-mZgF.lyAxlMiOQXCV3PxkoyOJeXhpyNIR3VqsF2LUgA'
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelId}/messages', headers=headers)
    jsonn = json.loads(r.text)
    for value in jsonn:
        if value['content'].find('HaNoi') != -1:
            print(value['content'], '\n')

retrieve_message(259536527221063683)