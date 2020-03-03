#NOTICE

# © 2020 The MITRE Corporation
#This software (or technical data) was produced for the U. S. Government under contract SB-1341-14-CQ-0010, and is subject to the Rights in Data-General Clause 52.227-14, Alt. IV (DEC 2007)
#Released under MITRE PRE #18-4297.


# FOR THIS TO WORK **kwargs MUST BE ADDED TO THE END OF ALL
# NLG self.functionS LIKE: core_Trace(has_changed,..., **kwargs)

from case_python_api.NLG import *
import case_python_api.case
from converter import *

import sys
import pprint

#====================================================
# Gather all dynamic data gathered from the wrapper.sh bash script for addition to user input.

cmd = sys.argv[1].strip().split("=")[1]
wrap_dict = {}
num = len(sys.argv)
for i in range(num):
    if i == 0:
        continue
    parts = sys.argv[i].strip().split("=")
    wrap_key = parts[0]
    wrap_val = parts[1]
    wrap_dict[wrap_key] = wrap_val
print "========================="

#====================================================
# Parse config and call respective API self.functions. Note the format of the config in notes.txt!
# self.obj_dict gathers config data and when a newline or "||||" is encountered object is created.

class ParseConfigToCallAPI:
    def __init__(self, wrap_dict):
        self.pp = pprint.PrettyPrinter(indent=4)
        self.all_modules = sys.modules[__name__]
        self.doc = case.Document()
        self.wrap_dict = wrap_dict

        self.NLG_type = None
        self.prop_key = None
        self.prop_val = None
        self.function = None

        self.obj_dict = {}
        self.tmp_dict = {}
        self.last_var = None
        self.last_obj = None
        self.root_var = []
        self.root_obj = []
        self.levl_dwn = 0
        self.prop_var = []
        self.prop_obj = []
        self.prop_dwn = 0
        self.flip_tmp = False
        
        self.tag      = None
        self.obj_refs = None
        self.clusters = {}      # List of all top-level objects (clusters of embedded objects).

#----------------------------------------------------
    # Parse the user's strings from the corresonding config file,
    # do type conversions, and call the API to create CASE objects.

    def parse_config(self):
        with open(cmd + ".config", "r") as cf:
            for line in cf:
                print "========================="
                print line.strip()
                print ""
#                self.pp.pprint(self.obj_dict)
#                self.pp.pprint(self.tmp_dict)
#                print ""
#                print "Last:", self.last_var
#                print "Last:", self.last_obj
#                print "Root:", self.root_var
#                print "Root:", self.root_obj
#                print "Prop:", self.prop_var
#                print "Prop:", self.prop_obj
#                self.pp.pprint(self.clusters)


                # Skip leading newlines that are empty.
                if (not line.strip()) and (self.NLG_type == None):
                    continue


                # Parse user-defined tags for referencing clusters.
                elif ("[{OBJ-TAG}]" in line) or ("[{OBJ-REF}]" in line) or ("[{list:OBJ-REF}]" in line):
                    if "[{OBJ-TAG}]" in line:
                        self.tag = line.strip().split("[{OBJ-TAG}]")[1]
                    elif ("[{OBJ-REF}]" in line) or ("[{list:OBJ-REF}]" in line):
                        if "list:" in line:
                            self.obj_refs = []
                            vals = line.strip().split("[{list:OBJ-REF}]")[1]
                            split_v = vals.strip().split("[ | ]")
                            for v in split_v:
                                self.obj_refs.append(self.clusters[v])
#                            print "OBJ-TAGS:", split_v
#                            print "OBJ-REFS:", self.obj_refs
                        else:
                            vals = line.strip().split("[{OBJ-REF}]")[1]
                            vals = vals.strip()
                            self.obj_refs = self.clusters[vals]
#                            print "OBJ-TAGS:", vals
#                            print "OBJ-REFS:", self.obj_refs
                    else:
                        print "~~~ Unexpected line."


                # If line is the end of an object.
                elif ((not line.strip()) or ("||||" in line) or ("|~~|" in line) \
                    and (self.NLG_type != None)):


                    if (not line.strip()):
                        self.call_api(embedded=False)

                        if self.root_obj:
                            self.clusters[self.tag] = self.root_obj[0]
                        else:
                            self.clusters[self.tag] = self.last_obj

                        self.root_var = []
                        self.root_obj = []
                        self.levl_dwn = 0
                        self.prop_var = []
                        self.prop_obj = []
                        self.prop_dwn = 0
                        self.tag      = None
                        self.obj_refs = None


                    elif ("||||" in line):
                        if (len(line.split("||||")) - 1) > self.levl_dwn:
                            self.levl_dwn += 1
                            self.call_api(embedded=False)
                            self.root_var.append(self.last_var)
                            self.root_obj.append(self.last_obj)
                        elif (len(line.split("||||")) -1) < self.levl_dwn:
                            self.levl_dwn -= 1
                            self.call_api(embedded=False)
                        else:
                            self.call_api(embedded=False)


                    elif ("|~~|" in line):
                        if self.flip_tmp == False:
                            self.tmp_dict = self.obj_dict
                            self.obj_dict = {}
                            self.flip_tmp = True
                        else:
                            if (len(line.split("|~~|")) - 1) > self.prop_dwn:
                                self.prop_dwn += 1
                                self.call_api(embedded=True)
                                self.prop_var.append(self.last_var)
                                self.prop_obj.append(self.last_obj)
                            elif (len(line.split("|~~|")) -1) < self.prop_dwn:
                                self.prop_dwn -= 1
                                self.call_api(embedded=True)
                            else:
                                self.call_api(embedded=True)
                            self.obj_dict = self.tmp_dict
                            self.tmp_dict = {}
                            self.flip_tmp = False
                    else:
                        print "~~~ Unexpected line."


                # If line is part of an object.
                else:
                    parts = line.strip().split("[==]")
                    CASE_key = parts[0]
                    self.NLG_type = CASE_key.split('.')[0]
                    self.prop_key = CASE_key.split('.')[1]
                    type_val = parts[1].split('}]', 1)[0].strip('[{')
                    self.prop_val = parts[1].split('}]', 1)[1]
                    self.prop_val = self.prop_val.strip()
                    self.prop_val = prop_converter(type_val, self.prop_val)

                    # Ignores inserting when empty.
                    if self.prop_key == '' and self.prop_val == '':
                        continue

                    # Handles setting embedded inheritance (i.e. properties being a sub_ of another NLG item.
                    if self.prop_val == "list:|^^|":
                        list_of_nlg_item = []
                        list_of_nlg_item.append(self.last_obj)
                        self.obj_dict[self.prop_key] = list_of_nlg_item
                    elif self.prop_val == "|^^|":
                        self.obj_dict[self.prop_key] = self.last_obj
                    else:
                        self.obj_dict[self.prop_key] = self.prop_val
#                    print "self.NLG_type", self.NLG_type
#                    print "self.prop_key", self.prop_key
#                    print "self.prop_val", self.prop_val

#----------------------------------------------------
    # Call the CASE Python API to create the appropriate objects.
    # (Assumes native type conversions have occurred first.)

    def call_api(self, embedded):

        self.function = getattr(self.all_modules, self.NLG_type)

        # For when no properties are specified but an NLG object is needed to create a sub-object.
        # I.e. the format of the config is: core_Trace.[==][{}]
        if (self.prop_key == '') and (self.prop_val == ''):
            if ("sub_" in self.NLG_type):
                self.last_var = self.NLG_type
                self.function = self.NLG_type + "(self.doc, self.last_obj)"
                exec("self.last_obj = {}".format(self.function))
                self.obj_dict={}
            elif ("propbundle_" in self.NLG_type):
                self.last_var = self.NLG_type
                self.function = self.NLG_type + "(self.last_obj)"
                exec("self.last_obj = {}".format(self.function))
                self.obj_dict={}
            #TODO Get rid of context_ (should be core_).
            elif ("core_" in self.NLG_type) or ("context_" in self.NLG_type) or ("duck_" in self.NLG_type):
                self.last_var = self.NLG_type
                self.function = self.NLG_type + "(self.doc)"
                exec("self.last_obj = {}".format(self.function))
                self.obj_dict={}
            else:
                print "Design logic issue."
                exit()

        # For when properties are specified.
        else:
            if ("sub_" in self.NLG_type):
                if embedded == False:
                    var = self.root_var
                    dct = self.root_obj
                    ref = self.levl_dwn - 1
                else:
                    var = self.prop_var
                    dct = self.prop_obj
                    ref = self.prop_dwn - 1
#                print ""
#                print "VAR:", var[ref]
#                print "DCT:", dct[ref]
#                print ""
                self.last_var = self.NLG_type
                self.last_obj = self.function(self.doc, dct[ref], **self.obj_dict)
                self.obj_dict={}
            elif ("propbundle_" in self.NLG_type):
                if embedded == False:
                    var = self.root_var
                    dct = self.root_obj
                    ref = self.levl_dwn - 1
                else:
                    var = self.prop_var
                    dct = self.prop_obj
                    ref = self.prop_dwn - 1
#                print ""
#                print "VAR:", var[ref]
#                print "DCT:", dct[ref]
#                print ""
                self.last_var = self.NLG_type
                self.last_obj = self.function(dct[ref], **self.obj_dict)
                self.obj_dict={}
            #TODO Get rid of context_ (should be core_).
            elif ("core_" in self.NLG_type) or ("context_" in self.NLG_type) or ("duck_" in self.NLG_type):
                self.last_var = self.NLG_type
                self.last_obj = self.function(self.doc, **self.obj_dict)
                self.obj_dict={}
            else:
                print "Unknown CASE category."
                exit()
        print "CREATED:", self.last_var, self.last_obj

#----------------------------------------------------
    # Serialize all CASE objects created into JSON-LD.

    def output_jsonLD(self):
        print "========================="
        #case_file = (datetime.datetime.now().strftime("%y-%m-%d")) + '_' + cmd + '.json'
        case_file = 'test_' + cmd + '.json'
        self.doc.serialize(format='json-ld', destination=case_file)
        #self.pp.pprint()

#====================================================

# Perform all the actions in this file (main).
get_the_parser = ParseConfigToCallAPI(wrap_dict)
all_the_things = get_the_parser.parse_config()
see_the_things = get_the_parser.output_jsonLD()





#====================================================
#with open("tmp_out.txt", "r") as cf:
#    for line in cf:
#        if not line.strip():
#            continue
#        else:
#            parts = line.strip().split("=")
#            CASE_key = parts[0]
#            self.NLG_type = CASE_key.split('.')[0]
#            self.prop_key = CASE_key.split('.')[1]
#            self.prop_val = parts[1]

