"""importing translator function"""
from deep_translator import MyMemoryTranslator

def english_to_french(englishtext):
    """code"""
    frenchtext = MyMemoryTranslator(source="en-IN", target="fr-FR").translate(englishtext)
    return frenchtext


def french_to_english(frenchtext):
    """code"""
    englishtext = MyMemoryTranslator(source="fr-FR", target="en-IN").translate(frenchtext)
    return englishtext
