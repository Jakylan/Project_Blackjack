def average():
    print()
    grades = []
    while True:
        response = input('grade: ').strip()
        if response == 'grade':
            break
        else:
            grades.append(int(response))
    average = round(sum(grades) / len(response))
    print(average)

    if average >= 90:
        print('Grade is a A')
    elif average >= 80:
        print('Grade is a B')
    elif average >= 70:
        print('Grade is a C')
    elif average >= 65:
        print('Grade is a D')
    elif average <= 64:
        print('Grade is a F')


average()
