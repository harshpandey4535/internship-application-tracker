import sqlite3


#adding application
def add_application():
    conn = sqlite3.connect("application.db")
    cursor = conn.cursor()

    company = input("Enter Company Name: ")
    Role = input("Enter Role: ")

    valid_status = ["applied", "interview" "rejected", "selected"]
    status = input("Enter status of Application \n(applied/interview/selected/rejected): ")
    while status not in valid_status:
        print("invalid status ")
        status = input("enter valid status").lower()

    date_applied = input("Enter date_applied: ")

    cursor.execute("""
    INSERT INTO APPLICATIONS(company, Role, status, date_applied) 
     VALUES (?,?,?,?)
    """,(company,Role,status,date_applied))
    
    conn.commit()
    conn.close()

    print("Application added successfully")



#viewing application
def view_application():
    conn = sqlite3.connect("application.db")
    cursor = conn.cursor()

    cursor.execute("""SELECT*FROM APPLICATIONS """)

    rows = cursor.fetchall()

    conn.close()


    if len(rows) == 0:
        print("No Application Found")

    else:
        print("=== Application Found ===")

        for row in rows:
            print(f"""
id: {row[0]}
company: {row[1]}
role: {row[2]}
status:{row[3]}
date_applied: {row[4]}
""")


#updating the application
def update_application():
    conn = sqlite3.connect("application.db")
    cursor = conn.cursor()

    id_numb = input("Enter the ID number to update the status: ")
    new_status = input("Enter the New Status: ")

    cursor.execute("""
    UPDATE APPLICATIONS
    set status = ?
    where id = ?
    """, (new_status, id_numb))

    conn.commit()
    conn.close()


# Deleting the Application
def delete_application():
    conn = sqlite3.connect("application.db")
    cursor = conn.cursor()

    id_num = input("Enter the ID No. to Delete the Application: ")

    cursor.execute("""
    DELETE FROM APPLICATIONS
    where id = ?
    """, (id_num))

    conn.commit()
    conn.close()

    print("Application deleted successfully: ")


#searching application
def search_application():
    conn = sqlite3.connect("application.db")
    cursor = conn.cursor()

    comp_name = input("Enter the Company name to search the Application: ")

    cursor.execute("""
    SELECT * FROM APPLICATIONS
    WHERE company = ?
    """, (comp_name,))

    rows = cursor.fetchall()

    conn.close()

    if len(rows) == "0":
        print("No application found")

    else:
        print("\n=== Search Results ===")
        
        
        for row in rows:
            print(f"""
id: {row[0]}
company: {row[1]}
role: {row[2]}
status:{row[3]}
date_applied: {row[4]}
""")


#showing statistics
def show_application():
    conn = sqlite3.connect("application.db")
    cursor = conn.cursor()

    #total application
    cursor.execute("""SELECT COUNT (*) FROM APPLICATIONS""")
    total = cursor.fetchone()[0]

    #selected application
    cursor.execute("""SELECT COUNT (*) FROM APPLICATIONS
    WHERE status = 'selected'
    """)
    selected = cursor.fetchone()[0]

    #rejected application
    cursor.execute("""SELECT COUNT (*) FROM APPLICATIONS
    WHERE status = 'rejected'
    """)
    rejected = cursor.fetchone()[0]

    conn.close()

    print("\n=== Statistics ===")
    print(f"Total Applications: {total}")
    print(f"Selected Applications: {selected}")
    print(f"Rejected Application: {rejected}")



while True:
    print("\n=== Internship Application tracker ===")
    print("1. Add Application")
    print("2. View Application")
    print("3. Update Application")
    print("4. Delete Application")
    print("5. Search Application")
    print("6. Statistics")
    print("7. Exit")

    choice = input("Enter the choice: ")

    if (choice == "1"):
        add_application()
    
    elif (choice == "2"):
        view_application()
    
    elif (choice == "3"):
        update_application()

    elif (choice == "4"):
        delete_application()
    
    elif (choice == "5"):
        search_application()

    elif (choice == "6"):
        show_application()
    
    elif (choice == "7"):
        print("Exited")
        break

    else:
        print("invalid choise")