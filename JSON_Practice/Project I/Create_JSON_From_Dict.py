import json

#this is the data we are going to turn into a JSON file
mydict = {
  "people": [
    {
      "name": "Bob",
      "age": 28,
      "weight": 80
    },
    {
      "name": "Anna",
      "age": 34,
      "weight": 67
    },
    {
      "name": "Charles",
      "age": 45,
      "weight": 78
    },
    {
      "name": "Daniel",
      "age": 34,
      "weight": 110
    }
  ]
}

#This will take our json, defined as a dictonary in 'mydict' and saved to  \\
# the variable 'json_string' with an indent of 2.
json_string = json.dumps(mydict, indent=2)
#This will open the json file in write mode (indicated by 'w')
with open ('mydata.json', 'w') as f:
    f.write(json_string)