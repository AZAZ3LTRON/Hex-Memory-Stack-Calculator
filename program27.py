class Hex_Mem_Stack_Calculator:
    """ A class developed according to the system requirements"""
    def __init__(self):
        pass
            
    def dec_hex_bin(self):
        """ Converts a decimal number to 16-bit binary, 
        and its signed interpretation"""
        
        print("===== Decimal Converter ===== ")
        
        while True:
            num = input("Enter a decimal number or 'back' to return to main menu:- ")
            
            if num.lower() == 'back':
                print("Returning to main menu...")
                break
            
            try:
                n = int(num)
                
                # Check if number provided is less than 0 (necessary for negative number conversion)
                if n < 0:
                    # Add 65536 to get the unsigned equivalent
                    unsigned_n = n + 65536 # Unsigned integer representing non-negative numbers
                else:
                    unsigned_n = n

                hexadecimal_value = format(unsigned_n, 'X') # Convert to hexadecimal with hex function
                binary_value = format(unsigned_n, '016b') # Convert to binary with leading zeros
                
                if unsigned_n < 32768:
                    signed_value = unsigned_n
                else:
                    signed_value = unsigned_n - 65536
        
                print(f"HEX = <{hexadecimal_value}>")
                print(f"BIN(16) = <{binary_value}>")
                print(f"SIGNED16 = <{signed_value}>")

            # If input is a string
            except ValueError:
                print("Error: Please enter a valid integer (numbers only, no letters or symbols)")
            
    def little_endian(self):
        """ Convert 16 bit numbers (find the least signficant bytle of the value)"""
        pass
    
    def ascii_dump(self):
        """Array addressing using offsets (base + index × element size)"""
        pass
    
    def array_addressing(self):
        """To be implemented"""
        pass
    
    def stack_frame(self):
        """To be implemented"""
        pass
    
def main():
    """ An interactive menu for the program """
    calculator = Hex_Mem_Stack_Calculator()
    
    # Using strings as keys to match input()
    actions = {
            "1": calculator.dec_hex_bin,
            "2": calculator.little_endian,
            "3": calculator.ascii_dump,
            "4": calculator.array_addressing,
            "5": calculator.stack_frame,  # Fixed: Removed () - now references method
            "0": "exit"  # Special marker for exit
        }
    
    print("==============================")
    print(" Hex Memory & Stack Calculator")
    print("==============================")
    print("1. Convert (decimal -> hex and 16-bit binary)")
    print("2. Little-endian pack/unpack (16-bit)")
    print("3. ASCII Memory Dump")
    print("4. Array Addressing")  
    print("5. Stack frame (bp offsets)")
    print("0. Exit")
    
    while True:
            choice = input("\nEnter your choice:- ")
            
            if choice in actions:
                if choice == "0":
                    print("Thank you for using the program")
                    break
                else:
                    # All options now handle their own input and looping
                    actions[choice]()  # Call the method (no calculator argument needed)
            else:
                print("Invalid choice. Please enter a number between 0-5.")
                
if __name__ == "__main__":
    main()