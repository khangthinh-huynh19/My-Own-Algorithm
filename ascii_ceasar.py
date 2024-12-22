 # Get ASCII value of a single character
char = 'A'
ascii_value = ord(char)
print(f"The ASCII value of '{char}' is {ascii_value}")
print(chr(66))
# Get ASCII values of multiple characters
string = "Hello"
ascii_values = [ord(char) for char in string]
print(f"The ASCII values of '{string}' are: {ascii_values}")

# Range ASCII của chữ thường: từ 97 đến 122
# Range ASCII của chữ in hoa: từ 65 đến 90
# Range ASCII của số: từ 48 đến 57

# input the password
while True:
    password_org = input(str("Input the password: "))
    step = 10
    ceasar_pass = []
    for i in password_org:
        dec_val = ord(i)
        
        # if dec_val in range(97, 123) or dec_val in range(65, 91) or dec_val in range(48, 58):
        #     print(dec_val)
        #     new_dec_val = dec_val + step
        #     if new_dec_val 
            
        if dec_val in range(97, 123):
            new_dec_val = dec_val + step
            if new_dec_val > 122:
                new_dec_val = 96 + (new_dec_val - 122)
        elif dec_val in range(65,91):
            new_dec_val = dec_val + step
            if new_dec_val > 90:
                new_dec_val = 64 + (new_dec_val - 90)
        elif dec_val in range(48, 65):
            new_dec_val = dec_val + step
            if new_dec_val > 64:
                new_dec_val = 47 + (new_dec_val - 64)
        
        ceasar_pass.append(str(new_dec_val))
        
    dec_result = ".".join(ceasar_pass)
    string_result = "".join([chr(int(i)) for i in ceasar_pass])
    print(f"The encrypted decimal password is: {dec_result}")
    print(f"The encrypted string password is: {string_result}")

    