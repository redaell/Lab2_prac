import Lab2_prac as lab2

def test_calc_min_max():
    expected = [22.0, 35.0]
    testlist =  [22.0, 33.0, 25.0, 27.0, 29.0, 35.0]
    result = lab2.calc_min_max_temperature(testlist)
    assert(result==expected)

def test_calc_average():
    expected = 28.5
    testlist =  [22.0, 33.0, 25.0, 27.0, 29.0, 35.0]
    result = lab2.calc_average(testlist)
    assert(result==expected)

def test_find_median():
    expected = 28.0
    testlist =  [22.0, 33.0, 25.0, 27.0, 29.0, 35.0]
    result = lab2.find_median(testlist)
    assert(result==expected)