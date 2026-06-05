

def calculate_bmi(height_in_cm,weight_in_kg):

    h_in_meter = height_in_cm / 100

    bmi = weight_in_kg / h_in_meter**2

    return bmi


print(calculate_bmi(175,78))


