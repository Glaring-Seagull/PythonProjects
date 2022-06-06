import json

#Like Project I, this will open our json file and load it to the variable json_object
with open('response.json', 'r') as f:
    json_object = json.loads(f.read())

print(json_object['computer_commands']['computer_command'][0]['computers']['computer']['ip_address'])