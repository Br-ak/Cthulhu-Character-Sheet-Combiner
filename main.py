import PyPDF2
from PyPDF2 import PdfReader

# path = '/Users/nathi/Downloads/Arthur_Cowell-12_30.pdf'
# path = '/Users/nathi/Downloads/Shady_McMan 12.30.2024.pdf' # different format, non editable
# path = '/Users/nathi/Downloads/Kevin_Hornback13.pdf' # different format, non editable
# path = '/Users/nathi/Downloads/Nigel Carrington.pdf'
# path = '/Users/nathi/Downloads/Jerry_Johnson 12.30.24.pdf'
# path = '/Users/nathi/Downloads/Arthur_Cowell (3).pdf'
# path = '/Users/nathi/Downloads/Shady_McMan.pdf'
# path = '/Users/nathi/Downloads/_Kevin_Hornback-1.pdf'


def init(path):
    pdf = open(path, 'rb')
    reader = PyPDF2.PdfReader(pdf)
    info = reader.metadata
    # print(info)
    # print(reader.pages[0].extract_text)

    results = []
    for i in range(0, len(reader.pages)):
        text = reader.pages[i].extract_text()
        results.append(text)

    # print(results)
    form_values = extract_form_values(path, reader)

    if form_values:
        for field, value in form_values.items():
            print(f"Field Name: {field}, Value: {value}")
    else:
        results = []
        for i in range(0, len(reader.pages)):
            text = reader.pages[i].extract_text()
            results.append(text)
        for value in results:
            print(f"{value}")

def extract_form_values(path, reader):
    with open(path, 'rb') as file:
        if not reader.get_fields():
            return
        
        form_fields = reader.get_fields()
        field_values = {}

        for field_name, field_data in form_fields.items():
            field_values[field_name] = field_data.get('/V', None)

        return field_values