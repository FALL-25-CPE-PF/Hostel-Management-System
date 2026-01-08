STUDENT_FILE = "students.txt"
ROOMS_FILE = "rooms.txt"

# ---------- HELPER FUNCTIONS ----------
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
def load_rooms():
    rooms = []
    try:
        with open(ROOMS_FILE, "r") as f:
            for line in f:
                h, rnum, rtype, maxc, occ = line.strip().split(",")
                rooms.append([h, rnum, rtype, int(maxc), int(occ)])
    except FileNotFoundError:
        # Initialize rooms if file not found
        rooms = []
        for hostel in ["A", "B", "C"]:
            for i in range(1, 11):
                # Poor rooms: 5 max, Good rooms: 3 max
                if i <= 5:
                    rooms.append([hostel, str(i), "Poor", 5, 0])
                else:
                    rooms.append([hostel, str(i), "Good", 3, 0])
        save_rooms(rooms)
    return rooms
def save_rooms(rooms):
    with open(ROOMS_FILE, "w") as f:
        for r in rooms:
            f.write(",".join([r[0], r[1], r[2], str(r[3]), str(r[4])]) + "\n")

# ---------- ROOM LOGIC ----------
def allocate_room(hostel, room_type):
    rooms = load_rooms()
    for r in rooms:
        if r[0] == hostel and r[2].lower() == room_type.lower() and r[4] < r[3]:
            r[4] += 1
            save_rooms(rooms)
            return r[1]  # return room number
    return None

def deallocate_room(hostel, room_number):
    rooms = load_rooms()
    for r in rooms:
        if r[0] == hostel and r[1] == room_number:
            if r[4] > 0:
                r[4] -= 1
            break
    save_rooms(rooms)
    
# ---------- ADMIN FUNCTIONS ----------
def add_student():
    student_id = input("Student ID: ")
    name = input("Name: ")
    department = input("Department: ")
    age = input("Age: ")
    hostel = input("Hostel (A/B/C): ").upper()
    room_type = input("Room Type (Poor/Good): ").capitalize()

    room_number = allocate_room(hostel, room_type)
    if room_number:
        students = load_students()
        students.append([student_id, name, department, age, hostel, room_number, room_type])
        save_students(students)
        print(f"Student {name} added to Hostel {hostel}, Room {room_number}")
    else:
        print("No room available in that hostel/type")

def remove_student():
    student_id = input("Enter Student ID to remove: ")
    students = load_students()
    new_list = []
    removed = False

    for s in students:
        if s[0] == student_id:
            deallocate_room(s[4], s[5])
            removed = True
        else:
            new_list.append(s)

    save_students(new_list)
    if removed:
        print("Student removed successfully")
    else:
        print("Student ID not found")

def update_student():
    student_id = input("Enter Student ID to update: ")
    students = load_students()
    found = False

    for s in students:
        if s[0] == student_id:
            s[1] = input("New Name: ")
            s[2] = input("New Department: ")
            s[3] = input("New Age: ")
            s[4] = input("New Hostel (A/B/C): ").upper()
            s[6] = input("New Room Type (Poor/Good): ").capitalize()
            room_number = allocate_room(s[4], s[6])
            if room_number:
                deallocate_room(s[4], s[5])
                s[5] = room_number
                found = True
                break
            else:
                print("No room available in that hostel/type")
                return

    save_students(students)
    if found:
        print("Student details updated")
    else:
        print("Student ID not found")

def view_students():
    students = load_students()
    if not students:
        print("No students found")
        return
    print("\n--- All Students ---")
    for s in students:
        print(f"ID: {s[0]}, Name: {s[1]}, Dept: {s[2]}, Age: {s[3]}, Hostel: {s[4]}, Room: {s[5]}, Type: {s[6]}")

def view_capacity():
    rooms = load_rooms()
    print("\n--- Hostel Room Capacity ---")
    for r in rooms:
        print(f"Hostel {r[0]}, Room {r[1]}, Type: {r[2]}, Max: {r[3]}, Occupied: {r[4]}")

def shift_student():
    student_id = input("Enter Student ID to shift: ")
    students = load_students()
    found = False

    for s in students:
        if s[0] == student_id:
            deallocate_room(s[4], s[5])
            new_hostel = input("New Hostel (A/B/C): ").upper()
            new_type = input("New Room Type (Poor/Good): ").capitalize()
            new_room = allocate_room(new_hostel, new_type)
            if new_room:
                s[4] = new_hostel
                s[5] = new_room
                s[6] = new_type
                found = True
            else:
                print("No room available in that hostel/type")
                return
            break

    save_students(students)
    if found:
        print("Student shifted successfully")
    else:
        print("Student ID not found")

# ---------- ADMIN MENU ----------
def admin_menu():
    print("Entered Admin Module")
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Update Student")
        print("4. View Students")
        print("5. View Hostel Capacity")
        print("6. Shift Student")
        print("7. Logout")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            view_students()
        elif choice == "5":
            view_capacity()
        elif choice == "6":
            shift_student()
        elif choice == "7":
            print("Logging out of Admin...")
            break
        else:
            print("Invalid choice")
