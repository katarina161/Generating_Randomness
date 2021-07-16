import random


def get_train_data(min_length):
    print("Please give AI some data to learn...")
    data_str = ""
    while True:
        print(f"The current data length is {len(data_str)}, {min_length - len(data_str)} symbols left")
        user_str = input("Print a random string containing 0 or 1:\n\n")
        data_str += "".join([ch for ch in user_str if ch in "10"])
        if len(data_str) >= min_length:
            print(f"Final data string:\n{data_str}")
            return data_str


def get_triad_pattern(data_str: str):
    # [no. of 0, no. of 1]
    triad_pattern = {
        "000": [0, 0],
        "001": [0, 0],
        "010": [0, 0],
        "011": [0, 0],
        "100": [0, 0],
        "101": [0, 0],
        "110": [0, 0],
        "111": [0, 0],
    }

    for key in triad_pattern:
        i = 0
        while i < len(data_str) - 3:
            index = data_str.find(key, i)
            if index == -1 or index >= len(data_str) - 3:
                break
            if data_str[index + 3] == "0":
                triad_pattern[key][0] += 1
            elif data_str[index + 3] == "1":
                triad_pattern[key][1] += 1
            i = index + 1

    return triad_pattern


def make_a_prediction(pattern, test):
    prediction = ""
    for _ in range(3):
        prediction += random.choice("01")

    i = 0
    while len(prediction) < len(test):
        triad = test[i: i + 3]
        if pattern[triad][0] > pattern[triad][1]:
            symbol = "0"
        elif pattern[triad][0] < pattern[triad][1]:
            symbol = "1"
        else:
            symbol = random.choice("01")
        prediction += symbol
        i += 1

    return prediction


def test_the_accuracy(test, prediction):
    guessed = 0
    for i in range(3, len(test)):
        if test[i] == prediction[i]:
            guessed += 1
    accuracy = guessed / (len(test) - 3)
    print(f"Computer guessed right {guessed} out of {len(test) - 3} symbols ({round(accuracy * 100, 2)}%)")
    return guessed


def play_the_game(pattern):
    capital = 1000
    print("""You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!""")
    while True:
        print()
        test_input = input("Print a random string containing 0 or 1:\n")
        if test_input == "enough":
            print("Game over!")
            return
        test = ""
        test += "".join([ch for ch in test_input if ch in "10"])
        if not test:
            continue
        prediction = make_a_prediction(pattern, test)
        print(f"prediction:\n{prediction}")
        print()
        guessed = test_the_accuracy(test, prediction)
        capital = capital - guessed + (len(test) - 3 - guessed)
        print(f"Your capital is now ${capital}")


if __name__ == "__main__":
    min_length = 100
    data_str = get_train_data(min_length)
    triad_pattern = get_triad_pattern(data_str)
    print()
    play_the_game(triad_pattern)
