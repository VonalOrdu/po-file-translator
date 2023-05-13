Source: https://github.com/alessio-livolsi/translation_tool

Thank you alessio-livolsi > https://github.com/alessio-livolsi


# Translation Tool

## Overview
A simple script that loads a PO file that iterates over each message and then translates the message using Google Translate API. 
The script uses the googletrans library and outputs translated text which, is then set as the message's msgstr attribute.

## Get Started
- Download or clone the repo
- Set up a virtual environment and `pip install -r requirements.txt`
- Drag the desired load file into the project
- Enter the language via the dest argument 
- A link to all the available languages is commented in the script
- Name the translated file accordingly
- To run the script `python translate.py -f <filename> -l <language_code>`
- Language Code : "af", "sq", "am", "ar", "hy", "az", "eu", "be", "bn", "bs", "bg", "ca", "ceb", "ny", "zh-cn", "zh-tw", "co", "hr", "cs", "da", "nl", "en", "eo", "et", "tl", "fi", "fr", "fy", "gl", "ka", "de", "el", "gu", "ht", "ha", "haw", "iw", "he", "hi", "hmn", "hu", "is", "ig", "id", "ga", "it", "ja", "jw", "kn", "kk", "km", "ko", "ku", "ky", "lo", "la", "lv", "lt", "lb", "mk", "mg", "ms", "ml", "mt", "mi", "mr", "mn", "my", "ne", "no", "or", "ps", "fa", "pl", "pt", "pa", "ro", "ru", "sm", "gd", "sr", "st", "sn", "sd", "si", "sk", "sl", "so", "es", "su", "sw", "sv", "tg", "ta", "te", "th", "tr", "uk", "ur", "ug", "uz", "vi", "cy", "xh", "yi", "yo", "zu"

## Considerations
In the requirements we are using version 4.0.0-rc1 of googletrans library. This is because the latest version of the library requires an API key to use Google Translate service.
Starting from version 4.1.0, Google requires a valid API key to use their Translation API service. Without a valid API key, the translation requests will fail with a 403 error. 

## Enjoy 🙃
