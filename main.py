import json
import csv
with open("data/main.json") as main_file:
    json_data = json.load(main_file)
sheets = [
    "spaces",
    "properties",
    # "theorems",
    # "traits"
]
# same as
# sheets = ["spaces", "properties", "theorems", "traits"]

for sheet in sheets:
    with open(f"data/main.{sheet}.csv", "w") as sheet_file:
        writer = csv.writer(sheet_file)
        writer.writerow([
            "Ref ID style",
            "Ref ID",
            "Ref title",
            "Object title",
            "Object ID"
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
                writer.writerow([ident_style, ident, ref["name"], obj["name"], obj["uid"]])
