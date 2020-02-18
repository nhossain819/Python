"""
Distance Conversion
The following function takes an input of distance in feet and returns a distance as
a string of miles, yards, feet, and inches.
"""

def imperial(distance_in_feet):
    inches = distance_in_feet * 12
    miles = round(inches / 63360)
    remaining_inches_after_miles = inches % 63360
    yards = round(remaining_inches_after_miles / 36)
    remaining_inches_after_yards = remaining_inches_after_miles % 36
    feet = round(remaining_inches_after_yards / 12)
    remaining_inches_after_feet = remaining_inches_after_yards % 12
    return "Distance is " + str(miles) + " miles " + str(yards) + " yards " + \
        str(feet) + " feet and " + str(round(remaining_inches_after_feet , 2)) + " inches"
