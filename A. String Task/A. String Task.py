

# text = input().strip().lower()
# voules =["a", "o", "y", "e", "u", "i"]
# def remove_vowels(text):
#     vowels = "aeiouAEIOU"
#     return ''.join([char for char in text if char not in vowels])


# # text =
# def insert_char_before_each(s, char):
#     return ''.join(char + ch for ch in s)
# text = insert_char_before_each(remove_vowels(text), ".")
# print(text)
            
def process_string(s):
    vowels = "aoyeui"
    result = ""
    for char in s.lower():
        if char not in vowels:
            result += '.' + char
    return result

# Test the function
input_string = input().strip()
output_string = process_string(input_string)
print(output_string)
             