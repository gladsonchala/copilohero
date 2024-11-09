from deep_translator import GoogleTranslator

class Translator:
    def __init__(self, from_lang, to_lang):
        self.translator = GoogleTranslator(source=from_lang, target=to_lang)

    def translate(self, text):
        return self.translator.translate(text)

# Example usage
if __name__ == "__main__":
    # Create a translator instance from English to Amharic
    translator = Translator(from_lang='en', to_lang='am')

    # Translate text
    text_to_translate = "Hello, how are you?"
    translated_text = translator.translate(text_to_translate)

    print(f"Original Text: {text_to_translate}")
    print(f"Translated Text: {translated_text}")
