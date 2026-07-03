import random
import pandas as pd

try:
    df = pd.read_csv("../data/patients.csv")
except:
    df = pd.DataFrame(columns=["patient_id", "day", "pH", "Oxy", "fever", "pain"])

patient_id = "P1"

pH = 6.5
oxy = 98

days = 43

for day in range(1, days + 1):

    pH += random.uniform(0.01, 0.05)          # infection trend: pH increases
    oxy += random.uniform(-1.0, -0.2)         # oxygen decreases

    pH = round(min(pH, 8.5), 2)
    oxy = round(max(min(oxy, 100), 70), 2)

    fever = 1 if oxy < 94 else random.randint(0, 1)
    pain = 1 if pH > 7.4 else random.randint(0, 1)

    df.loc[len(df)] = [patient_id, day, pH, oxy, fever, pain]

df.to_csv(
    r"C:\Users\HP\Desktop\Portfolio\Biomedical Decision System\data\patients.csv",
    index=False
)

print(df.head())