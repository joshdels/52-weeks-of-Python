import re

from pathlib import Path
from pypdf import PdfReader

#  ------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent
pdf_path = BASE_DIR / "resources" / "lottery.pdf"
#  ------------------------------------------------

reader = PdfReader(pdf_path)

num_villagers = 0
num_voice = 0

for page in reader.pages:
    text = page.extract_text()

    villagers = re.findall(r"villagers", text, re.IGNORECASE)
    voice = re.findall(r"voice", text, re.IGNORECASE)

    num_villagers += len(villagers)
    num_voice += len(voice)


print(f"Villagers: {num_villagers}")
print(f"Voice: {num_voice}")
