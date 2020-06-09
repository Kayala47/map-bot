#for word generation
import tracery
from tracery.modifiers import base_english

#for svg generation
import svgwrite

from rules import rules

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)

msg = grammar.flatten('#origin#')

def generate():
    return grammar.flatten('#origin#') + "\n"





