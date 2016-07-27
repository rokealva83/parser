# -*- coding: UTF-8 -*-
from os import listdir


def tuple_without(original_tuple):
    num = len(original_tuple)
    num -= 1
    i = 1
    new_tuple = []
    while num >= i:
        new_tuple.append(original_tuple[i])
        i += 1
    return new_tuple


def files_list():
    files = listdir('.')
    my_csv = filter(lambda x: x.endswith('.csv'), files)
    return my_csv


def rename(line_keys):
    line_keys = line_keys.replace('Art;', 'Artikel / Dienstleistung;')
    line_keys = line_keys.replace('Artikelbezeichnung;', 'Bezeichnung;')
    line_keys = line_keys.replace('Händlerkommission;', 'Händlerkommissionssatz;')
    line_keys = line_keys.replace('Cancellation Completed;', 'Stornodatum;')
    line_keys = line_keys.replace('Artikelpreis netto (CHF);', 'Artikelpreis netto;')
    line_keys = line_keys.replace('Artikelpreis brutto (CHF);', 'Artikelpreis brutto;')
    line_keys = line_keys.replace('Retouren definitiv exkl. MwSt (CHF);', 'Retouren definitiv netto;')
    line_keys = line_keys.replace('Retouren definitiv MwSt 8% (CHF);', 'Retouren definitiv MwSt;')
    line_keys = line_keys.replace('Retouren definitiv MwSt 0% (CHF);', 'Retouren definitiv brutto;')
    line_keys = line_keys.replace('Retouren definitiv inkl. MwSt (CHF);', 'Waren und Dienstleistungen netto;')
    line_keys = line_keys.replace('Waren und Dienstleistungen exkl. MwSt (CHF);', 'Waren und Dienstleistungen MwSt;')
    line_keys = line_keys.replace('Waren und Dienstleistungen MwSt 0% (CHF);', 'Waren und Dienstleistungen brutto;')
    line_keys = line_keys.replace('Waren und Dienstleistungen inkl. MwSt. (CHF);', 'Händlerkommissionsbetrag netto;')
    line_keys = line_keys.replace('Kreditkarten Typ;', 'Zahlungsmittel;')
    return line_keys


def move_key(line_keys):
    new_line_keys = []
    for line_key in line_keys:
        if line_key != 'White Label' \
                and line_key != 'Cancellation Initiated' \
                and line_key != 'Artikelpreis MwSt 2,5% (CHF)' \
                and line_key != 'Retouren definitiv MwSt 2,5% (CHF)' \
                and line_key != 'Retouren definitiv MwSt 8% (CHF)' \
                and line_key != 'Retouren definitiv MwSt 0% (CHF)' \
                and line_key != 'Waren und Dienstleistungen MwSt 0% (CHF)' \
                and line_key != 'Waren und Dienstleistungen MwSt 2,5% (CHF)' \
                and line_key != 'Waren und Dienstleistungen MwSt 8% (CHF)' \
                and line_key != 'Versandart' \
                and line_key != 'Artikelpreis MwSt 8% (CHF)' \
                and line_key != 'Retoure Begründung' \
                and line_key != 'Siroop Kundenbestellnummer' \
                and line_key != 'Stornodatum' \
                and line_key != 'Bestelldatum' \
                and line_key != 'Händlerkommissionsbetrag excl. MwSt.' \
                and line_key != 'Bestellstatus':
            new_line_keys.append(line_key)

            if line_key == 'Händlerkommissionssatz':
                line_key = 'Siroop Kundenbestellnummer'
                new_line_keys.append(line_key)

            if line_key == 'Bezeichnung':
                line_key = 'Versandart / Capping'
                new_line_keys.append(line_key)

            elif line_key == 'Menge':
                line_key = 'MwSt-Satz'
                new_line_keys.append(line_key)

            elif line_key == 'Artikelpreis netto':
                line_key = 'Artikelpreis MwSt'
                new_line_keys.append(line_key)

            elif line_key == 'Retoure End Datum':
                line_key = 'Retoure Begründung'
                new_line_keys.append(line_key)

            elif line_key == 'Händler Bestellnummer':
                line_key = 'Bestelldatum'
                new_line_keys.append(line_key)
                line_key = 'Stornodatum'
                new_line_keys.append(line_key)
                line_key = 'Bestellstatus'
                new_line_keys.append(line_key)

    return new_line_keys


def definitiv(val):
    try:
        value1 = float(val.get('Retouren definitiv MwSt 2,5% (CHF)'))
    except:
        value1 = 0
    try:
        value2 = float(val.get('Retouren definitiv MwSt 8% (CHF)'))
    except:
        value2 = 0
    try:
        value3 = float(val.get('Retouren definitiv MwSt 0% (CHF)'))
    except:
        value3 = 0
    if value1 and value2 and value3 or value1 and value2 or value1 and value3 or value2 and value3:
        value = 0
    elif value2 != 0:
        value = value2
    elif value1 != 0:
        value = value1
    elif value3 != 0:
        value = value3
    else:
        value = 0
    return value


def waren(val):
    try:
        value1 = float(val.get('Waren und Dienstleistungen MwSt 2,5% (CHF)'))
    except:
        value1 = 0
    try:
        value2 = float(val.get('Waren und Dienstleistungen MwSt 8% (CHF)'))
    except:
        value2 = 0
    try:
        value3 = float(val.get('Waren und Dienstleistungen MwSt 0% (CHF)'))
    except:
        value3 = 0
    if value1 and value2 and value3 or value1 and value2 or value1 and value3 or value2 and value3:
        value = 0
    elif value2 != 0:
        value = value2
    elif value1 != 0:
        value = value1
    elif value3 != 0:
        value = value3
    else:
        value = 0
    return value


def mwst(val):
    try:
        value1 = float(val.get('Artikelpreis MwSt 2,5% (CHF)'))
    except:
        value1 = "Error"
    try:
        value2 = float(val.get('Artikelpreis MwSt 8% (CHF)'))
    except:
        value2 = "Error"

    if value1 == "Error" and value2 == "Error":
        value = ''
    elif value2 != "Error":
        value = 8.00
    elif value1 != "Error":
        value = 2.50
    else:
        value = 0.00
    return value


def float_to_str(value):
    try:
        value = float(value) + 0.0000001
    except:
        value = 0.00
    value = "%.2f" % value
    value = str(value).replace('.', ',')
    return value


def parser():
    file_list = files_list()
    import codecs
    for f in file_list:

        open_file = codecs.open(f, 'r')
        # open_file = codecs.open(f, 'r', encoding='utf-8', errors='ignore')
        lines = open_file.readlines()
        if lines and 'Art;' in lines[0]:
            name = f.split('.')
            new_name = '%s_%s.%s' % (name[0], 'convert', name[1])
            new_file = open(new_name, 'wb')
            new_file.write(codecs.BOM_UTF8)
            line_keys = lines[0]
            line_keys = line_keys.replace('\n', '')
            line_keys = line_keys.split(';')
            new_line_keys = rename(lines[0])
            new_line_keys = new_line_keys.replace('\n', '')
            new_line_keys = new_line_keys.split(';')
            new_line_keys = move_key(new_line_keys)
            lines = tuple_without(lines)

            first_line = ''
            for key in new_line_keys:
                first_line += '%s;' % str(key)
            first_line += '\n'
            first_line = first_line.replace('\r', '')
            new_file.write(first_line)
            # new_file.write(bytes(first_line, 'UTF-8'))

            for line in lines:
                line = line.replace('\n', '')
                line = line.replace(',', '.')

                line = line.replace("'", "")
                line = line.replace("&#039;", "'")

                values = line.split(';')
                i = 0
                val = {}
                for value in values:
                    try:
                        val[line_keys[i]] = value
                        i += 1
                    except:
                        pass

                new_line = ''
                for key in new_line_keys:
                    if key == 'Artikel / Dienstleistung':
                        value = val.get('Art')
                        if value and value.lower() == 'expense':
                            value = 'Versand an Kunde'
                        new_line = '%s%s;' % (new_line, value)

                    elif key == 'Bezeichnung':
                        new_line = '%s%s;' % (new_line, val.get('Artikelbezeichnung'))

                    elif key == 'Händlerkommissionssatz':
                        try:
                            value = val.get('Händlerkommission').replace('.', ',')
                        except:
                            value = ''
                        new_line = '%s%s;' % (new_line, value)

                    elif key == 'Stornodatum':
                        new_line = '%s%s;' % (new_line, val.get('Cancellation Completed'))

                    elif key == 'Artikelpreis brutto':
                        value = val.get('Artikelpreis brutto (CHF)')
                        value = float_to_str(value)
                        new_line = '%s%s;' % (new_line, value)

                    elif key == 'Zahlungsmittel':
                        new_line = '%s%s;' % (new_line, val.get('Kreditkarten Typ'))

                    elif key == 'Artikelpreis netto':
                        value = val.get('Artikelpreis netto (CHF)')
                        value = float_to_str(value)
                        new_line = '%s%s;' % (new_line, value)

                    elif key == 'Retouren definitiv brutto':
                        value = val.get('Retouren definitiv inkl. MwSt (CHF)')
                        value = float_to_str(value)
                        new_line = '%s%s;' % (new_line, value)

                    elif key == 'Retouren definitiv MwSt':
                        value = definitiv(val)
                        value = float_to_str(value)
                        new_line = '%s%s;' % (new_line, value)

                    elif key == 'Retouren definitiv netto':
                        value = val.get('Retouren definitiv exkl. MwSt (CHF)')
                        value = float_to_str(value)
                        new_line = '%s%s;' % (new_line, value)

                    elif key == 'Waren und Dienstleistungen netto':
                        value = val.get('Waren und Dienstleistungen exkl. MwSt (CHF)')
                        value = float_to_str(value)
                        new_line = '%s%s;' % (new_line, value)

                    elif key == 'Waren und Dienstleistungen MwSt':
                        value = waren(val)
                        value = float_to_str(value)
                        new_line = '%s%s;' % (new_line, value)

                    elif key == 'Waren und Dienstleistungen brutto':
                        value = val.get('Waren und Dienstleistungen inkl. MwSt. (CHF)')
                        value = float_to_str(value)
                        new_line = '%s%s;' % (new_line, value)

                    elif key == 'Versandart / Capping':
                        new_line = '%s%s;' % (new_line, val.get('Versandart'))

                    elif key == 'MwSt-Satz':
                        value = mwst(val)
                        value = float_to_str(value)
                        value = str(value) + '%'
                        new_line = '%s%s;' % (new_line, value)

                    elif key == 'Retouren definitiv (%)':
                        value = val.get(key)
                        try:
                            value = float(value) + 0.0000001
                            value = "%.2f" % value
                            value = str(value).replace('.', ',')
                        except:
                            value = ''
                        if value:
                            value = str(value) + '%'
                        new_line = '%s%s;' % (new_line, value)

                    elif key == 'Artikelpreis MwSt':
                        value = mwst(val)
                        value3 = val.get('Artikelpreis netto (CHF)')
                        try:
                            value = float(value3) * value / 100.0
                        except:
                            value = 0.00
                        value = float_to_str(value)
                        new_line = '%s%s;' % (new_line, value)

                    elif key == 'Händlerkommissionsbetrag netto':
                        value = val.get('Händlerkommissionsbetrag excl. MwSt.')
                        value = float_to_str(value)
                        new_line = '%s%s;' % (new_line, value)
                    else:
                        new_line = '%s%s;' % (new_line, val.get(key))

                if new_line:
                    new_line = new_line.replace('\r', '')
                    new_line += '\n'
                    new_file.write(new_line)
                    # new_file.write(bytes(new_line, 'UTF-8'))

            new_file.close()

parser()
