# Activity 01: Understanding loops
# Goes through a list of 5 customer names and shows each one.
#
# Why I chose a for loop: the list has a known size, and for goes through
# each element directly, without needing a counter or a stop condition.
# A while loop would need an index variable and manual control of the end
# of the list, making the code longer and easier to get wrong.

customers = ['João', 'Maria', 'Carlos', 'Ana', 'Beatriz']

for customer in customers:
    print(customer)