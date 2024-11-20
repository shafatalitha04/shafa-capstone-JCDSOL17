def studentlist(x):
    print("Student List")
    for i in range(len(x)):
        print(f"{i+1}. {x[i]['name']}")

def integeronly(x):
    while True:
        try:
            value = int(input(x))
            return value
        except:
            print("Invalid input! Please put a number value only")
    
Student_Profile = [
    {
        'name' : 'Ivar Jenner',
        'grade_level' : 'Grade 1',
        'class' : '1-A',
        'DOB' : '26/10/2010',
        'nationality' : 'Indonesian',
        'name_of_father' : 'Budi',
        'name_of_mother' : 'Rebecca',
    },
    {
        'name' : 'Mees Hilgers',
        'grade_level' : 'Grade 2',
        'class' : '2-B',
        'DOB' : '04/09/2009',
        'nationality' : 'Indonesian',
        'name_of_father' : 'Michael',
        'name_of_mother' : 'Susi',
    },
    {
        'name' : 'Rafael Struick',
        'grade_level' : 'Grade 3',
        'class' : '3-C',
        'DOB' : '16/02/2008',
        'nationality' : 'Indonesian',
        'name_of_father' : 'Dean',
        'name_of_mother' : 'Maria',
    }
]

Student_Grade = [
    {
        'name' : 'Ivar Jenner',
        'grade' : {
            'Sport' : 80,
            'Math' : 75,
            'Biology' : 60,
            'Art' : 90,
            'Social Studies' : 85,
            'Chemistry' : 65,
            'Physics' : 80,
        },
    },
    {
        'name' : 'Mees Hilgers',
        'grade' : {
            'Sport' : 90,
            'Math' : 80,
            'Biology' : 95,
            'Art' : 80,
            'Social Studies' : 80,
            'Chemistry' : 80,
            'Physics' : 85,
        },
    },
    {
        'name' : 'Rafael Struick',
        'grade' : {
            'Sport' : 70,
            'Math' : 85,
            'Biology' : 85,
            'Art' : 95,
            'Social Studies' : 80,
            'Chemistry' : 75,
            'Physics' : 80,
        },
    }
]

mainmenu = 0
while mainmenu != 7:
    # MAIN MENU
    print("Welcome to Garuda Junior High School")
    print("1. Show Student Profiles")
    print("2. Show Student Grades")
    print("3. Add Student Data")
    print("4. Update Student Data")
    print("5. Student Grade Report")
    print("6. Delete Student Profile and Grade")
    print("7. Exit Program")

    mainmenu = integeronly("Please Select Menu (1-7): ")

    # SHOW STUDENT PROFILES
    if mainmenu == 1:
        while True:
            print("STUDENT PROFILE MENU")
            print("1. Show All Student Profiles")
            print("2. Search Student's Name")
            print("3. Back To Main Menu")

            menu = integeronly("Pick Menu (1/2/3): ")

            if menu == 1:
                for i in range(0,len(Student_Profile)):
                    print(f"{i+1}.  Name          : {Student_Profile[i]['name']}")
                    print(f"    Grade Level   : {Student_Profile[i]['grade_level']}")
                    print(f"    Class         : {Student_Profile[i]['class']}")
                    print(f"    Date of Birth : {Student_Profile[i]['DOB']}")
                    print(f"    Nationality   : {Student_Profile[i]['nationality']}")
                    print(f"    Father        : {Student_Profile[i]['name_of_father']}")
                    print(f"    Mother        : {Student_Profile[i]['name_of_mother']}")
                while True:
                    back = input("Back to menu (type yes): ").lower()
                    if back == 'yes':
                        break
                    else:
                        print("Wrong Input")
            elif menu == 2: 
                while True:
                    studentlist(Student_Profile)
                    existed_student = [nama['name'].lower() for nama in Student_Profile]
                    stud_name = input("Please enter student's full name: ")
                    if stud_name not in existed_student:
                        print("Student not found!")
                    else:
                        index_updt = existed_student.index(stud_name)
                        print('Student Profile')
                        print(f"Name          : {Student_Profile[index_updt]['name']}")
                        print(f"Grade Level   : {Student_Profile[index_updt]['grade_level']}")
                        print(f"Class         : {Student_Profile[index_updt]['class']}")
                        print(f"Date of Birth : {Student_Profile[index_updt]['DOB']}")
                        print(f"Nationality   : {Student_Profile[index_updt]['nationality']}")
                        print(f"Father        : {Student_Profile[index_updt]['name_of_father']}")
                        print(f"Mother        : {Student_Profile[index_updt]['name_of_mother']}")
                    while True:
                        search_again = input("Would you like to search for another student? (yes/no): ").lower()
                        if search_again == 'yes':
                            break
                        elif search_again == 'no':
                            returntomenu = True
                            break
                        else:
                            print("Wrong input, please only type 'yes' or 'no'")
                    if search_again == 'no':
                        break
            elif menu == 3:
                break
            else:
                print("Invalid input, please try again!")

    # SHOW STUDENT GRADE
    elif mainmenu == 2:
        while True:
            print("STUDENT GRADE MENU")
            print("1. Show All Student Grade")
            print("2. Search Student Name")
            print("3. Back to Main Menu")

            menu = integeronly("Pick menu (1/2/3): ")

            if menu == 1:
                    print('Student Grades')
                    for i in range(0, len(Student_Grade)):
                        print(f"{i+1}. Name : {Student_Grade[i]['name']}")
                        print("   Grades")
                        for i, j in Student_Grade[i]['grade'].items():
                            print(f"   {i}: {j}")
                    while True:
                        back = input("Back to menu (type yes): ").lower()
                        if back == 'yes':
                            break
                        else:
                            print("Wrong Input")
            elif menu == 2:
                while True:
                    studentlist(Student_Grade)
                    existed_student = [nama['name'].lower() for nama in Student_Profile]
                    Student_Name = input("Please enter student's full name: ").lower()
                    if Student_Name not in existed_student:
                        print("Student not found")
                    else:
                        index = existed_student.index(Student_Name)
                        print(f"Name: {Student_Profile[index]['name']}")
                        print("      Grades")
                        for subject, grade in Student_Grade[index]['grade'].items():
                            print(f"      {subject}: {grade}")
                    
                    while True:
                        search_again = input("Would you like to search for another student? (yes/no): ").lower()
                        if search_again == 'yes':
                            break
                        elif search_again == 'no':
                            returntomenu = True
                            break
                        else:
                            print("Wrong input, please only type 'yes' or 'no'")
                    if search_again == 'no':
                        break
            elif menu == 3:
                break
            else:
                print("Invalid input, please try again!")

    # ADD STUDENT DATA
    elif mainmenu == 3:
        while True:
            print("ADD STUDENT DATA MENU")
            print("1. Add New Student Data")
            print("2. Back to Main Menu")

            menu = integeronly("Pick Menu (1/2): ")
            
            if menu == 1:
                while True:
                    existed_student = [nama['name'].lower() for nama in Student_Profile]
                    print("New Student's Profile")
                    new_student = input("Input new student's full name: ").title()
                    if new_student.lower() in existed_student:
                        print("Student already existed!")
                    else:
                        new_grade = input("Input Grade Level: ").title()
                        new_class = input("Input Class: ").upper()
                        new_DOB = input("Input DOB (DD/MM/YYYY): ")
                        new_nat = input("Input Nationality: ").title()
                        new_father = input("Input Father's Name: ").title()
                        new_mother = input("Input Mother's Name: ").title()
                        print(" ")
                        print(f"Add {new_student}'s grade")
                        sport = integeronly("Input Grade for Sport: ")
                        math = integeronly("Input Grade for Math: ")
                        Biology = integeronly("Input Grade for Biology: ")
                        Art = integeronly("Input Grade for Art: ")
                        Social = integeronly("Input Grade for Social Studies: ")
                        Chem = integeronly("Input Grade for Chemistry: ")
                        Physics = integeronly("Input Grade for Physics: ")
                        save = input("Save Added Data? (yes/no): ")
                        if save == 'yes':
                            Student_Profile.append({
                                'name' : new_student,
                                'grade_level' : new_grade,
                                'class' : new_class,
                                'DOB' : new_DOB,
                                'nationality' : new_nat,
                                'name_of_father' : new_father,
                                'name_of_mother' : new_mother,
                            })
                            Student_Grade.append({
                                'name' : new_student,
                                'grade' : {
                                    'Sport' : sport,
                                    'Math' : math,
                                    'Biology' : Biology,
                                    'Art' : Art,
                                    'Social_Studies' : Social,
                                    'Chemistry' : Chem,
                                    'Physics' : Physics,
                                }
                            })
                            print(f"Student {new_student} has been successfully added!")
                        else:
                            print("Data Not Saved")

                        while True:
                            search_again = input("Would you like to add another student data? (yes/no): ").lower()
                            if search_again == 'yes':
                                break
                            elif search_again == 'no':
                                returntomenu = True
                                break
                            else:
                                print("Wrong input, please only type 'yes' or 'no'")
                        if search_again == 'no':
                            break
            elif menu == 2:
                break
            else:
                print("Invalid input, please try again!")

    # UPDATE STUDENT PROFILE & GRADES
    elif mainmenu == 4:
        while True:
            print("UPDATE STUDENT DATA MENU")
            print("1. Update Student Profile")
            print("2. Update Student Grade")
            print("3. Back to Main Menu")
            
            menu = integeronly("Pick Menu (1/2/3): ")
            
            if menu == 1:
                while True:
                    studentlist(Student_Profile)
                    existed_student = [nama['name'].lower() for nama in Student_Profile]
                    stud_updt = input("Input student's full name: ").lower()
                    if stud_updt not in existed_student:
                        print("Student Not Found!")
                    else:
                        while True:
                            print("Which data you would like to update?")
                            print("1. Name")
                            print("2. Grade Level")
                            print("3. Class")
                            print("4. Date of Birth")
                            print("5. Nationality")
                            print("6. Name of Father")
                            print("7. Name of Mother")
                            while True:
                                data = integeronly("Input Data Number (1-7): ")
                                if data >= 1 and data <= 7 :
                                    break
                                else:
                                    print("Wrong input! Please enter a valid number")
                            index_updt = existed_student.index(stud_updt)
                            new_data = input("Input new data: ").title()
                            updt = input("Are you sure you want to update data? (yes/no): ").lower()
                            if updt == 'yes':
                                if data == 1:
                                    Student_Profile[index_updt]['name'] = new_data
                                    Student_Grade[index_updt]['name'] = new_data
                                elif data == 2:
                                    Student_Profile[index_updt]['grade_level'] = new_data
                                elif data == 3:
                                    Student_Profile[index_updt]['class'] = new_data
                                elif data == 4:
                                    Student_Profile[index_updt]['DOB'] = new_data
                                elif data == 5:
                                    Student_Profile[index_updt]['nationality'] = new_data
                                elif data == 6:
                                    Student_Profile[index_updt]['name_of_father'] = new_data
                                elif data == 7:
                                    Student_Profile[index_updt]['name_of_mother'] = new_data
                                print(f"{stud_updt}'s Data has successfully been updated!")
                            else:
                                print("Data update cancelled")
                            continue_updt = input("Do you want to continue updating student data? (yes/no): ").lower()
                            if continue_updt == 'no':
                                break
                            elif continue_updt != 'yes':
                                print("Wrong input, please only type 'yes' or 'no'")

                    while True:
                        search_again = input("Would you like to update another student data? (yes/no): ").lower()
                        if search_again == 'yes':
                            break
                        elif search_again == 'no':
                            returntomenu = True
                            break
                        else:
                            print("Wrong input, please only type 'yes' or 'no'")
                    if search_again == 'no':
                        break    

            elif menu == 2:
                while True:
                    studentlist(Student_Grade)
                    existed_student = [nama['name'].lower() for nama in Student_Grade]
                    stud_updt = input("Input full student's name: ").lower()
                    if stud_updt not in existed_student:
                        print("Student Not Found!")
                    else:
                        while True:
                            print("Which grade you would like to update?")
                            print("1. Sport")
                            print("2. Math")
                            print("3. Biology")
                            print("4. Art")
                            print("5. Social Studies")
                            print("6. Chemistry")
                            print("7. Physics")
                            while True:
                                data = integeronly("Input Data Number (1-7): ")
                                if data >= 1 and data <= 7 :
                                    break
                                else:
                                    print("Wrong input! Please enter a valid number")
                            index_updt = existed_student.index(stud_updt)
                            new_grade = integeronly("Input new grade: ")
                            updt = input("Are you sure you want to update data? (yes/no): ").lower()
                            if updt == 'yes':
                                grade_keys = ["Sport", "Math", "Biology", "Art", "Social_Studies", "Chemistry", "Physics"]
                                selected_key = grade_keys[data - 1]
                                Student_Grade[index_updt]['grade'][selected_key] = new_grade
                                print(f"{stud_updt.capitalize()} grade for {selected_key} successfully updated!")
                            else:
                                print("Data Update Cancelled")
                            continue_updt = input("Do you want tp continue updating student data? (yes/no): ").lower()
                            if continue_updt == 'no':
                                break
                            elif continue_updt != 'yes':
                                print("Wrong input, please only type 'yes' or 'no'")

                    while True:
                        search_again = input("Would you like to update another student data? (yes/no): ").lower()
                        if search_again == 'yes':
                            break
                        elif search_again == 'no':
                            returntomenu = True
                            break
                        else:
                            print("Wrong input, please only type 'yes' or 'no'")
                    if search_again == 'no':
                        break 

            elif menu == 3:
                break
            else:
                print("Invalid input, please try again!")

    # STUDENT GRADE REPORT
    elif mainmenu == 5:
        while True:
            print("GRADE REPORT MENU")
            print("1. Student Report Card")
            print("2. Student Ranking")
            print("3. Back to Main Menu")

            menu = integeronly("Pick Menu (1/2/3): ")
            if menu == 1:
                while True:
                    existed_student = [nama['name'].lower() for nama in Student_Grade]
                    studentlist(Student_Profile)
                    stud_name = input("Please enter student's full name: ")
                    if stud_name not in existed_student:
                        print("Student not found!")
                    else:
                        index_updt = existed_student.index(stud_name)
                        print('Student Report Card')
                        print(f"Student's Name : {Student_Grade[index_updt]['name']}")
                        print("Subject Grades")
                        for i, j in Student_Grade[index_updt]['grade'].items(): 
                            print(f"  {i}: {j}")
                        grade_list = []
                        for i, j in Student_Grade[index_updt]['grade'].items():
                            grade_list.append(j)
                        for i in grade_list:
                            average_grade = round(sum(grade_list)/len(grade_list),1)
                        print(" ")
                        print(f"Average Grade : {average_grade}")
                        subject_list = []
                        for subject, grade in Student_Grade[index_updt]['grade'].items():
                            subject_list.append((subject, grade))
                        top = subject_list[0][1]
                        top_subject = subject_list[0][0]  
                        least = subject_list[0][1]
                        least_subject = subject_list[0][0]  
                        for subject, grade in subject_list:
                            if grade < least:
                                least = grade
                                least_subject = subject 
                            if grade > top:
                                top = grade
                                top_subject = subject
                        print (f"Top Performing Subject : {top_subject}")
                        print(f"Least Performing Subject : {least_subject}")
                        if average_grade > 75.0:
                            print("Status: PASS")
                        else:
                            print("Status: NO PASS")

                        while True:
                            search_again = input("Would you like to see another student report card? (yes/no): ").lower()
                            if search_again == 'yes':
                                break
                            elif search_again == 'no':
                                returntomenu = True
                                break
                            else:
                                print("Wrong input, please only type 'yes' or 'no'")
                        if search_again == 'no':
                            break

            elif menu == 2:
                print("The student rank is based on student's average grade")
                average_grade = []
                for stud in Student_Grade:
                    grades = list(stud['grade'].values())
                    average = round(sum(grades)/len(grades),1)
                    average_grade.append({
                        'name' : stud['name'],
                        'avg' : average
                    })

                n = len(average_grade)
                for i in range(n):
                    for j in range(0, n-i-1):
                        if average_grade[j]['avg'] < average_grade[j+1]['avg']:
                            average_grade[j], average_grade[j+1] = average_grade[j+1], average_grade[j]

                print("\t\t\tSTUDENT RANKING\n")
                print("\tRank\t\tStudent Name\t\t\tGrade\t")
                for rank, stud in enumerate(average_grade, 1):
                    print(f"\t{rank}\t\t{stud['name']}\t\t\t{stud['avg']}")
                
                while True:
                    back = input("Back to menu (type yes): ").lower()
                    if back == 'yes':
                        break
                    else:
                        print("Wrong Input")
            else:
                print("Invalid input, please try again!")
    
    # DELETE STUDENT PROFILE & GRADE
    elif mainmenu == 6:
        while True:
            print("DELETE STUDENT DATA MENU")
            print("1. Delete Student Data")
            print("2. Back to Main Menu")

            menu = integeronly("Pick Menu (1/2): ")
            if menu == 1:
                while True:
                    studentlist(Student_Profile)
                    existed_student = [nama['name'].lower() for nama in Student_Profile]
                    stud_del = input("Input student's name to be deleted: ").lower()
                    if stud_del not in existed_student:
                        print("Student Not Found")
                    else:
                        print("Delete entire student data?")
                        ans = input("yes/no: ").lower()
                        if ans == 'yes':
                            index_del = existed_student.index(stud_del)
                            del Student_Profile[index_del]
                            del Student_Grade[index_del]
                            print("Data Successfully Deleted")
                        elif ans == 'no':
                            print("Data deletion canceled")
                        else:
                            print("Invalid input. Please enter 'yes' or 'no'.")
                    while True:
                        search_again = input("Would you like to do other action? (yes/no): ").lower()
                        if search_again == 'yes':
                            break
                        elif search_again == 'no':
                            returntomenu = True
                            break
                        else:
                            print("Wrong input, please only type 'yes' or 'no'")
                    if search_again == 'no':
                        break
            else:
                print("Invalid input, please try again!")
else:
    print("Goodbye!\n")



