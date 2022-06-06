import json

#This is a sample of loading a JSON object as a string to a variable to call in other functions
with open('mydata.json', 'r') as f:
    json_object = json.loads(f.read())

#This function will print out the stated information from the JSON object, \\
#in this case, the dictionary 'people' the 2nd key in the array, the name 'Anna'
print(json_object['people'][1]['name'])