from json import load
from googletrans import Translator
from langdetect import detect, DetectorFactory
from scripts.strings_processing import string_processing


def translating_line(line: str, file_type, target_language=None, translator=None) -> str:
    line_and_stack = string_processing(line, file_type, 'replace')
    try:
        translation = translator.translate(line_and_stack[0], src='en', dest=target_language).text
    except TypeError:
        translation = line
    translation = string_processing((translation, line_and_stack[-1]), file_type, 'return')

    return translation


def defining_translator(func):
    with open("Properties.json", 'r', encoding='utf-8') as properties:
        target_language = load(properties)["target_language"]

    translator = Translator(service_urls=['translate.googleapis.com',
                                          'translate.google.com'])

    def wrapper(line, file_type):
        translation = func(line, file_type, target_language, translator)

        return translation

    return wrapper


@defining_translator
def translate_line(line, file_type, target_language=None, translator=None):
    DetectorFactory.seed = 0

    if detect(line) != target_language:
        translation = translating_line(line, file_type, target_language, translator)
    else:
        translation = line

    return translation
