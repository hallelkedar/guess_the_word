from game import game_loop

def main():
    while True:
        choice = game_loop()

        if choice == 'exit':
            return
if __name__ == '__main__':
    main()