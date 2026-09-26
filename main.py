import student_management_system
from student_management_system import add_student, remove_student, search_student, update_student, display_students, calculate_average, find_highest_scorer, save_data, load_data

MENU = """
===== STUDENT MANAGEMENT SYSTEM =====
1. Add Student
2. Remove Student
3. Search Student
4. Update Student
5. Display Students
6. Calculate Average
7. Find Highest Scorer
8. Save Data
9. Load Data
10. Exit
"""
 
 
def main():
    actions = {
        "1": add_student,
        "2": remove_student,
        "3": search_student,
        "4": update_student,
        "5": display_students,
        "6": calculate_average,
        "7": find_highest_scorer,
        "8": save_data,
        "9": load_data,
    }
 
    while True:
        print(MENU)
        choice = input("Enter your choice: ").strip()
 
        if choice == "10":
            print("Goodbye!")
            break
 
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please try again.")
 
 
if __name__ == "__main__":
    main()