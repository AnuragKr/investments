import mysql.connector
def displayInvNameAndCompName():
    try:
        conn = mysql.connector.connect(user='root',password='Anurag',host='127.0.0.1',database='sharktank')
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    cursor = conn.cursor()
    query = "SELECT * from investorNamesAndCompanyNames"
    cursor.execute(query)
    for (iD,investorName,companyName) in cursor:
        print("Investor Name:{}\nCompany Name:{}".format(investorName,companyName))
        print("\n")
    cursor.close()
    conn.close()

def displayCompNameAndValue():
    try:
        conn = mysql.connector.connect(user='root',password='Anurag',host='127.0.0.1',database='sharktank')
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    cursor = conn.cursor()
    query = "SELECT * from  companyNamesAndCompanyValues"
    cursor.execute(query)
    for (iD,investorName,companyName) in cursor:
        print("Company Name:{}\nCompany Value:{}".format(investorName,companyName))
        print("\n")
    cursor.close()
    conn.close()
def displayCompNameAndValue():
    try:
        conn = mysql.connector.connect(user='root',password='Anurag',host='127.0.0.1',database='sharktank')
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    cursor = conn.cursor()
    query = "SELECT * from  companyNamesAndCompanyValues"
    cursor.execute(query)
    for (iD,investorName,companyName) in cursor:
        print("Company Name:{}\nCompany Value:{}".format(investorName,companyName))
        print("\n")
    cursor.close()
    conn.close()
def displayInvNameAndAmountInvested():
    try:
        conn = mysql.connector.connect(user='root',password='Anurag',host='127.0.0.1',database='sharktank')
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    cursor = conn.cursor()
    query = "SELECT * from  investorNamesAndAmountInvested"
    cursor.execute(query)
    for (iD,investorName,amountInvested) in cursor:
        print("Investor Name:{}\nAmount Invested:{}".format(investorName,amountInvested))
        print("\n")
    cursor.close()
    conn.close()

displayInvNameAndCompName()
displayCompNameAndValue()
displayInvNameAndAmountInvested()
    
