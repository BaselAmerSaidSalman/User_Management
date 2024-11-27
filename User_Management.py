import time
user_list = []

# User_Class
class User:
  def __init__ (self, first_name, last_name, email, password, status = "inactive"):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.password = password
    self.status = status
    user_list.append(f"---------------------------\nFirst name: {self.first_name}\nLast name: {self.last_name}\nEmail: {self.email}\nPassword: {self.password}\nStatus: {self.status}\n---------------------------")


# Create_User
def create_user():
   first_name = input("Enter your first name: ")
   last_name = input("Enter your last name: ")
   email = input("Enter your email: ")
   password = input("Enter your password: ")

   return User(first_name, last_name, email, password)


# Login_User
def introduction_page():
  # User_Choice
  print("Welcome to the User Management System\n\n")
  print("Choose an action\n\n1. Add new user\n2. Display all users\n3. Exit\n")
  user_choice = input("Enter your choice: ")
  while user_choice != "1" and user_choice != "2" and user_choice != "3":
    print("Sorry, Invalid Input")
    user_choice = input("Enter your choice: ")

  # Create_New_User
  if user_choice == "1":
    create_user()
    print("User added successfully")
    introduction_page()

  # Display_All_Users
  elif user_choice == "2":
    print("Displaying all users........")
    print("".join(user_list))
    introduction_page()

  # Exit
  elif user_choice == "3":
    print("Exiting.........")
    time.sleep(2)

# Code
introduction_page()

