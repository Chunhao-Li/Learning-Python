from random import randint


name = input("Please input your name: ")

f = open('game.txt')
lines = f.readlines()
f.close()

scores = {}

for l in lines:
	s = l.split()
	scores[s[0]] = s[1:]

score = scores.setdefault(name, [0,0,0])

game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])


if game_times > 0:
	ave_times = total_times / game_times
else:
	ave_times = 0

print('%s have played %d times, at least %d times to guess the answer.\
	Average times are %.2f' %(name, game_times, min_times, ave_times))



num = randint(1, 100)
times = 0

print('Guess what I think?')
bingo = False 





while bingo == False:
	times +=1
	answer = int(input())
	if answer < num:
		print('too small!')
	if answer > num:
		print('too big')
	if answer == num:
		print('bingo')
		bingo = True


		

if game_times == 0 or times < min_times:
			min_times = times 

total_times += times
game_times += 1


scores[name] = [str(game_times), str(min_times), str(total_times)]
result = ''
# print(scores)
for n in scores:
	line = n + ' ' + ' '.join(scores[name]) + '\n'
	result += line 


f = open('game.txt', 'w')
f.write(result)
f.close()





















