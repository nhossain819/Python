"""
Body Mass Index (BMI)
The following function returns the BMI based on a height in inches and a weight in pounds.
"""

def bmi(height_in_inches , weight_in_lbs):
    body_mass_index = 703 * (weight_in_lbs / ((height_in_inches) ** 2))
    return body_mass_index
