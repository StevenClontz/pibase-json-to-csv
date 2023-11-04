import json
import csv
with open("data/main.json") as main_file:
    json_data = json.load(main_file)
sheets = [
    "spaces",
    "properties",
    "theorems",
    "traits"
]

for sheet in sheets:
    with open(f"data/main.{sheet}.csv", "w") as sheet_file:
        writer = csv.writer(sheet_file)
        if sheet == "spaces":
            writer.writerow([
                "Ref ID style",
                "Ref ID",
                "Ref title",
                "Space title",
                "Space ID"
            ])
        elif sheet == "properties":
            writer.writerow([
                "Ref ID style",
                "Ref ID",
                "Ref title",
                "Property title",
                "Property ID"
            ])
        elif sheet == "theorems":
            writer.writerow([
                "Ref ID style",
                "Ref ID",
                "Ref title",
                "Theorem ID"
            ])
        else: #traits
            writer.writerow([
                "Ref ID style",
                "Ref ID",
                "Ref title",
                "Space ID",
                "Space title",
                "Property ID",
                "Property title"
            ])
        for obj in json_data[sheet]:
            for ref in obj["refs"]:
                if "doi" in ref.keys():
                    ident_style = "doi"
                    ident = ref["doi"]
                elif "mathse" in ref.keys():
                    ident_style = "mathse"
                    ident = ref["mathse"]
                elif "mo" in ref.keys():
                    ident_style = "mo"
                    ident = ref["mo"]
                elif "mr" in ref.keys():
                    ident_style = "mr"
                    ident = ref["mr"]
                elif "wikipedia" in ref.keys():
                    ident_style = "wikipedia"
                    ident = ref["wikipedia"]
                else:
                    ident_style = "unknown"
                if sheet == "spaces":
                    writer.writerow([
                        ident_style, #"Ref ID style",
                        ident, #"Ref ID",
                        ref["name"], #"Ref title",
                        obj["name"], #"Space title",
                        obj["uid"], #"Space ID"
                    ])
                elif sheet == "properties":
                    writer.writerow([
                        ident_style, #"Ref ID style",
                        ident, #"Ref ID",
                        ref["name"], #"Ref title",
                        obj["name"], #"Property title",
                        obj["uid"], #"Property ID"
                    ])
                elif sheet == "theorems":
                    writer.writerow([
                        ident_style, #"Ref ID style",
                        ident, #"Ref ID",
                        ref["name"], #"Ref title",
                        obj["uid"], #"Theorem ID"
                    ])
                else: #traits
                    writer.writerow([
                        ident_style, #"Ref ID style",
                        ident, #"Ref ID",
                        ref["name"], #"Ref title",
                        obj["space"], #"Space ID"
                        obj["property"], #"Property ID"
                    ])
