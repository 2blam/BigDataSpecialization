def split_fileA(line):
    #split the input line in word and count on the comma
    word, count  = line.split(",")
    #turn count to an integer
    count = int(count)
    return (word, count)
