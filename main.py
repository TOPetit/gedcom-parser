import json
from src import gedcom_parser

parser = gedcom_parser.GedcomParser(path="private/Theo-Export.ged")
print(parser.verify())

data = parser.parse()

print(parser.get_stats())

json_string = parser.export()
with open("private/test.json", "w") as file:
    file.write(json_string)
