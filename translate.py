# Python
from tqdm import tqdm
import polib
from googletrans import Translator
import os
import logging
import json

import getopt
import sys


def isset(variable):
    try:
        variable
    except NameError:
        return False
    else:
        return True


argumentList = sys.argv[1:]
try:
    opts, args = getopt.getopt(argumentList, "hf:l:", ["filename=", "language="])
    for opt, arg in opts:
        if opt == '-h':
            print('python translate.py -f <filename> -l <language>')
            sys.exit()
        elif opt in ("-f", "--filename"):
            filename = arg
        elif opt in ("-l", "--language"):
            language = arg
    print('Input file is ', filename)
    # print('Output file is ', language)
except getopt.error as err:
    print(str(err))
if not isset('filename') or not isset('language'):
    print('python translate.py -f "example.pot" -l "en"')
    exit()
# exit()


# import tkinter as tk
# from tkinter import filedialog

# root = tk.Tk()
# root.withdraw()

# filetypes = (
#     ('Pot File', '*.pot'),
#     ('Po File', '*.po'),
#     ('All files', '*.*'),
# )

# file_path = filedialog.askopenfilename(
#     title='Choice pot or po file...',
#     filetypes=filetypes,
#     defaultextension='.txt'
# )
# print(file_path)
# exit()

# Third Party

# Set up logging to a file
logging.basicConfig(
    level=logging.DEBUG,
    filename="translation.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
)

LANGUAGES = '{ "af":"afrikaans", "sq":"albanian", "am":"amharic", "ar":"arabic", "hy":"armenian", "az":"azerbaijani", "eu":"basque", "be":"belarusian", "bn":"bengali", "bs":"bosnian", "bg":"bulgarian", "ca":"catalan", "ceb":"cebuano", "ny":"chichewa", "zh-cn":"chinese (simplified)", "zh-tw":"chinese (traditional)", "co":"corsican", "hr":"croatian", "cs":"czech", "da":"danish", "nl":"dutch", "en":"english", "eo":"esperanto", "et":"estonian", "tl":"filipino", "fi":"finnish", "fr":"french", "fy":"frisian", "gl":"galician", "ka":"georgian", "de":"german", "el":"greek", "gu":"gujarati", "ht":"haitian creole", "ha":"hausa", "haw":"hawaiian", "iw":"hebrew", "he":"hebrew", "hi":"hindi", "hmn":"hmong", "hu":"hungarian", "is":"icelandic", "ig":"igbo", "id":"indonesian", "ga":"irish", "it":"italian", "ja":"japanese", "jw":"javanese", "kn":"kannada", "kk":"kazakh", "km":"khmer", "ko":"korean", "ku":"kurdish (kurmanji)", "ky":"kyrgyz", "lo":"lao", "la":"latin", "lv":"latvian", "lt":"lithuanian", "lb":"luxembourgish", "mk":"macedonian", "mg":"malagasy", "ms":"malay", "ml":"malayalam", "mt":"maltese", "mi":"maori", "mr":"marathi", "mn":"mongolian", "my":"myanmar (burmese)", "ne":"nepali", "no":"norwegian", "or":"odia", "ps":"pashto", "fa":"persian", "pl":"polish", "pt":"portuguese", "pa":"punjabi", "ro":"romanian", "ru":"russian", "sm":"samoan", "gd":"scots gaelic", "sr":"serbian", "st":"sesotho", "sn":"shona", "sd":"sindhi", "si":"sinhala", "sk":"slovak", "sl":"slovenian", "so":"somali", "es":"spanish", "su":"sundanese", "sw":"swahili", "sv":"swedish", "tg":"tajik", "ta":"tamil", "te":"telugu", "th":"thai", "tr":"turkish", "uk":"ukrainian", "ur":"urdu", "ug":"uyghur", "uz":"uzbek", "vi":"vietnamese", "cy":"welsh", "xh":"xhosa", "yi":"yiddish", "yo":"yoruba", "zu":"zulu" }'
l = json.loads(LANGUAGES)
# print(l["tr"])
if language in l:
    # Print the success message and the value of the key
    print("Language selected: ", language)
else:
    # Print the message if the value does not exist
    # print("%s is not found in JSON data" %keyVal)
    print("Please select a valid language code.")
    print('{ "af":"afrikaans", "sq":"albanian", "am":"amharic", "ar":"arabic", "hy":"armenian", "az":"azerbaijani", "eu":"basque", "be":"belarusian", "bn":"bengali", "bs":"bosnian", "bg":"bulgarian", "ca":"catalan", "ceb":"cebuano", "ny":"chichewa", "zh-cn":"chinese (simplified)", "zh-tw":"chinese (traditional)", "co":"corsican", "hr":"croatian", "cs":"czech", "da":"danish", "nl":"dutch", "en":"english", "eo":"esperanto", "et":"estonian", "tl":"filipino", "fi":"finnish", "fr":"french", "fy":"frisian", "gl":"galician", "ka":"georgian", "de":"german", "el":"greek", "gu":"gujarati", "ht":"haitian creole", "ha":"hausa", "haw":"hawaiian", "iw":"hebrew", "he":"hebrew", "hi":"hindi", "hmn":"hmong", "hu":"hungarian", "is":"icelandic", "ig":"igbo", "id":"indonesian", "ga":"irish", "it":"italian", "ja":"japanese", "jw":"javanese", "kn":"kannada", "kk":"kazakh", "km":"khmer", "ko":"korean", "ku":"kurdish (kurmanji)", "ky":"kyrgyz", "lo":"lao", "la":"latin", "lv":"latvian", "lt":"lithuanian", "lb":"luxembourgish", "mk":"macedonian", "mg":"malagasy", "ms":"malay", "ml":"malayalam", "mt":"maltese", "mi":"maori", "mr":"marathi", "mn":"mongolian", "my":"myanmar (burmese)", "ne":"nepali", "no":"norwegian", "or":"odia", "ps":"pashto", "fa":"persian", "pl":"polish", "pt":"portuguese", "pa":"punjabi", "ro":"romanian", "ru":"russian", "sm":"samoan", "gd":"scots gaelic", "sr":"serbian", "st":"sesotho", "sn":"shona", "sd":"sindhi", "si":"sinhala", "sk":"slovak", "sl":"slovenian", "so":"somali", "es":"spanish", "su":"sundanese", "sw":"swahili", "sv":"swedish", "tg":"tajik", "ta":"tamil", "te":"telugu", "th":"thai", "tr":"turkish", "uk":"ukrainian", "ur":"urdu", "ug":"uyghur", "uz":"uzbek", "vi":"vietnamese", "cy":"welsh", "xh":"xhosa", "yi":"yiddish", "yo":"yoruba", "zu":"zulu" }')
# exit()

# Load the PO file
po_file = polib.pofile(filename)

# Translate each message in the PO file
translator = Translator()
for entry in tqdm(po_file, desc="Translating messages"):
    if entry.msgstr:
        # Skip messages that have already been translated
        continue
    # Translate the message using Google Translate
    # dest = language code
    # All language codes can be found here > https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages
    try:
        translation = translator.translate(entry.msgid, dest=language).text
    except Exception as e:
        logging.error(f"Error translating '{entry.msgid}': {e}")
        continue
    # Set the translation as the message's msgstr
    entry.msgstr = translation

# Save the translated PO file with a new filename
base_filename = os.path.splitext(filename)[0]
dest_lang_code = language
translated_filename = f"{base_filename}_{dest_lang_code}.po"
po_file.save(translated_filename)
print(f"Your file has been translated and saved as {translated_filename}.")
