import sys
import shutil
import subprocess

def main():
    while True:
        sys.stdout.write("$ ")
        command = input()
        if len(command) == 0:
            continue
        
        new_command, *parts = command.split(" ")
        
        # first find executable and then find the file_path to that executable
        # executable = new_command 
        file_path = shutil.which(new_command)
        
        # first find if the path to the script even exists
        if file_path is not None:
            # first we find the value and then append python3 to show which python version we applying
            # then we pass in the executable function
            arr = ["python3", file_path]
            # add all the params to the array, we will pass this in the next function
            for part in parts:
                arr.append(part)
            process = subprocess.run(arr)
                                    #    stdout= subprocess.PIPE,
                                    #    stderr= subprocess.PIPE, 
                                    #    text= True)
            
            # process.wait()
            # output, error = process.communicate()
            # print(output)
            print(process.decode())
        
        else:    
            match new_command:
                case "type":
                    check_file = shutil.which(parts[0])
                    if parts[0] == "exit" or parts[0] == "echo" or parts[0]== "type":
                        print(f"{parts[0]} is a shell builtin")
                    elif check_file is not None:
                        print(f"{parts[0]} is {check_file}")
                    else:
                        sentence = " ".join(parts)
                        print(f"{sentence}: not found")
                case "exit":
                    sys.exit(0)
                case "echo":
                    print(" ".join(parts))
                case default:
                    print(f"{new_command}: command not found")
    
    


if __name__ == "__main__":
    main()
