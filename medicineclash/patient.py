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
                        prescription_date_list = []
                        for x in range (0, presc.days_supply):
                            prescription_date_list.append(presc.dispense_date + timedelta(days = x))
                        
                        if day_to_check in prescription_date_list:
                            took_that_day.append(medicine.name)

            took_all_medicine_that_day = all(elem in took_that_day for elem in medicine_names)


            

            if took_all_medicine_that_day == True:
                clash_days.append(day_to_check)
        return clash_days