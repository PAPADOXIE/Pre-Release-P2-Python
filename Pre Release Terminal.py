#PreReleaseP2.py
#Made by Nofil Qasim (Papadoxie) | https://github.com/PAPADOXIE
#License = Opensource (Redistributable) (Modifiable)
#Made using micro (A command-line text editor)

#General Notes
#print(null) statements are used only to add an empty line between other outputs to the console
#print(/n) was not used to keep the code reader friendly and also because multiple empty lines were
#not needed
#break statements have been used to exit loops as soon as specified parameters have been met. This is
#not required but is good practice to keep processing time short

#Library Calls
#Importing sys to enable exit() function usage
import sys

#Global Declarations
#Defining a null string identifier as python doesn't have one built-in
null = ''

#Routine for managing method calls. Only used to make code look cleaner and readable
def main():

    #Defining a list of student names and emails
    student_data = []
    #Reading data previously saved into file
    read_from_file(student_data)
    #Calling a method to display a menu on the console
    menu(student_data)
       
#Method for displaying a menu on the console
def menu(student_data):

    print(null)
    print('1. Add New Student')
    print('2. View All Students')
    print('3. Search a Student')
    print('4. Delete a Student')
    print('5. Exit')
    print(null)
    
    #Stand-in for a select-case statement (Processing user selections in menu)
    select = int(input('Select a Number = '))
    if select == 1:
        #Entering student details
        new_student(student_data)
    elif select == 2:
        #Viewing the whole list of students (student_data)
        view_students(student_data)
    elif select == 3:
        #Searching the list of students (student_data) for a student
        search_students(student_data)
    elif select == 4:
        #Removing a student from the list of students (student_data)
        delete_a_student(student_data)
    elif select == 5:
        print(null)
        sure = input('Are you sure (y/n) = ')
        if sure == 'y' or sure == 'Y':
            print(null)
            exit()
        else:
            menu(student_data)
    else:
        menu(student_data)
        

#Method for entering students names and emails into list student_data
def new_student(student_data):

    print(null)
    #Inputting name
    name =  input('Enter Name of Student = ')
    #Inputting email
    email = input ('Enter Email of Student = ')
    #Inputting Date of Birth
    dob = input ('Enter Date of Birth = ')
    
    #Presence check for entered data so null values are not entered
    if name == null or email == null or dob == null:             
      new_student()
    else:
        #len(student_data) is used to assign an ID to each student as its value increases with each 
        #addition to the list student_data
        student_data.append([len(student_data),name,email,dob])
        write_to_file(len(student_data),name,email,dob)
        
    #Calling Menu method again    
    menu(student_data)


#Method for viewing the whole list of students (student_data)    
def view_students(student_data):
    length = len(student_data)
    print(null)
    print('ID, Name, Email, Date of Birth')
    print(null)
    
    for i in range (0,len(student_data)):            
        print(student_data[i])        
        
    #Calling Menu method again    
    menu(student_data)


#Method for searching a student from the list of students (student_data)
def search_students(student_data):
    #User input for searching list of students (student_data)
    search_parameter = input('Enter the Name of the Student that you want to find = ')

    #Declaring a boolean value for the case when no students were found matching given parameters
    flag = False
        
    #Searching list of students (student_data)
    for i in range (0,len(student_data)):
    
        #Parsing list data for individual components (name) by looking for (#) seperator      
        name = str(student_data[i][0])
        
        #Looking for user specified parameters in current string
        if name == search_parameter:
            print(null)
            print('ID, Name, Email, Date of Birth')
            print(null)
            print(student_data[i])
            flag = True
            break
                
    if flag == False:
        print('Student not found')
        
    #Calling Menu method again    
    menu(student_data)

#Method for removing a student from the list of students (student_data)
def delete_a_student(student_data):

    #User input for removing a student from list of students (student_data)
    search_parameter = input('Enter the Name of the Student that you want to remove = ')

    #Declaring a boolean value for the case when no students were found matching given parameters
    flag = False
    
    #Searching list of students (student_data)
    for i in range (0,len(student_data)):
        #Parsing list data for individual components (name) by looking for (#) seperator
        name = (str(student_data[i][0]))
            
        #Looking for user specified parameters in current string
        if name == search_parameter:
            print(null)
            #Informing the user that the specified student has been removed
            print(student_data[i][0]+' has been removed')
            del(student_data[i])
            flag = True
            break
                    
        if flag == False:
            print("Student not found")
        
          
    #Calling Menu method again    
    menu(student_data)

#Method for writing to a file of students modelled on the list (student_array)
def write_to_file(ID,name,email,dob):

    #Opening a file (student_file) for writing
    student_file = open('student file.txt','a')
    
    #Writing list data to file (student_file)
    student_file.write(str((ID,name,email,dob)))
    student_file.write('\n')
    
    #Closing the file (student_file)
    student_file.close()

#Method for reading previously saved data from file 
def read_from_file(student_data):

    #Opening a file (student_file) for reading
    student_file = open('student file.txt','r')   

    #Appending file contents to list (student_data)
    for i in student_file:
        student_data.append(i)

    #Closing the file (student_file)
    student_file.close()   
    
#Calling Start of Program into console. Replace this for modular debugging
main()
