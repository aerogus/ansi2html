#!/usr/bin/env python3
##
# Conversion d'une log texte avec couleurs ANSI en fichier HTML
# ex: cat appli.log | ansi2html
#
from ansi2html import Ansi2HTMLConverter
conv = Ansi2HTMLConverter()
ansi = "".join(sys.stdin.readlines())
html = conv.convert(ansi)

