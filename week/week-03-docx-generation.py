'''
Simple exercise to create documents using python

Key practice here is the pathing of pathlib and using docxtpl 
'''

from pathlib import Path
from docxtpl import DocxTemplate

BASE_DIR = Path(__file__).resolve().parent
template_path = (BASE_DIR / "../resources/assessor.docx").resolve()

data = {
    "pin_id": "123-232-131",
    "owner_raw": "Gina De Leon",
    "lot_number": "LOT-123",
    "barangay_name": "Visyan Village",
    "land_class": "C1",
    "area_declared": 300.00,
}

doc = DocxTemplate(template_path)
doc.render(data)

output_path = Path("~/Downloads/generated_doc.docx").expanduser()
doc.save(output_path)
