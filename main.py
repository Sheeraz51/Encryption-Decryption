Operation = int(input("Type '1' for Encryption & Type '2' for Decryption: "))
if Operation == 1:
    Operation_2 = int(input("Type '3' for Manual Input & Type '4' for File Input: "))

def xor(number_1, number_2):
    # Convert binary strings to integers
    num1 = int(number_1, 2)
    num2 = int(number_2, 2)
    # Perform XOR operation using bitwise XOR operator
    XOR = num1 ^ num2
    binary_result = bin(XOR)[2:]
    limit = 7
    result = binary_result.zfill(limit)
    #print("XOR_Output",result)
    return result

def not_operation(binary_string):
    # Convert the binary string to an integer
    number = int(binary_string, 2)
    # Perform the bitwise NOT operation
    mirrored_number = ~number
    # Convert the mirrored number back to a binary string
    mirrored_binary_string = bin(mirrored_number)[3:]  # Remove the prefix '0b'
    return mirrored_binary_string

def binary_right_shift(binary_string, shift):
    # Convert the binary string to an integer
    number = int(binary_string, 2)
    number_2 = int(shift, 2)
    # Perform the right shift operation
    shifted_number = number >> number_2
    # Convert the shifted number back to a binary string
    shifted_binary_string = bin(shifted_number)[2:]
    # Pad the binary string with leading zeros if necessary
    shifted_binary_string_2 = shifted_binary_string.zfill(len(binary_string))
    #print("shifted_binary_string",shifted_binary_string_2)
    return shifted_binary_string_2

def binary_left_shift(binary_string, shift):
    # Convert the binary string to an integer
    number = int(binary_string, 2)
    number_2 = int(shift, 2)
    # Perform the right shift operation
    shifted_number = number << number_2
    # Convert the shifted number back to a binary string
    shifted_binary_string = bin(shifted_number)[2:]
    # Pad the binary string with leading zeros if necessary
    #shifted_binary_string = shifted_binary_string.zfill(len(binary_string))
    print("shifted_binary_string",shifted_binary_string)
    return shifted_binary_string

def sum_key(raw_key):
    number_str = str(raw_key)
    digit_sum = 0
    for char in number_str:
    #Convert the character back to an integer and add it to the sum
        digit_sum += int(char)
    print("sum Key", digit_sum)
    return digit_sum

def encrypt(plaintext, raw_key):
    ciphertext = ""
    key = raw_key % 127
    binary_key = bin(key)[2:]
    print("Given Key (Decimal Version)", raw_key)
    print("Key (In Binary Version)", binary_key)
    sum = sum_key(raw_key) % 5
    Key_Sum = bin(sum)[2:]
    print("The Sum of all the digits of Key is: ", Key_Sum)
    for char in plaintext:
        #Conversion of Selected Character into ASCII and Binary Value
        ascii_value = ord(char)
        binary_char = bin(ascii_value)[2:]
        #Encryption Step 1 (XOR Operation)
        XOR_Result = xor(binary_char, binary_key)
        print("XOR_Result", XOR_Result)
        #Encryption Step 2 (Shifting)
        shift_result = binary_right_shift(XOR_Result, Key_Sum)
        print("Shifted_Result", shift_result)
        # Encryption Step 3 (NOT)
        #NOT_result = not_operation(shift_result)
        #print("Transposition Result", NOT_result)
        #Convertion of the Result into Character
        encrypted_decimal = (int(shift_result, 2)) % 256
        encrypted_char = chr(encrypted_decimal)
        ciphertext += encrypted_char
    return ciphertext
def decrypt(ciphertext, raw_key_2):
    plaintext = ""
    key = raw_key_2 % 127
    binary_key = bin(key)[2:]
    print("Given Key (Decimal Version)", raw_key_2)
    print("Key (In Binary Version)", binary_key)
    sum_2 = sum_key(raw_key_2) % 5
    binary_sum_2 = bin(sum_2)[2:]
    for char in ciphertext:
        encrypted_decimal = ord(char)
        encrypted_binary = bin(encrypted_decimal)[2:]
        binary_char = encrypted_binary
        # Decryption Step 1 - NOT_Result
        #NOT_Result = not_operation(binary_char)
        #print("NOT Operation Result",NOT_Result)
        #Decryption Step 2 - Shifted Result
        Shifted_Result = binary_left_shift(binary_char, binary_sum_2)
        print("Shifted Result", Shifted_Result)
        #Decryption Step 3 - XOR Operation
        XOR_Result = xor(Shifted_Result, binary_key)
        print("XOR_Result", XOR_Result)
        #Convertion of Result into Character
        decrypted_decimal = int(XOR_Result, 2)
        decrypted_char = chr(decrypted_decimal)
        plaintext += decrypted_char
    return plaintext

def main():
    if Operation == 1 and Operation_2 == 4:
        raw_key = int(input("Enter the encryption key (Decimal Format): "))
        input_file = open('file.txt', "r")
        plaintext = input_file.read()
        ciphertext = encrypt(plaintext, raw_key)
        print("The Complete Encrypted Text is given below:", ciphertext)
        output_file = open('encrypted_output.txt', "w")
        output_file.write(ciphertext)
    if Operation == 1 and Operation_2 == 3:
        raw_key = int(input("Enter the encryption key (Decimal Format): "))
        plaintext = input("Enter the plaintext: ")
        ciphertext = encrypt(plaintext, raw_key)
        print("The Complete Encrypted Text is given below:", ciphertext)
        output_file = open('encrypted_output.txt', "w")
        output_file.write(ciphertext)
    if Operation == 2:
        raw_key_2 = int(input("Enter the encryption key (Decimal Format): "))
        input_file = open('encrypted_output.txt', "r")
        ciphertext = input_file.read()
        plaintext = decrypt(ciphertext, raw_key_2)
        print("The Decrypted Text is given below: ", plaintext)
        output_file = open('decrypted_output.txt', "w")
        output_file.write(plaintext)

if __name__ == "__main__":
    main()
