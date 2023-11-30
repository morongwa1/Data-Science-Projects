
#=====importing libraries===========
from datetime import date
import datetime

#====Login Section====

'''-------------Functions---------------------'''
def reg_user():
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
        is_user = False

        user_file = open('user.txt','r+', encoding='utf-8') 
        # Checking if the entered passwords match
        if new_password == confirm_password:                

            user_info = user_file.read()
            # Spliting the lines into a list
            user_lines = user_info.split("\n") 
            
            # This loop checks if the new surname entered already exists in the user file.
            for line in user_lines:
                task_lines2 = line.split(", ")
                if new_username == task_lines2[0]:
                    is_user = True
            
            if is_user == False:
                user_file.write("\n" + new_username + ", " + new_password)
            else: 
                print("The user name you have enter is already in use. Please enter another one.")
        else:
            print("The passwords you entered do not match. Try again.")

        user_file.close()
    else:
        print("Only the admin is allowed to register new users.")


def add_task():
    '''Allow a user to add a new task to task.txt file
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
    current_date = date.today().strftime("%d %b %Y")

    tasks_file1 = open('tasks.txt','a+', encoding='utf-8') 

    tasks_file1.write(f"\n{chosen_person}, {task_title}, {task_description}, {current_date}, {task_due_date}, {task_status}")
    tasks_file1.close


def view_all():
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
        Task title:                 {task_lines2[1]}
        Assigned to:                {task_lines2[0]}
        Date assigned:              {task_lines2[-3]}
        Due date:                   {task_lines2[-2]}
        Task completed:             {task_lines2[-1]}
        Task description:           {task_lines2[2]}
        ''')
    tasks_file2.close()


def view_mine():
    '''Read the task from task.txt file and
        print to the console in the format of Output 2 presented in the L1T19 pdf
        - Read a line from the file
        - Split the line where there is comma and space.
        - Check if the username of the person logged in is the same as the username you have
        read from the file.
        - If they are the same you print the task in the format of output 2 shown in L1T19 pdf '''
    
    vm_option =  int(input("Enter the task number you wanna select or -1 to return to the main menu."))
    view_counter = 0

    with open('tasks.txt','r+', encoding='utf-8') as tasks_file3:
        tasks_info3 = tasks_file3.read()
        task_lines3 = tasks_info3.split("\n") 
    
    for line in task_lines3:

        task_lines3 = line.split(", ")
        if vm_option == view_counter:
            if username == task_lines3[0]:
                print(f''' Task {view_counter}
                Task title:                 {task_lines3[1]}
                Assigned to:                {task_lines3[0]}
                Date assigned:              {task_lines3[-3]}
                Due date:                   {task_lines3[-2]}
                Task completed:             {task_lines3[-1]}
                Task description:           {task_lines3[2]}
                ''')
                edit = input("Do you wanna edit this task(Y/N)?").lower()
                if edit == 'y':
                    info_selected = input('''Which of the task options would you like to edit?
                    Task title
                    Assinged to
                    Date assigned:    
                    Due date:                   
                    Task status:             
                    Task description:           
                    ''')
                    new_info = input("Enter the new information.")

                    match info_selected:
                        case "task title":
                            task_lines3[1] = new_info
                        case "assigned to":
                            task_lines3[0] = new_info
                        case "date assinged": 
                            task_lines3[-3] = new_info
                        case "due date":
                            task_lines3[-2] = new_info
                        case "task status":
                            task_lines3[-1] = new_info
                        case "task description":
                            task_lines3[2] = new_info

                    # tasks_file3.write(f"{task_lines3[1]}, {task_lines3[0]}, {task_lines3[-3]}, {task_lines3[-2]}, {task_lines3[-1]}, {task_lines3[2]}\n")[view_counter]
                    task_lines3[view_counter] = f"{task_lines3[0]}, {task_lines3[1]}, {task_lines3[-3]}, {task_lines3[-2]}, {task_lines3[-1]}, {task_lines3[2]}\n"
                    
                    with open('tasks.txt', 'w',encoding='utf-8') as tasks_file3:
                        tasks_file3.writelines(task_lines3)

                elif edit == 'n':
                    exit
                    
        elif vm_option == -1:
            exit

        view_counter += 1

    tasks_file3.close()


def generate_reports():

###### Task Overview stuff
    number_of_tasks = 0
    completed_tasks = 0
    incompleted_tasks = 0
    overdue_tasks = 0
    current_date = date.today().strftime("%d %b %Y")

    with open('tasks.txt','r+', encoding='utf-8') as tasks_file:
        tasks_info = tasks_file.read()
        task_lines = tasks_info.split("\n") 

        lines = []   #this list stores all the file lines in it

        for line in task_lines:
            number_of_tasks += 1
            lines.append(line)
            task_lines = line.split(", ")
            date_object = datetime.datetime.strptime(task_lines[-2].strip(), "%d %b %Y")
            date_str = datetime.datetime.strftime(date_object, "%d %b %Y")

            if task_lines[-1] == 'Yes':
                completed_tasks += 1
            else:
                incompleted_tasks += 1
            if task_lines[-1] == 'No' and date_str<current_date:
                overdue_tasks += 1

    incompleted_percentage = (incompleted_tasks/number_of_tasks)*100
    overdue_percentage = (overdue_tasks/number_of_tasks)*100

    overview_file = open('task_overview.txt','r+', encoding='utf-8')

    overview_file.write(f'''
Total number of tasks:                          {number_of_tasks}
Total number of completed tasks:                {completed_tasks}
Total number of incompleted tasks:              {incompleted_tasks}
Total number of incompleted and overdue tasks:  {overdue_tasks}
The percentage of incompleted tasks:            {incompleted_percentage}%
The percentage of overdue tasks:                {overdue_percentage}%
''')

    

##### User Overview stuff
    overview_file2 = open('user_overview.txt','r+', encoding='utf-8')

    with open('user.txt','r+', encoding='utf-8') as user_file:
        user_info = user_file.read()
        user_lines = user_info.split("\n")

            # overview_file2 = open('user_overview.txt','r+', encoding='utf-8')

        users_number = 0
        user_counter = 0
        
            
        for line1 in user_lines:
            user_lines = line1.split(", ")
            users_number += 1
            user_counter = 0
            completed_tasks = 0
            incompleted_tasks = 0
            incompleted_percentage = 0
            overdue_tasks = 0
            overdue_percentage = 0

            for i in range(0,len(lines)):
                tasks_lines_split = lines[i].split(", ")
                if tasks_lines_split[0] == user_lines[0]:
                    user_counter += 1
                    date_object = datetime.datetime.strptime(task_lines[-2].strip(), "%d %b %Y")
                    date_str = datetime.datetime.strftime(date_object, "%d %b %Y")

                    if tasks_lines_split[-1] == 'Yes':
                        completed_tasks += 1
                    else:
                        incompleted_tasks += 1
                    if task_lines[-1] == 'No' and date_str<current_date:
                        overdue_tasks += 1

            incompleted_percentage = round((incompleted_tasks/number_of_tasks)*100,2)
            overdue_percentage = round((overdue_tasks/number_of_tasks)*100, 2)

            overview_file2.write(f'''
For User:{user_lines[0]}
Total number of tasks:                          {user_counter}
Total number of completed tasks:                {completed_tasks}
Total number of incompleted tasks:              {incompleted_tasks}
Total number of incompleted and overdue tasks:  {overdue_tasks}
The percentage of incompleted tasks:            {incompleted_percentage}%
The percentage of overdue tasks:                {overdue_percentage}%
\n''')

    tasks_file.close()
    user_file.close()



def view_stats():
    ''' Read the number of tasks and users and display them.
    '''
    user_counter = 0
    task_counter = 0

    user_file2 = open('user.txt','r', encoding='utf-8') 
    user_info2 = user_file2.read()
    user_lines2 = user_info2.split("\n") 

    for line in user_lines2:
        user_counter += 1
    user_file2.close()

    tasks_file4 = open('tasks.txt','r', encoding='utf-8') 
    tasks_info4 = tasks_file4.read()
    task_lines4 = tasks_info4.split("\n") 

    for line in task_lines4:
        task_counter += 1
    tasks_file4.close()

    print(f"The total number of tasks is: {task_counter}\nThe total number of users is: {user_counter}")
    
    generate_reports()

    #The variable tasks_file is stored as a list of file lines
    overview_file1 = open('task_overview.txt','r+', encoding='utf-8') 
    tasks_overview = overview_file1.read()
    task_line = tasks_overview.split("\n") #Spliting the lines into a list
    
    for line in task_line:
        task_lines = line.split(", ")
        print(task_lines)
    overview_file1.close()

    #The variable tasks_file is stored as a list of file lines
    overview_file2 = open('user_overview.txt','r+', encoding='utf-8') 
    user_overview = overview_file2.read()
    user_line = user_overview.split("\n") #Spliting the lines into a list
    
    for line in user_line:
        user_lines = line.split(", ")
        print(user_lines)
    overview_file1.close()



''' MAIN CODE'''

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
    # task_counter = 0
    # user_counter = 0
    # presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.

    menu = input('''Select one of the following Options below: 
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - View my task
        gr - Generate reports
        ds - Display stastics
        e - Exit
        : ''').lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()
    
    elif menu == 'gr':
        generate_reports()

    elif menu == 'ds':
        view_stats()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")

