def count_words(text):
    list_1 = text.split(" ")
    return len(list_1)
 
def average_word_length(text):
    list_1 = text.split(" ")
    list_2 = []
    for i in list_1:
        list_2.append(len(i))
    return sum(list_2)/len(list_2)
