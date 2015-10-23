def split_fileB(line):
    #split the input line into word, date and count_string
    key_value, count_string = line.split(",")
    date, word = key_value.split(" ")
    return (word, date + " " + count_string)
