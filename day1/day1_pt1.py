#On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

file_input = open("input.txt", "r")

line = file_input.readline()
sum = 0
first_digit=0
last_digit=0

while(line != ""):
    #first digit
    i=0
    while(line[i].isdigit() == False):
        i+=1
    first_digit = int(line[i])

    #last digit
    i = len(line)-1
    while(line[i].isdigit() == False):
        i-=1
    last_digit = int(line[i])

    #sum
    sum += (first_digit*10 + last_digit)

    line = file_input.readline()

print(sum)

file_input.close()