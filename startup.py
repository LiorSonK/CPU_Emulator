class startup:
    debug = False

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
                startup.debug = True
                return
            elif inpt.lower().strip() == "n":
                startup.debug = False
                return
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