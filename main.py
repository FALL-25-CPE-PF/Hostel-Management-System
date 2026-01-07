import my_admin_module
import my_student_module

def login(role):
    username = input("Username: ")
    password = input("Password: ")

    if role == "admin":
        if username == "admin" and password == "admin123":
            my_admin_module.admin_menu()
        else:
            print("Invalid Admin Login")

    elif role == "student":
        if username == "student" and password == "student123":
            my_student_module.student_menu()
        else:
            print("Invalid Student Login")

def main():
    while True:
        print("\n\t === Hostel Management System === \n")
        print("1. Admin Login")
        print("2. Student Login")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            login("admin")
        elif choice == "2":
            login("student")
        elif choice == "3":
            print("Program Closed")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
