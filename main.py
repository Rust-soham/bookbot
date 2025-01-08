def count_characters(string): # returns a dictionary
    count_dict = {}

    # first convert the string to lowercase
    lowered_text = string.lower()

    # now somehow, you have to count how many times a specific character appears in the lowered_text
    # key -> value 
    ## key ->  character (every key should be unique)
    # value -> how many times it appear over the lowered_text

    # so a for loop obv
    # how can i get each character from this giant ass essay
    for char in lowered_text:
        if char.isalpha():
            if char not in count_dict:
                count_dict[char] = 1
            else:
                count_dict[char] += 1
    
    # have to return a dictionary
    return count_dict




def count_words(string):
    count = 0
    
    # do something to count the string
    words = string.split()
    count = len(words)

    return count

def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(dictionary):
    return dictionary['occurrences']


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)

    char_dict = count_characters(text)
    # print(my_dict)
    
    char_list = [{'character': k, 'occurrences': v} for k, v in char_dict.items()]

    char_list.sort(reverse = True, key = sort_on)
    # print(char_list)

    # logging
    print("--- Begin report of books/frankenstein.txt ---")
    
    print(f"{num_words} words found in the document") 

    # logging of which character is found how many times
    for item in char_list:
        print(f"The '{item['character']}' character was found {item['occurrences']} times")

    print("--- End report ---")
    



main()

