import time
import random

print('_*65')
print('I am A Magic Eight Ball!')
question = input('What is your question?')
time.sleep(0.7)
print('Shaking!')
time.sleep(0.7)
print('...Thinking...')
time.sleep(0.7)
print('...Thinking...')
time.sleep(0.7)
print('...Thinking...')
time.sleep(0.7)

choice = random.randint(1,4)

if choice == 1:
	print('Yeth!')
elif choice == 2:
	print('ew no')
elif choice == 3:
	print('Ask Later')
else:
	print('idk')



