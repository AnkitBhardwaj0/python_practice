#Save a list of 10 numbers in a JSON file and read it back
import json
with open("python_fundamental_02/q19.json",'w') as f:
    number =list(range(1,11))
    json.dump(number,f)
with open("python_fundamental_02/q19.json",'r') as f:
    print(json.load(f))