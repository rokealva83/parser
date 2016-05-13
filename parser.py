# -*- coding: UTF-8 -*-

file_path = '/home/kindgeek/odoo-dev/parser/original.csv'
f = open(file_path)

wf = open('/home/kindgeek/odoo-dev/parser/original_convert.csv', 'wb')

# wf.write('Händler ID;'
#          'Händler;'
#          'Whitelabel Lieferant ID;'
#          'Whitelabel Lieferant;'
#          'Siroop Artikelnummer;'
#          'Händler Artikelnummer;'
#          'Artikel / Dienstleistung;'
#          'White Label;Bezeichnung;'
#          'Prioo Artikel;'
#          'Versandart / Capping;Warengruppe;'
#          'Händlerkommissionssatz;'
#          'Siroop Kundenbestellnummer;'
#          'MSOI ID;'
#          'Merchant Order UUID;'
#          'Händler Bestellnummer;'
#          'Bestelldatum;'
#          'Cancellation Initiated;'
#          'Stornodatum;Bestellstatus;'
#          'Auslieferdatum;Zulieferdatum;'
#          'Zahlart;Zahlungs ID;'
#          'Menge;MwSt-Satz;'
#          'Artikelpreis netto;'
#          'Artikelpreis MwSt;'
#          'Artikelpreis MwSt 2,5% (CHF);'
#          'Artikelpreis brutto;RetoureNr;'
#          'Retoure Start Datum;'
#          'Retoure End Datum;'
#          'Retoure Menge;'
#          'Retoure Begründung;'
#          'Retouren definitiv (%);'
#          'Retouren definitiv netto;'
#          'Retouren definitiv MwSt;'
#          'Retouren definitiv MwSt 2,5% (CHF);'
#          'Retouren definitiv brutto;'
#          'Waren und Dienstleistungen netto;'
#          'Waren und Dienstleistungen MwSt;'
#          'Waren und Dienstleistungen MwSt 2,5% (CHF);'
#          'Waren und Dienstleistungen brutto;'
#          'Händlerkommissionsbetrag netto;'
#          'Ist Pickup;Abholstation Name;'
#          'Abholstation Adresse;'
#          'Lieferaddresse Vorname;'
#          'Lieferaddresse Nachname')

lines = f.readlines()
line_keys = lines[0]
line_keys = line_keys.split(';')

vals = []
for line in lines:
    values = line.split(';')
    i = 0
    val = {}
    for value in values:
        val[line_keys[i]] = value
        i += 1
    vals.append(val)
print vals[1]


wf.close()
