def bmicalculator(weight,height):
    bmi=round(weight/(height/100)**2,1)
    bmi_output=[(16, 'Severely underweight'), (18.5, 'Underweight'),(25, 'Normal'), (30, 'Overweight'),(35, 'Moderately obese'), (float('inf'), 'Severely obese')]
    for tup1,tup2 in bmi_output:
        if bmi<tup1:
            print('Your BMI is ',bmi,' and you are ',tup2)
            break


wgt = float(input('Enter Weight in kg\n'))
hgt = float(input('Enter Height in cm\n'))
bmicalculator(wgt,hgt)