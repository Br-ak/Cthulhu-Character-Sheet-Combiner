import PyPDF2, json, os

VALUES_TO_KEEP = ['Investigator_Name', 'Investigators_Name', 'CurrentHP', 'CurrentSanity', 'STR', 'DEX', 'INT',
                      'CON', 'APP', 'POW', 'SIZ', 'EDU', 'MOV']
CHARACTER_VALUES = {}

def init(paths):
    CHARACTER_VALUES.clear()
    for path in paths:
        parse(path)

    json_path = "data.json"
    if os.path.exists("static\data.json"):
        os.remove("static\data.json")
        print(f"File '{json_path}' deleted")
    with open('static\data.json', 'w') as f:
        json.dump(CHARACTER_VALUES, f)


def parse(path):
    pdf = open(path, 'rb')
    reader = PyPDF2.PdfReader(pdf)
    results = []
    
    for i in range(0, len(reader.pages)):
        text = reader.pages[i].extract_text()
        results.append(text)

    form_values = extract_form_values(path, reader)
    CHARACTER_VALUES[len(CHARACTER_VALUES)] = form_values
    pdf.close()

def extract_form_values(path, reader):
    with open(path, 'rb') as file:
        if not reader.get_fields():
            return
        
        form_fields = reader.get_fields()
        field_values = {}

        for field_name, field_data in form_fields.items():
            if field_name in VALUES_TO_KEEP:
                if field_name == "Investigator_Name":
                    field_values["Investigators_Name"] = field_data.get('/V', None)
                else:
                    field_values[field_name] = field_data.get('/V', None)
        return field_values
