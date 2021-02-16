from json import load
from googletrans import Translator
from langdetect import detect, DetectorFactory
from scripts.strings_processing import string_processing


def translating_line(line: str, file_type, target_language=None, translator=None) -> str:
    symbols_stack = []  # Contains symbols specific for each of the file types found in the current string

    line, symbols_stack = string_processing(line, symbols_stack, file_type, 'replace')
    try:
        translation = translator.translate(line, src='en', dest=target_language).text  # TODO issue #8
    except TypeError:
        translation = line
    translation, symbols_stack = string_processing(translation, symbols_stack, file_type, 'return')

    return translation


def defining_translator(func):
    with open("Properties.json", 'r', encoding='utf-8') as properties:
        target_language = load(properties)["target_language"]

    translator = Translator(service_urls=['translate.googleapis.com',
                                          'translate.googleapis.en',
                                          'translate.googleapis.ru',
                                          'translate.googleapis.uk',
                                          'translate.googleapis.pl', ],)
                            # proxies={'http': 'foo.bar:3128',
                            #          'http://host.name': 'foo.bar:4012'})

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
