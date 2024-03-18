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

def getAllStudents():
    cur.execute("SELECT * FROM students;")
    rows = cur.fetchall()
    
    # Print the rows
    for row in rows:
        print(row)
        
def addStudent(firstName, lastName, email, enrollmentDate):
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s , %s, %s, %s)", (firstName, lastName, email, enrollmentDate))
    conn.commit()
    
def updateStudent(studentID, email):
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s",(email, studentID))
    conn.commit()
    
def deleteStudent(studentID):
    cur.execute("DELETE from students WHERE student_id = %s", (studentID,))
    conn.commit()

def closeConnection(): 
    cur.close()
    conn.close()



# getAllStudents()
# addStudent("Test", "test", "Test.test@example.com", "2024-03-18")
# updateStudent(4, "Test.test@gmail.com")
# deleteStudent(5)