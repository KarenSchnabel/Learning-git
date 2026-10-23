# Exercise 1
import pandas as pd

patients = pd.DataFrame({ 
    "patientid": ["P01", "P02", "P03", "P04", "P05"], 
    "heightcm": [172, 165, 181, 158, 175], 
    "weight_kg": [68, 72, 85, 54, 91] 
})
# Calculate BMI
patients["bmi"] = patients["weight_kg"] / (patients["heightcm"] / 100) ** 2
print(patients)

# Exercise 2
patients = pd.DataFrame({ 
    "patientid": ["P01", "P02", "P03", "P04", "P05", "P06"], 
    "heartrate": [72, 88, 105, 64, 112, 79] 
})
# Find patients with heart rate above 100 bpm
high_hr = patients[patients["heartrate"] > 100]
print(high_hr)

# Exercise 3 
bp = pd.DataFrame({ 
    "patient_id": ["P01", "P02", "P03", "P04", "P05"], 
    "systolic": [118, 135, 142, 125, 155], 
    "diastolic": [76, 82, 91, 79, 95] 
})
mean_systolic = sum(bp[])
# Exercise 3 
bp = pd.DataFrame({ 
    "patient_id": ["P01", "P02", "P03", "P04", "P05"], 
    "systolic": [118, 135, 142, 125, 155], 
    "diastolic": [76, 82, 91, 79, 95] 
})
# Mean systolic 
mean_systolic = bp["systolic"].mean()
print(mean_systolic)
