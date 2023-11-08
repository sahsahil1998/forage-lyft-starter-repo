from car_factory import CarFactory
from datetime import date

# Sample
current_date = date.today()
last_service_date = date(2020, 1, 1)
current_mileage = 35000
last_service_mileage = 10000
warning_light_on = False

calliope = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
glissade = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
palindrome = CarFactory.create_palindrome(current_date, last_service_date, warning_light_on)

# Check if cars need service
print(calliope.needs_service())
print(glissade.needs_service())  
print(palindrome.needs_service())  