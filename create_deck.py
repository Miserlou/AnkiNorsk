import genanki
import os
import sys

MODEL_ID = 444222000
DECK_ID = 699699699

lang_model = genanki.Model(
  MODEL_ID,
  'Basic English-Norwegian',
  fields=[
    {'name': 'English'},
    {'name': 'Norwegian'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '<h2>{{Norwegian}}</h2>',
      'afmt': '<h2>{{FrontSide}}<hr id="answer">{{English}}</h2>',
    },
  ])

with open ("all_english.txt", "r") as english:
    english_words = [word.replace('\n', '') for word in english.readlines()]
with open ("all_norwegian.txt", "r") as norwegian:
    norwegian_words = [word.replace('\n', '') for word in norwegian.readlines()]

language_deck = genanki.Deck(
  DECK_ID,
  'Basic English-Norwegian'
)

i = 0
count = len(english_words)
while i < count:
    note = genanki.Note(
      model=lang_model,
      fields=[english_words[i], norwegian_words[i]])
    language_deck.add_note(note)
    i+=1

genanki.Package(language_deck).write_to_file('basic_english_norwegian.apkg')