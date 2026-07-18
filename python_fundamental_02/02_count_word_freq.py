#Count word frequency using a dictionary.
with open("python_fundamental_02/q2.txt",'w')as f:
    f.write("Python is one of the most popular programming languages in the world. It is easy to learn and easy to read. Many students choose Python because it is simple and powerful. Python is used for web development, data analysis, artificial intelligence, machine learning, automation, and software development. Learning Python requires regular practice. Practice helps students improve their programming skills and build real-world projects. Consistent learning and practice are the keys to becoming a good programmer.")


with open("python_fundamental_02/q2.txt",'r') as f:
    data=f.read().split()
    freq_dict={}
    for word in data:
        if word not in freq_dict:
            freq_dict[word]=1
        else:
            freq_dict[word]+=1
print("word freq")
for key, value in freq_dict.items():
    print(f"{key} : {value}")
        