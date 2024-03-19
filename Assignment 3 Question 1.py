import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="COMP3005 Assignment 3 Q1",
    user="postgres",
    password="1262523",
    host="localhost",
    port="5432"
)

# Create a cursor object
cur = conn.cursor()

"""
Retrieve all the tuples from the students table
"""
def getAllStudents():
    cur.execute("SELECT * FROM students;") #SQL Query
    rows = cur.fetchall()
    
    # Print the rows
    for row in rows:
        print(row)

"""
Add a student entry into the table given the firstName, lastName, email, and enrollmentDate
"""    
def addStudent(firstName, lastName, email, enrollmentDate):
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s , %s, %s, %s)", (firstName, lastName, email, enrollmentDate))
    conn.commit()

"""
Update an email address in the student table based on the studentID
"""    
def updateStudent(studentID, email):
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s",(email, studentID)) #SQL Query
    conn.commit()

"""
Delete the entry of student which studentID
""" 
def deleteStudent(studentID):
    cur.execute("DELETE from students WHERE student_id = %s", (studentID,)) #SQL Query
    conn.commit()

"""
Close the connection to the Database
"""
def closeConnection(): 
    cur.close()
    conn.close()


###TEST METHOD CALLS######
#getAllStudents()
    
#addStudent("Test", "test", "Test.test@example.com", "2024-03-18")
#getAllStudents()
    
#updateStudent(4, "Test.test@gmail.com")
#getAllStudents()
    
#deleteStudent(4)
#getAllStudents()