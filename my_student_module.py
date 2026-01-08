STUDENT_FILE = "students.txt"

# ---------- STUDENT FUNCTIONS ----------
def load_students():
    students = []
    try:
        with open(STUDENT_FILE, "r") as f:
            for line in f:
                students.append(line.strip().split(","))
    except FileNotFoundError:
        pass
    return students

def save_students(students):
    with open(STUDENT_FILE, "w") as f:
        for s in students:
            f.write(",".join(s) + "\n")

def apply_hostel():
    student_id = input("Student ID: ")
    name = input("Name: ")
    department = input("Department: ")
    age = input("Age: ")
    hostel = input("Choose Hostel (A/B/C): ").upper()
    room_number = input("Choose Room Number: ")
    room_type = input("Room Type (Poor/Good): ").capitalize()

    students = load_students()
    students.append([student_id, name, department, age, hostel, room_number, room_type])
    save_students(students)
    print(f"✅ Student {name} added to Hostel {hostel}, Room {room_number}")

def view_details():
    student_id = input("Enter your Student ID: ")
    students = load_students()
    found = False

    for s in students:
        if s[0] == student_id:
            print("\n--- Your Details ---")
            print(f"ID: {s[0]}")
            print(f"Name: {s[1]}")
            print(f"Department: {s[2]}")
            print(f"Age: {s[3]}")
            print(f"Hostel: {s[4]}")
            print(f"Room Number: {s[5]}")
            print(f"Room Type: {s[6]}")
            found = True
            break
    if not found:
        print("❌ No record found for this Student ID")

def remove_self():
    student_id = input("Enter your Student ID to remove: ")
    students = load_students()
    new_list = []
    removed = False

    for s in students:
        if s[0] == student_id:
            removed = True
        else:
            new_list.append(s)

    save_students(new_list)
    if removed:
        print("✅ Removed from hostel successfully")
    else:
        print("❌ Student ID not found")

# ---------- STUDENT MENU ----------
def student_menu():
    print("✅ Entered Student Module")
    while True:
        print("\n--- Student Menu ---")
        print("1. Apply for Hostel")
        print("2. View Details")
        print("3. Remove Myself")
        print("4. Logout")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            apply_hostel()
        elif choice == "2":
            view_details()
        elif choice == "3":
            remove_self()
        elif choice == "4":
            print("Logging out of Student...")
            break
        else:
            print("❌ Invalid choice")
