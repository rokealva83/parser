# -*- coding: UTF-8 -*-

def tuple_without(original_tuple):
    num = len(original_tuple)
    num -= 1
    i = 1
    new_tuple = []
    while num >= i:
        new_tuple.append(original_tuple[i])
        i += 1
    return new_tuple


file_path = '/home/kindgeek/odoo-dev/parser/original.csv'
f = open(file_path)

wf = open('/home/kindgeek/odoo-dev/parser/original_convert.csv', 'wb')

lines = f.readlines()
line_keys = lines[0]
line_keys = line_keys.replace('Art;', 'Artikel / Dienstleistung;')
line_keys = line_keys.replace('Artikelbezeichnung;', 'Bezeichnung;')
line_keys = line_keys.replace('Cancellation Completed;', 'Stornodatum;')

line_keys = line_keys.replace('Artikelpreis brutto (CHF);', 'Artikelpreis brutto;')
line_keys = line_keys.replace('Artikelbezeichnung;', 'Artikelpreis brutto;')
line_keys = line_keys.replace(';(CHF);', ';Artikelpreis netto;')

line_keys = line_keys.replace('Retouren definitiv exkl. MwSt (CHF);', 'Retouren definitiv netto;')
line_keys = line_keys.replace('Retouren definitiv MwSt 8% (CHF);', 'Retouren definitiv MwSt;')

line_keys = line_keys.replace('Retouren definitiv MwSt 0% (CHF);', 'Retouren definitiv brutto;')
line_keys = line_keys.replace('Retouren definitiv inkl. MwSt (CHF);', 'Waren und Dienstleistungen netto;')
line_keys = line_keys.replace('Waren und Dienstleistungen exkl. MwSt (CHF);', 'Waren und Dienstleistungen MwSt;')

line_keys = line_keys.replace('Waren und Dienstleistungen MwSt 0% (CHF);', 'Waren und Dienstleistungen brutto;')

line_keys = line_keys.split(';')
new_line_keys = []

for line_key in line_keys:
    if line_key != 'White Label' \
            and line_key != 'Cancellation Initiated' \
            and line_key != 'Artikelpreis MwSt 2,5% (CHF)' \
            and line_key != 'Retouren definitiv MwSt 2,5% (CHF)' \
            and line_key != 'Waren und Dienstleistungen MwSt 2,5% (CHF)' \
            and line_key != 'Versandart':
        new_line_keys.append(line_key)

        if line_key == 'Prioo Artikel':
            line_key = 'Versandart / Capping'
            new_line_keys.append(line_key)

        elif line_key == 'Menge':
            line_key = 'MwSt-Satz'
            new_line_keys.append(line_key)

        elif line_key == 'Artikelpreis netto':
            line_key = 'Artikelpreis MwSt'
            new_line_keys.append(line_key)

        elif line_key == 'Retouren definitiv netto':
            line_key = 'Retouren definitiv MwSt'
            new_line_keys.append(line_key)

        elif line_key == 'Waren und Dienstleistungen netto':
            line_key = 'Waren und Dienstleistungen MwSt'
            new_line_keys.append(line_key)

        elif line_key == 'Retoure Menge':
            line_key = 'Retoure Begründung'
            new_line_keys.append(line_key)

lines = tuple_without(lines)




first_line = ''
for key in new_line_keys:
    first_line += '%s;' % str(key)
wf.write(first_line)

vals = []
for line in lines:
    values = line.split(';')
    i = 0
    val = {}
    for value in values:
        val[line_keys[i]] = value
        i += 1
    vals.append(val)

wf.close()
