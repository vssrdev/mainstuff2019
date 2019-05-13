#!/bin/python

def gather_info():
    height = float(raw_input("Enter your height"))
    weight = float(raw_input("Enter your weight"))
    unit = raw_input("Are your measurements in Metric or imperial units").lower().strip()
    return (height,weight,unit)


def caluculate_bmi(weight, height, unit='metric'):
    if unit=='metric':
        bmi =  (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    print("Your bmi is %s" %bmi)


while True:
    height, weight, unit = gather_info()
    if unit.startswith('i'):
        caluculate_bmi(height=height, weight=weight, unit='imperial')
        break
    elif unit.startswith('m'):
        caluculate_bmi(weight, height)
        break
    else:
        print("Error: Unknown Measurement System. Please use imperial or metric")

