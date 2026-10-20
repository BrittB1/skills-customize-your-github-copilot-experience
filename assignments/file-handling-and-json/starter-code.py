import json


def load_data(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return {}
    except json.JSONDecodeError:
        print("The file does not contain valid JSON.")
        return {}


def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)
    print(f"Saved data to {filename}")


# Example usage
if __name__ == "__main__":
    data = load_data("data.json")
    print(data)
