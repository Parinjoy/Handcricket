import random

score=0
boundaries=0
runs=[0,1,2,3,4,6]

def ball():
	global score,boundaries
	player=int(input('Enter: '))
	if player not in runs:
		print('Invalid. Enter Again')
		return ball()
	i=random.randint(0,len(runs)-1)
	run=runs[i]
	if player==run:
		print('OUT')
		return
	score+=player
	if player==4 or player==6:
		boundaries+=1
	return(run)

n=int(input('Enter no. of overs you want to play: '))
for i in range(6*n):
	play=ball()
	if play==None:
		break
	else:
		print(play)
print(score,boundaries)