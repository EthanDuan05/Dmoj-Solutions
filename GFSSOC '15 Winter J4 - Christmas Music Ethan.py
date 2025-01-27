import sys

D = {'C': 1, 'D': 2, 'E': 3,
     'F': 4, 'G': 5, 'A': 6, 'B': 7}

N = int(input())
state = True
state_2 = False

previous_1 = ' '
previous_2 = 0
leap_cnt = 0
leap_state = False
leap_t_cnt = []
debug = False

for _ in range(N):
     note = input()
     note_1 = note[0]
     note_2 = int(note[1])

     if previous_1 == ' ':
          previous_1 = note_1
          previous_2 = note_2
     else:
          if D[note_1] - D[previous_1] >= 1 and previous_2 != note_2:
               state = False
               if debug:
                    print(2)
               break

          if D[note_1] - D[previous_1] > 4:
               state = True
               break

          if D[note_1] - D[previous_1] == 1 and previous_2 == note_2:
               leap_cnt += 1
               if leap_cnt == 4:
                    leap_state = True
                    leap_cnt = 0

          if leap_state and (D[note_1] - D[previous_1] == 1 and previous_2 == note_2):
               state = False
               break

          if leap_state:
               leap_t_cnt.append(1)
               leap_state = False
          else:
               leap_t_cnt.append(0)

          previous_1 = note_1
          previous_2 = note_2

for i in range(len(leap_t_cnt)-1):
     if leap_t_cnt[i] == 1 and leap_t_cnt[i+1] == 1:
          print("Salieri's music")
          sys.exit(0)

if state:
     print('Melodious!')
     sys.exit(0)
else:
     print("Salieri's music")
     sys.exit(0)