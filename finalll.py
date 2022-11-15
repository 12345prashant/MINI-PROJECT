# CODE FOR VACCINE REGISTRATION AND CERTIFICATE

from datetime import datetime, timedelta   # import date time library to get current time and date
from geopy.geocoders import Nominatim      # this library is used to get current location
import random                              # this library is used to get random number
import cProfile                            # this library is used for profiling
loc = Nominatim(user_agent="GetLoc")

global First_Name , Last_Name , location_for_appointment,Aadhar_no,first_dose_date,dob,age,vaccine
Application_id=random.randint(1000,100000)
print("Hey! Welcome To The Vaccination Drive...\n")
print("Enter Your Phone Number To Login or Sign up")
phone_no = int(input())                    # getting phone number input from user

OTP_generate=random.randint(1000,100000)   # this will generate a random OTP
print("Your OTP for Login in vaccination is ", OTP_generate) 
'''
This function is used to verify OTP entered by the user
'''
def Verify_OTP( otp):
    if(otp==OTP_generate):
        print("OTP verified!! Let's Continue ")
    else:
        print("INCORRECT OTP, Please click on Resend OTP To Try Again") 
        Get_OTP()  
       
'''
This function is used to take input for OTP from user
'''
def Get_OTP():
    print(''' OTP Sent on The Given Phone Number
      Verify To Continue''')
    global otp
    otp = int(input("Enter the OTP\n"))
    Verify_OTP(otp)                       # calling the function to verify OTP

Get_OTP()                                 # calling the function to get OTP

'''
Below function will generate your second dose certificate
'''
def second_dose_certificate(second_dose_date):                
    print("\n")
    print('''                        Certificate Of Covid - 19 Vaccination                  ''')
    print('''                                    Second Dose                                 ''')
    print("\n")
    print("APPLICATION ID: ",Application_id)
    print("\n")
    print("NAME: "+ First_Name +" "+ Last_Name)
    print("\n")
    print("Gender: "+ gender)
    print("\n")
    print("ID VERIFIED: ",Aadhar_no)
    print("\n")
    print("DATE OF BIRTH: "+ dob)
    print("\n")
    print("AGE: ",age)
    print("\n")
    print("Vaccination Status : Fully Vaccinated (1st Dose)")
    print("\n")
    print("Vaccination Details:")
    print("Vaccine Name: "+ vaccine)
    print("\n")
    print("Vaccine Type: Covid 19 vaccine, non- replacing viral vector")
    print("\n")
    print("Dose Number: 2")
    print("\n")
    print("Date Of First Dose: ",first_dose_date.strftime('%d-%m-%Y'))
    print("\n")
    print("Date of Second Dose: ",second_dose_date.strftime('%d-%m-%Y'))
    print("\n")
    print("Vaccination At : "+ str(location_for_appointment))

'''
 Below function will count the number of days left for your second dose 
'''    
def second_dose_status():
    global days_left
    days_left = second_dose_date-presentday                 # finding days left by subtracting second dose day with present day using date time library function
    print("Total Days left for Your Second Dose are",days_left)

'''
Below Function will take appllication id input from user
if the entered id is correct then only user can do further process

'''
def Verification_for_second_dose():
    print("Enter the Application id provided during 1st dose")
    apply=int(input())
    if(apply==Application_id):                               # this condition is used to check entered number with application id
        print("You Can Apply On or After: \n",second_dose_date.strftime('%d-%m-%Y'))
        second_dose_status()                                # calling second dose staus function

    else:
        print("Incorrect ID\n")    

'''
Below function will schedule the second dose date 
'''
def schedule_second_dose(vaccine,first_dose_date):
    global second_dose_date
    if(vaccine=="Covishield"):                            # if covishield vaacine is entered by user than second dose will be after 90 days 
        second_dose_date= first_dose_date +timedelta(90)  # time delta will show the date after 90 days from present day
    elif(vaccine=="Covaccine"):                           # if covaccine vaacine is entered by user than second dose will be after 28 days
        second_dose_date= first_dose_date +timedelta(28)  # time delta will show the date after 28 days from present day  

'''
Below function is used to get first dose certificate of the user
'''
def first_dose_certificate(second_dose_date):
    print("Enter application ID\n")                      # taking application id from user for verification
    h1=int(input())
    if(h1==Application_id):
        print("\n")
        print('''                        Certificate Of Covid - 19 Vaccination                  ''')
        print('''                                    First Dose                                 ''')
        print("\n")
        print("APPLICATION ID: ",Application_id)
        print("\n")
        print("NAME: "+ First_Name +" "+ Last_Name)
        print("\n")
        print("Gender: "+ gender)
        print("\n")
        print("ID VERIFIED: ",Aadhar_no)
        print("\n")
        print("DATE OF BIRTH: "+ dob)
        print("\n")
        print("AGE: ",age)
        print("\n")
        print("Vaccination Status : Half Vaccinated (1st Dose)")
        print("\n")
        print("Vaccination Details:")
        print("Vaccine Name: "+ vaccine)
        print("\n")
        print("Vaccine Type: Covid 19 vaccine, non- replacing viral vector")
        print("\n")
        print("Dose Number: 1")
        print("\n")
        print("Dose Date: ",first_dose_date.strftime('%d-%m-%Y'))
        print("\n")
        print("Apply For Second Dose After 2nd Dose Date: ",second_dose_date.strftime('%d-%m-%Y'))
        print("\n")
        print("Vaccination At : "+ str(location_for_appointment))
    else:
        print("Incorrect ID, Try Again..")
        first_dose_certificate(second_dose_date)    




'''
 Below function will show the guidlines for vaccination for user
'''

def guidlines_for_vaccination():
    print('''                                     GUIDLINES FOR VACCINATION                  ''')
    print('''Make sure you have:
    
    1. A Mask that covers your nose and mouth and fits tightly and comfortably.
    2. Hand Sanitizer.
    3. The Notification you received about your appointment.
    4. Your ID''')
'''
Below function will generate a message confirming the appointment of user for second dose with date , time and location
'''
def second_dose_message(location_for_appointment,First_Name,Last_Name,dob,age,Aadhar_no,second_dose_date,vaccine,Application_id,gender):
    print("\n")
    print(''' YOUR 1st DOSE APPOINTMENT IS BOOKED \n''')
    print("Below are the Following Detalis\n")
    print("APPLICATION ID: ",Application_id)
    print("\n")
    print("NAME: "+ First_Name +" "+ Last_Name)
    print("\n")
    print("Gender: "+ gender)
    print("\n")
    print("AADHAR NUMBER: ",Aadhar_no)
    print("\n")
    print("DATE OF BIRTH: "+ dob)
    print("\n")
    print("AGE: ",age)
    print("\n")
    print("VACCINATION VENUE: "+ str(location_for_appointment))
    print("\n")
    print("Time: 11AM - 3PM")
    print("\n")
    print("First Dose Date: ", second_dose_date.strftime('%d-%m-%Y'))
    print("\n")
    print("Vaccine Name: "+ vaccine)
    print("\n")
    guidlines_for_vaccination()                       # Calling Guidlines for vaccination function
    
    '''
Below function will generate a message confirming the appointment of user for first dose with date , time and location
'''

def first_dose_message(location_for_appointment,First_Name,Last_Name,dob,age,Aadhar_no,first_dose_date,vaccine,Application_id,gender):
    print("\n")
    print(''' YOUR 1st DOSE APPOINTMENT IS BOOKED \n''')
    print("Below are the Following Detalis\n")
    print("APPLICATION ID: ",Application_id)
    print("\n")
    print("NAME: "+ First_Name +" "+ Last_Name)
    print("\n")
    print("Gender: "+ gender)
    print("\n")
    print("AADHAR NUMBER: ",Aadhar_no)
    print("\n")
    print("DATE OF BIRTH: "+ dob)
    print("\n")
    print("AGE: ",age)
    print("\n")
    print("VACCINATION VENUE: "+ str(location_for_appointment))
    print("\n")
    print("Time: 11AM - 3PM")
    print("\n")
    print("First Dose Date: ", first_dose_date.strftime('%d-%m-%Y'))
    print("\n")
    print("Vaccine Name: "+ vaccine)
    print("\n")
    guidlines_for_vaccination()                       # Calling Guidlines for vaccination function
    schedule_second_dose(vaccine,first_dose_date)     # calling schedule second dose function
    

'''
Below function will generate a new location from user's existing location 
'''
def Set_Vaccination_Venue():
    global location_for_appointment
    print("Enter Your Location\n")
    your_location=input()                             # Taking current location as user input
    print("Your Appointement Request is Being Processed . Please Wait..")
    getloc = loc.geocode(your_location)
    # generating some random loactions according to user preference
    getloc1 = loc.geocode("Vijay nagar indore")
    getloc2 = loc.geocode("abhay prashal indore")
    getloc3 = loc.geocode("rajwada indore")
    getloc4 = loc.geocode("Geeta bhawan indore")
    getloc5 = loc.geocode("Regal square indore")
    
    locations=[getloc1,getloc2,getloc3,getloc4,getloc5]
    rand_idx = random.randrange(len(locations))
    random_num = locations[rand_idx]
    location_for_appointment=(random_num)
   # calling first dose message function
    first_dose_message(location_for_appointment,First_Name,Last_Name,dob,age,Aadhar_no,first_dose_date,vaccine,Application_id,gender) 
    
    '''
Below function will schedule appointment for first dose
'''
def Schedule_Appointment():
    global Aadhar_no,first_dose_date,presentday
    print("Enter Your Aadhar Number:\n")             # asking for user aadhar number
    Aadhar_no=int(input())
    presentday = datetime.now()                      # Fetching present day date and time 
    first_dose_date=presentday + timedelta(3)        # Setting first dose date after 3 days from present day by date time library

    Set_Vaccination_Venue()                          # calling set vaccination venue function

'''
Below Function will ask for vaccine name that user wants
'''
def get_vaccine_name():
    global vaccine
    print("Enter The Vaccine You Want: Covishield or Covaccine:\n")
    vaccine=input()
    Schedule_Appointment()                                       # calling schedule appointment function after that

'''
Below function will ask for general details for appointment 
'''

def Apply_Vaccination():
    global First_Name ,Last_Name,dob,age,Application_id,gender
    
                        # this will generate random id using random library function
    print("Enter your First Name\n")
    First_Name=input()                                            # Asking for user name
    print("Enter your Last Name\n")
    Last_Name=input()
    print("Your Gender\n")                                        # asking for gender
    gender=input()
    print("Enter Your Date Of Birth\n")                           # asking date of birth
    dob=input()

    print("Enter your Age\n")                                     # Asking age input
    age=int(input())
    
    get_vaccine_name()                                            # Calling get vaccine name function
    
        



