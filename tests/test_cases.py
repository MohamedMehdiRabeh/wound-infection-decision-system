from engine.scoring_rules import (
    get_ph_score,
    get_spo2_score,
    get_symptom_score
)

from engine.decision_engine import classify_patient


def run_tests():

    print("\n--- BIOMEDICAL SYSTEM TESTS ---\n")

    # ----------------------------
    # 1. NORMAL CASE (Healthy)
    # ----------------------------
    ph_score = get_ph_score(7.2)
    oxy_score = get_spo2_score(98)
    symptom_score = get_symptom_score(0, 0)

    score, status = classify_patient(ph_score, oxy_score, symptom_score)

    print("Test 1 - Healthy Case")
    print(score, status)
    print("-" * 40)

    # ----------------------------
    # 2. RISK CASE
    # ----------------------------
    ph_score = get_ph_score(7.8)
    oxy_score = get_spo2_score(92)
    symptom_score = get_symptom_score(1, 1)

    score, status = classify_patient(ph_score, oxy_score, symptom_score)

    print("Test 2 - Risk Case")
    print(score, status)
    print("-" * 40)

    # ----------------------------
    # 3. CRITICAL CASE (LOW OXYGEN)
    # ----------------------------
    ph_score = get_ph_score(7.3)
    oxy_score = get_spo2_score(82)
    symptom_score = get_symptom_score(0, 0)

    score, status = classify_patient(ph_score, oxy_score, symptom_score)

    print("Test 3 - Critical (Hypoxia)")
    print(score, status)
    print("-" * 40)

    # ----------------------------
    # 4. CRITICAL CASE (HIGH pH + symptoms)
    # ----------------------------
    ph_score = get_ph_score(8.3)
    oxy_score = get_spo2_score(96)
    symptom_score = get_symptom_score(1, 1)

    score, status = classify_patient(ph_score, oxy_score, symptom_score)

    print("Test 4 - Critical (Infection Risk)")
    print(score, status)
    print("-" * 40)

    # ----------------------------
    # 5. EDGE CASE (EXTREME LOW VALUES)
    # ----------------------------
    ph_score = get_ph_score(5.0)
    oxy_score = get_spo2_score(70)
    symptom_score = get_symptom_score(2, 2)

    score, status = classify_patient(ph_score, oxy_score, symptom_score)

    print("Test 5 - Extreme Case")
    print(score, status)
    print("-" * 40)


if __name__ == "__main__":
    run_tests()