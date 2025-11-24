# inventarry-and-billing-management-system
Student Result System – README (Text Version)
This is a small Python project I made to manage student records and calculate results.
The program runs in the terminal and stores everything in a JSON file, so there is no need for any database.

What this program can do
	•	Add a new student with name and roll number
	•	Delete a student
	•	Enter marks for different subjects along with their credits
	•	Remove a subject from a student’s record
	•	Show the full report of any student (marks, percentage, CGPA, etc.)
	•	Display class statistics like average, maximum, minimum, and standard deviation
	•	Show the topper list based on total marks

All the data is stored automatically in students.json.
How the marks entry works
Marks are entered in one line in the format:
subject:marks:credits

Example:
Math:95:4, Physics:88:3

The program checks if marks are valid (0–100) and then saves everything.

GPA System Used
The CGPA is calculated using this simple GPA mapping:
	•	90 and above → 10
	•	80–89 → 9
	•	70–79 → 8
	•	60–69 → 7
	•	50–59 → 6
	•	Below 50 → 0

The final CGPA is based on weighted credits.

Menu Options in the Program
When you run the file, you will see a menu like this:
1. Add Student
2. Delete Student
3. Enter Marks
4. Delete Subject
5. Show Result
6. Class Analysis
7. Toppers
8. Exit

You can choose any option by typing the number.
How to run the project
	1.Make sure Python 3 is installed
	2.Install NumPy (needed for analytics):
pip install numpy
	3.Run the Python file:
python main.py
The program will create students.json automatically if it does not exist.

What the data file looks like
This is the structure that gets saved:

{
  "students": {
    "101": {
      "name": "Amit",
      "marks": {
        "Math": 95,
        "Physics": 88
      },
      "credits": {
        "Math": 4,
        "Physics": 3
      }
    }
  }
}

Additional Notes
This project is simple on purpose so that it’s easy to understand.
It can be expanded later, like adding a GUI, exporting results, or adding a login system.
But for now, it works well for basic student result management.
