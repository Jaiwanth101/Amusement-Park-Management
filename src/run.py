import subprocess as sp
import pymysql
import pymysql.cursors
from prettytable import PrettyTable

def listridesvisitor(con):
    cursor = con.cursor()
    sql = "SELECT NAME,VIP,COST FROM RIDE"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        result = cursor.fetchall()
        table = PrettyTable()
        table.field_names = ["Ride Name", "VIP", "COST"]
        for row in result:
            # print(row)
            # print(row['NAME'],row['VIP'],row['COST'])
            new_row = [row['NAME'], row['VIP'], row['COST']]
            table.add_row(new_row)
        print(table)
        # Commit your changes in the database
        con.commit()
    except:
        # Rollback in case there is any error
        con.rollback()

def listrides(con):
    cursor = con.cursor()
    sql = "SELECT * FROM RIDE"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        result = cursor.fetchall()
        table = PrettyTable()
        table.field_names = ["Ride ID", "Ride Name", "VIP", "COST"]
        for row in result:
            # print(row)
            # print(row['NAME'],row['VIP'],row['COST'])
            new_row = [row['ID'], row['NAME'], row['VIP'], row['COST']]
            table.add_row(new_row)
        print(table)
        # Commit your changes in the database
        con.commit()
    except:
        # Rollback in case there is any error
        con.rollback()

def listshops(con):
    cursor = con.cursor()
    sql = "SELECT * FROM SHOP"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        result = cursor.fetchall()
        table = PrettyTable()
        table.field_names = ["License", "Shop Name",
                             "Open?", "Shop Type", "owner SSN"]
        for row in result:
            # print(row)
            # print(row['NAME'],row['VIP'],row['COST'])
            new_row = [row['SHOP_LICENSE'], row['NAME'],
                       row['OPEN'], row['TYPE'], row['OWNER_SSN']]
            table.add_row(new_row)
        print(table)
        # Commit your changes in the database
        con.commit()
    except:
        # Rollback in case there is any error
        con.rollback()

def listshopsvisitor(con):
    cursor = con.cursor()
    sql = "SELECT NAME,OPEN,TYPE FROM SHOP"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        result = cursor.fetchall()
        table = PrettyTable()
        table.field_names = ["Shop Name", "Open?", "Shop Type"]
        for row in result:
            # print(row)
            # print(row['NAME'],row['VIP'],row['COST'])
            new_row = [row['NAME'], row['OPEN'], row['TYPE']]
            table.add_row(new_row)
        print(table)
        # Commit your changes in the database
        con.commit()
    except:
        # Rollback in case there is any error
        con.rollback()

def listmess(con):
    cursor = con.cursor()
    sql = "SELECT * FROM MESS"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        result = cursor.fetchall()
        table = PrettyTable()
        table.field_names = ["Mess Name", "Price", "Vegetarian?"]
        for row in result:
            # print(row)
            # print(row['NAME'],row['VIP'],row['COST'])
            new_row = [row['NAME'], row['PRICE'], row['VEGETARIAN']]
            table.add_row(new_row)
        print(table)
        # Commit your changes in the database
        con.commit()
    except:
        # Rollback in case there is any error
        con.rollback()

def listmessnewvis(con):
    cursor = con.cursor()
    sql = "SELECT @a:=@a+1 Sno, NAME as Mess FROM MESS, (SELECT @a:= 0) AS a"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        result = cursor.fetchall()
        table = PrettyTable()
        table.field_names = ["SNO", "MESS"]
        for row in result:
            # print(row)
            # print(row['NAME'],row['VIP'],row['COST'])
            new_row = [int(row['Sno']), row['Mess']]
            table.add_row(new_row)
        print(table)
        # Commit your changes in the database
        con.commit()
    except:
        # Rollback in case there is any error
        con.rollback()

def issuecard(con):
    while True:
        try:
            visitor_number = int(input("Enter your visitor number : "))
        except ValueError:
            print("Please Enter a valid integer")
            continue
        else:
            break
    cursor = con.cursor()
    sql = "SELECT NUMBER FROM VISITOR"
    sql1 = "SELECT VISITOR_NUMBER,CARD_ID FROM CARD WHERE VISITOR_NUMBER = {}".format(
        visitor_number)
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        arr = []
        for row in result:
            arr.append(row['NUMBER'])
        # print(arr)
        cursor.execute(sql1)
        result = cursor.fetchall()
        arr1 = []
        for row in result:
            arr1.append(row['CARD_ID'])
        # print(arr1)
    except:
        cursor.rollback()
    if(visitor_number not in arr):
        print("Invalid visitor number. exiting ..")
    else:
        print("To issue a new card you have to specify its balance and VIP status")
        while True:
            try:
                balance = int(input("Enter balance of new card : "))
            except ValueError:
                print("Please Enter a valid integer")
                continue
            else:
                break
        while True:
            new_status = input(
                "Enter VIP status for the card : ")
            if (new_status.lower() not in ('yes', 'no')):
                print(
                    "Please enter either yes or no corresponding to VIP status")
                continue
            else:
                break
        if not arr1:
            card_id = "C001"
        else:
            new_card_id = int(arr1[-1][1:4]) + 1
            if(len(str(new_card_id)) == 1):
                card_id = "C00" + str(new_card_id)
            elif(len(str(new_card_id)) == 2):
                card_id = "C0" + str(new_card_id)
            elif(len(str(new_card_id)) == 3):
                card_id = "C" + str(new_card_id)

        query = "INSERT INTO CARD(VISITOR_NUMBER,CARD_ID ,BALANCE , VIP) VALUES ('%s','%s',%d,'%s')" % (
            visitor_number, card_id, balance, new_status)
        try:
            cursor.execute(query)
            con.commit()
            print("Database Updated")
            print("A new card with card id", card_id, "issued to",
                  visitor_number, "with balance", balance)
        except:
            cursor.rollback()
        # print(visitor_number, balance, new_status)

def enjoyride(con):
    print("enjoyride")
    print("To enjoy rides you have to enter your visitor number card ID name of the ride you wish to enjoy")
    print("Make sure you have sufficient balance in your card")
    print("Make sure you give feedback of the ride at the end")
    ride_name = input("Enter the name of the ride : ")
    sql = "SELECT * FROM RIDE"
    cursor = con.cursor()
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        arr = []
        vip = {}
        ride_id = {}
        cost = {}
        for row in result:
            arr.append(row['NAME'].lower())
            vip[row['NAME'].lower()] = row['VIP']
            ride_id[row['NAME'].lower()] = row['ID']
            cost[row['NAME'].lower()] = row['COST']
    except:
        cursor.rollback()
    if (ride_name.lower() not in arr):
        print("Given ride name does not exist. exiting ..")
    else:
        while True:
            try:
                visitor_number = int(input("Enter your visitor number : "))
            except ValueError:
                print("Please Enter a valid integer")
                continue
            else:
                break
        card_id = input("Enter Card ID : ")
        sql = "SELECT * FROM CARD"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            # print(results)
            a = []
            balance = {}
            vip_card = {}
            for row in results:
                b = []
                b.append(row['VISITOR_NUMBER'])
                b.append(row['CARD_ID'])
                a.append(b)
                balance[str(b[0])+b[1]] = row['BALANCE']
                vip_card[str(b[0])+b[1]] = row['VIP'].lower()
            # print(a)
        except:
            cursor.rollback()
        c = [visitor_number, card_id]
        if c not in a:
            print(
                "Entered visitor number card id combination does not exist. exiting ..")
        else:
            if(vip[ride_name.lower()].lower() == "yes"):
                if(vip_card[str(visitor_number)+card_id].lower() == "yes"):
                    new_val = balance[str(visitor_number) +
                                      card_id] - cost[ride_name.lower()]
                    try:
                        query = "UPDATE CARD SET BALANCE = %d WHERE VISITOR_NUMBER = %d AND CARD_ID = '%s'" % (
                            new_val, visitor_number, card_id)
                        cursor.execute(query)
                        con.commit()
                        print("Visitor with number", visitor_number, "enjoyed ride",
                              ride_name.lower(), "and used his card with id", card_id)
                        print("Updated balance in the card is", new_val)
                        query1 = "INSERT INTO ENJOYS (VISITOR_NUMBER,RIDE_ID) VALUES (%d,%d)" % (
                            visitor_number, ride_id[ride_name.lower()])
                        try:
                            cursor.execute(query1)
                            con.commit()
                        except:
                            con.rollback()
                        print("Please give your valuable feedback on the ride")
                        while True:
                            try:
                                rating = int(
                                    input("Enter the rating you would like to give : "))
                            except ValueError:
                                print(
                                    "Please Enter a valid integer between 0 and 5")
                                continue
                            else:
                                if(rating > 5 or rating < 0):
                                    print(
                                        "Please enter a valid integer between 0 and 5")
                                else:
                                    break
                        # print(visitor_number, card_id , int(ride_id[ride_name]))
                        review = input("Please write your review : ")
                        query2 = "SELECT VISITOR_NUMBER,FEEDBACK_NUMBER FROM FEEDBACK WHERE VISITOR_NUMBER = {}".format(
                            visitor_number)
                        cursor.execute(query2)
                        result = cursor.fetchall()
                        if not result:
                            feedback_no = "F001"
                        else:
                            arr1 = []
                            for row in result:
                                arr1.append(row['FEEDBACK_NUMBER'])
                            new_feedback_no = int(arr1[-1][1:4]) + 1
                            if(len(str(new_feedback_no)) == 1):
                                feedback_no = "F00" + str(new_feedback_no)
                            elif(len(str(new_feedback_no)) == 2):
                                feedback_no = "F0" + str(new_feedback_no)
                            elif(len(str(new_feedback_no)) == 3):
                                feedback_no = "F" + str(new_feedback_no)
                        query3 = "INSERT INTO FEEDBACK(VISITOR_NUMBER,FEEDBACK_NUMBER,RATING,REVIEW) VALUES(%d,'%s',%d,'%s')" % (
                            visitor_number, feedback_no, rating, review)
                        query4 = "INSERT INTO USES(VISITOR_NUMBER,CARD_ID,FEEDBACK_NUMBER,RIDE_ID) VALUES(%d,'%s','%s',%d)" % (
                            visitor_number, card_id, feedback_no, int(ride_id[ride_name]))
                        cursor.execute(query3)
                        con.commit()
                        cursor.execute(query4)
                        con.commit()

                    except:
                        cursor.rollback()

                else:
                    print("Ride only available to VIP issued cards")
            else:
                if(cost[ride_name.lower()] > balance[str(visitor_number)+card_id]):
                    print("Insufficient Balance")
                else:
                    new_val = balance[str(visitor_number) +
                                      card_id] - cost[ride_name.lower()]
                    try:
                        query = "UPDATE CARD SET BALANCE = %d WHERE VISITOR_NUMBER = %d AND CARD_ID = '%s'" % (
                            new_val, visitor_number, card_id)
                        cursor.execute(query)
                        con.commit()
                        print("Visitor with number", visitor_number, "enjoyed ride",
                              ride_name.lower(), "and used his card with id", card_id)
                        print("Updated balance in the card is", new_val)
                        print(ride_id[ride_name.lower()])
                        query1 = "INSERT INTO ENJOYS (VISITOR_NUMBER, RIDE_ID) VALUES (%d,%d)" % (visitor_number, ride_id[ride_name.lower()])
                        try:
                            cursor.execute(query1)
                            con.commit()
                        except:
                            con.rollback()
                        print("Please give your valuable feedback on the ride")
                        while True:
                            try:
                                rating = int(
                                    input("Enter the rating you would like to give : "))
                            except ValueError:
                                print(
                                    "Please Enter a valid integer between 0 and 5")
                                continue
                            else:
                                if(rating > 5 or rating < 0):
                                    print(
                                        "Please enter a valid integer between 0 and 5")
                                else:
                                    break
                        # print(visitor_number, card_id , int(ride_id[ride_name]))
                        review = input("Please write your review : ")
                        query2 = "SELECT VISITOR_NUMBER,FEEDBACK_NUMBER FROM FEEDBACK WHERE VISITOR_NUMBER = {}".format(
                            visitor_number)
                        try:
                            cursor.execute(query2)
                            con.commit()
                        except:
                            con.rollback()
                        result = cursor.fetchall()
                        if not result:
                            feedback_no = "F001"
                        else:
                            arr1 = []
                            for row in result:
                                arr1.append(row['FEEDBACK_NUMBER'])
                            new_feedback_no = int(arr1[-1][1:4]) + 1
                            if(len(str(new_feedback_no)) == 1):
                                feedback_no = "F00" + str(new_feedback_no)
                            elif(len(str(new_feedback_no)) == 2):
                                feedback_no = "F0" + str(new_feedback_no)
                            elif(len(str(new_feedback_no)) == 3):
                                feedback_no = "F" + str(new_feedback_no)
                        query3 = "INSERT INTO FEEDBACK(VISITOR_NUMBER,FEEDBACK_NUMBER,RATING,REVIEW) VALUES(%d,'%s',%d,'%s')" % (
                            visitor_number, feedback_no, rating, review)
                        query4 = "INSERT INTO USES(VISITOR_NUMBER,CARD_ID,FEEDBACK_NUMBER,RIDE_ID) VALUES(%d,'%s','%s',%d)" % (
                            visitor_number, card_id, feedback_no, int(ride_id[ride_name]))
                        cursor.execute(query3)
                        con.commit()
                        cursor.execute(query4)
                        con.commit()

                    except:
                        cursor.rollback()

def buyfromshop(con):
    print("To buy items at a shop you have to enter your visitor number card ID name of the shop and price of items purchased")
    print("Make sure you have sufficient balance in your card")
    listshopsvisitor(con)
    shop_name = input("Enter the name of the shop : ")
    sql = "SELECT SHOP_LICENSE,NAME FROM SHOP"
    cursor = con.cursor()
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        arr = []
        license = {}
        for row in result:
            arr.append(row['NAME'].lower())
            license[row['NAME'].lower()] = row['SHOP_LICENSE']
    except:
        cursor.rollback()
    if (shop_name.lower() not in arr):
        print("Entered shop name is invalid. exiting..")
    else:
        while True:
            try:
                visitor_number = int(input("Enter your visitor number : "))
            except ValueError:
                print("Please Enter a valid integer")
                continue
            else:
                break
        card_id = input("Enter Card ID : ")
        sql = "SELECT VISITOR_NUMBER,CARD_ID,BALANCE FROM CARD"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            # print(results)
            a = []
            balance = {}
            for row in results:
                b = []
                b.append(row['VISITOR_NUMBER'])
                b.append(row['CARD_ID'])
                a.append(b)
                balance[str(b[0])+b[1]] = row['BALANCE']
            # print(a)
        except:
            cursor.rollback()
        c = [visitor_number, card_id]
        if c not in a:
            print(
                "Entered visitor number card id comnbination does not exist. exiting ..")
        else:
            while True:
                try:
                    amount = int(
                        input("Enter the amount of the items purchased : "))
                except ValueError:
                    print("Please Enter a valid integer")
                    continue
                else:
                    break
            if(amount > balance[str(visitor_number)+card_id]):
                print("Insufficient Balance")
            else:
                new_val = balance[str(visitor_number) + card_id] - amount
                try:
                    query = "UPDATE CARD SET BALANCE = %d WHERE VISITOR_NUMBER = %d AND CARD_ID = '%s'" % (
                        new_val, visitor_number, card_id)
                    cursor.execute(query)
                    con.commit()
                    print("Visitor with number", visitor_number, "bought items at shop",
                          shop_name, "and used his card with id", card_id)
                    print("Updated balance in the card is", new_val)
                    query1 = "INSERT INTO  BUYS (VISITOR_NUMBER,SHOP_LICENSE) VALUES ('%s','%s')" % (
                        visitor_number, license[shop_name.lower()])
                    cursor.execute(query1)
                    con.commit()
                except:
                    cursor.rollback()

def eatatmess(con):
    print("To eat at mess you have to enter your visitor number card ID and mess you want to have food at")
    print("Make sure you have sufficient balance in your card")
    listmess(con)
    mess_name = input(
        "Please enter the name of the mess where you want to have food : ")
    cursor = con.cursor()
    sql = "SELECT NAME,PRICE FROM MESS"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        arr = []
        cost = {}
        for row in result:
            if (row['NAME'].lower() not in arr):
                arr.append(row['NAME'].lower())
            cost[row['NAME'].lower()] = row['PRICE']
        # print(result)
        # print(arr)
        # print(cost)
    except:
        cursor.rollback()
    if (mess_name.lower() not in arr):
        print("Given Mess name is not registered exiting ..")
    else:
        while True:
            try:
                visitor_number = int(input("Enter your visitor number : "))
            except ValueError:
                print("Please Enter a valid integer")
                continue
            else:
                break
        card_id = input("Enter Card ID : ")
        sql = "SELECT VISITOR_NUMBER,CARD_ID,BALANCE FROM CARD"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            # print(results)
            a = []
            balance = {}
            for row in results:
                b = []
                b.append(row['VISITOR_NUMBER'])
                b.append(row['CARD_ID'])
                a.append(b)
                balance[str(b[0])+b[1]] = row['BALANCE']
            # print(a)
        except:
            cursor.rollback()
        c = [visitor_number, card_id]
        if c not in a:
            print(
                "Entered visitor number card id comnbination does not exist. exiting ..")
        else:
            if(cost[mess_name.lower()] > balance[str(visitor_number)+card_id]):
                print("Insufficient Balance")
            else:
                new_val = balance[str(visitor_number) +
                                  card_id] - cost[mess_name.lower()]
                try:
                    query = "UPDATE CARD SET BALANCE = %d WHERE VISITOR_NUMBER = %d AND CARD_ID = '%s'" % (
                        new_val, visitor_number, card_id)
                    cursor.execute(query)
                    con.commit()
                    print("Visitor with number", visitor_number, "ate food at",
                          mess_name.lower(), "and used his card with id", card_id)
                    print("Updated balance in the card is", new_val)
                    query1 = "UPDATE VISITOR SET EATS_AT = '%s' WHERE NUMBER = %d" % (
                        mess_name, visitor_number)
                    cursor.execute(query1)
                    con.commit()
                except:
                    cursor.rollback()

def listemployees(con):
    print("employees")
    cursor = con.cursor()
    sql = "SELECT * FROM EMPLOYEE"
    try:
            # Execute the SQL command
        cursor.execute(sql)
        result = cursor.fetchall()
        table = PrettyTable()
        table.field_names = ["SSN", "Name", "Birth Date", "Street",
                             "Area", "City", "Assigned_Mess", "Assigned_Ride_ID", "Job_Type"]
        for row in result:
                # print(row)
                # print(row['NAME'],row['VIP'],row['COST'])
            new_row = [row["SSN"], row["NAME"], row["BIRTHDATE"], row["STREET"], row["AREA"],
                       row["CITY"], row["ASSIGNED_MESS"], row["ASSIGNED_RIDE_ID"], row["JOB_TYPE"]]
            table.add_row(new_row)
        print(table)
        # Commit your changes in the database
        con.commit()
    except:
        # Rollback in case there is any error
        con.rollback()

def modifyemployeedetails(con):
    while True:
        try:
            SSN = int(
                input("Enter SSN of the Employee whose details have to be modified : "))
        except ValueError:
            print("Please Enter a valid integer")
            continue
        else:
            break
    cursor = con.cursor()
    sql = "SELECT SSN FROM EMPLOYEE WHERE SSN = {}".format(SSN)
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        if (result == None):
            print("Could Not find a Employee with given SSN.\n Exiting ..")
        else:
            while(1):
                SSN = result["SSN"]
                print("You can modify the following entries.")
                print("1. Name")
                print("2. Birthdate")
                print("3. Street")
                print("4. Area")
                print("5. City")
                while True:
                    try:
                        choice = int(
                            input("Enter which field you want to modify for this EMPLOYEE : "))
                    except ValueError:
                        print("Please Enter a valid integer")
                        continue
                    else:
                        break
                if(choice == 1 ) :
                    print("Modifying Name of the Employee")       
                    while True:
                        try:
                            new_Name= str(
                                    input("Enter New Name for the employee : "))
                        except ValueError:
                            print("Please Enter a valid string")
                            continue
                        else:
                            break
                    query = "UPDATE EMPLOYEE SET NAME = '%s' where SSN = %d" % (
                        new_Name,SSN)
                    try:
                        cursor.execute(query)
                        con.commit()
                        print("Database Updated")
                    except:
                        cursor.rollback()
                    break
                elif (choice==2):
                    print("Modifying BIRTHDATE of the Employee")       
                    while True:
                        try:
                            new_birth= str(
                                    input("Enter updated DATE_OF_BIRTH for the employee: "))
                        except ValueError:
                                print("Please Enter a valid string")
                                continue
                        else:
                            break
                    while True:
                        try:
                            new_age = int(input("Enter updated AGE of the employee: "))
                        except ValueError:
                            print("Please Enter a valid integer.")
                            continue
                        else:
                            break

                    cursor.execute("SET foreign_key_checks = 0;")
                    query = "UPDATE EMPLOYEE SET BIRTHDATE = '%s' where SSN = %d" % (new_birth, SSN)                
                    try:
                        cursor.execute(query)
                        con.commit()
                        print("Database Updated: EMPLOYEE.BIRTHDATE")
                    except:
                            cursor.rollback()

                    query = "INSERT IGNORE INTO EMP_AGE (BIRTHDATE, AGE) VALUES ('%s', %d)" % (new_birth, new_age)
                    try:
                        cursor.execute(query)
                        con.commit()
                        print("Database Updated: EMP_AGE.BIRTHDATE")
                    except:
                        cursor.rollback()

                    cursor.execute("SET foreign_key_checks = 1;")

                elif(choice==3):
                    print("Modifying Street of the Employee")       
                    while True:
                        try:
                            new_Name= str(
                                    input("Enter updated Street for the employee : "))
                        except ValueError:
                                print("Please Enter a valid string")
                                continue
                        else:
                            break
                    query = "UPDATE EMPLOYEE SET STREET = '%s' where SSN = %d" % (
                        new_Name,SSN)
                    try:
                        cursor.execute(query)
                        con.commit()
                        print("Database Updated")
                    except:
                            cursor.rollback()
                    break
                elif(choice==4):
                    print("Modifying Area of the Employee")       
                    while True:
                        try:
                            new_Name= str(
                                    input("Enter updated Area for the employee : "))
                        except ValueError:
                            print("Please Enter a valid string")
                            continue
                        else:
                            break
                    query = "UPDATE EMPLOYEE SET AREA = '%s' where SSN = %d" % (
                        new_Name,SSN)
                    try:
                        cursor.execute(query)
                        con.commit()
                        print("Database Updated")
                    except:
                        cursor.rollback()
                    break
                elif(choice==5):
                    print("Modifying City of the Employee")       
                    while True:
                        try:
                            new_Name= str(
                                    input("Enter updated City for the employee : "))
                        except ValueError:
                            print("Please Enter a valid string")
                            continue
                        else:
                            break
                    query = "UPDATE EMPLOYEE SET CITY = '%s' where SSN = %d" % (
                        new_Name,SSN)
                    try:
                        cursor.execute(query)
                        con.commit()
                        print("Database Updated")
                    except:
                        cursor.rollback()
                    break
                else:
                    print("enter 1 to 5 with respect to the field you want to edit")
                continue
    except:
        cursor.rollback()

def modifyridedetails(con):
    while True:
        try:
            ride_id = int(
                input("Enter Ride ID of the ride whose details have to be modified : "))
        except ValueError:
            print("Please Enter a valid integer")
            continue
        else:
            break
    cursor = con.cursor()
    sql = "SELECT ID FROM RIDE WHERE ID = {}".format(ride_id)
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        # print(result)
        if (result == None):
            print("Could Not find a Ride with given Ride ID exiting ..")
        else:
            while(1):
                id = result['ID']
                print("You can modify the following entries.")
                print("1. Cost")
                print("2. VIP status")
                while True:
                    try:
                        choice = int(
                            input("Enter which field you want to modify for this ride : "))
                    except ValueError:
                        print("Please Enter a valid integer")
                        continue
                    else:
                        break
                if(choice == 1):
                    print("Modifying field Cost of ", ride_id)
                    while True:
                        try:
                            new_cost = int(
                                input("Enter New Cost for the ride : "))
                        except ValueError:
                            print("Please Enter a valid integer")
                            continue
                        else:
                            break
                    query = "UPDATE RIDE SET COST = %d WHERE ID = %d" % (
                            new_cost, id)
                    try:
                        cursor.execute(query)
                        con.commit()
                        print("Database Updated")
                    except:
                        cursor.rollback()
                    break
                elif(choice == 2):
                    print("Modifying field Cost of ", ride_id)
                    while True:
                        new_status = input(
                            "Enter New VIP status for the ride : ")
                        if (new_status.lower() not in ('yes', 'no')):
                            print(
                                "Please enter either yes or no corresponding to VIP status")
                            continue
                        else:
                            break
                    query = "UPDATE RIDE SET VIP = '%s' WHERE ID = %d" % (
                        new_status, id)
                    try:
                        cursor.execute(query)
                        con.commit()
                        print("Database Updated")
                    except:
                        cursor.rollback()
                    break

                else:
                    print(
                        "Enter either 1 or 2 with respect to the field you want to edit")
                    continue
    except:
        cursor.rollback()

def modifyshopdetails(con):
    shop_license = input(
        "Enter Shop license of the shop whose details have to be modified : ")
    # print(shop_license)
    cursor = con.cursor()
    sql = "SELECT SHOP_LICENSE FROM SHOP"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        arr = []
        for row in result:
            arr.append(row['SHOP_LICENSE'])
        # print(result)
        # print(arr)
    except:
        cursor.rollback()
    if (shop_license not in arr):
        print("Could not find a shop with given license exiting .. ")
    else:
        print("You can modify the field \"OPEN\" for the given shop")
        tmp = input("Enter any key to CONTINUE>")
        while True:
            new_status = input(
                "Enter New shop status : ")
            if (new_status.lower() not in ('yes', 'no')):
                print("Please enter either yes or no corresponding to shop status")
                continue
            else:
                break
        query = "UPDATE SHOP SET OPEN = '%s' WHERE SHOP_LICENSE = '%s'" % (
            new_status, shop_license)
        try:
            cursor.execute(query)
            con.commit()
            print("Database Updated")
        except:
            cursor.rollback()

def modifymessdetails(con):
    mess_name = input(
        "Please enter the name of the mess whose details have to be modified : ")
    cursor = con.cursor()
    sql = "SELECT NAME FROM MESS_FOOD"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        arr = []
        for row in result:
            if (row['NAME'].lower() not in arr):
                arr.append(row['NAME'].lower())
        # print(result)
        # print(arr)
    except:
        cursor.rollback()
    if (mess_name.lower() not in arr):
        print("Given Mess name is not registered exiting ..")
    else:
        print("You can add more items to given mess")
        tmp = input("Enter any key to CONTINUE>")
        new_item = input(
            "Enter New item to be added to given mess : ")
        query = "INSERT INTO MESS_FOOD(NAME ,ITEM) VALUES ('%s','%s')" % (
            mess_name, new_item)
        try:
            cursor.execute(query)
            con.commit()
            print("Database Updated")
        except:
            cursor.rollback()

def hireemployee(con):
    print("Adding New Employee:")
    while True:
        try:
            SSN = int(
                input("Enter the SSN of the New Employee:"))
        except ValueError:
            print("Please Enter a valid integer")
            continue
        else:
            break
    while True:
        try:
            new_name = str(
                input("Please enter the name of the new employee: "))
        except ValueError:
            print("Please enter a valid string")
            continue
        else:
            break
    # new_ssn = int(
        # input("Enter New Cost for the ride : ")) 
    # new_name = input(
        # "Please enter the name of the new employee: ")
    new_bday = input(
        "Please enter the BirthDate of the new employee: ")
    new_street = input(
        "Please enter the Street of the new employee: ")
    new_area = input(
        "Please enter the Area of the new employee: ")
    new_city = input(
        "Please enter the City of the new employee: ")
    new_AssignedMess = input(
        "Please enter the Assigned_mess of the new employee: ")
    new_AssignedRide = input(
        "Please enter the AssignedRide of the new employee: ")
    new_JobType = input(
        "Please enter the Job_Type of the new employee: ")
    new_Age = int(input(
        "Please enter the Age of the new employee: "))
    cursor = con.cursor()
    cursor.execute("SET foreign_key_checks = 0")
    query = "INSERT INTO `EMPLOYEE` VALUES (%d,'%s','%s','%s','%s','%s','%s','%s','%s');" % (
        SSN,new_name,new_bday,new_street,new_area,new_city,new_AssignedMess,new_AssignedRide,new_JobType) 
    try:
        cursor.execute(query)
        con.commit()
    except:
        cursor.rollback()

    query = "INSERT IGNORE INTO `EMP_AGE` (BIRTHDATE, AGE) VALUES ('%s',%d)" % (new_bday, new_Age)
    try:
        cursor.execute(query)
        con.commit()
        print("Database Updated")
    except:
        cursor.rollback()
    cursor.execute("SET foreign_key_checks = 1")

def fireemployee(con):
    print("To remove employee")
    while True:
        try:
            SSN = int(
                input("Enter the SSN of Employee you want to remove and he cant be a shop_owner:"))
        except ValueError:
            print("Please Enter a valid integer")
            continue
        else:
            break
    cursor = con.cursor()
    query = "DELETE FROM `EMPLOYEE` WHERE SSN = %d" % (
        SSN)
    try:
        cursor.execute(query)
        con.commit()
        print("Database Updated")
    except:
        cursor.rollback()    

def newvisitor(con):
    cursor = con.cursor()
    print("Registering new visitor...")
    while True:
        try:
            visit_number = int(input("Enter phone number: "))
        except ValueError:
            print("Please enter a valid number.")
        else:
            break
    visit_name = input("Enter full name: ")
    visit_age = int(input("Enter age:"))
    print("Choose the desired mess:")
    # listmess(con)
    list_mess = "SELECT @a:=@a+1 Sno, NAME as Mess FROM MESS, (SELECT @a:= 0) AS a;"
    try:
        cursor.execute(list_mess)
    except:
        cursor.rollback()
    # callfunction(3, con)   
    listmessnewvis(con)
    while True: 
        try:
            visit_mess = int(input())
        except ValueError:
            print("Please enter a valid option.")
        else:
            break

    alloc_mess_cmd = "SELECT list.Mess FROM (SELECT @a:=@a+1 Sno, NAME as Mess FROM MESS, (SELECT @a:= 0) AS a) as list WHERE list.Sno = {};".format(visit_mess)
    alloc_mess = []
    try:
        cursor.execute(alloc_mess_cmd)
        result = cursor.fetchall()
        for row in result:
            alloc_mess.append(row["Mess"])       
    except:
        cursor.rollback()
    add_visit = "INSERT INTO VISITOR (NUMBER, NAME, AGE, EATS_AT) VALUES (%d, '%s', %d, '%s');" % (visit_number, visit_name, visit_age, alloc_mess[0])
    try:
        cursor.execute(add_visit)
        con.commit()
        print("Database updated!")
    except:
        cursor.rollback()

def callfunction(choice, con):
    if(choice == 1):
        listrides(con)
    elif (choice == 2):
        listshops(con)
    elif (choice == 3):
        listmess(con)
    elif (choice == 4):
        listemployees(con)
    elif (choice == 5):
        modifyemployeedetails(con)
    elif (choice == 6):
        modifyridedetails(con)
    elif(choice == 7):
        modifymessdetails(con)
    elif(choice == 8):
        modifyshopdetails(con)
    elif (choice == 9):
        hireemployee(con)
    elif(choice == 10):
        fireemployee(con)
    elif(choice == 11):
        newvisitor(con)


while (1):
    tmp = sp.call('clear', shell=True)
    print("1. Visitor")
    print("2. Employee")
    print("3. Exit")
    while True:
        try:
            choice = int(input("Enter number corresponding to your status : "))
        except ValueError:
            print("Please Enter a valid integer")
            continue
        else:
            break
    if(choice == 1):
        try:
            con = pymysql.connect(host='localhost',
                                  user='username',
                                  password='password',
                                  db='AMUSEMENT_PARK',
                                  cursorclass=pymysql.cursors.DictCursor)
            tmp = sp.call('clear', shell=True)

            if(con.open):
                print("Connected")
            else:
                print("Failed to connect")
                tmp = input("Enter any key to CONTINUE>")
            with con:
                while(1):
                    print("1. View list of all rides")
                    print("2. View list of all shops")
                    print("3. View list of all mess")
                    print("4. Issue a card")
                    print("5. Enjoy ride")
                    print("6. Buy from shop")
                    print("7. Eat at Mess")
                    print("8. Logout")
                    while True:
                        try:
                            choice_visitor = int(
                                input("Enter your preference : "))
                        except ValueError:
                            print("Please Enter a valid integer")
                            continue
                        else:
                            break
                    if(choice_visitor == 1):
                        listridesvisitor(con)
                    elif (choice_visitor == 2):
                        listshopsvisitor(con)
                    elif (choice_visitor == 3):
                        listmess(con)
                    elif (choice_visitor == 4):
                        issuecard(con)
                    elif (choice_visitor == 5):
                        enjoyride(con)
                    elif (choice_visitor == 6):
                        buyfromshop(con)
                    elif(choice_visitor == 7):
                        eatatmess(con)
                    elif (choice_visitor == 8):
                        print("Logging out ....")
                        break
        except:
            tmp = sp.call('clear', shell=True)
            print("Sorry, we could not connect to the database")
            tmp = input("Enter any key to CONTINUE>")

    elif (choice == 2):
        tmp = sp.call('clear', shell=True)
        print("Employee Authentication")
        username = input("Username: ")
        password = input("Password: ")

        try:
            con = pymysql.connect(host='localhost',
                                  user='username',
                                  password='password',
                                  db='AMUSEMENT_PARK',
                                  cursorclass=pymysql.cursors.DictCursor)
            tmp = sp.call('clear', shell=True)

            if(con.open):
                print("Connected")
            else:
                print("Failed to connect")
            tmp = input("Enter any key to CONTINUE>")

            with con:
                while(1):
                    print("1. View list of all rides")
                    print("2. View list of all shops")
                    print("3. View list of all mess")
                    print("4. View list of all employees")
                    print("5. Modify employee details")
                    print("6. Modify ride details")
                    print("7. Modify mess details")
                    print("8. Modify shop details")
                    print("9. Recruit new employee")
                    print("10. Fire an employee")
                    print("11. Add new visitor")
                    print("12. Logout")
                    while True:
                        try:
                            choice_employee = int(
                                input("Enter your choice : "))
                        except ValueError:
                            print("Please Enter a valid integer")
                            continue
                        else:
                            break
                    if(choice_employee == 12):
                        print("Logging out ....")
                        break
                    else:
                        callfunction(choice_employee, con)
        except:
            tmp = sp.call('clear', shell=True)
            print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
            tmp = input("Enter any key to CONTINUE>")
    elif(choice == 3):
        exit()
