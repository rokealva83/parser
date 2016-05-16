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
    line_keys = line_keys.replace('Cancellation Completed;', 'Stornodatum;')
    line_keys = line_keys.replace('Artikelpreis netto (CHF);', 'Artikelpreis netto;')
    line_keys = line_keys.replace('Artikelpreis brutto (CHF);', 'Artikelpreis brutto;')
    line_keys = line_keys.replace('Händlerkommissionsbetrag excl. MwSt.;', 'RetoureNr;')
    line_keys = line_keys.replace('Retouren definitiv exkl. MwSt (CHF);', 'Retouren definitiv netto;')
    line_keys = line_keys.replace('Retouren definitiv MwSt 8% (CHF);', 'Retouren definitiv MwSt;')
    line_keys = line_keys.replace('Retouren definitiv MwSt 0% (CHF);', 'Retouren definitiv brutto;')
    line_keys = line_keys.replace('Retouren definitiv inkl. MwSt (CHF);', 'Waren und Dienstleistungen netto;')
    line_keys = line_keys.replace('Waren und Dienstleistungen exkl. MwSt (CHF);', 'Waren und Dienstleistungen MwSt;')
    line_keys = line_keys.replace('Waren und Dienstleistungen MwSt 0% (CHF);', 'Waren und Dienstleistungen brutto;')
    line_keys = line_keys.replace('Waren und Dienstleistungen inkl. MwSt. (CHF);', 'Händlerkommissionsbetrag netto;')
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
                and line_key != 'Artikelpreis MwSt 8% (CHF)':
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

            elif line_key == 'Retoure Menge':
                line_key = 'Retoure Begründung'
                new_line_keys.append(line_key)
    return new_line_keys

def definitiv(val):
    try:
        value1 = float(val.get('Retouren definitiv MwSt 2,5% (CHF)'))
    except:
        value1 = 0
    try:
        value2 = val.get('Retouren definitiv MwSt 8% (CHF)')
    except:
        value2 = 0
    try:
        value3 = val.get('Retouren definitiv MwSt 0% (CHF)')
    except:
        value3 = 0
    if value1 and value2 and value3 or value1 and value2 or value1 and value3 or value2 and value3:
        value = 0
    elif value2 != 0:
        value = 8
    elif value1 != 0:
        value = 2.5
    elif value1 != 0:
        value = 0
    else:
        value = 0
    return value

def waren(val):
    try:
        value1 = float(val.get('Waren und Dienstleistungen MwSt 2,5% (CHF)'))
    except:
        value1 = 0
    try:
        value2 = val.get('Waren und Dienstleistungen MwSt 8% (CHF)')
    except:
        value2 = 0
    try:
        value3 = val.get('Waren und Dienstleistungen MwSt 0% (CHF)')
    except:
        value3 = 0
    if value1 and value2 and value3 or value1 and value2 or value1 and value3 or value2 and value3:
        value = 0
    elif value2 != 0:
        value = 8
    elif value1 != 0:
        value = 2.5
    elif value1 != 0:
        value = 0
    else:
        value = 0
    return value

def mwst(val):
    try:
        value1 = float(val.get('Artikelpreis MwSt 2,5% (CHF)'))
    except:
        value1 = 0
    try:
        value2 = val.get('Artikelpreis MwSt 8% (CHF)')
    except:
        value2 = 0

    if value1 and value2:
        value = 0
    elif value2 != 0:
        value = 8
    elif value1 != 0:
        value = 2.5
    else:
        value = 0
    return value

def parser():
    file_list = files_list()
    for f in file_list:
        open_file = open(f)
        lines = open_file.readlines()
        if 'Art;' in lines[0]:
            name = f.split('.')
            new_name = ''
            if len(name) != 2:
                print 'Error!!! File is not have correct name - (name.csv)'
                continue
            else:
                new_name = '%s_%s.%s' % (name[0], 'convert', name[1])
            new_file = open(new_name, 'wb')
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
            new_file.write(first_line)

            for line in lines:
                line = line.replace('\n', '')
                line = line.replace(',', '.')

                values = line.split(';')
                i = 0
                val = {}
                for value in values:
                    val[line_keys[i]] = value
                    i += 1

                new_line = ''
                i = 1
                for key in new_line_keys:
                    if key == 'Artikel / Dienstleistung':
                        value = val.get('Art')
                        if value.lower() == 'expense':
                            value = 'Versand an Kunde'
                        new_line = '%s%s;' % (new_line, value)

                    elif key == 'Bezeichnung':
                        new_line = '%s%s;' % (new_line, val.get('Artikelbezeichnung'))

                    elif key == 'Stornodatum':
                        new_line = '%s%s;' % (new_line, val.get('Cancellation Completed'))

                    elif key == 'Artikelpreis brutto':
                        new_line = '%s%s;' % (new_line, val.get('Artikelpreis brutto (CHF)'))

                    elif key == 'Artikelpreis netto':
                        value = val.get('Artikelpreis netto (CHF)')
                        try:
                            value = float(value)
                        except:
                            value = 0
                        new_line = '%s%s;' % (new_line, value)

                    elif key == 'RetoureNr':
                        new_line = '%s%s;' % (new_line, val.get('Händlerkommissionsbetrag excl. MwSt.'))

                    elif key == 'Retouren definitiv brutto':
                        new_line = '%s%s;' % (new_line, val.get('Retouren definitiv exkl. MwSt (CHF)'))

                    elif key == 'Retouren definitiv MwSt':
                        value = definitiv(val)
                        value4 =val.get('Retouren definitiv exkl. MwSt (CHF)')
                        try:
                            value = value4 * float(value) / 100.0
                        except:
                            value = 0
                        new_line = '%s%s;' % (new_line, value)

                    elif key == 'Retouren definitiv netto':
                        value = definitiv(val)
                        value4 =val.get('Retouren definitiv exkl. MwSt (CHF)')
                        try:
                            value = value4 - value4 * float(value) / 100.0
                        except:
                            value = 0
                        new_line = '%s%s;' % (new_line, value)

                    elif key == 'Waren und Dienstleistungen netto':
                        value = waren(val)

                        value4 =val.get('Waren und Dienstleistungen inkl. MwSt. (CHF)')
                        try:
                            value = value4 - value4 * float(value) / 100.0
                        except:
                            value = 0
                        new_line = '%s%s;' % (new_line, value)

                    elif key == 'Waren und Dienstleistungen MwSt':
                        value4 =val.get('Waren und Dienstleistungen inkl. MwSt. (CHF)')
                        try:
                            value = value4 * float(value) / 100.0
                        except:
                            value = 0
                        new_line = '%s%s;' % (new_line, value)

                    elif key == 'Waren und Dienstleistungen brutto':
                        new_line = '%s%s;' % (new_line, val.get('Waren und Dienstleistungen inkl. MwSt. (CHF)'))

                    elif key == 'Versandart / Capping':
                        new_line = '%s%s;' % (new_line, val.get('Versandart'))

                    elif key == 'MwSt-Satz':
                        value = mwst(val)
                        new_line = '%s%s;' % (new_line, value)

                    elif key == 'Artikelpreis MwSt':
                        value = mwst(val)
                        value3 = val.get('Artikelpreis netto (CHF)')
                        try:
                            value = int(value3) * value / 100.0
                        except:
                            value = 0
                        new_line = '%s%s;' % (new_line, value)

                    elif key == 'Händlerkommissionsbetrag netto':
                        value = val.get('Waren und Dienstleistungen inkl. MwSt. (CHF)')
                        new_line = '%s%s;' % (new_line, value)
                    else:

                        new_line = '%s%s;' % (new_line, val.get(key))

                new_line += '\n'
                new_file.write(new_line)
            new_file.close()


#
# wf.close()
parser()
