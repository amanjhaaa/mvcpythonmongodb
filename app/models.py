from flask import Flask,render_template,request
from pymongo import MongoClient
from random import randint
from app import app


from random import randint


try:
    client = MongoClient("mongodb://localhost:27017")
    db = client['patientData']
    Collection = db["mysamecollectionforpatient"]
    # client.server_info() #trigger exception if it cannot connect to database
    
except Exception as e:
    print(e)
    print("Error - Cannot connect to database")

# mysql = MySQL(app)



firstname = " "
add = 0
result = " "
age = ""
smoke = ""
alcohol = ""
measurement = ""
physical = ""
disease_family_hist = ""
patient_id = " "


# route to get data from html form and insert data into database
@app.route('/registration', methods=["GET", "POST"])
def registration():
    global patient_id
    global firstname
    # middlename = " "
    lastname = " "
    email = " "
    gender = " "
    birthday = " "
    pincode = " "

    patient_id = randint(10000000000000,99999999999999)

    if request.method == "POST":
    
        firstname = request.form['fname']

        # middlename = request.form['mname']
        lastname = request.form['lname']
        email =  request.form['email']
        gender = request.form['gender']
        birthday = request.form['birthday']
        pincode = request.form["pincode"]
        if (firstname.isspace()):
                return render_template('registration.html',
                    error_firstname="Error: First Name can't start with a SPACE",lastname=lastname,email=email,gender=gender,
                    birthday=birthday,pincode=pincode)

        if (lastname.isspace()):
                return render_template('registration.html',
                    error_lastname="Error: Last Name can't start with a SPACE",firstname=firstname,email=email,gender=gender,
                    birthday=birthday,pincode=pincode)
        Collection.insert_one(
                    {"id" :patient_id,
                        "firstname" : firstname,
                # 'middlename': middlename,
                "lastname":lastname,
                "email":email,
                "gender":gender,
                "birthday":birthday,
                "pincode":pincode}
                )
   
    return render_template("ncd1.html",patient_id = patient_id , fname = firstname,lname =  lastname,email1 = email,gender1 = gender,birthday1 = birthday,pincode1 = pincode)




@app.route('/result1',methods=['GET',"POST"])
def result1():
    if request.method == "POST":
        count = 0

# getting the value for age

        while True :
            global age 
            global smoke 
            global alcohol 
            global measurement
            global physical 
            global disease_family_hist

        
            age = request.form['age']
            
            smoke = request.form['smoke']
            
            alcohol =request.form['alcohol']

            
            measurement = request.form['measurement']
            
            physical =  request.form['physical']



            disease_family_hist =  request.form['history']
        

            count = int(age)+int(smoke)+int(alcohol)+int(measurement)+int(physical)+int(disease_family_hist)
            
            global add 
            add = count
            print(add)
            global result
            if count>4:
                result="you need screening" 

                
 
            else:
                result="No screening needed"
 

            Collection.update_one(
            {"id" :patient_id,},{"$set": {"total_count" :add,"result" :result}})

            return render_template('result1.html', add1=add,prescription=result)
    return render_template('result1.html', add1="result not found in session.")




@app.route("/searching1", methods=['GET', 'POST'])
def searching():
    if request.method == 'POST':
        x = request.form['patient if']
        mydoc =  Collection.find()
        print("++++++++++++++++++++++++++++++++++++++++")
        print(type(mydoc))
        print("++++++++++++++++++++++++++++++++++++++++")
        print(mydoc)
        lis = []
        dat=[]
        for j in mydoc:
            # print(f"  llllllllllllllll {type(j)}")
            # print(j)
            lis.append(j)
            # print(j)
            # print(type(j))
        # print(lis)
        for item in lis:
        #     # print(x)
            print(item)
            print("this is the reality ")
            print(type(item['id']))
           
            if item['id'] == int(x) :

                print(x)
               
                dat.append(item)
        #         data = item
        #         print(data)
                
            # else:
            #     print("ID is not  matching " + x)
        
    # return render_template("search.html",data = dat"a , numrows = mydoc )
    return render_template("search.html",data = dat )