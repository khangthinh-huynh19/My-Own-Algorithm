import random
def generate_random_number(*ranges):
    # Select a random range
    selected_range = random.choice(ranges)
    
    # Generate a random number from the selected range
    return random.randint(selected_range[0], selected_range[1])

# Define our ranges
ranges = [(48, 57), (65, 90), (97, 122)]
while True:
    pass_length = int(input("Input the length of password: "))

    gen_pass = []

    for i in range(0,pass_length):
        char = chr(generate_random_number(*ranges))
        gen_pass.append(char)
        
    gen_pass = "".join(gen_pass)
    print(f"The generated password is: {gen_pass}")




# Generate and print 5 random numbers
# for _ in range(5):
#     print(generate_random_number(*ranges))