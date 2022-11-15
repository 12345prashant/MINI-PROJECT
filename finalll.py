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

