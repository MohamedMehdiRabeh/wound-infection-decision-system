import pandas as pd

from engine.scoring_rules import (
    get_ph_score,
    get_spo2_score,
    get_symptom_score
)

from engine.decision_engine import classify_patient


def run_analysis():

    df = pd.read_csv("data/patients.csv")

    for i in range(len(df)):

        ph = df.loc[i, "pH"]
        spo2 = df.loc[i, "SpO2"]
        fever = df.loc[i, "fever"]
        pain = df.loc[i, "pain"]

        ph_score = get_ph_score(ph)
        oxy_score = get_spo2_score(spo2)
        symptom_score = get_symptom_score(fever, pain)

        risk_score, status = classify_patient(
            ph_score,
            oxy_score,
            symptom_score
        )

        print(f"Day {i + 1}: Risk Score = {risk_score} | Status = {status}")


if __name__ == "__main__":
    run_analysis()