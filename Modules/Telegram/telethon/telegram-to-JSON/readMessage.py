# importing the module
import json

# Opening JSON file
with open('channel_messages.json') as json_file:
    data = json.load(json_file)
    
    for i in range(0,3):
        print(data[i]["message"])
        print("-----------------")

