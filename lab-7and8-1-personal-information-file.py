# Tim Lucas
# Chapter 7 and 8 Lab 1
# 2025-06-24

# read file function
def read_file(file):
    
    try:
        # open "data.txt" in read mode
        with open(file, "r") as data_file:

            # read the first line from the file and assign it to the variable "first_name".    
            first_name = data_file.readline()            
                
            # read second line and assign it to the variable "last_name"
            last_name = data_file.readline()

            # read third line and assign it to the variable "street_address"
            street_address = data_file.readline()

            # read fourth line and assign it to the variable "city"
            city = data_file.readline()

            # read fifth line and assign it to the variable "state"
            state = data_file.readline()
            
            # read sixth line and assign it to the variable "zip_code"
            zip_code = data_file.readline()

            # strip the newline characters from the fields.
            first_name = first_name.rstrip("\n")
            last_name = last_name.rstrip("\n")
            street_address = street_address.rstrip("\n")
            city = city.rstrip("\n")
            state = state.rstrip("\n")
            zip_code = zip_code.rstrip("\n")

            # display the record
            print()
            print(f"The contents of \"{file}\" is:")
            print()
            print(first_name, last_name,)
            print(street_address)
            print(city, state, zip_code)
            print()
    # exception for user calling a non-existent file
    except FileNotFoundError:
        print(f"\"{file}\" does not exist")

    # exception for a file that does exist but could not be read
    except OSError:
        print(f"Could not read \"{file}\"")               

# write file funtion
def write_file(file):

    # get user input for fields for record
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    street_address = input("Enter the street address: ")
    city = input("Enter the city: ")
    state = input("Enter the state: ")
    zip_code = input("Enter the zip code: ")

    # write data to file
    try:
        with open (file, "w") as data_file:
            data_file.write(f"{first_name}\n")
            data_file.write(f"{last_name}\n")
            data_file.write(f"{street_address}\n")
            data_file.write(f"{city}\n")
            data_file.write(f"{state}\n")
            data_file.write(f"{zip_code}\n")
        print()
        print(f"\"{file}\" was successfully written")
        print()
        
    # exception if file not able to be written        
    except:
        print(f"could not write, {data_file}")

def main():
    while True:
        file_name = input("What is the name of the file you wish to work with? ")
        mode = input("Are you going to (r)ead the file or (w)rite the file? ")

        if mode == "r":
            read_file(file_name)
            break
        elif mode =="w":
            write_file(file_name)
            break
        else:
            print("please enter \"r\" to read, or \"w\" to write")

if __name__ == "__main__":
    main()
