everybody = []
while True:
    try:
        i = input('Name: ')
        if len(i) != 0:
            everybody.append(i)

    except EOFError:
        print('Adieu, adieu, to ', end='')
        if len(everybody) > 2:
            for e in everybody:
                if e is not everybody[-1]:
                    e += ', '
                else:
                    e = 'and ' + e
                print(e, end='')

        elif len(everybody) == 2:
            for e in everybody:
                if e is everybody[0]:
                    e += ' and '
                print(e, end='')

        elif len(everybody) == 1:
            print(i, end='')

        print()
        break
