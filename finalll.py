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