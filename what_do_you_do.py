def main():
    duties = {
        'Nate Clark': 'technical director',
        'Sean Anthony': 'director',
        'Glen Evans': 'co-founder',
        'Kagan Coughlin': 'co-founder',
        'Bethany Cooper': 'founding trustee',
        'Sage Nichols': 'founding trustee',
        'John Marsalis': 'founding trustee',
        'Carla Lewis': 'trustee'
    }

    name = input('\nWhat is your name?\n')
    print()
    print(duties[name])


if __name__ == '__main__':
    main()
