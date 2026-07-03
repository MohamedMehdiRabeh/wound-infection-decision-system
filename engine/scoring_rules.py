def get_ph_score(ph):
    if 6.5 <= ph <= 7.4:
        return 0
    elif 7.5 <= ph <= 7.9:
        return 1
    elif ph >= 8.0:
        return 2
    else:
        return 0


def get_spo2_score(spo2):
    if 95 <= spo2 <= 100:
        return 0
    elif 90 <= spo2 <= 94:
        return 1
    elif 85 <= spo2 <= 89:
        return 2
    elif spo2 < 85:
        return 3
    else:
        return 0


def get_symptom_score(fever, pain):
    return fever + pain