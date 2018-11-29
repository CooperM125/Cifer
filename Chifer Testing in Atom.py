print("Hello, this is a letter shifting chifer")
shift_num = int(input("please enter a number from 0 - 25 for the shift.\n")) #takes in a int input for shit
if 0 <= shift_num <= 25:
    text_in = str(input("What is the text you want to encode\n"))            #takes in message as string
    count = 0                                                                #declare varable
    text_num = 0                                                             #declare varable
    coded_message = [None]*length_in                                         #makes a empty list

    length_in = len(text_in)                                                 #collection and formating input
    int(length_in)                                                           #
    message = text_in.lower()                                                #
    message = list(message)                                                  #collection and formating input

    while count < length_in:
        coded_message[count] = ord(message[count]) +shift_num
        if coded_message[count] > 122:                                       #accounts for shifts that go over z
            coded_message[count] = coded_message[count] - 26

        if not 97 <= coded_message[count] <= 122:                            #ensures spaces are kept
            coded_message[count] = 32
        coded_message[count] = chr(coded_message[count])                     #rewrites coded_message to actually be coded
        count += 1
    print(''.join(coded_message))
else:
    print("That is not a number between 0-25")
