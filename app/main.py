import sys


def main():
    # Uncomment this block to pass the first stage
    
    # I used a while statment which is basically an infinite loop but we can use a recursive algorithm
    while(True):
        sys.stdout.write("$ ")

    # Wait for user input
        command = input()
        if(command == "exit 0"):
            break
        if(len(command) == 0):
            continue
        print(f"{command}: command not found")
    
    # sys.stdout.write("$ ")
    # command = input()
    
    
    # if(len(command) > 0):
    #         print(f"{command}: command not found")
    
    # recursively call main within itself so it never breaks out, infinite loop
    # main()
    
    


if __name__ == "__main__":
    main()
