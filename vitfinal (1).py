import json
import os
import numpy as np

# file where all data will be saved
DATA_FILE = "students.json"

# reading data
def loadData():

    if not os.path.exists(DATA_FILE):
        return {"students": {}}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# saving data
def saveData(obj):
    with open(DATA_FILE, "w") as f:
        json.dump(obj, f, indent=2)
# adding new student
def addStudent():
    data = loadData()
    name = input("Enter student name: ").strip()
    roll = input("Enter roll no (unique pls): ").strip()
    if roll in data["students"]:
        print("Roll number already present :(")
        return
    data["students"][roll] = {
        "name": name,
        "marks": {},
        "credits": {}
        }
    saveData(data)
    print("Student added successfully!")

# deleting student
def deleteStudent():

    data = loadData()

    roll = input("Enter roll to delete: ").strip()



    if roll in data["students"]:

        del data["students"][roll]

        saveData(data)

        print("Deleted successfully.")

    else:

        print("Roll not found.")

# entering marks
def enterMarks():
    data = loadData()
    roll = input("Enter roll no to enter marks: ")
    if roll not in data["students"]:
        print("Invalid roll number")
        return
    try:
        entries = input("Enter marks like sub:marks:credits (comma separated): ").split(",")
        for e in entries:
            sub, m, c = e.split(":")
            marks = int(m)
            credit = int(c)
            if marks < 0 or marks > 100:
                print("Marks should be between 0-100.")
                return
            data["students"][roll]["marks"][sub.strip()] = marks
            data["students"][roll]["credits"][sub.strip()] = credit
        saveData(data)
        print("Marks saved!")
    except:
        print("Format error!! use sub:marks:credits properly")

# deletion of one subject
def deleteSubject():
    data = loadData()
    roll = input("Enter roll no: ").strip()
    if roll not in data["students"]:
        print("Roll not found.")
        return
    sub = input("Enter subject to delete: ").strip()
    if sub in data["students"][roll]["marks"]:
        del data["students"][roll]["marks"][sub]
        del data["students"][roll]["credits"][sub]
        saveData(data)
        print("Subject deleted.")
    else:
        print("Subject not found.")

# GPA mapping
def gpa(score):
    if score >= 90: return 10
    if score >= 80: return 9
    if score >= 70: return 8
    if score >= 60: return 7
    if score >= 50: return 6
    return 0

# showing full result
def showResult():
    data = loadData()
    roll = input("Enter roll no: ")
    if roll not in data["students"]:
        print("No such roll!")
        return
    stud = data["students"][roll]
    marks = stud["marks"]
    creds = stud["credits"]
    if len(marks) == 0:
        print("No marks entered yet.")
        return
    total = sum(marks.values())
    percentage = (total / (len(marks) * 100)) * 100
    tot_points = 0
    tot_creds = 0
    for s in marks:
        gp = gpa(marks[s])
        cr = creds[s]
        tot_points += gp * cr
        tot_creds += cr
        cgpa = tot_points / tot_creds
        print("\n---- REPORT CARD ----")
        print("Name:", stud["name"])
        print("Roll:", roll)
        print("Marks:", marks)
        print("Total:", total)
        print("Percentage:", round(percentage, 2))
        print("CGPA:", round(cgpa, 2))
        print("----------------------")

# class analytics
def classAnalysis():
    data = loadData()
    totals = []
    for r, s in data["students"].items():
        if len(s["marks"]) == 0:
            continue
        totals.append(sum(s["marks"].values()))
        if len(totals) == 0:
            print("Not enough data for analysis.")
            return
    arr = np.array(totals)
    print("\n--- Class Stats ---")
    print("Avg:", round(arr.mean(), 2))
    print("Max:", arr.max())
    print("Min:", arr.min())
    print("Std Dev:", round(arr.std(), 2))

# topper list
def toppers():
    data = loadData()
    all_data = []
    for r, s in data["students"].items():
        if len(s["marks"]) == 0: continue
        total = sum(s["marks"].values())
        all_data.append((total, r, s["name"]))
    if not all_data:
        print("No data :(")
        return
    all_data.sort(reverse=True)
    print("\n*** TOPPERS ***")
    rank = 1
    for total, roll, name in all_data:
        print(f"Rank {rank}: {name} ({roll})  Total = {total}")
        rank += 1
# simple menu
def menu():
    while True:
        print("""

===== STUDENT RESULT SYSTEM =====

1. Add Student
2. Delete Student
3. Enter Marks
4. Delete Subject
5. Show Result
6. Class Analysis
7. Toppers
8. Exit
""")
        ch = input("Enter choice: ")
        if ch == "1": addStudent()
        elif ch == "2": deleteStudent()
        elif ch == "3": enterMarks()
        elif ch == "4": deleteSubject()
        elif ch == "5": showResult()
        elif ch == "6": classAnalysis()
        elif ch == "7": toppers()
        elif ch == "8":
            print("Bye! Saving data...")
            break
        else:
            print("Invalid choice!")
menu() 