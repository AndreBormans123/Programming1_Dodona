# https://dodona.ugent.be/nl/courses/1286/series/14353/activities/172219463


import random

def kaartspel():
  # lijst met alle mogelijke rangen
  rangen = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
  # lijst met alle mogelijke kleuren
  kleuren = ["C", "D", "H", "S"]

  kaarten = []

  # itereer over elke mogelijke rang
  for rang in rangen:
    # itereer over elke mogelijke kleur
    for kleur in kleuren:
      kaart = rang + kleur
      kaarten.append(kaart)

  # willekeurig door elkaar schudden
  random.shuffle(kaarten)

  return kaarten