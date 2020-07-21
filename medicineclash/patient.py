from datetime import timedelta  
from datetime import date

class Patient(object):
    
    def __init__(self, medicines = None):
        self._medicines = medicines or []
    
    def add_medicine(self, medicine):
        self._medicines.append(medicine)
    
    def clash(self, medicine_names, days_back=90):
        clash_days = []
        for day in range(days_back):
            day_to_check = date.today() - timedelta(days=day)
            took_that_day = []                
            for medicine in self._medicines:
                if (medicine.name in medicine_names):
                    for presc in medicine.prescriptions:
                        #only checking the prescription date for the moment 
                        #todo : replace by date ranges
                        if day_to_check == presc.dispense_date:
                            took_that_day.append(medicine.name)

            if took_that_day == medicine_names:
                clash_days.append(day_to_check)
        return clash_days