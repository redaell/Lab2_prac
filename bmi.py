def calculate_bmi(height,weight):
    print("Height = ", height)
    print("Weight = ", weight)

    bmi = weight / (height*height)

    print ("BMI = ", bmi)

    if(bmi < 18.5):
        print("Under weight")
        return -1
    elif(18.5<=bmi<=25.0):
        print("Normal weight")
        return 0
    elif(bmi>25.0):
        print("Over weight")
        return 1

calculate_bmi(weight=57, height=1.73)
