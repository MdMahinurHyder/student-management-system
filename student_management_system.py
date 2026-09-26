import os
import json

STUDENT_FILE = "student1.json"

def _load_json(filename):
    """Load a JSON file into a dict. Returns {} if missing, empty, or corrupted."""
    if not os.path.exists(filename):
        return {}
    try:
        with open(filename, "r") as f:
            content = f.read().strip()
            if not content:
                return {}
            return json.loads(content)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error reading {filename}: {e}")
        return {}


def _save_json(filename, data):
    """Write a dict to a JSON file. Returns True on success."""
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        return True
    except IOError as e:
        print(f"Error writing to {filename}: {e}")
        return False

def get_all_students():
    return _load_json(STUDENT_FILE)

class Student:

    def __init__(self, name, age, student_id, department, marks):
        self.name =  name
        self.age = age
        self.student_id = student_id
        self.department = department
        self.marks = marks

    def display(self):
        try:
            print(f"Hey there mate. My name is {self.name}, my id is {self.student_id}, "
                f"I'm in {self.department} department, and I scored {self.marks}.")
        except Exception as e:
            print(f"Error in display(): {e}")

    def is_passed(self):
        try:
            if self.marks > 40:
                print("Yes, you passed.")
                return True
            elif self.marks == 40:
                print("You barely passed.")
                return True
            else:
                print("Sorry, you failed.")
                return False
        except Exception as e:
            print(f"Error in is_passed(): {e}")
            return None
        
    def save_to_json(self, filename=STUDENT_FILE):
        try:
            data = _load_json(filename)
        
            if self.student_id in data:
                print(f"Error: Student ID '{self.student_id}' is already saved.")
                return False
        
            data[self.student_id] = {
                "name": self.name,
                "age": self.age,
                "student_id": self.student_id,
                "department": self.department,
                "marks": self.marks
            }
        
            if _save_json(filename, data):
                print(f"Student '{self.name}' saved successfully.")
                return True
            return False
        
        except Exception as e:
            print(f"Error in save_to_json(): {e}")
            return False

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "student_id": self.student_id,
            "department": self.department,
            "marks": self.marks
        }

def add_student():
    data = get_all_students()
 
    student_id = input("Enter Student ID: ").strip()
    if not student_id:
        print("Student ID cannot be empty.")
        return
    if student_id in data:
        print(f"Error: Student ID '{student_id}' already exists.")
        return
 
    name = input("Enter Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
 
    try:
        age = int(input("Enter Age: ").strip())
        marks = float(input("Enter Marks: ").strip())
    except ValueError:
        print("Invalid input: Age must be a whole number and Marks must be a number.")
        return
 
    department = input("Enter Department: ").strip()
 
    student = Student(name, age, student_id, department, marks)
    data[student_id] = student.to_dict()
 
    if _save_json(STUDENT_FILE, data):
        print(f"Student '{name}' added successfully.")
 
 
def remove_student():
    data = get_all_students()
    student_id = input("Enter Student ID to remove: ").strip()
 
    if student_id not in data:
        print(f"No student found with ID '{student_id}'.")
        return
 
    removed = data.pop(student_id)
    if _save_json(STUDENT_FILE, data):
        print(f"Student '{removed['name']}' (ID: {student_id}) removed successfully.")
 
 
def search_student():
    data = get_all_students()
    student_id = input("Enter Student ID to search: ").strip()
 
    record = data.get(student_id)
    if not record:
        print(f"No student found with ID '{student_id}'.")
        return
 
    student = Student(**record)
    student.display()
 
 
def update_student():
    data = get_all_students()
    student_id = input("Enter Student ID to update: ").strip()
 
    if student_id not in data:
        print(f"No student found with ID '{student_id}'.")
        return
 
    record = data[student_id]
    print("Leave a field blank to keep its current value.")
 
    name = input(f"Name [{record['name']}]: ").strip()
    age = input(f"Age [{record['age']}]: ").strip()
    department = input(f"Department [{record['department']}]: ").strip()
    marks = input(f"Marks [{record['marks']}]: ").strip()
 
    if name:
        record["name"] = name
    if age:
        try:
            record["age"] = int(age)
        except ValueError:
            print("Invalid age entered, keeping previous value.")
    if department:
        record["department"] = department
    if marks:
        try:
            record["marks"] = float(marks)
        except ValueError:
            print("Invalid marks entered, keeping previous value.")
 
    data[student_id] = record
    if _save_json(STUDENT_FILE, data):
        print(f"Student '{record['name']}' (ID: {student_id}) updated successfully.")
 
 
def display_students():
    data = get_all_students()
    if not data:
        print("No students found.")
        return
 
    print("-" * 70)
    for record in data.values():
        Student(**record).display()
    print("-" * 70)
    print(f"Total students: {len(data)}")
 
 
def calculate_average():
    data = get_all_students()
    if not data:
        print("No students found.")
        return
 
    total = sum(record["marks"] for record in data.values())
    avg = total / len(data)
    print(f"Average marks of {len(data)} student(s): {avg:.2f}")
 
 
def find_highest_scorer():
    data = get_all_students()
    if not data:
        print("No students found.")
        return
 
    top_id, top_record = max(data.items(), key=lambda item: item[1]["marks"])
    print(f"Highest scorer: {top_record['name']} (ID: {top_id}) with {top_record['marks']} marks.")
 
 
def save_data():
    data = get_all_students()
    filename = input(f"Enter filename to save to [{STUDENT_FILE}]: ").strip() or STUDENT_FILE
    if _save_json(filename, data):
        print(f"Data saved to '{filename}'.")
 
 
def load_data():
    global STUDENT_FILE
    filename = input(f"Enter filename to load from [{STUDENT_FILE}]: ").strip() or STUDENT_FILE
 
    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist.")
        return
 
    data = _load_json(filename)
    STUDENT_FILE = filename
    print(f"Loaded {len(data)} student(s) from '{filename}'.")

    if data:
        print("-" * 70)
        for record in data.values():
            Student(**record).display()
        print("-" * 70)