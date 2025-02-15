import PyPDF2, json, os

VALUES_TO_KEEP = ['Investigator_Name', 'Investigators_Name', 'CurrentHP', 'CurrentSanity', 'CurrentLuck', 'LuckTotal', 
                  'STR', 'DEX', 'INT', 'CON', 'APP', 'POW', 'SIZ', 'EDU', 'MOV']
CHARACTER_VALUES = {}

def init(paths):
    CHARACTER_VALUES.clear()
    for path in paths:
        parse(path)

    json_path = os.path.join("static", "data.json")
    fileDelete(json_path)
    
    with open(json_path, 'w') as f:
        json.dump(CHARACTER_VALUES, f)

def fileDelete(path):
    if os.path.exists(path):
        os.remove(path)
        print(f"File '{path}' deleted")
    else:
        print(f"File not found at `{path}`.")

def fileDeleteUploads():
    folder = "uploads/"
    if os.path.exists(folder):
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            if os.fsdecode(file_path).endswith(".pdf"):
                fileDelete(file_path)
                print(f"File '{file_path}' deleted")

def parse(path):
    pdf = open(path, 'rb')
    reader = PyPDF2.PdfReader(pdf)
    results = []
    
    for i in range(0, len(reader.pages)):
        text = reader.pages[i].extract_text()
        results.append(text)

    form_values = extract_form_values(path, reader)
    if form_values != None:
        CHARACTER_VALUES[len(CHARACTER_VALUES)] = form_values
    else:
        CHARACTER_VALUES[len(CHARACTER_VALUES)] = "" # shows undefined
    pdf.close()

def extract_form_values(path, reader):
    with open(path, 'rb') as file:
        if not reader.get_fields():
            return
        
        form_fields = reader.get_fields()
        field_values = {}

        for field_name, field_data in form_fields.items():
            #print(field_name)
            if field_name in VALUES_TO_KEEP:
                #print(field_name, " ", field_data)
                if field_name == "Investigator_Name": # edge case for certain character sheets
                    field_values["Investigators_Name"] = field_data.get('/V', None)
                elif field_name == "LuckTotal": # edge case for certain character sheets
                    field_values["CurrentLuck"] = field_data.get('/V', None)
                else:
                    field_values[field_name] = field_data.get('/V', None)
        return field_values
