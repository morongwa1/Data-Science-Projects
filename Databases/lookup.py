import sqlite3
import json
import xml.etree.ElementTree as ET

try:
    conn = sqlite3.connect("HyperionDev.db")     #usign sqlite to connect to the database
except sqlite3.Error:
    print("Please store your database as HyperionDev.db")
    quit()

cur = conn.cursor()

def usage_is_incorrect(input, num_args):
    if len(input) != num_args + 1:
        print(f"The {input[0]} command requires {num_args} arguments.")
        return True
    return False

def store_data_as_json(data, filename):
    # the dumps function converts the data tuple into a json string
    json_object = json.dumps(data, indent=1)

    with open(filename, "w") as jsonfile:
        for obj in json_object:
            jsonfile.write(obj)

def store_data_as_xml(data, filename):
    # # make root element
    # user_query = ET.Element("user_query")
    # # create sub element
    # user_query = ET.SubElement(user_query, "user_query")

    # # insert list element into sub elements
    # for qry in range(len(data)):
    #     query = ET.SubElement(user_query, "query")
    #     query.text = str(data[qry])

    # tree = ET.ElementTree(user_query)
    # # write the tree into an XML file
    # tree.write(filename, encoding='utf-8', xml_declaration=True)

    root = ET.Element("user_query")
    for item in data:
        ET.SubElement(root, "query").text = "\n" + str(item) + "\n"
    xml_tree = ET.ElementTree(root)
    xml_tree.write(filename)

def offer_to_store(data):
    while True:
        print("Would you like to store this result?")
        choice = input("Y/[N]? : ").strip().lower()

        if choice == "y":
            filename = input("Specify filename. Must end in .xml or .json: ")
            ext = filename.split(".")[-1]
            if ext == 'xml':
                store_data_as_xml(data, filename)
            elif ext == 'json':
                store_data_as_json(data, filename)
            else:
                print("Invalid file extension. Please use .xml or .json")

        elif choice == 'n':
            break

        else:
            print("Invalid choice")

usage = '''
What would you like to do?

d - demo
vs <student_id>            - view subjects taken by a student
la <firstname> <surname>   - lookup address for a given firstname and surname
lr <student_id>            - list reviews for a given student_id
lc <teacher_id>            - list all courses taken by teacher_id
lnc                        - list all students who haven't completed their course
lf                         - list all students who have completed their course and achieved 30 or below
e                          - exit this program

Type your option here: '''

print("Welcome to the data querying app!")

while True:
    print()
    # Get input from user
    user_input = input(usage).split(" ")
    print()

    # Parse user input into command and args
    command = user_input[0]
    if len(user_input) > 1:
        args = user_input[1:]
        # print(args)

    if command == 'd': # demo - a nice bit of code from me to you - this prints all student names and surnames :) Thank you :)
        data = cur.execute("SELECT * FROM Student")
        for _, firstname, surname, _, _ in data:
            print(f"{firstname} {surname}")
        
    elif command == 'vs': # view subjects by student_id
        if usage_is_incorrect(user_input, 1):
            continue
        student_id = args[0]
        
        # Run SQL query and store in data
        # . . . 
        data = cur.execute("SELECT course_name FROM Course INNER JOIN StudentCourse ON Course.course_code = StudentCourse.course_code WHERE StudentCourse.student_id = ?", (student_id,))
        course_names = data.fetchone()

        print(f"The student wiht the ID: {student_id} is taking these course: ")
        for course in course_names:
            print(course)

        offer_to_store(course_names)
    

    elif command == 'la':# list address by name and surname
        if usage_is_incorrect(user_input, 2):
            continue
        firstname, surname = args[0], args[1]
        data = None

        # Run SQL query and store in data
        # . . . 
        data = cur.execute("SELECT street, city FROM Address INNER JOIN Student ON Address.address_id = Student.address_id WHERE first_name =? AND last_name = ?", (firstname, surname ,))
        address = data.fetchone()
        
        print(f" s{firstname} {surname}tays at: {address}")

        offer_to_store(address)
    
    elif command == 'lr':# list reviews by student_id
        if usage_is_incorrect(user_input, 1):
            continue
        student_id = args[0]
        data = None

        # Run SQL query and store in data
        # . . . 

        data = cur.execute("SELECT review_text, completeness, efficiency, style, documentation FROM Review INNER JOIN StudentCourse ON Review.student_id = StudentCourse.student_id WHERE StudentCourse.student_id = ?", (student_id,))
        reviews = data.fetchall()

        print(f"These are the reviews for student {student_id}: {reviews} ")
        # print(f"Review_text: {reviews[0]}\nCompleteness score: {reviews[1]}\nEfficiency score: {reviews[2]}\nStyle score: {reviews[3]}\nDocumentation score: {reviews[4]}")

        offer_to_store(reviews)
        pass
    
    elif command == 'lc':# list all courses taken by teacher_id
        if usage_is_incorrect(user_input, 1):
            continue
        teacher_id = args[0]
        data = None
        # Run SQL query and store in data
        # . . . 

        data = cur.execute("SELECT course_name FROM Course INNER JOIN Teacher ON Course.teacher_id = Teacher.teacher_id WHERE Teacher.teacher_id = ?", (teacher_id,))
        teacher_courses = data.fetchall()

        print(type(teacher_courses))
        
        offer_to_store(teacher_courses)
        pass

    elif command == 'lnc':# list all students who haven't completed their course
        data = None

        # Run SQL query and store in data
        # . . . 
        data = cur.execute("SELECT Student.student_id, first_name, last_name, email, course_name FROM Student INNER JOIN StudentCourse ON Student.student_id = StudentCourse.student_id INNER JOIN Course ON StudentCourse.course_code = Course.course_code WHERE is_complete = 0")
        
        data = data.fetchall()

        for data_index in data:
            print(data_index)

        offer_to_store(data)
        pass
    
    elif command == 'lf':# list all students who have completed their course and got a mark <= 30
        data = None

        # Run SQL query and store in data
        # . . . 

        data = cur.execute("SELECT Student.student_id, first_name, last_name, email, course_name, mark FROM Student INNER JOIN StudentCourse ON Student.student_id = StudentCourse.student_id INNER JOIN Course ON StudentCourse.course_code = Course.course_code WHERE is_complete = 1 AND mark <= 30 ")
        
        data = data.fetchall()
        print(data)

        for data_index in data:
            print(data_index)


        offer_to_store(data)
        pass
    
    elif command == 'e':# list address by name and surname
        print("Programme exited successfully!")
        break
    
    else:
        print(f"Incorrect command: '{command}'")
    

    
