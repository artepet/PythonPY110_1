import json


def task(input_filename: str, output_filename: str) -> None:
    with open(input_file) as f: # TODO считать содержимое json файл input.json
        idn = json.load(f)

    with open(output_filename, "w") as f: # TODO записать содержимое в json файл output.json с отступами
        json.dump(idn, f, indent = 4)


if __name__ == "__main__":
    input_file = "input.json"
    output_file = "output.json"

    task(input_file, output_file)

    with open(output_file) as output_f:
        for line in output_f:
            print(line, end="")
