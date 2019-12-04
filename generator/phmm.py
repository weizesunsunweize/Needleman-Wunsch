import numpy as np 

STR = ['A', 'T', 'C', 'G']
STATES = ['ix', 'iy', 'a']
TRANSITION_PROB = {
	'ix':{'ix':0.79, 'iy':0.01, 'a':0.2},
	'iy':{'ix':0.01, 'iy':0.79, 'a':0.2},
	 'a':{'ix':0.1, 'iy':0.1, 'a':0.8},
}
INITIAL_PROB = {'ix':0.3, 'iy':0.3, 'a':0.4}
LENGTH = 50

# generate hidden states
states = [np.random.choice(STATES, p=[INITIAL_PROB[s] for s in STATES])]
for i in range(1, LENGTH):
	states.append(np.random.choice(STATES, p=[TRANSITION_PROB[states[-1]][s] for s in STATES]))

# generate sequences
x = []
y = []
xstr = ''
ystr = ''
for s in states:
	str = np.random.choice(STR)
	if s == 'a':
		x.append(str)
		xstr += str
		y.append(str)
		ystr += str
	elif s == 'ix':
		x.append(str)
		xstr += str
		ystr += '-'
	else:
		xstr += '-'
		y.append(str)
		ystr += str


print(xstr)
print(ystr)
print(''.join(x))
print(''.join(y))
