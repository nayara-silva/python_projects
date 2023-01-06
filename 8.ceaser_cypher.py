alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
exit = False

def ceaser_cypher(text, shift, direction):
    index_list = []
    letter_list = [] 
    new_index = 0
    
    for i in range(0, len(text)):
        
        letter_list.append(text[i])
        index = alphabet.index(text[i]) #Store the index of each letter on the text
        index_list.append(index) #Turns the index on a list
        
        if direction == "encode":
            new_index = index_list[i] + shift #Sum each item on the list with the shift to find the new index
        
            if new_index >= len(alphabet): # For indexes out of the range of alphabet list
                new_index = new_index - len(alphabet) 
        elif direction == "decode":
            new_index = index_list[i] - shift #Sum each item on the list with the shift to find the new index
        
            if new_index < 0:
                new_index = new_index + len(alphabet)      
        else:
            print(f"'{direction}' is not a valid option.")
            
        letter_list[i] = alphabet[new_index]
        
    result = "".join(letter_list)
    print(f"Here's the word: {result}")
            
     

# def encode(text, shift):
    
#     for i in range(0, len(text)):
        
#         letter_list.append(text[i])
#         index = alphabet.index(text[i]) #Store the index of each letter on the text
#         index_list.append(index) #Turns the index on a list
#         new_index = index_list[i] + shift #Sum each item on the list with the shift to find the new index
        
#         if new_index >= len(alphabet): # For indexes out of the range of alphabet list
#             new_index = new_index - len(alphabet) 
            
#         letter_list[i] = alphabet[new_index]
    
#     encode_word = "".join(letter_list)
#     print(f"Here's the encode result: {encode_word}")

# def decode(text, shift):
#     for i in range(0, len(text)):
        
#         letter_list.append(text[i])
#         index = alphabet.index(text[i]) #Store the index of each letter on the text
#         index_list.append(index) #Turns the index on a list
#         new_index = index_list[i] - shift #Sum each item on the list with the shift to find the new index
        
#         if new_index < 0:
#             new_index = new_index + len(alphabet)
            
#         letter_list[i] = alphabet[new_index]
    
#     decryptd_word = "".join(letter_list)
#     print(f"Here's the decryptd word: {decryptd_word}")
            
        
# if direction == 'encode':
#     encode(text, shift)
# elif direction == 'decode':
#     decode(text, shift)
# else:
#     print(f"'{direction}' is not a valid option.")
while exit == False:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser_cypher(text, shift, direction)
    answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if answer == 'no':
        exit = True
    




    
    
    