# program 1
# name:numberofSkills

students =  ["student1","student2","student3","student4"]
marks = [11,22,33,44,55,66,77,88,99,00]
info = ["sai","wate",26,True]

# program 1

students = [
    {
        "firstName":"sai",
        "lastName":"wate",
        "age": 86,
        "city":"Chandigarh",
        "skills":["python","html","css"]
    },

    {
        "firstName":"appam",
        "lastName":"deshe",
        "age":56,
        "city":"pune",
        "skills":["djnago","tosca","css","javascript"]
    }
    ,
    {
        "firstName":"amol",
        "lastName":"nimbalkar",
        "age":35,
        "city":"warora",
        "skills":["sql","powerBI"]
    }


]



for student in students:
    print(student['firstName'], len(student['skills']))  #   sai 3, appam 4, amol 2

# program 2
# name of person living at pune
for student in students:
    if(student['city'] == "pune"):
        print(student['firstName'])  #   appam

# program 3
# add a property
# institude:minskole
for student in students:
    student.update({"institude": "minskole"})
print(students)

# program 4
# add the skill of every user - "prompt engineering"
for student in students:
    student['skills'].append('prompt engineering')
print(students)

# program 5
# average age of all students
totalAge = 0
for student in students:
    totalAge += student['age']
print(totalAge/len(students))  #   59.0

# program 6
# name of person with python skills
for student in students:
    if "python" in student['skills']:
        print(student['firstName'])  #   sai
