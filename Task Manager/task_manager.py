
#=====importing libraries===========
from datetime import date

#====Login Section====
'''User to login.
    - Read usernames and password from the user.txt file
    - Use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
username, password = " ", " "
sign_in = True

while sign_in:
    username, password = input("Enter username: "), input("Enter password: ")

    user_file = open('user.txt','r+', encoding='utf-8') #The variable user_file is stored as a list of file lines
    user_info = user_file.read()
    user_lines = user_info.split("\n") #Spliting the lines into a list

    if username == "" and password == "":
        print("Invalid credentials. Try again!")
    else:
        for line in user_lines:
            credentials = line.split(", ") # Split on the space, and store the results in a list of two strings
            if username == credentials[0] and password == credentials[1]:
                sign_in = False
    if sign_in == True:
        print("Incorrect credentials.")
    else:
        print("You have successfully logged in.")
    
    user_file.close()


while True:
    task_counter = 0
    user_counter = 0
    # presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.

    menu = input('''Select one of the following Options below: 
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
vs - View stastics
e - Exit
: ''').lower()

    if menu == 'r':
        '''Add a new user to the user.txt file
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''
        
        if username == "admin":
            new_username = input("Enter new username: ")
            new_password = input("Enter new password: ")
            confirm_password = input("Confirm the new password: ")

            user_file1 = open('user.txt','a+', encoding='utf-8') 

            if new_password == confirm_password:
                user_file1.write("\n" + new_username + ", " + new_password)
            else:
                print("The passwords you entered do not match. Try again.")

            user_file1.close()
        else:
            print("Only the admin is allowed to register new users.")


    elif menu == 'a':
        '''Add a new task to task.txt file
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''
        
        chosen_person = input("Enter a username of the person whom the task is assigned to: ")
        task_title = input("Enter a title of the task: ")
        task_description =  input("Enter the description of the task: ")
        task_due_date = input("Enter the due date of the task: ")
        task_status = "No"
        current_date = date.today()

        tasks_file1 = open('tasks.txt','a+', encoding='utf-8') 

        tasks_file1.write(f"\n{chosen_person}, {task_title}, {task_description}, {current_date}, {task_due_date}, {task_status}")
        tasks_file1.close


    elif menu == 'va':
        '''Read the task from task.txt file and 
            print to the console in the format of Output 2 presented in the L1T19 pdf file page 6
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in L1T19 pdf
            - It is much easier to read a file using a for loop.'''
        
        tasks_file2 = open('tasks.txt','r+', encoding='utf-8') #The variable tasks_file is stored as a list of file lines
        tasks_info2 = tasks_file2.read()
        task_line2 = tasks_info2.split("\n") #Spliting the lines into a list
        
        for line in task_line2:
            task_lines2 = line.split(", ")
            print(f'''
            Task:                       {task_lines2[1]}
            Assigned to:                {task_lines2[0]}
            Date assigned:              {task_lines2[-3]}
            Due date:                   {task_lines2[-2]}
            Task Completed:             {task_lines2[-1]}
            Task  description:          {task_lines2[2]}
            ''')
        tasks_file2.close()

    elif menu == 'vm':
        pass
        '''Read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same you print the task in the format of output 2 shown in L1T19 pdf '''
        
        tasks_file3 = open('tasks.txt','r+', encoding='utf-8') 
        tasks_info3 = tasks_file3.read()
        task_lines3 = tasks_info3.split("\n") 
        
        for line in task_lines3:
            task_lines3 = line.split(", ")
            if username == task_lines3[0]:
                print(f'''
                Task:                       {task_lines3[1]}
                Assigned to:                {task_lines3[0]}
                Date assigned:              {task_lines3[-3]}
                Due date:                   {task_lines3[-2]}
                Task Completed:             {task_lines3[-1]}
                Task  description:          {task_lines3[2]}
                ''')
        tasks_file3.close()

    elif menu == 'vs':
        ''' Read the number of tasks and users and display them.
        '''
        user_file2 = open('user.txt','r', encoding='utf-8') 
        user_info2 = user_file2.read()
        user_lines2 = user_info2.split("\n") 

        for line in user_lines:
            user_counter += 1
        user_file2.close()

        tasks_file4 = open('tasks.txt','r', encoding='utf-8') 
        tasks_info4 = tasks_file4.read()
        task_lines4 = tasks_info4.split("\n") 

        for line in task_lines4:
            task_counter += 1
        tasks_file4.close()


        print(f"The total number of tasks is: {task_counter}\nThe total number of users is: {user_counter}")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")

