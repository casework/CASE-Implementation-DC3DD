#NOTICE

# © 2020 The MITRE Corporation
#This software (or technical data) was produced for the U. S. Government under contract SB-1341-14-CQ-0010, and is subject to the Rights in Data-General Clause 52.227-14, Alt. IV (DEC 2007)
#Released under MITRE PRE #18-4297.

import datetime


def prop_converter(type_val, prop_val):
    if (type_val == 'list:|^^|'):
        return 'list:|^^|'
    elif (type_val == '|^^|'):
        return '|^^|'
    elif 'list:' in type_val:
        new_val = []
        split_p = prop_val.strip().split('[ | ]') 
        for s in split_p:
            con_val = string_converter(s, type_val.split('list:')[1])
            new_val.append(con_val)
    else:
        new_val = string_converter(prop_val, type_val)
    return new_val


# This function defines all type conversions from user-inputted strings to
# CASE-specific format (only for native types; excludes NLG object types).
def string_converter(prop_val, type_val):
    if type_val == 'str':
        con_val = str(prop_val.strip('"'))
    elif type_val == 'bool':
        if prop_val == 'True' or prop_val == 'true':
            con_val = True
        elif prop_val == 'False' or prop_val == 'false':
            con_val = False
        else:
            print '~~~ Improper bool value.'
    elif type_val == 'int':
        con_val = int(prop_val)
    elif type_val == 'datetime':
        con_val = datetime.datetime.strptime(prop_val, "%Y-%m-%dT%H:%M:%S.%fZ")
    else:
        print "~~~ Error with parsing property."
    return con_val
