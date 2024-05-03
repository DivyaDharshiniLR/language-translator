from translate import Translator

text = "Hello, how are you?"
translator = Translator(to_lang="fr")
translation = translator.translate(text)
print(translation)
