#Save a list of dictionaries (3 students) in both JSON and Pickle, then compare the files.
import pickle
import json
with open("python_fundamental_02/q21.pkl",'wb') as f:
    student1 = {
    "name": "Ankit",
    "roll": 101,
    "marks": [90, 85, 95, 88, 91]
    }
    student2 = {
    "name": "shan",
    "roll": 102,
    "marks": [91, 85, 90, 82, 91]
    }
    student3 = {
    "name": "Amit",
    "roll": 103,
    "marks": [90, 80, 92, 88, 91]
    }
    pickle.dump(student1, f)
    pickle.dump(student2, f)
    pickle.dump(student3, f)

with open("python_fundamental_02/q21.pkl",'rb') as f:
    student1 = pickle.load(f)
    student2 = pickle.load(f)
    student3 = pickle.load(f)
    print(student1,"\n",student2,"\n",student3)

with open("python_fundamental_02/q21.json",'w') as f:
    student1 = {
    "name": "Ankit",
    "roll": 101,
    "marks": [90, 85, 95, 88, 91]
    }
    student2 = {
    "name": "shan",
    "roll": 102,
    "marks": [91, 85, 90, 82, 91]
    }
    student3 = {
    "name": "Amit",
    "roll": 103,
    "marks": [90, 80, 92, 88, 91]
    }
    json.dump((student1,student2,student3),f,indent=4)

with open("python_fundamental_02/q21.json",'r') as f:
    print(json.load(f))