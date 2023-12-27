#It looks like some of the digits are actually spelled out with letters: 
#one, two, three, four, five, six, seven, eight, and nine also count as valid "digits"

file_input = open("input.txt", "r")

line = file_input.readline()
sum = 0
first_digit=0
last_digit=0

while(line != ""):
    #first digit
    for i in range(0, len(line)):
        if(line[i] in "123456789"):
            first_digit = int(line[i])
            break
        elif(line[i] in "otfsen"):
            if(line[i] == "o"):
                first_digit = 1
            elif(line[i] == "t" and line[i+1] == "w"):
                first_digit = 2
            elif(line[i] == "t" and line[i+1] == "h"):
                first_digit = 3
            elif(line[i] == "f" and line[i+1] == "o"):
                first_digit = 4
            elif(line[i] == "f" and line[i+1] == "i"):
                first_digit = 5
            elif(line[i] == "s" and line[i+1] == "i"):
                first_digit = 6
            elif(line[i] == "s" and line[i+1] == "e"):
                first_digit = 7
            elif(line[i] == "e"):
                first_digit = 8
            elif(line[i] == "n"):
                first_digit = 9
            break

    #last digit
    for i in range(len(line)-1, 0, -1):
        if(line[i] in "123456789"):
            last_digit = int(line[i])
            break
        elif(line[i] in "eorxnt"):
            if(line[i] == "e" and line[i-1] == "n" and line[i-2] == "o"):
                last_digit = 1
            elif(line[i] == "e" and line[i-1] == "e"):
                last_digit = 3
            elif(line[i] == "e" and line[i-1] == "v"):
                last_digit = 5
            elif(line[i] == "e" and line[i-1] == "n"):
                last_digit = 9
            elif(line[i] == "o" and line[i-1] == "w"):
                last_digit = 2
            elif(line[i] == "r" and line[i-1] == "u"):
                last_digit = 4
            elif(line[i] == "x" and line[i-1] == "i"):
                last_digit = 6
            elif(line[i] == "n" and line[i-1] == "e"):
                last_digit = 7
            elif(line[i] == "t" and line[i-1] == "h"):
                last_digit = 8
            break

    #sum
    sum += (first_digit*10 + last_digit)

    line = file_input.readline()

print(sum)

file_input.close()