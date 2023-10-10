kolvo_partiy = int(input())
wins = input()
n = 0
AntonWins = 0
DanikWins = 0
for win in range(kolvo_partiy):
    if wins[n] == 'A':
        AntonWins += 1
        n += 1
    else:
        n += 1
        DanikWins += 1

if AntonWins > DanikWins:
    print('Anton')
if DanikWins > AntonWins:
    print('Danik')
if DanikWins == AntonWins:
    print('Friendship')
