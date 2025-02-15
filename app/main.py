import sys


def main():
    # Uncomment this block to pass the first stage
    
    # I used a while statment which is basically an infinite loop but we can use a recursive algorithm
    while True:
        sys.stdout.write("$ ")
    # Wait for user input
        command = input()
        parts = command.split(" ")
        new_command = parts[0]
        
        if new_command == "echo":
            sentence = ""
            for i in range (1, len(parts)):
                sentence += parts[i] + " "
            print(sentence)    
        elif(command == "exit 0"):
            # break
            # instead of breaking using command sys.exit(0), this indicates program has exited successfully
            sys.exit(0)
        elif(len(command) == 0):
            continue
        else:
            print(f"{new_command}: command not found")
    
    # sys.stdout.write("$ ")
    # command = input()
    
    
    # if(len(command) > 0):
    #         print(f"{command}: command not found")
    
    # recursively call main within itself so it never breaks out, infinite loop
    # main()
    
    sentence = "hello"
    parts = sentence.split(" ")
    print(parts)
    


if __name__ == "__main__":
    main()
