# Activity 02: What is an infinite loop?
# Fixes a while loop that never stops.
#
# Problem: the counter starts at 0 and is never changed inside the loop,
# so the condition counter < 10 is always true and the loop runs forever.
#
# Solution: increase the counter by 1 on each iteration, so it eventually
# reaches 10 and the loop ends.

counter = 0

while counter < 10:
    print('Processing Data...')
    counter += 1