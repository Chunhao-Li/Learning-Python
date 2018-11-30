def charge_up():

    in_index = input('''Choose an operation:
    1. charge up
    2. check balance
    3. detail of income and expenditure'''
                     )
    if in_index == '1':
        f = open('Tolly Book.txt', 'a')
        amount = input('Amount: ')
        item = input('Item: ')
        f.write(str(datetime.date.today()) + ' ' +amount + ' ' + item + '\n')
        f.close()
        print('Data has been recorded.')
        charge_up()

    if in_index == '2':
        acc = 0
        f = open('Tolly Book.txt', 'r')
        lines = f.readlines()
        for line in lines:
            amount = re.findall(r'-?\d+\s', line[10:])
            acc += float(amount[0])
        print(acc)
        f.close()
        charge_up()

    if in_index == '3':
        f = open('Tolly Book.txt', 'r')
        lines = f.readlines()
        for line in lines:
            line.strip()
            print(line,end='')
        f.close()
        charge_up()