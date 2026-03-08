# sample3.py
# Use a nested dictionary to store student grades by subject.

def main():
    grades = {
        "Alice": {"math": 90, "science": 85},
        "Bob": {"math": 75, "science": 80}
    }
    for student, subjects in grades.items():
        print(student)
        for subj, score in subjects.items():
            print(f"  {subj}: {score}")

if __name__ == '__main__':
    main()

