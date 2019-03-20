import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = "https://translate.yandex.net/api/v1/tr.json/translate"
def translate_de(text, to_lang):
  new_file_de = open("de1.txt")
  text = open("DE.txt")
  to_lang = "ru"
  options = {
    "id": "79f20f9e.5c9243dc.1cf2a8d0-1-0",
    'key': API_KEY,
    "text": text,
    "lang": 'de-{}'.format(to_lang),
    "srv": "tr-text"
  }
  response = requests.get(URL, params=options)
  json1 = response.json()
  return "de1.txt".join(json1["text"])
print(translate_de("DE.txt", "ru"))


def translate_es(text, to_lang):
  new_file_de = open("es1.txt")
  text = open("ES.txt")
  to_lang = "ru"
  options = {
    "id": "79f20f9e.5c9243dc.1cf2a8d0-1-0",
    'key': API_KEY,
    "text": text,
    "lang": 'es-{}'.format(to_lang),
    "srv": "tr-text"
  }
  response = requests.get(URL, params=options)
  json1 = response.json()
  return "es1.txt".join(json1["text"])
print(translate_es("ES.txt", "ru"))

def translate_fr(text, to_lang):
  new_file_de = open("fr1.txt")
  text = open("FR.txt")
  to_lang = "ru"
  options = {
    "id": "79f20f9e.5c9243dc.1cf2a8d0-1-0",
    'key': API_KEY,
    "text": text,
    "lang": 'fr-{}'.format(to_lang),
    "srv": "tr-text"
  }
  response = requests.get(URL, params=options)
  json1 = response.json()
  return "fr1.txt".join(json1["text"])
print(translate_fr("FR.txt", "ru"))
