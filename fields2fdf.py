import os
import sys
from fdfgen import forge_fdf


def parse_fields(input_fields_file):
    fields = list()
    with open(input_fields_file, "r") as input_f:
        field_name = None
        field_value = None
        field_type = None
        for line in input_f:
            line = line.strip()
            if line == "---" and field_name is not None and field_value is not None and field_type.lower() == "text":
                fields.append((field_name, field_value))
                print(fields[-1])
                field_name = None
                field_value = None
                field_type = None
            elif line.startswith("FieldName:"):
                field_name = line[len("FieldName: "):]
            elif line.startswith("FieldValue:"):
                parsed_field_value = line[len("FieldValue: "):]
                if parsed_field_value:
                    field_value = parsed_field_value
            elif line.startswith("FieldType:"):
                field_type = line[len("FieldType: "):]
    return fields


def main(input_fields_file):
    output_fdf = f"{os.path.basename(input_fields_file)}.fdf"
    fields = parse_fields(input_fields_file)
    fdf = forge_fdf("", fields, [], [])
    with open(output_fdf, "wb") as output_f:
        output_f.write(fdf)


if __name__ == "__main__":
    input_fields_file = sys.argv[1]
    main(input_fields_file)
