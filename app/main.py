import sys


def main():
    # Uncomment this block to pass the first stage
    
    # I used a while statment which is basically an infinite loop but we can use a recursive algorithm
    while True:
        sys.stdout.write("$ ")
    # # Wait for user input
        command = input()
        if len(command) == 0:
            continue
        
        new_command, *parts = command.split(" ")
        # new_command = parts[0]
        
        # if new_command == "echo":
        #     sentence = ""
        #     for i in range (1, len(parts)):
        #         sentence += parts[i] + " "
        #     print(sentence)    
        # elif(command == "exit 0"):
        #     # break
        #     # instead of breaking using command sys.exit(0), this indicates program has exited successfully
        #     sys.exit(0)
        # elif(len(command) == 0):
        #     continue
        # else:
        #     print(f"{new_command}: command not found")
        
        # use a match block, think of it like a lot of if statements in one 
        
        
        match new_command:
            case "type":
                if parts[0] == "exit" or parts[0] == "echo" or parts[0]== "type":
                    print(f"{parts[0]} is a shell builtin")
                else:
                    sentence = " ".join(parts)
                    print(f"{sentence}: not found")
            case "exit":
                break
            case "echo":
                # we join the array of parts with a space in between
                print(" ".join(parts))
            case default:
                print(f"{new_command}: command not found")
    
    # sys.stdout.write("$ ")
    # command = input()
    
    
    # if(len(command) > 0):
    #         print(f"{command}: command not found")
    
    # recursively call main within itself so it never breaks out, infinite loop
    # main()
    
    


if __name__ == "__main__":
    main()
