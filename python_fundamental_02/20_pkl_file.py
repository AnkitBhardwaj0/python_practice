#Save a dictionary of student marks in a Pickle file and read it back.
import pickle
with open("python_fundamental_02/q20.pkl",'wb') as f:
    student = {
    "name": "Ankit",
    "roll": 101,
    "marks": [90, 85, 95, 88, 91]
}
    pickle.dump(student,f)
with open("python_fundamental_02/q20.pkl",'rb') as f:
    print(pickle.load(f))