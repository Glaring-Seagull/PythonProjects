import json
#This project is like the last in this serise but using a slightly more complicated dataset 
#Like Project I, this will open our json file and load it to the variable json_object
with open('response.json', 'r') as f:
    json_object = json.loads(f.read())

#This print statement is targeting the "ip_address key in our first dict"
print(json_object['computer_commands']['computer_command'][0]['computers']['computer']['ip_address'])