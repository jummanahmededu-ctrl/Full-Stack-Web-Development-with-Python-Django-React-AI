print("=========================================")
print("             STUDENT REPORT")
print("=========================================")


# Create a Python program that performs the following tasks:
# 1. Student Information
name= input("Student Name : ")
id= str(input("Student ID : "))
department= input("Department : ")
print(name)
print(id)
print(department)

# 2. Subject Marks
# ["Python", "Math", "English", "Physics", "ICT"]
subjects= ["Python", "Math", "English", "Physics", "ICT"]
marks= {}

for subject in subjects:
    while True:
        mark= int(input(f"Enter marks for {subject} : "))
# Using Continue
        if mark < 0 or mark > 100:
            print("Invalid Mark! Please enter again")
            continue
        marks[subject]= mark
# Using Break
        break
print("Subjects & Marks :", marks)

# 3. Calulate Result
# Calculate - Total Marks, - Average Marks, - Highest Mark, - Lowest Mark
total= sum(marks.values())
average= total/len(marks)
highest= max(marks.values())
lowest= min(marks.values())
print("Total Marks : ", total)
print("Average Marks",average)
print("Highest Mark : ",highest)
print("Lowest Mark : ",lowest)

# 4. Grade Calculation
# Using if-elif-else, assign grades
if 80<=average<=100:
    print("Grade : A+")
elif 70<=average<=79:
    print("Grade : A")
elif 60<=average<=69:
    print("Grade : A-")
elif 50<=average<=59:
    print("Grade : B")
elif 40<=average<=49:
    print("Grade : C")
else:
    print("Grade : F")

# Pass or Fail
# If your subject mark is below 40, display Satus: Failed Otherwise Status: Passed
if average<40:
    print("Satus: Failed")
else:
    print("Status: Passed")

# Password Verification
# Ask the user to enter a password. Correct password: python123
password= str(input("Enter your password : "))
correctpassword= "python123"
if password==correctpassword:
    print("Congratulations! This is the Correct Password")
else:
    print("WARNING! Wrong Password") 

# 7. String Operations
# Display:
# - Student name in uppercase
# - Student name in lowercase
# - Length of the student name
# - First three characters
# - Last three characters
print(name.upper())
print(name.lower())
print(len(name))
print(name[:3])
print(name[-3:])

# 8.Set Example
#Create two sets.
#sports= {"Football","Cricket", "Badminton"}
#clubs= {"Programming","Cricket","Photography"}
#Display 
#- Common items
#- All unique items

sports= {"Football","Cricket", "Badminton"}
clubs= {"Programming","Cricket","Photography"}
print("Common Items : ",sports.intersection(clubs))
print("All Unique Items : ",sports.union(clubs))

# 9. Tuple Example
# Create a tuple containing weekdays
# Display
# - First day
# - Last day
# - Total number of days
weekdays= ("Monday","Tuesday","Wednesday","Thursday","Friday")
print("First day : ",weekdays[0])
print("Last day : ",weekdays[-1])
print("Total number of days : ",len(weekdays))

