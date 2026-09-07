#fill letter template using name and date

l = '''Dear <|name|>,
U r selected for the interview on <|date|>.'''

print(l.replace("<|name|>", "Naved").replace("<|date|>","27 oct 2026"))

