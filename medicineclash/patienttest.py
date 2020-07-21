import unittest
from freezegun import freeze_time
from datetime import date

from patient import Patient
from medicine import Medicine
from prescription import Prescription


class PatientTest(unittest.TestCase):

    def test_no_clash_when_no_medecine_history(self):
        patient = Patient() 
        self.assertEqual(patient.clash(["A", "B"], 1), [])
    
    @freeze_time("2020-07-02")
    def test_clash_on_medecine_taken_one_day(self):
        prescA = Prescription(date(2020, 7, 1), 20)
        prescB = Prescription(date(2020, 7, 1), 4)
        prescC = Prescription(date(2020, 7, 2), 10)

        patient = self.prepare_data(prescA, prescB, prescC)

        self.assertEqual(patient.clash(["A", "B"], 2), [date(2020,7,1)])

    def test_noclash_on_medecine_taken_one_day(self):

        prescA = Prescription(date(2020, 7, 1), 20)
        prescB = Prescription(date(2020, 7, 1), 4)
        prescC = Prescription(date(2020, 7, 2), 10)

        patient = self.prepare_data(prescA, prescB, prescC)

        self.assertEqual(patient.clash(["A", "B", "C"], 2), [])

    def prepare_data(self, prescA, prescB, prescC):
        patient = Patient()
        medA = Medicine("A")
        medB = Medicine("B")
        medC = Medicine("C")

        medA.add_prescription(prescA)
        medB.add_prescription(prescB)
        medC.add_prescription(prescC)

        patient.add_medicine(medA)
        patient.add_medicine(medB)
        patient.add_medicine(medC)
        return patient


    # @freeze_time("2020-07-20")
    # def test_clash_when_medecines_in_history(self):
    #     patient = Patient()
    #     medA = Medicine("A")
    #     medB = Medicine("B")
    #     medC = Medicine("C")

    #     prescA = Prescription("2020-07-01", 20)
    #     prescB = Prescription("2020-07-10", 4)
    #     prescC = Prescription("2020-07-10", 10)

    #     medA.add_prescription(prescA)
    #     medB.add_prescription(prescB)
    #     medC.add_prescription(prescC)

    #     patient.add_medicine(medA)
    #     patient.add_medicine(medB)
    #     patient.add_medicine(medC)
    

    #     self.assertEqual(patient.clash(["A", "B"], 90), ["2020-07-10", "2020-07-11", "2020-07-12", "2020-07-13"])
                

if __name__ == '__main__':
    unittest.main()

