def calculate_bmi(height,weight):
    print("Height = ", height)
    print("Weight = ", weight)

    bmi = weight / (height*height)

    print ("BMI = ", bmi)

    if(bmi < 18.5):
        print("Under weight")
    elif(18.5<=bmi<=25.0):
        print("Normal weight")
    elif(bmi>25.0):
        print("Over weight")

calculate_bmi(weight=57, height=1.73)