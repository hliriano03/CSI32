# COMMENT: Please, always put code into a function like "main()"

#With List

Inputs = []
posnum_count = 0
negnum_count = 0 
zeros_count = 0

while True:

    num = ""

    try:

        num = input("input something: ")  

        if num == "":

            break

        else:
            Inputs.append(int(num))


    except ValueError:
        print("Only input real numbers.")
    
for num in Inputs:

    if num < 0:

        negnum_count = negnum_count + 1

    elif num > 0:

        posnum_count = posnum_count + 1

    else:
        zeros_count = zeros_count + 1

print("How many negative numbers?\n ", negnum_count)
print("How many zeros?\n ", zeros_count)
print("How many positive numbers?\n ", posnum_count)


#Without List

##Inputs = []
##posnum_count = 0
##negnum_count = 0 
##zeros_count = 0

##while True:
##
##    num = input("input something: ")
##
##    try:
##
##        if num == "":
##
##            break
##
##        if int(num) < 0:
##
##            negnum_count = negnum_count + 1
##
##        elif int(num) > 0:
##
##            posnum_count = posnum_count + 1
##
##        else:
##            zeros_count = zeros_count + 1
##
##    except ValueError:
##        print("Only input real numbers.")
##
##print("How many negative numbers?\n ", negnum_count)
##print("How many zeros?\n ", zeros_count)
##print("How many positive numbers?\n ", posnum_count)

        

    

    


