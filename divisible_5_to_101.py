#Write a program which prints the sum of numbers
#from 1 to 101 that are divisible by 5

start_num = 1
Final_sum = 0
while start_num <= 101:
    if start_num % 5 == 0:
        Final_sum = Final_sum + start_num
        start_num = start_num + 1
    else:
        start_num = start_num + 1
print(Final_sum)
        
    
