# Decision Logic

## Overview
The decision engine transforms physiological signals into a single clinical risk classification.

---

## Step 1: Scoring Inputs

Each parameter is converted into a numerical risk score.

### pH Scoring
- 6.5 – 7.4 → 0 (Normal)
- 7.5 – 7.9 → 1 (Risk)
- ≥ 8.0 → 2 (Infection indicator)

### SpO2 Scoring
- 95 – 100 → 0 (Normal oxygenation)
- 90 – 94 → 1 (Mild hypoxia)
- 85 – 89 → 2 (Moderate hypoxia)
- < 85 → 3 (Severe hypoxia)

### Symptoms
- Fever → +1 risk per unit
- Pain → +1 risk per unit

---

## Step 2: Risk Calculation

Total risk score:

Risk = pH_score + SpO2_score + symptom_score

---

## Step 3: Safety Overrides

These rules override normal scoring:

- If SpO2 score = 3 → Critical (Severe Hypoxia)
- If pH is high (≥8) AND symptoms present → Critical (Infection risk)

---

## Step 4: Final Classification

- 0–2 → Healthy
- 3–5 → Risk
- >5 → Critical