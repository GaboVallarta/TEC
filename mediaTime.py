"""
These program calculates the media time of a person who runs monday, wednesday and friday the same distance.

Pseudocode:
1. Ask for the minutes and seconds that he ran of the three days 
2. Convert time to seconds to have the total time
3. Calculate the media of time by adding them and dividing the result by 3
4. Print the result dividing the time by 60 to get minutes and use modulus to get seconds
"""



mondaym=float(input("Enter the time in minutes of monday: "))
mondays=float(input("Enter the time in seconds of monday: "))
wednesdaym=float(input("Enter the time in minutes of wednesday: "))
wednesdays=float(input("Enter the time in seconds of wednesday: "))
fridaym=float(input("Enter the time in minutes of friday: "))
fridays=float(input("Enter the time in seconds of friday: "))


totmonday=mondaym*60+mondays
totwednesday=wednesdaym*60+wednesdays
totfriday=fridaym*60+fridays


mediatime=(totmonday+totwednesday+totfriday)/3


print(f"The media time is: {mediatime//60:.0f} minutes and {mediatime%60:.0f} seconds")
