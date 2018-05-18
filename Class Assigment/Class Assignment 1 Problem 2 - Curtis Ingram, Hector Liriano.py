RandList = [8, 0, 'hi', -4, '5', 2.3]

def main(List):

    sumofposnum = 0

    for a in List:
    
        try:

            if a > 0:

                sumofposnum = sumofposnum + a
                
        except TypeError:
            pass

    return sumofposnum

print(main(RandList))
