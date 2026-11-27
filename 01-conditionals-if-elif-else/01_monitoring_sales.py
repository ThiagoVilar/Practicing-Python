# Activity 01: Monitoring sales
# Compares the number of apples and bananas sold
# and shows which fruit had higher sales.


apples = int(input('Enter the number of apples sold: '))
bananas = int(input('Enter the number of bananas sold: '))

if apples > bananas:
    print('Apples had higher sales.')
elif bananas > apples:
    print('Bananas had higher sales.')
else:
    print('The sales were the same.')
