from colorama.ansi import clear_screen


class startup:

    @staticmethod
    def print_logo():
        print("""-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
      ____ ____  _   _   _____                 _       _             
     / ___|  _ \| | | | | ____|_ __ ___  _   _| | __ _| |_ ___  _ __ 
    | |   | |_) | | | | |  _| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|
    | |___|  __/| |_| | | |___| | | | | | |_| | | (_| | || (_) | |   
     \____|_|    \___/  |_____|_| |_| |_|\__,_|_|\__,_|\__\___/|_|   

-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """)
    @staticmethod
    def debug_mode():
        while True:
            inpt = input("Debug mode (Y/N): ")
            if inpt.lower().strip() == "y":
                return True
            elif inpt.lower().strip() == "n":
                return False
            print("Please answer y/n!")

    @staticmethod
    def start_menu():
        startup.print_logo()
        debug = startup.debug_mode()
        startup.clear_screen()
        return debug

    @staticmethod
    def clear_screen():
        print("\n"*32) #32 bit reference (: