array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 8, 10]

# array = [1, 1, 1, 1, 1]
# sequence = [1, 1, 1]

def isValidSubsequence(array, sequence):
    arrIndex=0
    seqIndex=0
    for a in array:
        if seqIndex < len(sequence):
            if a == sequence[seqIndex]:
                seqIndex+=1

    if seqIndex== len(sequence):
        return True
    else:
        return False

print(isValidSubsequence(array, sequence))