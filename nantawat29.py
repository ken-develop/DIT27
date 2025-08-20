def _input(text):
    return input(text)

def addNumber(_n1, _n2):
    return _n1 + _n2

def main():
    while True:
        _n = []
        labels = ["first", "second"]
        for i in range(2):
            user_input = int(_input(f"Enter the {labels[i]} number: "))
            _n.append(user_input)
        
        print(f"Sum: {addNumber(_n[0], _n[1])}")

        play_again = _input("Play again? y/n: ").strip().lower()
        if play_again not in ["y", "yes"]:
            print("Thank you for using the program!")
            break

if __name__ == "__main__":
    main()
