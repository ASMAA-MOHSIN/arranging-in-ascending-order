#Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.
def solution(statues):
   statues.sort()
   additional_statues = 0
   for i in range(1,len(statues)):
       difference= statues[i] -  statues[i-1]
       if difference > 1:
                additional_statues += difference - 1
   return additional_statues
