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
    
    @freeze_time("2020-07-01")
    def test_clash_on_medecine_taken_one_day(self):
        prescA = Prescription(date(2020, 7, 1), 20)
        prescB = Prescription(date(2020, 7, 1), 4)
        prescC = Prescription(date(2020, 7, 1), 10)
        patient = self.prepare_data(prescA, prescB, prescC)
        self.assertEqual(patient.clash(["A", "B"], 2), [date(2020,7,1)])

    @freeze_time("2020-07-01")
    def test_noclash_on_medecine_taken_one_day(self):
        prescA = Prescription(date(2020, 7, 1), 20)
        prescB = Prescription(date(2020, 7, 1), 4)
        prescC = Prescription(date(2020, 7, 2), 10)
        patient = self.prepare_data(prescA, prescB, prescC)
        self.assertEqual(patient.clash(["A", "B", "C"], 2), [])

    @freeze_time("2020-07-20")
    def test_clash_when_medecines_in_history(self):
        prescA = Prescription(date(2020, 7, 1), 20)
        prescB = Prescription(date(2020, 7, 10), 4)
        prescC = Prescription(date(2020, 7, 10), 10)
        patient = self.prepare_data(prescA, prescB, prescC)
        self.assertEqual(patient.clash(["A", "B"], 90), [date(2020, 7, 13), date(2020, 7, 12), date(2020, 7, 11), date(2020, 7, 10)])
                
    @freeze_time("2020-07-20")
    def test_clash_when_medecines_in_history_any_order(self):
        prescA = Prescription(date(2020, 7, 1), 20)
        prescB = Prescription(date(2020, 7, 10), 4)
        prescC = Prescription(date(2020, 7, 10), 10)
        patient = self.prepare_data(prescA, prescB, prescC)
        self.assertEqual(patient.clash(["B", "A"], 20), [date(2020, 7, 13), date(2020, 7, 12), date(2020, 7, 11), date(2020, 7, 10)])

    @freeze_time("2020-07-20")
    def test_clash_AB_outofrange_C(self):
        prescA = Prescription(date(2020, 7, 15), 5)
        prescB = Prescription(date(2020, 7, 15), 5)
        prescC = Prescription(date(2020, 7, 10), 5)
        patient = self.prepare_data(prescA, prescB, prescC)
        self.assertEqual(patient.clash(["A", "B"], 6), [date(2020, 7, 19), date(2020, 7, 18), date(2020, 7, 17), date(2020, 7, 16), date(2020, 7, 15)])
        self.assertEqual(patient.clash(["A", "B", "C"], 6), [])

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
    
if __name__ == '__main__':
    unittest.main()

