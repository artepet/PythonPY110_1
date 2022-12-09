OUTPUT_FILE = "output.txt"


def task():
    with open(OUTPUT_FILE, "w") as f:  # TODO записать лесенку в файл
        for count_asterisk in range(1, 11):
            f.write(
            rows = 10
            for i in range(0, rows):
            for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
