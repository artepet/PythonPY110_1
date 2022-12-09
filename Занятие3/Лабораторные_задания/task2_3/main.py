import json


def task():
    filename = "input.json"
    with open(filename) as f:
        max_score = json.load(f)
        return max(max_score, key=lambda p: p["score"])

     # TODO найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())
