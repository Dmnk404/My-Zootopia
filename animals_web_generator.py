import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def main():
    '''Main function'''
    animals_data = load_data('animals_data.json')
    try:
        for animal in animals_data:
            print("Tier:")

            if "name" in animal:
                print(f"  Name: {animal['name']}")

            if animal.get("characteristics", {}).get("diet"):
                print(f"  Diet: {animal['characteristics']['diet']}")

            if animal.get("locations"):
                print(f"  Location: {animal['locations'][0]}")

            if animal.get("characteristics", {}).get("type"):
                print(f"  Type: {animal['characteristics']['type']}")

            print()

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()