# Student Management System

A simple, menu-driven command-line application for managing student records, built in Python. It supports full CRUD operations, basic analytics, and persistent storage using JSON — making it a lightweight tool for tracking student data without needing a database.

## Features

- **Add Student** — Create a new record with input validation for age and marks
- **Remove Student** — Delete a record by student ID
- **Search Student** — Look up and view a specific student's details
- **Update Student** — Edit any field while leaving others unchanged
- **Display Students** — List all records along with pass/fail status
- **Calculate Average** — Compute the average marks across all students
- **Find Highest Scorer** — Identify the top-performing student
- **Save Data** — Export current records to a chosen JSON file
- **Load Data** — Import records from an existing JSON file

## Demo

```
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

Enter your choice:
```

## Getting Started

### Prerequisites

- Python 3.7 or higher

No external libraries are required — the project only uses Python's built-in `os` and `json` modules.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/student-management-system.git
   cd student-management-system
   ```
2. Run the program:
   ```bash
   python main.py
   ```

## Project Structure

```
student-management-system/
├── main.py                       # Entry point — runs the menu loop
├── student_management_system.py  # Student class and core logic
├── .gitignore
└── README.md
```

## How It Works

Each student is represented by a `Student` class with the following attributes:

| Field | Description |
|---|---|
| `student_id` | Unique identifier for the student |
| `name` | Student's full name |
| `age` | Student's age |
| `department` | Department or major |
| `marks` | Score used to determine pass/fail status |

Records are stored in a JSON file (`student1.json` by default), keyed by student ID. Every menu action reads from and writes to this file directly, so changes are saved automatically — no separate "save" step is required for day-to-day use. The **Save Data** and **Load Data** options are there for exporting to or importing from a different file.

A student is marked as **passed** if their marks are 40 or above.

## Error Handling

The application is built to fail gracefully:
- Missing, empty, or corrupted JSON files are treated as an empty dataset rather than crashing the program
- Non-numeric input for age or marks is rejected with a clear message, and the original data is left untouched
- Attempting to add a duplicate student ID, or search/update/remove a nonexistent one, is caught and reported to the user

## Possible Improvements

- Add sorting and filtering options (e.g., by department or marks range)
- Support CSV import/export
- Add unit tests
- Build a simple GUI or web interface on top of the existing logic

## License

This project is open source and available for personal and educational use.
