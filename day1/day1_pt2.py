#It looks like some of the digits are actually spelled out with letters: 
#one, two, three, four, five, six, seven, eight, and nine also count as valid "digits"

def find(line,pox):
    
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(0, len(numbers)):
        found=0
        for j in range(0, len(numbers[i])):
            try:
                if(line[pox+j] == numbers[i][j]):
                    #print(line[pox+j], numbers[i][j])
                    found+=1
                else:
                    #print("skip")
                    break
            except:
                break
        if(found == len(numbers[i])):
            return i+1
        

file_input = open("input.txt", "r")

line = file_input.readline()
sum = 0


while(line != ""):

    first_digit=0
    last_digit=0

    #first digit
    for i in range(0, len(line)):
        if(line[i].isdigit()):
            first_digit = int(line[i])
            break
        elif(line[i] in "otfsen"):
            if(find(line,i) != None):
                first_digit = find(line,i)
                break     

    #last digit
    for i in range(0, len(line)):
        if(line[i].isdigit()):
            last_digit = int(line[i])
            
        elif(line[i] in "otfsen"):
            if(find(line,i) != None):
                last_digit = find(line,i)
                    
    #sum
    num = first_digit*10 + last_digit
    sum += num

    line = file_input.readline()

print(sum)

file_input.close()


