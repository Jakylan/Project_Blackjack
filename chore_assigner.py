from random import shuffle


def main():
    students = [
        'Cole Anderson', 'Timothy Bowling', 'Logan Harrell', 'Desma Hervey',
        'Ginger Keys', 'Matt Lipsey', 'Myeisha Madkins', 'Henry Moore',
        'John Morgan', 'Irma Patton', 'Danny Peterson', 'Jakylan Standifer',
        'Justice Taylor', 'Ray Turner', 'Cody van der Poel', 'Andrew Wheeler'
    ]
    chores = [
        'chore 1',
        'chore 2',
        'chore 3',
        'chore 4',
        'chore 5',
        'chore 6',
        'chore 7',
        'chore 8',
        'chore 9',
        'chore 10',
        'chore 11',
        'chore 12',
        'chore 13',
        'chore 14',
        'chore 15',
        'chore 16',
    ]
    shuffle(chores)
    for student in students:
        print(student, chores.pop())


if __name__ == '__main__':
    main()
