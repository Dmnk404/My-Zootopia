import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def main():
    '''Main function'''
    animals_data = load_data('animals_data.json')
    with open("animals_template.html", encoding="utf-8") as f:
        html_file = f.read()

    try:
        output = ""
        for animal in animals_data:
            output += '<li class="cards__item">'
            output += '<div class="card__title">'
            if "name" in animal:
                output += f"{animal['name']}<br/>\n"
            output += "</div>"
            output += '<p class="card__text">'
            if animal.get("characteristics", {}).get("diet"):
                output += f"<strong>Diet</strong>: {animal['characteristics']['diet']}<br/>\n"
            if animal.get("locations"):
                output += f"<strong>Location</strong>: {animal['locations'][0]}<br/>\n"
            if animal.get("characteristics", {}).get("type"):
                output += f"<strong>Type</strong>: {animal['characteristics']['type']}<br/>\n"
            output += "</p>"
            output += "</li>"

        new_html = html_file.replace("__REPLACE_ANIMALS_INFO__", output)

        with open("animals.html", "w", encoding="utf-8") as output_file:
            output_file.write(new_html)


    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()