import os
import pandas as pd
import matplotlib.pyplot as plt

from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet

from engine.scoring_rules import get_ph_score, get_spo2_score, get_symptom_score
from engine.decision_engine import classify_patient


def generate_report():

    df = pd.read_csv("data/patients.csv")

    os.makedirs("output", exist_ok=True)

    days = list(range(1, len(df) + 1))

    risk_values = []

    for i in range(len(df)):

        ph_score = get_ph_score(df.loc[i, "pH"])
        oxy_score = get_spo2_score(df.loc[i, "SpO2"])
        symptom_score = get_symptom_score(df.loc[i, "fever"], df.loc[i, "pain"])

        risk_score, status = classify_patient(ph_score, oxy_score, symptom_score)

        risk_values.append(risk_score)

    plt.figure()
    plt.plot(days, df["pH"], label="pH")
    plt.title("pH Trend")
    plt.savefig("output/ph.png")
    plt.close()

    plt.figure()
    plt.plot(days, df["SpO2"], label="SpO2")
    plt.title("SpO2 Trend")
    plt.savefig("output/spo2.png")
    plt.close()

    plt.figure()
    plt.plot(days, risk_values, label="Risk Score")
    plt.title("Risk Evolution")
    plt.savefig("output/risk.png")
    plt.close()

    doc = SimpleDocTemplate("output/clinical_report.pdf")
    styles = getSampleStyleSheet()
    content = []

    content.append(Paragraph("Biomedical Clinical Report", styles["Title"]))
    content.append(Spacer(1, 12))

    final_risk = risk_values[-1]

    if final_risk <= 2:
        status = "Healthy"
    elif final_risk <= 5:
        status = "Risk"
    else:
        status = "Critical"

    content.append(Paragraph(f"Final Patient Status: {status}", styles["Normal"]))
    content.append(Spacer(1, 12))

    content.append(Image("output/ph.png", width=400, height=200))
    content.append(Spacer(1, 12))

    content.append(Image("output/spo2.png", width=400, height=200))
    content.append(Spacer(1, 12))

    content.append(Image("output/risk.png", width=400, height=200))

    doc.build(content)

    print("PDF report generated at output/clinical_report.pdf")