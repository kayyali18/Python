



def far_2_cel (far):
    # convert a temp in fahrenheit to celsius

    celsius = (far - 32) * (5/9)
    return celsius

def far_2_kel (far):
    celsius = far_2_cel(far)
    kelvin = celsius + 273.15
    return kelvin


x = far_2_cel (45)
y = far_2_cel (112)




