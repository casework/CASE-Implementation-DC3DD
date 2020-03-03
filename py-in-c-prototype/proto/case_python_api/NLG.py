# © 2020 The MITRE Corporation
#This software (or technical data) was produced for the U. S. Government under contract SB-1341-14-CQ-0010, and is subject to the Rights in Data-General Clause 52.227-14, Alt. IV (DEC 2007)
#Released under MITRE PRE #18-4297.


#====================================================
# CASE NLG VERIFIER v0.1.0

"""
The Natural Language Glossary (NLG) is an alphabetical list of types of CASE classes (categories of CASE types).
The functions in this file create CASE objects (instances of such types) while automatically checking ontology and type.
The API (case.py) could be used directly to create non-typed objects if ontology and type checking are not requirements.
However, we advise against this to maintain consistency across community usage of the ontology.

Note that different versions of the NLG exist for different realizations of the Unified Cyber Ontology.
The human legible NLG corresponding to this version of CASE (one realization of UCO) can be found here:
https://casework.github.io/case/case-v0.1.0-natural-language-glossary.html

-----------------------------------------------------
NOTES ON FUNCTION STRUCTURE

    CASE objects:         Search "CREATE A CASE OBJECT" in the API (case.py) to understand the high-level CASE objects.
    Parameters:           All parameters use underscores coming in and are set by default to a Missing object.
    Required parameters:  The CASE Document class is passed in ('_sub' functions also require their superseding CASE class).
    Ontology parameters:  All other parameters are specified by the CASE ontology, and may be required or optional.
    Function docstrings:  'Any number of' = must be a list (otherwise pass in a single Python object)
                          'Exactly one' or 'At least one' = required parameter
                          'At most one' = optional parameter
    Body asserts:         1) superseding CASE class/type (if applicable)
                          2) required parameters
                          3) optional parameters 
    Return:               The desired object is instantiated and parameters converted to CamelCase for JSON-LD output.

    See examples/NLG_template.txt for a list of all instances of function definitions, docstrings, and assert statements found in the NLG.

-----------------------------------------------------
ORGANIZATION FOR DEVELOPERS

As development of the ontology moves forward new functions and API classes may be added.
If you wish to contribute to improvement, follow these note-taking standards to help us stay on the same proverbial page.
    - #TODO:NothingElseToCheck - If no parameters are checked (incomplete ontology or ambiguity).
    - #NOCHECK:<param_name>    - If a parameter does not have a check (but at least one other parameter does).
    - #TODO:<type_name>        - If a standard has not been defined yet for a type check (e.g. #TODO:URI).
                                 Custom functions for such types may be found in the last section of this file.
    - There are two 'Identity' NLG types, one a 'core_' and one a 'propbundle_'.
      In assert output state which is required via "of type Identity (core)" or "of type Identity (propbundle)".
"""


import case
import sys
import unittest
import datetime

class Missing(object):
    def __init__(self):
        self.is_missing = True


#====================================================
#-- CORE IN ALPHABETICAL ORDER

def core_Action(uco_document, action_status=Missing(), start_time=Missing(), end_time=Missing(), errors=Missing(),
                action_count=Missing(), subaction_refs=Missing()):
    '''
    :param ActionStatus: At most one occurrence of type ControlledVocabulary.
    :param StartTime: At most one value of type Datetime.
    :param EndTime: At most one value of type Datetime.
    :param Errors: Any number of values of any type.
    :param ActionCount: At most one value of type PositiveInteger.
    :param SubactionRefs: Any number of occurrences of type Action.
    :return: A CoreObject object.
    '''

    if not isinstance(action_status, Missing):
        assert (isinstance(action_status, case.CoreObject) and (action_status.type=='ControlledVocabulary')),\
        "[core_Action] action_status must be of type ControlledVocab."
    if not isinstance(start_time, Missing):
        assert isinstance(start_time, datetime.datetime),\
        "[core_Action] start_time must be of type Datetime."
    if not isinstance(end_time, Missing):
        assert isinstance(end_time, datetime.datetime),\
        "[core_Action] end_time must be of type Datetime."
    #NOCHECK:errors
    if not isinstance(action_count, Missing):
        assert (isinstance(action_count, int) and (action_count > 0)),\
        "[core_Action] action_count must be of type Int and positive."
    if not isinstance(subaction_refs, Missing):
        assert isinstance(subaction_refs, list),\
        "[core_Action] subaction_refs must be of type List of Action."
        assert all( (isinstance(i, case.CoreObject) and i.type=='Action') for i in subaction_refs),\
        "[core_Action] subaction_refs must be of type List of Action."

    return uco_document.create_CoreObject('Action', ActionStatus=action_status, StartTime=start_time, EndTime=end_time,
                                          Errors=errors, ActionCount=action_count, SubactionRefs=subaction_refs)


def core_Assertion(uco_document):
    '''
    :return: A CoreObject object.
    '''

    #TODO:NothingElseToCheck

    return uco_document.create_CoreObject('Assertion')


def core_Bundle(uco_document):
    '''
    :return: A CoreObject object.
    '''

    #TODO:NothingElseToCheck

    return uco_document.create_CoreObject('Bundle')


def core_ControlledVocabulary(uco_document, value=Missing(), constraining_vocabulary_name=Missing(),
                              constraining_vocabulary_ref=Missing()):
    '''
    :param Value: Exactly one value of type String.
    :param ConstrainingVocabularyName: At most one value of type String.
    :param ConstrainingVocabularyReference: At most one value of type URI.
    :return: A CoreObject object.
    '''

    assert not isinstance(value, Missing),\
    "[core_ControlledVocabulary] value is required."
    if not isinstance(value, Missing):
        assert isinstance(value, str),\
        "[core_ControlledVocabulary] value must be of type String."

    if not isinstance(constraining_vocabulary_name, Missing):
        assert isinstance(constraining_vocabulary_name, str),\
        "[core_ControlledVocabulary] constraining_vocabulary_name must be of type URI."
    #TODO:URI

    return uco_document.create_CoreObject('ControlledVocabulary', Value=value,
                                          ConstrainingVocabularyName=constraining_vocabulary_name,
                                          ConstrainingVocabularyRef=constraining_vocabulary_ref)


def core_Identity(uco_document):
    '''
    :return: A CoreObject object.
    '''

    #TODO:NothingElseToCheck

    return uco_document.create_CoreObject('Identity')


def core_Location(uco_document):
    '''
    :return: A CoreObject object.
    '''

    #TODO:NothingElseToCheck

    return uco_document.create_CoreObject('Location')


def core_MarkingDefinition(uco_document, definition_type=Missing(), definition=Missing()):
    '''
    :param DefinitionType: Exactly one value of type String.
    :param Definition: Any number of occurrences of type MarkingModel.
    :return: A CoreObject object.
    '''

    assert not isinstance(definition_type, Missing),\
    "[core_MarkingDefinition] defintion_type is required."
    if not isinstance(definition_type, Missing):
        assert isinstance(definition_type, str),\
        "[core_MarkingDefinition] definition_type must be of type String."

    if not isinstance(definition, Missing):
        assert isinstance(definition, list),\
        "[core_MarkingDefinition] definition must be of type List of MarkingModel."
        assert all( (isinstance(i, case.DuckObject) and i.type=='MarkingModel') for i in definition),\
        "[core_MarkingDefinition] definition must be of type List of MarkingModel."

    return uco_document.create_CoreObject('MarkingDefinition', DefinitionType=definition_type, Definition=definition)


def core_Relationship(uco_document, is_directional=Missing(), target_ref=Missing(), source_ref=Missing(),
                      start_time=Missing(), end_time=Missing(), kind_of_relationship=Missing()):
    '''
    :param IsDirectional: Exactly one value of type Bool.
    :param TargetRef: Exactly one ocurrence of type CoreObject.
    :param SourceRef: At least one ocurrence of type CoreObject.
    :param StartTime: Any number of values of type Datetime.
    :param EndTime: Any number of values of Datetime.
    :param KindOfRelationship: At most one occurrence of type ControlledVocabulary.
    :return: A CoreObject object.
    '''

    assert not isinstance(is_directional, Missing),\
    "[core_Relationship] is_directional is required."
    if not isinstance(is_directional, Missing):
        assert isinstance(is_directional, bool),\
        "[core_Relationship] is_directional must be of type Bool."
    assert not isinstance(target_ref, Missing),\
    "[core_Relationship] target_ref is required."
    if not isinstance(target_ref, Missing):
        assert isinstance(target_ref, case.CoreObject),\
        "[core_Relationship] target_ref must be of type CoreObject."
    assert not isinstance(source_ref, Missing),\
    "[core_Relationship] source_ref is required."
    if not isinstance(source_ref, Missing):
        assert isinstance(source_ref, list),\
        "[core_Relationship] source_ref must be of type List of CoreObject."
        assert all(isinstance(i, case.CoreObject) for i in source_ref),\
        "[core_Relationship] source_ref must be of type List of CoreObject."

    if not isinstance(start_time, Missing):
        assert isinstance(start_time, list),\
        "[core_Relationship] start_time must be of type List of Datetime."
        assert all(isinstance(i, datetime.datetime) for i in start_time),\
        "[core_Relationship] start_time must be of type List of Datetime."
    if not isinstance(end_time, Missing):
        assert isinstance(end_time, list),\
        "[core_Relationship] end_time must be of type List of Datetime."
        assert all(isinstance(i, datetime.datetime) for i in end_time),\
        "[core_Relationship] end_time must be of type List of Datetime."
    if not isinstance(kind_of_relationship, Missing):
        assert (isinstance(kind_of_relationship, case.CoreObject) and (kind_of_relationship.type=='ControlledVocabulary')),\
        "[core_Relationship] kind_of_relationship must be of type ControlledVocabulary."

    return uco_document.create_CoreObject('Relationship', IsDirectional=is_directional, TargetRef=target_ref,
                                          SourceRef=source_ref, StartTime=start_time, EndTime=end_time,
                                          KindOfRelationship=kind_of_relationship)


def core_Role(uco_document):
    '''
    :return: A CoreObject object.
    '''

    #TODO:NothingElseToCheck

    return uco_document.create_CoreObject('Role')


def core_Tool(uco_document, name=Missing(), version=Missing(), tool_type=Missing(), service_pack=Missing(),
              creator=Missing(), references=Missing()):
    '''
    :param Name: At most one value of type String.
    :param Version: At most one value of type String.
    :param ToolType: At most one value of type String.
    :param ServicePack: At most one value of type String.
    :param Creator: At most one value of type String.
    :param References: Any number of values of URI.
    :return: A CoreObject object.
    '''

    if not isinstance(name, Missing):
        assert isinstance(name, str),\
        "[core_Tool] name must be of type String."
    if not isinstance(version, Missing):
        assert isinstance(version, str),\
        "[core_Tool] version must be of type String."
    if not isinstance(tool_type, Missing):
        assert isinstance(tool_type, str),\
        "[core_Tool] tool_type must be of type String."
    if not isinstance(service_pack, Missing):
        assert isinstance(service_pack, str),\
        "[core_Tool] service_pack must be of type String."
    if not isinstance(creator, Missing):
        assert isinstance(creator, str),\
        "[core_Tool] creator must be of type String."
    #TODO:URI
    #check for list and then URI type

    return uco_document.create_CoreObject('Tool', Name=name, Version=version, ToolType=tool_type,
                                          ServicePack=service_pack, Creator=creator, References=references)


def core_Trace(uco_document, has_changed=Missing(), state=Missing()):
    '''
    :param HasChanged: Exactly one value of type Bool.
    :param State: At most one occurrence of type ControlledVocabulary.
    :return: A CoreObject object.
    '''

    assert not isinstance(has_changed, Missing),\
    "[core_Trace] has_changed is required."
    if not isinstance(has_changed, Missing):
        assert isinstance(has_changed, bool),\
        "[core_Trace] has_changed must be of type Bool."

    if not isinstance(state, Missing):
        assert (isinstance(state, case.CoreObject) and (state.type=='ControlledVocabulary')),\
        "[core_Trace] state must be of type ControlledVocabulary."

    return uco_document.create_CoreObject('Trace', HasChanged=has_changed, State=state)


#====================================================
#-- CORE CHILDREN IN ALPHABETICAL ORDER

def core_sub_ActionLifecycle(uco_document, uco_object):
    '''
    :param PhraseRefs: Exactly one occurrence of type ArrayOfAction.
    :param ActionStatus: Exactly zero occurrences of type ControlledVocabulary.
    :param StartTime: Exactly zero values of type Datetime.
    :param EndTime: Exactly zero values of type Datetime.
    :param (Unnamed Class): Exactly zero values of any type.
    :param ActionCount: Exactly zero values of type PositiveInteger.
    :return: A SubObject object.
    '''

    assert (isinstance(uco_object, case.CoreObject) and (uco_object.type=='Action')),\
    "[core_sub_ActionLifecycle] uco_object must be of type Action."

    # TODO:This class checks if the fields for core_Action are not present.
    # If they are this object cannot be used and an error should be thrown. Is this a correct interpretation?

    return uco_document.create_SubObject('ActionLifecycle')


def core_sub_ForensicAction(uco_document, uco_object):
    '''
    :return: A SubObject object.
    '''

    assert (isinstance(uco_object, case.CoreObject) and (uco_object.type=='Action')),\
    "[core_sub_ForensicAction] uco_object must be of type Action."

    #TODO:NothingElseToCheck

    return uco_document.create_SubObject('ForensicAction')


#====================================================
#-- CONTEXT IN ALPHABETICAL ORDER

def context_Grouping(uco_document, context_strings=Missing()):
    '''
    :param Context: At least one value of type String.
    :return: A ContextObject object.
    '''

    assert not isinstance(context_strings, Missing),\
    "[context_Grouping] context_strings is required."
    if not isinstance(context_strings, Missing):
        assert isinstance(context_strings, list),\
        "[context_Grouping] context_strings must be of type List of String."
        assert all(isinstance(i, str) for i in context_strings),\
        "[context_Grouping] context_strings must be of type List of String."

    return uco_document.create_ContextObject('Grouping', ContextStrings=context_strings)


def context_Investigation(uco_document, investigation_form=Missing(), investigation_status=Missing(),
                          start_time=Missing(), end_time=Missing, focus=Missing(), object_refs=Missing()):
    '''
    :param InvestigationForm: Exactly one occurrence of type ControlledVocabulary.
    :param InvestigationStatus: At most one occurrence of type ControlledVocabulary.
    :param StartTime: At most one value of type Datetime.
    :param EndTime: At most one value of type Datetime.
    :param Focus: Any number of values of type String.
    :param ObjectRefs: Any number of occurrences of type CoreObject.
    :return: A ContextObject object.
    '''

    assert not isinstance(investigation_form, Missing),\
    "[context_Investigation] investigation_form is required."
    if not isinstance(investigation_form, Missing):
        assert (isinstance(investigation_form, case.CoreObject) and (investigation_form.type=='ControlledVocabulary')),\
        "[context_Investigation] investigation_form must be of type ControlledVocabulary."

    if not isinstance(investigation_status, Missing):
        assert (isinstance(investigation_status, case.CoreObject) and (investigation_status.type=='ControlledVocabulary')),\
        "[context_Investigation] investigation_status must be of type ControlledVocabulary."
    if not isinstance(start_time, Missing):
        assert isinstance(start_time, datetime.datetime),\
        "[context_Investigation] start_time must be of type Datetime."
    if not isinstance(end_time, Missing):
        assert isinstance(end_time, datetime.datetime),\
        "[context_Investigation] end_time must be of type Datetime."
    if not isinstance(focus, Missing):
        assert isinstance(focus, list),\
        "[context_Investigation] focus must be of type List of Strings."
        assert all(isinstance(i, str) for i in focus),\
        "[context_Investigation] focus must be of type List of Strings."
    if not isinstance(object_refs, Missing):
        assert isinstance(object_refs, list),\
        "[context_Investigation] object_refs must be of type List of CoreObject."
        assert all(isinstance(i, case.CoreObject) for i in object_refs),\
        "[context_Investigation] object_refs must be of type List of CoreObject."

    return uco_document.create_ContextObject('Investigation', InvestigationForm=investigation_form,
                                             InvestigationStatus=investigation_status, StartTime=start_time,
                                             EndTime=end_time, Focus=focus, ObjectRefs=object_refs)


def context_ProvenanceRecord(uco_document, exhibit_number=Missing(), object_refs=Missing()):
    '''
    :param ExhibitNumber: At most one value of type String.
    :param ObjectRefs: Any number of occurrences of type CoreObject.
    :return: A ContextObject object.
    '''

    if not isinstance(exhibit_number, Missing):
        assert isinstance(exhibit_number, str),\
        "[context_ProvenanceRecord] exhibit_number must be of type String."
    if not isinstance(object_refs, Missing):
        assert isinstance(object_refs, list),\
        "[context_ProvenanceRecord] object_refs must be of type List of CoreObject."
        assert all(isinstance(i, case.CoreObject) for i in object_refs),\
        "[context_ProvenanceRecord] object_refs must be of type List of CoreObject."

    return uco_document.create_ContextObject('ProvenanceRecord', ExhibitNumber=exhibit_number, ObjectRefs=object_refs)


#====================================================
#-- CONTEXT CHILDREN IN ALPHABETICAL ORDER

    # NO CHILDREN OF CONTEXT YET


#====================================================
#-- PROPERTYBUNDLES IN ALPHABETICAL ORDER

def propbundle_Account(uco_object, account_id=Missing(), expiration_time=Missing(), created_time=Missing(),
                       account_type=Missing(), account_issuer_ref=Missing(), is_active=Missing(),
                       modified_time=Missing(), owner_ref=Missing()):
    '''
    :param AccoundID: Exactly one value of type String.
    :param ExprationTime: At most one value of type Datetime.
    :param CreatedTime: At most one value of type Datetime.
    :param AccountType: At most one occurrence of type ControlledVocabulary.
    :param AccountIssuerRef: At most one occurrence of type CoreObject.
    :param IsActive: At most one value of type Bool.
    :param ModifiedTime: At most one value of type Datetime.
    :param OwnerRef: At most one occurrence of type CoreObject.
    :return: A PropertyBundle object.
    '''
    
    assert not isinstance(account_id, Missing),\
    "[propbundle_Account] account_id is required."
    if not isinstance(account_id, Missing):
        assert isinstance(account_id, str),\
        "[propbundle_Account] account_id must be of type String."

    if not isinstance(expiration_time, Missing):
        assert isinstance(expiration_time, datetime.datetime),\
        "[propbundle_Account] expiration_time must be of type Datetime."
    if not isinstance(created_time, Missing):
        assert isinstance(created_time, datetime.datetime),\
        "[propbundle_Account] created_time must be of type TimeStamp."
    if not isinstance(account_type, Missing):
        assert (isinstance(account_type, case.CoreObject) and (account_type.type=='ControlledVocabulary')),\
        "[propbundle_Account] account_type must be of type ControlledVocabulary."
    if not isinstance(account_issuer_ref, Missing):
        assert isinstance(account_issuer_ref, case.CoreObject),\
        "[propbundle_Account] account_issuer_ref must be of type CoreObject."
    if not isinstance(is_active, Missing):
        assert isinstance(is_active, bool),\
        "[propbundle_Account] is_active must be of type Bool."
    if not isinstance(modified_time, Missing):
        assert isinstance(modified_time, datetime.datetime),\
        "[propbundle_Account] modified_time must be of type Datetime."
    if not isinstance(owner_ref, Missing):
        assert isinstance(owner_ref, case.CoreObject),\
        "[propbundle_Account] owner_ref must be of type CoreObject."

    return uco_object.create_PropertyBundle('Account', AccoundID=account_id, ExpirationTime=expiration_time,
                                            CreatedTime=created_time,  AccountType=account_type,
                                            AccountIssuerRef=account_issuer_ref, IsActive=is_active,
                                            ModifiedTime=modified_time, OwnerRef=owner_ref)


def propbundle_AccountAuthentication(uco_object, password=Missing(), password_type=Missing(),
                                     password_last_changed=Missing()):
    '''
    :param Password: At most one value of type String.
    :param PasswordType: At most one value of type String.
    :param PasswordLastChanged: At most one value of type Datetime.
    :return: A PropertyBundle object.
    '''

    if not isinstance(password, Missing):
        assert isinstance(password, str),\
        "[propbundle_AccountAuthentication] password must be of type String."
    if not isinstance(password_type, Missing):
        assert isinstance(password_type, str),\
        "[propbundle_AccountAuthentication] password_type must be of type String."
    if not isinstance(password_last_changed, Missing):
        assert isinstance(password_last_changed, datetime.datetime),\
        "[propbundle_AccountAuthentication] password_last_changed must be of type Datetime."

    return uco_object.create_PropertyBundle('AccountAuthentication', Password=password,
                                            PasswordType=password_type,
                                            PasswordLastChanged = password_last_changed)


def propbundle_ActionReferences(uco_object, environment_ref=Missing(), result_refs=Missing(),
                                performer_refs=Missing(), participant_refs=Missing(),
                                object_refs=Missing(), location_refs=Missing(), instrument_refs=Missing()):
    '''
    :param EnvironmentRef: At most one occurrence of type CoreObject.
    :param ResultRefs: Any number of occurrences of type CoreObject.
    :param PerformerRef: At most one occurrence of type CoreObject.
    :param ParticipantRefs: Any number of occurrences of type CoreObject.
    :param ObjectRefs: Any number of occurrences of type CoreObject.
    :param LocationRefs: Any number of occurrences of type Location.
    :param InstrumentRefs: Any number of occurrences of type CoreObject.
    :return: A PropertyBundle object.
    '''

    if not isinstance(environment_ref, Missing):
        assert isinstance(environment_ref, case.CoreObject),\
        "[propbundles_ActionReferences] environment_ref must be of type CoreObject."
    if not isinstance(result_refs, Missing):
        assert isinstance(result_refs, list),\
        "[propbundles_ActionReferences] result_refs must be of type List of CoreObject."
        assert all(isinstance(i, case.CoreObject) for i in result_refs),\
        "[propbundles_ActionReferences] result_refs must be of type List of CoreObject."
    if not isinstance(performer_refs, Missing):
        assert isinstance(performer_refs, case.CoreObject),\
        "[propbundles_ActionReferences] performer_refs must be of type CoreObject."
    if not isinstance(participant_refs, Missing):
        assert isinstance(participant_refs, list),\
        "[propbundles_ActionReferences] participant_refs must be of type List of CoreObject."
        assert all(isinstance(i, case.CoreObject) for i in participant_refs),\
        "[propbundles_ActionReferences] participant_refs must be of type List of CoreObject."
    if not isinstance(object_refs, Missing):
        assert isinstance(object_refs, list),\
        "[propbundles_ActionReferences] object_refs must be of type List of CoreObject."
        assert all(isinstance(i, case.CoreObject) for i in object_refs),\
        "[propbundles_ActionReferences] object_refs must be of type List of CoreObject."
    if not isinstance(location_refs, Missing):
        assert isinstance(location_refs, list),\
        "[propbundles_ActionReferences] location_refs must be of type List of Location."
        assert all( (isinstance(i, case.CoreObject)) and (i.type=='Location') for i in location_refs),\
        "[propbundles_ActionReferences] location_refs must be of type List of Location."
    if not isinstance(instrument_refs, Missing):
        assert isinstance(instrument_refs, list),\
        "[propbundles_ActionReferences] instrument_refs must be of type List of CoreObject."
        assert all(isinstance(i, case.CoreObject) for i in instrument_refs),\
        "[propbundles_ActionReferences] instrument_refs must be of type List of CoreObject."

    return uco_object.create_PropertyBundle('ActionReferences', EnvironmentRef=environment_ref,
                                            ResultRefs=result_refs, PerformerRefs=performer_refs,
                                            ParticipantRefs=participant_refs, ObjectRefs=object_refs,
                                            LocationRefs=location_refs, InstrumentRefs=instrument_refs)


def propbundle_Application(uco_object, application_identifier=Missing(), version=Missing(),
                           operating_system_ref=Missing(), number_of_launches=Missing()):
    '''
    :param ApplicationIdentifier: At most one value of type String.
    :param Version: At most one value of type String.
    :param OperatingSystemRef: At most one occurrence of type Trace.
    :param NumberOfLaunches: At most one value of type PositiveInteger.
    :return: A PropertyBundle object.
    '''

    if not isinstance(application_identifier, Missing):
        assert isinstance(application_identifier, str),\
        "[propbundle_Application] application_identifier must be of type String."
    if not isinstance(version, Missing):
        assert isinstance(version, str),\
        "[propbundle_Application] version must be of type String."
    if not isinstance(operating_system_ref, Missing):
        assert (isinstance(operating_system_ref, case.CoreObject) and (operating_system_ref.type=='Trace')),\
        "[propbundle_Application] operating_system_ref must be of type Trace."
    if not isinstance(number_of_launches, Missing):
        assert (isinstance(number_of_launches, int) and (number_of_launches > 0)),\
        "[propbundle_Application] number_of_launches must be of type PositiveInteger."

    return uco_object.create_PropertyBundle('Application', ApplicationIdentifier=application_identifier,
                                            Version=version, OperatingSystemRef=operating_system_ref,
                                            NumberOfLaunches=number_of_launches)


def propbundle_ApplicationAccount(uco_object, application_ref=Missing()):
    '''
    :param ApplicationRef: Exactly one occurrence of type Trace.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(application_ref, Missing),\
    "[propbundle_ApplicationAccount] application_ref is required."
    if not isinstance(application_ref, Missing):
        assert (isinstance(application_ref, case.CoreObject) and (application_ref.type=='Trace')),\
        "[propbundle_ApplicationAccount] application_ref must be of type Trace."

    return uco_object.create_PropertyBundle('ApplicationAccount', ApplicationRef=application_ref)


def propbundle_ArchiveFile(uco_object, version=Missing(), comment=Missing(), archive_type=Missing()):
    '''
    :param Version: At most one value of type String.
    :param Comment: At most one value of type String.
    :param ArchiveType: At most one value of type String.
    :return: A PropertyBundle object.
    '''

    if not isinstance(version, Missing):
        assert isinstance(version, str),\
        "[propbundle_ArchiveFile] version must be of type String."
    if not isinstance(comment, Missing):
        assert isinstance(comment, str),\
        "[propbundle_ArchiveFile] comment must be of type String."
    if not isinstance(archive_type, Missing):
        assert isinstance(archive_type, str),\
        "[propbundle_ArchiveFile] archive_type must be of type String."

    return uco_object.create_PropertyBundle('ArchiveFile', Version=version, Comment=comment, ArchiveType=archive_type)


def propbundle_Attachment(uco_object, url):
    '''
    :param URL: Exactly one value of type URI.
    :return: A PropertyBundle object.
    '''

    #TODO:URL

    return uco_object.create_PropertyBundle('Attachment', URL=url)


def propbundle_Audio(uco_object, audio_format=Missing(), audio_type=Missing(), bit_rate=Missing(), duration=Missing()):
    '''
    :param AudioFormat: At most one value of type String.
    :param AudioType: At most one value of type String.
    :param BitRate: At most one value of type Long.
    :param Duration: At most one value of type Long.
    :return: A PropertyBundle object.
    '''

    if not isinstance(audio_format, Missing):
        assert isinstance(audio_format, str),\
        "[propbundle_Audio] audio_format must be of type String."
    if not isinstance(audio_type, Missing):
        assert isinstance(audio_type, str),\
        "[propbundle_Audio] audio_type must be of type String."
    if not isinstance(bit_rate, Missing):
        assert isinstance(bit_rate, long),\
        "[propbundle_Audio] bit_rate must be of type Long."
    if not isinstance(duration, Missing):
        assert isinstance(duration, long),\
        "[propbundle_Audio] duration must be of type Long."

    return uco_object.create_PropertyBundle('Audio', AudioFormat=audio_format, AudioType=audio_type,
                                            BitRate=bit_rate, Duration=duration)


def propbundle_Authorization(uco_object, authorization_type=Missing(), authorization_identifier=Missing()):
    '''
    :param AuthorizationType: Exactly one occurrence of type ControlledVocabulary.
    :param AuthorizationIdentifier: At least one value of type String.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(authorization_type, Missing),\
    "[propbundle_Authorization] authorization_type is required."
    if not isinstance(authorization_type, Missing):
        assert (isinstance(authorization_type, case.CoreObject) and (authorization_type.type=='ControlledVocabulary')),\
        "[propbundle_Authorization] authorization_type must be of type ControlledVocabulary."

    if not isinstance(authorization_identifier, Missing):
        assert isinstance(authorization_identifier, str),\
        "[propbundle_Authorization] authorization_identifier must be of type String."

    return uco_object.create_PropertyBundle('Authorization', AuthorizationType=authorization_type,
                                            AuthorizationIdentifier=authorization_identifier)


def propbundle_AutonomousSystem(uco_object, number=Missing(), as_handle=Missing(),
                                regional_internet_registry=Missing()):
    '''
    :param Number: Exactly one value of type Integer.
    :param AsHandle: At most one value of type String.
    :param RegionalInternetRegistry: At most one occurrence of type ControlledVocabulary.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(number, Missing),\
    "[propbundle_AutonomousSystem] number is required."
    if not isinstance(number, Missing):
        assert isinstance(number, int),\
        "[propbundle_AutonomousSystem] number must be of type Integer."

    if not isinstance(as_handle, Missing):
        assert isinstance(as_handle, str),\
        "[propbundle_AutonomousSystem] as_handle must be of type String."
    if not isinstance(regional_internet_registry, Missing):
        assert (isinstance(regional_internet_registry, case.CoreObject) and
                (regional_internet_registry.type=='ControlledVocabulary')),\
        "[propbundle_AutonomousSystem] regional_internet_registry must be of type ControlledVocabulary."

    return uco_object.create_PropertyBundle('AutonomousSystem', Number=number, AsHandle=as_handle,
                                            RegionalInternetRegistry=regional_internet_registry)


def propbundle_BrowserBookmark(uco_object, accessed_time=Missing(), application_ref=Missing(),
                               created_time=Missing(), modified_time=Missing(), bookmark_path=Missing(),
                               url_targeted=Missing(), visit_count=Missing()):
    '''
    :param AccessedTime: At most one value of type Datetime.
    :param ApplicationRef: At most one occurrence of type Trace.
    :param CreatedTime: At most one value of type Datetime.
    :param ModifiedTime: At most one value of type Datetime.
    :param BookmarkPath: At most one value of type String.
    :param URLTargeted: At most one occurrence of type URL.
    :param VisitCount: At most one value of type Integer.
    :return: A PropertyBundle object.
    '''

    if not isinstance(accessed_time, Missing):
        assert isinstance(accessed_time, datetime.datetime),\
        "[propbundle_BrowserBookmark] accessed_time must be of type Datetime."
    if not isinstance(application_ref, Missing):
        assert (isinstance(application_ref, case.CoreObject) and (application_ref.type=='Trace')),\
        "[propbundle_BrowserBookmark] application_ref must be of type Trace."
    if not isinstance(created_time, Missing):
        assert isinstance(created_time, datetime.datetime),\
        "[propbundle_BrowserBookmark] created_time must be of type Datetime."
    if not isinstance(modified_time, Missing):
        assert isinstance(modified_time, datetime.datetime),\
        "[propbundle_BrowserBookmark] modified_time must be of type Datetime."
    if not isinstance(bookmark_path, Missing):
        assert isinstance(bookmark_path, str),\
        "[propbundle_BrowserBookmark] bookmark_path must be of type String."
    #TODO:URL
    if not isinstance(visit_count, Missing):
        assert isinstance(visit_count, int),\
        "[propbundle_BrowserBookmark] visit_count must be of type Integer."

    return uco_object.create_PropertyBundle('BrowserBookmark', AccessedTime=accessed_time,
                                            ApplicationRef=application_ref, CreatedTime=created_time,
                                            ModifiedTime=modified_time, BookmarkPath=bookmark_path,
                                            URLTargeted=url_targeted, VisitCount=visit_count)


def propbundle_BrowserCookie(uco_object, accessed_time=Missing(), application_ref=Missing(),
                             created_time=Missing(), expiration_time=Missing(), domain_ref=Missing(),
                             cookie_name=Missing(), cookie_path=Missing(), is_secure=Missing()):
    '''
    :param AccessedTime: At most one value of type Datetime.
    :param ApplicationRef: At most one occurrence of type Trace.
    :param CreatedTime: At most one value of type Datetime.
    :param ExpirationTime: At most one value of type Datetime.
    :param DomainRef: At most one occurrence of type Trace.
    :param CookieName: At most one value of type String.
    :param CookiePath: At most one value of type String.
    :param IsSecure: At most one value of type Bool.
    :return: A PropertyBundle object.
    '''

    if not isinstance(accessed_time, Missing):
        assert isinstance(accessed_time, datetime.datetime),\
        "[propbundle_BrowserCookie] accessed_time must be of type Datetime."
    if not isinstance(application_ref, Missing):
        assert (isinstance(application_ref, case.CoreObject) and (application_ref.type=='Trace')),\
        "[propbundle_BrowserCookie] application_ref must be of type Trace."
    if not isinstance(created_time, Missing):
        assert isinstance(created_time, datetime.datetime),\
        "[propbundle_BrowserCookie] created_time must be of type Datetime."
    if not isinstance(expiration_time, Missing):
        assert isinstance(expiration_time, datetime.datetime),\
        "[propbundle_BrowserCookie] expiration_time must be of type Datetime."
    if not isinstance(domain_ref, Missing):
        assert (isinstance(domain_ref, case.CoreObject) and (domain_ref.type=='Trace')),\
        "[propbundle_BrowserCookie] domain_ref must be of type Trace."
    if not isinstance(cookie_name, Missing):
        assert isinstance(cookie_name, str),\
        "[propbundle_BrowserCookie] cookie_name must be of type String."
    if not isinstance(cookie_path, Missing):
        assert isinstance(cookie_path, str),\
        "[propbundle_BrowserCookie] cookie_path must be of type String."
    if not isinstance(is_secure, Missing):
        assert isinstance(is_secure, bool),\
        "[propbundle_BrowserCookie] is_secure must be of type Bool."

    return uco_object.create_PropertyBundle('BrowserCookie', AccessedTime=accessed_time,
                                            ApplicationRef=application_ref, CreatedTime=created_time,
                                            ExpirationTime=expiration_time, DomainRef=domain_ref,
                                            CookieName=cookie_name, CookiePath=cookie_path, IsSecure=is_secure)


def propbundle_Build(uco_object, build_information=Missing()):
    '''
    :param BuildInformation: Exactly one occurrence of type BuildInformationType.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(build_information, Missing),\
    "[propbundle_Build] build_information is required."
    if not isinstance(build_information, Missing):
        assert (isinstance(build_information, case.DuckObject) and (build_information.type=='BuildInformationType')),\
        "[propbundle_Build] build_information must be of type BuildInformationType."

    return uco_object.create_PropertyBundle('Build', BuildInformation=build_information)


def propbundle_Calendar(uco_object, application_ref=Missing(), owner=Missing()):
    '''
    :param ApplicationRef: At most one occurrence of type Trace.
    :param Owner: At most one occurrence of type Trace.
    :return: A PropertyBundle object.
    '''

    if not isinstance(application_ref, Missing):
        assert (isinstance(application_ref, case.CoreObject) and (application_ref.type=='Trace')),\
        "[propbundle_Calendar] application_ref must be of type Trace."
    if not isinstance(owner, Missing):
        assert (isinstance(owner, case.CoreObject) and (owner.type=='Trace')),\
        "[propbundle_Calendar] owner must be of type Trace."

    return uco_object.create_PropertyBundle('Calendar', ApplicationRef=application_ref, Owner=owner)


def propbundle_CalendarEntry(uco_object, application_ref=Missing(), attendant_refs=Missing(),
                             categories=Missing(), created_time=Missing(), modified_time=Missing(), duration=Missing(),
                             end_time=Missing(), start_time=Missing(), labels=Missing(), location_ref=Missing(),
                             owner_ref=Missing(), is_private=Missing(), recurrence=Missing(), remind_time=Missing(),
                             event_status=Missing(), subject=Missing(), event_type=Missing()):
    '''
    :param ApplicationRef: At most one occurrence of type Trace.
    :param AttendantRefs: Any number of occurrences of type CoreObject.
    :param Categories: Any number of values of type String.
    :param CreatedTime: At most one value of type Datetime.
    :param ModifiedTime: At most one value of type Datetime.
    :param Duration: At most one value of type Long.
    :param EndTime: At most one value of type Datetime.
    :param StartTime: At most one value of type Datetime.
    :param Labels: Any number of values of type String.
    :param LocationRef: At most one occurrence of type Location.
    :param OwnerRef: At most one occurrence of type Identity (core).
    :param IsPrivate: At most one value of type Bool.
    :param Recurrence: At most one value of type String.
    :param RemindTime: At most one value of type Datetime.
    :param EventStatus: At most one value of type String.
    :param Subject: At most one value of type String.
    :param EventType: At most one value of type String.
    :return: A PropertyBundle object.
    '''

    if not isinstance(application_ref, Missing):
        assert (isinstance(application_ref, case.CoreObject) and (application_ref.type=='Trace')),\
        "[propbundle_CalendarEntry] application_ref must be of type Trace."
    if not isinstance(attendant_refs, Missing):
        assert isinstance(attendant_refs, list),\
        "[propbundle_CalendarEntry] attendant_refs must be of type List of CoreObject."
        assert all(isinstance(i, case.CoreObject) for i in attendant_refs),\
        "[propbundle_CalendarEntry] attendant_refs must be of type List of CoreObject."
    if not isinstance(categories, Missing):
        assert isinstance(categories, list),\
        "[propbundle_CalendarEntry] categories must be of type List of String."
        assert all(isinstance(i, str) for i in categories),\
        "[propbundle_CalendarEntry] categories must be of type List of String."
    if not isinstance(created_time, Missing):
        assert isinstance(created_time, datetime.datetime),\
        "[propbundle_CalendarEntry] created_time must be of type Datetime."
    if not isinstance(modified_time, Missing):
        assert isinstance(modified_time, datetime.datetime),\
        "[propbundle_CalendarEntry] modified_time must be of type Datetime."
    if not isinstance(duration, Missing):
        assert isinstance(duration, datetime.datetime),\
        "[propbundle_CalendarEntry] duration must be of type Datetime."
    if not isinstance(end_time, Missing):
        assert isinstance(end_time, datetime.datetime),\
        "[propbundle_CalendarEntry] end_time must be of type Datetime."
    if not isinstance(start_time, Missing):
        assert isinstance(start_time, datetime.datetime),\
        "[propbundle_CalendarEntry] start_time must be of type Datetime."
    if not isinstance(labels, Missing):
        assert isinstance(labels, list),\
        "[propbundle_CalendarEntry] labels must be of type List of String."
        assert all(isinstance(i, str) for i in labels),\
        "[propbundle_CalendarEntry] labels must be of type List of String."
    if not isinstance(location_ref, Missing):
        assert (isinstance(location_ref, case.CoreObject) and (location_ref.type=='Location')),\
        "[propbundle_CalendarEntry] location_ref must be of type Location."
    if not isinstance(owner_ref, Missing):
        assert (isinstance(owner_ref, case.CoreObject) and (owner_ref.type=='Identity')),\
        "[propbundle_CalendarEntry] owner_ref must be of type Identity."
    if not isinstance(is_private, Missing):
        assert isinstance(is_private, bool),\
        "[propbundle_CalendarEntry] is_private must be of type Bool."
    if not isinstance(recurrence, Missing):
        assert isinstance(recurrence, str),\
        "[propbundle_CalendarEntry] recurrence must be of type String."
    if not isinstance(remind_time, Missing):
        assert isinstance(remind_time, datetime.datetime),\
        "[propbundle_CalendarEntry] remind_time must be of type Datetime."
    if not isinstance(event_status, Missing):
        assert isinstance(event_status, str),\
        "[propbundle_CalendarEntry] event_status must be of type String."
    if not isinstance(subject, Missing):
        assert isinstance(subject, str),\
        "[propbundle_CalendarEntry] subject must be of type String."
    if not isinstance(event_type, Missing):
        assert isinstance(event_type, str),\
        "[propbundle_CalendarEntry] event_type must be of type String."

    return uco_object.create_PropertyBundle('CalendarEntry', ApplicationRef=application_ref,
                                            AttendantRefs=attendant_refs, Categories=categories,
                                            CreatedTime=created_time, ModifiedTime=modified_time,
                                            Duration=duration, EndTime=end_time, StartTime=start_time,
                                            Labels=labels, LocationRef=location_ref, OwnerRef=owner_ref,
                                            IsPrivate=is_private, Recurrence=recurrence, RemindTime=remind_time,
                                            EventStatus=event_status, Subject=subject, EventType=event_type )


def propbundle_CompressedStream(uco_object, compression_method=Missing(), compression_ratio=Missing()):
    '''
    :param CompressionMethod: At most one value of type String.
    :param CompressionRatio: At most one value of type Float.
    :return: A PropertyBundle object.
    '''

    if not isinstance(compression_method, Missing):
        assert isinstance(compression_method, str),\
        "[propbundle_CompressedStream] compression_method must be of type String."
    if not isinstance(compression_ratio, Missing):
        assert isinstance(compression_ratio, float),\
        "[propbundle_CompressedStream] compression_ratio must be of type Float."

    return uco_object.create_PropertyBundle('CompressedStream', CompressionMethod=compression_method,
                                            CompressionRatio=compression_ratio)


def propbundle_ComputerSpecification(uco_object, available_ram=Missing(), bios_date=Missing(),
                                     bios_manufacturer=Missing(), bios_release_date=Missing(),
                                     bios_serial_number=Missing(), bios_version=Missing(),
                                     current_system_date=Missing(), hostname=Missing(),
                                     local_time=Missing(), network_interface_refs=Missing(),
                                     processor_architecture=Missing(), cpu_family=Missing(),
                                     cpu=Missing(), gpu_family=Missing(), gpu=Missing(), system_time=Missing(),
                                     timezone_dst=Missing(), timezone_standard=Missing(), total_ram=Missing(),
                                     uptime=Missing()):
    '''
    :param AvailableRAM: At most one value of type Long.
    :param BIOSDate: At most one value of type Datetime.
    :param BIOSManufacturer: At most one value of type String.
    :param BIOSReleaseDate: At most one value of type Datetime.
    :param BIOSSerialNumber: At most one value of type String.
    :param BIOSVersion: At most one value of type String.
    :param LocalTime: At most one value of type Datetime.
    :param NetworkInterfaceRefs: Any number of occurrences of type Trace.
    :param ProcessorArchitecture: At most one value of type String.
    :param CPUFamily: At most one value of type String.
    :param CPU: At most one value of type String.
    :param GPUFamily: At most one value of type String.
    :param GPU: At most one value of type String.
    :param SystemTime: At most one value of type Datetime.
    :param TimezoneDST: At most one value of type String.
    :param TimezoneStandard: At most one value of type String.
    :param TotalRAM: At most one value of type Long.
    :param Uptime: At most one value of type String.
    :return: A PropertyBundle object.
    '''

    if not isinstance(available_ram, Missing):
        assert isinstance(available_ram, long),\
        "[propbundle_ComputerSpecification] available_ram must be of type Long."
    if not isinstance(bios_date, Missing):
        assert isinstance(bios_date, datetime.datetime),\
        "[propbundle_ComputerSpecification] bios_date must be of type Datetime."
    if not isinstance(bios_manufacturer, Missing):
        assert isinstance(bios_manufacturer, str),\
        "[propbundle_ComputerSpecification] bios_manufacturer must be of type String."
    if not isinstance(bios_release_date, Missing):
        assert isinstance(bios_release_date, datetime.datetime),\
        "[propbundle_ComputerSpecification] bios_release_date must be of type Datetime."
    if not isinstance(bios_serial_number, Missing):
        assert isinstance(bios_serial_number, str),\
        "[propbundle_ComputerSpecification] bios_serial_number must be of type String."
    if not isinstance(bios_version, Missing):
        assert isinstance(bios_version, str),\
        "[propbundle_ComputerSpecification] bios_version must be of type String."
    if not isinstance(local_time, Missing):
        assert isinstance(local_time, datetime.datetime),\
        "[propbundle_ComputerSpecification] local_time must be of type Datetime."
    if not isinstance(network_interface_refs, Missing):
        assert isinstance(network_interface_refs, list),\
        "[propbundle_ComputerSpecification] network_interface_refs must be of type List of Trace."
        assert all( (isinstance(i, case.CoreObject) and i.type=='Trace') for i in network_interface_refs),\
        "[propbundle_ComputerSpecification] network_interface_refs must be of type List of Trace."
    if not isinstance(processor_architecture, Missing):
        assert isinstance(processor_architecture, str),\
        "[propbundle_ComputerSpecification] processor_architecture must be of type String."
    if not isinstance(cpu_family, Missing):
        assert isinstance(cpu_family, str),\
        "[propbundle_ComputerSpecification] cpu_family must be of type String."
    if not isinstance(cpu, Missing):
        assert isinstance(cpu, str),\
        "[propbundle_ComputerSpecification] cpu must be of type String."
    if not isinstance(gpu_family, Missing):
        assert isinstance(gpu_family, str),\
        "[propbundle_ComputerSpecification] gpu_family must be of type String."
    if not isinstance(gpu, Missing):
        assert isinstance(gpu, str),\
        "[propbundle_ComputerSpecification] gpu must be of type String."
    if not isinstance(system_time, Missing):
        assert isinstance(system_time, datetime.datetime),\
        "[propbundle_ComputerSpecification] system_time must be of type Datetime."
    if not isinstance(timezone_dst, Missing):
        assert isinstance(timezone_dst, str),\
        "[propbundle_ComputerSpecification] timezone_dst must be of type String."
    if not isinstance(timezone_standard, Missing):
        assert isinstance(timezone_standard, str),\
        "[propbundle_ComputerSpecification] timezone_standard must be of type String."
    if not isinstance(total_ram, Missing):
        assert isinstance(total_ram, long),\
        "[propbundle_ComputerSpecification] total_ram must be of type Long."
    #TODO:Why is uptime a string? This needs further clarification. Startup time? Or total time to boot?
    if not isinstance(uptime, Missing):
        assert isinstance(uptime, str),\
        "[propbundle_ComputerSpecification] uptime must be of type String."

    return uco_object.create_PropertyBundle('ComputerSpecification', AvailableRAM=available_ram, BIOSDate=bios_date,
                                            BIOSManufacturer=bios_manufacturer, BIOSReleaseDate=bios_release_date,
                                            BIOSSerialNumber=bios_serial_number, BIOSVersion=bios_version,
                                            CurrentSystemDate=current_system_date, Hostname=hostname,
                                            LocalTime=local_time, NetworkInterfaceRefs=network_interface_refs,
                                            ProcessorArchitecture=processor_architecture, CPUFamily=cpu_family,
                                            CPU=cpu, GPUFamily=gpu_family, SystemTime=system_time,
                                            TimezoneDST=timezone_dst, TimezoneStandard=timezone_standard,
                                            TotalRAM=total_ram, Uptime=uptime)


def propbundle_Confidence(uco_object, value=Missing()):
    '''
    :param Value: Exactly one occurrence of type ControlledVocabulary.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(value, Missing),\
    "[propbundle_Confidence] value is required."
    if not isinstance(value, Missing):
        assert (isinstance(value, case.CoreObject) and (value.type=='ControlledVocabulary')),\
        "[propbundle_Confidence] value must be of type ControlledVocabulary."

    return uco_object.create_PropertyBundle('Confidence', Value=value)


def propbundle_Contact(uco_object, application_ref=Missing(), contact_id=Missing(), email_address_refs=Missing(),
                       first_name=Missing(), last_name=Missing(), middle_name=Missing(), contact_name=Missing(),
                       phone_numbers=Missing(), contact_type=Missing(), screen_name=Missing()):
    '''
    :param ApplicationRef: At most one occurrence of type Trace.
    :param ContactID: At most one value of type String.
    :param EmailAddressRefs: Any number of occurrences of type Trace.
    :param FirstName: At most one value of type String.
    :param LastName: At most one value of type String.
    :param MiddleName: At most one value of type String.
    :param ContactName: At most one value of type String.
    :param PhoneNumbers: Any number of values of type String.
    :param ContactType: At most one value of type String.
    :param ScreenName: At most one value of type String.
    :return: A PropertyBundle object.
    '''

    if not isinstance(application_ref, Missing):
        assert (isinstance(application_ref, case.CoreObject) and (application_ref.type=='Trace')),\
        "[propbundle_Contact] application_ref must be of type Trace."
    if not isinstance(contact_id, Missing):
        assert isinstance(contact_id, str),\
        "[propbundle_Contact] contact_id must be of type String."
    if not isinstance(email_address_refs, Missing):
        assert isinstance(email_address_refs, list),\
        "[propbundle_Contact] email_address_refs must be of type List of Trace."
        assert all( (isinstance(i, case.CoreObject) and i.type=='Trace') for i in email_address_refs),\
        "[propbundle_Contact] email_address_refs must be of type List of Trace."
    if not isinstance(first_name, Missing):
        assert isinstance(first_name, str),\
        "[propbundle_Contact] first_name must be of type String."
    if not isinstance(last_name, Missing):
        assert isinstance(last_name, str),\
        "[propbundle_Contact] last_name must be of type String."
    if not isinstance(middle_name, Missing):
        assert isinstance(middle_name, str),\
        "[propbundle_Contact] middle_name must be of type String."
    if not isinstance(contact_name, Missing):
        assert isinstance(contact_name, str),\
        "[propbundle_Contact] contact_name must be of type String."
    if not isinstance(phone_numbers, Missing):
        assert isinstance(phone_numbers, list),\
        "[propbundle_Contact] phone_numbers must be of type List of String."
        assert all(isinstance(i, str) for i in phone_numbers),\
        "[propbundle_Contact] phone_numbers must be of type List of String."
    if not isinstance(contact_type, Missing):
        assert isinstance(contact_type, str),\
        "[propbundle_Contact] contact_type must be of type String."
    if not isinstance(screen_name, Missing):
        assert isinstance(screen_name, str),\
        "[propbundle_Contact] screen_name must be of type String."

    return uco_object.create_PropertyBundle('Contact', ApplicationRef=application_ref, ContactID=contact_id,
                                            EmailAddressRefs=email_address_refs, FirstName=first_name,
                                            LastName=last_name, MiddleName=middle_name, ContactName=contact_name,
                                            PhoneNumbers=phone_numbers, ContactType=contact_type,
                                            ScreenName=screen_name)


def propbundle_ContentData(uco_object, byte_order=Missing(), mime_class=Missing(), mime_type=Missing(),
                           magic_number=Missing(), size_in_bytes=Missing(), data_payload=Missing(),
                           data_payload_ref_url=Missing(), entropy=Missing(), hashes=Missing(),
                           is_encrypted=Missing()):
    '''
    :param ByteOrder: At most one occurrence of type ControlledVocabulary.
    :param MIMEClass: At most one value of type String.
    :param MIMEType: At most one value of type String.
    :param MagicNumber: At most one value of type String.
    :param SizeInBytes: At most one value of type Long.
    :param DataPayload: At most one value of type String.
    :param DataPayloadRefURL: At most one occurrence of type Trace.
    :param Entropy: At most one value of type Float.
    :param Hashes: Any number of occurrences of type Hash.
    :param IsEncrypted: At most one value of type Bool.
    :return: A PropertyBundle object.
    '''

    if not isinstance(byte_order, Missing):
        assert (isinstance(byte_order, case.CoreObject) and (byte_order.type=='ControlledVocabulary')),\
        "[propbundle_ContentData] byte_order must be of type ControlledVocabulary."
    if not isinstance(mime_class, Missing):
        assert isinstance(mime_class, str),\
        "[propbundle_ContentData] mime_class must be of type String."
    if not isinstance(mime_type, Missing):
        assert isinstance(mime_type, str),\
        "[propbundle_ContentData] mime_type must be of type String."
    if not isinstance(magic_number, Missing):
        assert isinstance(magic_number, str),\
        "[propbundle_ContentData] magic_number must be of type String."
    if not isinstance(size_in_bytes, Missing):
        assert isinstance(size_in_bytes, long),\
        "[propbundle_ContentData] size_in_bytes must be of type Long."
    if not isinstance(data_payload, Missing):
        assert isinstance(data_payload, str),\
        "[propbundle_ContentData] data_payload must be of type String."
    if not isinstance(data_payload_ref_url, Missing):
        assert (isinstance(data_payload_ref_url, case.CoreObject) and (data_payload_ref_url.type=='Trace')),\
        "[propbundle_ContentData] data_payload_ref_url must be of type Trace."
    if not isinstance(entropy, Missing):
        assert isinstance(entropy, float),\
        "[propbundle_ContentData] entropy must be of type Float."
    if not isinstance(hashes, Missing):
        assert isinstance(hashes, list),\
        "[propbundle_ContentData] hashes must be of type List of Hash."
        assert all( (isinstance(i, case.DuckObject) and i.type=='Hash') for i in hashes),\
        "[propbundle_ContentData] hashes must be of type List of Hash."
    if not isinstance(is_encrypted, Missing):
        assert isinstance(is_encrypted, bool),\
        "[propbundle_ContentData] is_encrypted must be of type Bool."

    return uco_object.create_PropertyBundle('ContentData', ByteOrder=byte_order, MIMEClass=mime_class,
                                            MIMEType=mime_type, MagicNumber=magic_number, SizeInBytes=size_in_bytes,
                                            DataPayload=data_payload, DataPayloadRefURL=data_payload_ref_url,
                                            Entropy=entropy, Hashes=hashes, IsEncrypted=is_encrypted)


def propbundle_Device(uco_object, device_type=Missing(), manufacturer=Missing(), model=Missing(),
                      serial_number=Missing()):
    '''
    :param DeviceType: At most one occurrence of type ControlledVocabulary.
    :param Manufacturer: At most one value of type String.
    :param Model: At most one value of type String.
    :param SerialNumber: At most one value of type String.
    :return: A PropertyBundle object.
    '''

    if not isinstance(device_type, Missing):
        assert (isinstance(device_type, case.CoreObject) and (device_type.type=='ControlledVocabulary')),\
        "[propbundle_Device] device_type must be of type ControlledVocabulary."
    if not isinstance(manufacturer, Missing):
        assert isinstance(manufacturer, str),\
        "[propbundle_Device] manufacturer must be of type String."
    if not isinstance(model, Missing):
        assert isinstance(model, str),\
        "[propbundle_Device] model must be of type String."
    if not isinstance(serial_number, Missing):
        assert isinstance(serial_number, str),\
        "[propbundle_Device] serial_number must be of type String."

    return uco_object.create_PropertyBundle('Device', DeviceType=device_type, Manufacturer=manufacturer, Model=model,
                                            SerialNumber=serial_number)


def propbundle_DigitalAccount(uco_object, account_login=Missing(), first_login_time=Missing(),
                              last_login_time=Missing(), is_disabled=Missing(), display_name=Missing()):
    '''
    :param AccountLogin: Any number of values of type String.
    :param FirstLoginTime: At most one value of type Datetime.
    :param LastLoginTime: At most one value of type Datetime.
    :param IsDisabled: At most one value of type Bool.
    :param DisplayName: At most one value of type String.
    :return: A PropertyBundle object.
    '''

    if not isinstance(account_login, Missing):
        assert isinstance(account_login, list),\
        "[propbundle_DigitalAccount] account_login must be of type List of String."
        assert all(isinstance(i, str) for i in account_login),\
        "[propbundle_DigitalAccount] account_login must be of type List of String."
    if not isinstance(first_login_time, Missing):
        assert isinstance(first_login_time, datetime.datetime),\
        "[propbundle_DigitalAccount] first_login_time must be of type Datetime."
    if not isinstance(last_login_time, Missing):
        assert isinstance(last_login_time, datetime.datetime),\
        "[propbundle_DigitalAccount] last_login_time must be of type Datetime."
    if not isinstance(is_disabled, Missing):
        assert isinstance(is_disabled, bool),\
        "[propbundle_DigitalAccount] is_disabled must be of type Bool."
    if not isinstance(display_name, Missing):
        assert isinstance(display_name, str),\
        "[propbundle_DigitalAccount] display_name must be of type String."

    return uco_object.create_PropertyBundle('DigitalAccount', AccountLogin=account_login,
                                            FirstLoginTime=first_login_time, LastLoginTime=last_login_time,
                                            IsDisabled=is_disabled, DisplayName=display_name)


def propbundle_DigitalSignatureInfo(uco_object, signature_exists=Missing(), signature_verified=Missing(),
                                    certificate_issuer=Missing(), certificate_subject=Missing(),
                                    signature_description=Missing()):
    '''
    :param SignatureExists: Exactly one value of type Bool.
    :param SignatureVerified: Exactly one value of type Bool.
    :param CertificateIssuer: At most one occurrence of type Identity (core).
    :param CertificateSubject: At most one occurrence of type Identity (core).
    :param SignatureDescription: At most one value of type String.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(signature_exists, Missing),\
    "[propbundle_DigitalSignature] signature_exists is required."
    if not isinstance(signature_exists, Missing):
        assert isinstance(signature_exists, bool),\
        "[propbundle_DigitalSignature] signature_exists must be of type Bool."

    if not isinstance(signature_verified, Missing):
        assert isinstance(signature_verified, bool),\
        "[propbundle_DigitalSignature] signature_verified must be of type Bool."
    if not isinstance(certificate_issuer, Missing):
        assert (isinstance(certificate_issuer, case.CoreObject) and (certificate_issuer.type=='Identity')),\
        "[propbundle_DigitalSignature] certificate_issuer must be of type Identity."
    if not isinstance(certificate_subject, Missing):
        assert (isinstance(certificate_subject, case.CoreObject) and (certificate_subject.type=='Identity')),\
        "[propbundle_DigitalSignature] certificate_subject must be of type Identity."
    if not isinstance(signature_description, Missing):
        assert isinstance(signature_description, str),\
        "[propbundle_DigitalSignature] signature_description must be of type String."

    return uco_object.create_PropertyBundle('DigitalSignatureInfo', SignatureExists=signature_exists,
                                            SignatureVerified=signature_verified, CertificateIssuer=certificate_issuer,
                                            CertificateSubject=certificate_subject,
                                            SignatureDescription=signature_description)


def propbundle_Disk(uco_object, disk_size=Missing(), disk_type=Missing(), free_space=Missing(),
                    partition_refs=Missing()):
    '''
    :param DiskSize: At most one value of type Long.
    :param DiskType: At most one occurrence of type ControlledVocabulary.
    :param FreeSpace: At most one value of type Long.
    :param PartitionRefs: Any number of occurrences of type Trace.
    :return: A PropertyBundle object.
    '''

    if not isinstance(disk_size, Missing):
        assert isinstance(disk_size, long),\
        "[propbundle_Disk] disk_size must be of type Long."
    if not isinstance(disk_type, Missing):
        assert (isinstance(disk_type, case.DuckObject) and (disk_type.type=='ControlledDictionary')),\
        "[propbundle_Disk] disk_type must be of type ControlledDictionary."
    if not isinstance(free_space, Missing):
        assert isinstance(free_space, long),\
        "[propbundle_Disk] free_space must be of type Long."
    if not isinstance(partition_refs, Missing):
        assert (isinstance(partition_refs, case.CoreObject) and (partition_refs.type=='Trace')),\
        "[propbundle_Disk] partition_refs must be of type Trace."

    return uco_object.create_PropertyBundle('Disk', DiskSize=disk_size, DiskType=disk_type,
                                            FreeSpace=free_space, PartitionRefs=partition_refs)


def propbundle_DiskPartition(uco_object, mount_point=Missing(), partition_id=Missing(), partition_length=Missing(),
                             partition_offset=Missing(), space_left=Missing(), space_used=Missing(),
                             total_space=Missing(), disk_partition_type=Missing(), created_time=Missing()):
    '''
    :param MountPoint: At most one value of type String.
    :param PartitionID: At most one value of type Integer.
    :param PartitionLength: At most one value of type Long.
    :param PartitionOffset: At most one value of type Long.
    :param SpaceLeft: At most one value of type Long.
    :param SpaceUsed: At most one value of type Long.
    :param TotalSpace: At most one value of type Long.
    :param DiskPartitionType: At most one occurrence of type ControlledVocabulary.
    :param CreatedTime: At most one value of type Datetime.
    :return: A PropertyBundle object.
    '''

    if not isinstance(mount_point, Missing):
        assert isinstance(mount_point, str),\
        "[propbundle_DiskPartition] mount_point must be of type String."
    if not isinstance(partition_id, Missing):
        assert isinstance(partition_id, int),\
        "[propbundle_DiskPartition] partition_id must be of type Integer."
    if not isinstance(partition_length, Missing):
        assert isinstance(partition_length, long),\
        "[propbundle_DiskPartition] partition_length must be of type Long."
    if not isinstance(partition_offset, Missing):
        assert isinstance(partition_offset, long),\
        "[propbundle_DiskPartition] partition_offset must be of type Long."
    if not isinstance(space_left, Missing):
        assert isinstance(space_left, long),\
        "[propbundle_DiskPartition] space_left must be of type Long."
    if not isinstance(space_used, Missing):
        assert isinstance(space_used, long),\
        "[propbundle_DiskPartition] space_used must be of type Long."
    if not isinstance(total_space, Missing):
        assert isinstance(total_space, long),\
        "[propbundle_DiskPartition] total_space must be of type Long."
    if not isinstance(disk_partition_type, Missing):
        assert (isinstance(disk_partition_type, case.DuckObject) and
                (disk_partition_type.type=='ControlledDictionary')),\
                "[propbundle_DiskPartition] email_address_ref must be of type ControlledDictionary."
    if not isinstance(created_time, Missing):
        assert isinstance(created_time, datetime.datetime),\
        "[propbundle_DiskPartition] created_time must be of type Datetime."

    return uco_object.create_PropertyBundle('DiskPartition', MountPoint=mount_point, PartitionID=partition_id,
                                            PartitionLength=partition_length, PartitionOffset=partition_offset,
                                            SpaceLeft=space_left, SpaceUsed=space_used, TotalSpace=total_space,
                                            DiskPartitionType=disk_partition_type, CreatedTime=created_time)


def propbundle_DomainName(uco_object, value=Missing(), is_tld=Missing()):
    '''
    :param Value: Exactly one value of type String.
    :param IsTLD: At most one value of type Bool.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(value, Missing),\
    "[propbundle_DomainName] value is required."
    if not isinstance(value, Missing):
        assert isinstance(value, str),\
        "[propbundle_DomainName] value must be of type String."

    if not isinstance(is_tld, Missing):
        assert isinstance(is_tld, bool),\
        "[propbundle_DomainName] is_tld must be of type Bool."

    return uco_object.create_PropertyBundle('DomainName', Value=value, IsTLD=is_tld)


def propbundle_EmailAccount(uco_object, email_address_ref=Missing()):
    '''
    :param EmailAddressRef: Exactly one occurrence of type Trace.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(email_address_ref, Missing),\
    "[propbundle_EmailAccount] email_address_ref is required."
    if not isinstance(email_address_ref, Missing):
        assert (isinstance(email_address_ref, case.CoreObject) and (email_address_ref.type=='Trace')),\
        "[propbundle_EmailAccount] email_address_ref must be of type Trace."

    return uco_object.create_PropertyBundle('EmailAccount', EmailAddressRef=email_address_ref)


def propbundle_EmailAddress(uco_object, value=Missing(), display_name=Missing()):
    '''
    :param Value: Exactly one value of type String.
    :param DisplayName: At most one value of type String.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(value, Missing),\
    "[propbundle_EmailAddress] value is required."
    if not isinstance(value, Missing):
        assert isinstance(value, str),\
        "[propbundle_EmailAddress] value must be of type String."

    if not isinstance(display_name, Missing):
        assert isinstance(display_name, str),\
        "[propbundle_EmailAddress] display_name must be of type String."

    return uco_object.create_PropertyBundle('EmailAddress', Value=value, DisplayName=display_name)


def propbundle_EmailMessage(uco_object, is_mime_encoded=Missing(), is_multipart=Missing(),
                            application_ref=Missing(), bcc_refs=Missing(), cc_refs=Missing(), body=Missing(),
                            body_multipart=Missing(), body_raw_ref=Missing(), categories=Missing(),
                            content_disposition=Missing(), content_type=Missing(), from_ref=Missing(),
                            to_refs=Missing(), header_raw_ref=Missing(), in_reply_to_refs=Missing(), is_read=Missing(),
                            labels=Missing(), message_id_ref=Missing(), modified_time=Missing(),
                            other_headers=Missing(), priority=Missing(), received_lines=Missing(),
                            received_time=Missing(), references=Missing(), sender_ref=Missing(),
                            sent_time=Missing(), subject=Missing(), x_mailer=Missing(), x_originating_ip=Missing()):
    '''
    :param IsMIMEEncoded: Exactly one value of type Bool.
    :param IsMultipart: Exactly one value of type Bool.
    :param ApplicationRef: At most one occurrence of type Trace.
    :param BCCRefs: Any number of occurrences of type Trace.
    :param CCRefs: Any number of occurrences of type Trace.
    :param Body: At most one value of type String.
    :param BodyMultipart: Any number of occurrences of type MIMEPartType.
    :param BodyRawRef: At most one occurrence of type Trace.
    :param Categories: Any number of values of type String.
    :param ContentDisposition: At most one value of type String.
    :param ContentType: At most one value of type String.
    :param FromRef: At most one occurrence of type Trace.
    :param ToRefs: Any number of occurrences of type Trace.
    :param HeaderRawRef: At most one occurrence of type Trace.
    :param InReplyToRefs: At most one occurrence of type Trace.
    :param IsRead: At most one value of type Bool.
    :param Labels: Any number of values of type String.
    :param MessageIDRef: At most one occurrence of type Trace.
    :param ModifiedTime: At most one value of type Datetime.
    :param OtherHeaders: At most one occurrence of type Dictionary.
    :param Priority: At most one value of type String.
    :param ReceivedLines: Any number of values of type String.
    :param ReceivedTime: At most one value of type Datetime.
    :param References: Any number of occurrences of type Trace.
    :param SenderRef: At most one occurrence of type Trace.
    :param SentTime: At most one value of type Datetime.
    :param Subject: At most one value of type String.
    :param xMailer: At most one value of type String.
    :param xOriginatingIP: At most one occurrence of type Trace.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(is_mime_encoded, Missing),\
    "[propbundle_EmailMessage] is_mime_encoded is required."
    if not isinstance(is_mime_encoded, Missing):
        assert isinstance(is_mime_encoded, bool),\
        "[propbundle_EmailMessage] is_mime_encoded must be of type Bool."
    assert not isinstance(is_multipart, Missing),\
    "[propbundle_EmailMessage] is_multipart is required."
    if not isinstance(is_multipart, Missing):
        assert isinstance(is_multipart, bool),\
        "[propbundle_EmailMessage] is_multipart must be of type Bool."

    if not isinstance(application_ref, Missing):
        assert (isinstance(application_ref, case.CoreObject) and (application_ref.type=='Trace')),\
        "[propbundle_EmailMessage] application_ref must be of type Trace."
    if not isinstance(bcc_refs, Missing):
        assert isinstance(bcc_refs, list),\
        "[propbundle_EmailMessage] bcc_refs must be of type List of Trace."
        assert all( (isinstance(i, case.CoreObject) and i.type=='Trace') for i in bcc_refs),\
        "[propbundle_EmailMessage] bcc_refs must be of type List of Trace."
    if not isinstance(cc_refs, Missing):
        assert isinstance(cc_refs, list),\
        "[propbundle_EmailMessage] cc_refs must be of type List of Trace."
        assert all( (isinstance(i, case.CoreObject) and i.type=='Trace') for i in cc_refs),\
        "[propbundle_EmailMessage] cc_refs must be of type List of Trace."
    if not isinstance(body, Missing):
        assert isinstance(body, str),\
        "[propbundle_EmailMessage] body must be of type String."
    if not isinstance(body_multipart, Missing):
        assert isinstance(body_multipart, list),\
        "[propbundle_EmailMessage] body_multipart must be of type List of MIMEPartType."
        assert all( (isinstance(i, case.DuckObject) and i.type=='MIMEPartType') for i in body_multipart),\
        "[propbundle_EmailMessage] body_multipart must be of type List of MIMEPartType."
    if not isinstance(body_raw_ref, Missing):
        assert (isinstance(body_raw_ref, case.CoreObject) and (body_raw_ref.type=='Trace')),\
        "[propbundle_EmailMessage] body_raw_ref must be of type Trace."
    if not isinstance(categories, Missing):
        assert isinstance(categories, list),\
        "[propbundle_EmailMessage] categories must be of type List of String."
        assert all(isinstance(i, str) for i in categories),\
        "[propbundle_EmailMessage] categories must be of type List of String."
    if not isinstance(content_disposition, Missing):
        assert isinstance(content_disposition, str),\
        "[propbundle_EmailMessage] content_disposition must be of type String."
    if not isinstance(content_type, Missing):
        assert isinstance(content_type, str),\
        "[propbundle_EmailMessage] content_type must be of type String."
    if not isinstance(from_ref, Missing):
        assert (isinstance(from_ref, case.CoreObject) and (from_ref.type=='Trace')),\
        "[propbundle_EmailMessage] from_ref must be of type Trace."
    if not isinstance(to_refs, Missing):
        assert isinstance(to_refs, list),\
        "[propbundle_EmailMessage] to_refs must be of type List of Trace."
        assert all( (isinstance(i, case.CoreObject) and i.type=='Trace') for i in to_refs),\
        "[propbundle_EmailMessage] to_refs must be of type List of Trace."
    if not isinstance(header_raw_ref, Missing):
        assert (isinstance(header_raw_ref, case.CoreObject) and (header_raw_ref.type=='Trace')),\
        "[propbundle_EmailMessage] header_raw_ref must be of type Trace."
    if not isinstance(in_reply_to_refs, Missing):
        assert (isinstance(in_reply_to_refs, case.CoreObject) and (in_reply_to_refs.type=='Trace')),\
        "[propbundle_EmailMessage] in_reply_to_refs must be of type Trace."
    if not isinstance(is_read, Missing):
        assert isinstance(is_read, bool),\
        "[propbundle_EmailMessage] is_read must be of type Bool."
    if not isinstance(labels, Missing):
        assert isinstance(labels, list),\
        "[propbundle_EmailMessage] labels must be of type List of String."
        assert all(isinstance(i, str) for i in labels),\
        "[propbundle_EmailMessage] labels must be of type List of String."
    if not isinstance(message_id_ref, Missing):
        assert (isinstance(message_id_ref, case.CoreObject) and (message_id_ref.type=='Trace')),\
        "[propbundle_EmailMessage] message_id_ref must be of type Trace."
    if not isinstance(modified_time, Missing):
        assert isinstance(modified_time, datetime.datetime),\
        "[propbundle_EmailMessage] modified_time must be of type Datetime."
    if not isinstance(other_headers, Missing):
        assert (isinstance(other_headers, case.DuckObject) and (other_headers.type=='Dictionary')),\
        "[propbundle_EmailMessage] other_headers must be of type Dictionary."
    if not isinstance(priority, Missing):
        assert isinstance(priority, str),\
        "[propbundle_EmailMessage] priority must be of type String."
    if not isinstance(received_lines, Missing):
        assert isinstance(received_lines, list),\
        "[propbundle_EmailMessage] received_lines must be of type List of String."
        assert all(isinstance(i, str) for i in received_lines),\
        "[propbundle_EmailMessage] received_lines must be of type List of String."
    if not isinstance(received_time, Missing):
        assert isinstance(received_time, datetime.datetime),\
        "[propbundle_EmailMessage] received_time must be of type Datetime."
    if not isinstance(references, Missing):
        assert isinstance(references, list),\
        "[propbundle_EmailMessage] references must be of type List of Trace."
        assert all( (isinstance(i, case.CoreObject) and i.type=='Trace') for i in references),\
        "[propbundle_EmailMessage] references must be of type List of Trace."
    if not isinstance(sender_ref, Missing):
        assert (isinstance(sender_ref, case.CoreObject) and (sender_ref.type=='Trace')),\
        "[propbundle_EmailMessage] sender_ref must be of type Trace."
    if not isinstance(sent_time, Missing):
        assert isinstance(sent_time, datetime.datetime),\
        "[propbundle_EmailMessage] sent_time must be of type Datetime."
    if not isinstance(subject, Missing):
        assert isinstance(subject, str),\
        "[propbundle_EmailMessage] subject must be of type String."
    if not isinstance(x_mailer, Missing):
        assert isinstance(x_mailer, str),\
        "[propbundle_EmailMessage] x_mailer must be of type String."
    if not isinstance(x_originating_ip, Missing):
        assert (isinstance(x_originating_ip, case.CoreObject) and (x_originating_ip.type=='Trace')),\
        "[propbundle_EmailMessage] x_originating_ip must be of type Trace."

    return uco_object.create_PropertyBundle('EmailMessage', IsMIMEEncoded=is_mime_encoded,
                                            IsMultipart=is_multipart, ApplicationRef=application_ref, BCCRefs=bcc_refs,
                                            CCRefs=cc_refs, Body=body, BodyMultipart=body_multipart,
                                            BodyRawRef=body_raw_ref, Categories=categories,
                                            ContentDisposition=content_disposition, ContentType=content_type,
                                            FromRef=from_ref, ToRefs=to_refs, HeaderRawRef=header_raw_ref,
                                            InReplyToRefs=in_reply_to_refs, IsRead=is_read, Labels=labels,
                                            MessageIDRef=message_id_ref, ModifiedTime=modified_time,
                                            OtherHeaders=other_headers, Priority=priority,
                                            ReceivedLines=received_lines, ReceivedTime=received_time,
                                            References=references, SenderRef=sender_ref, SentTime=sent_time,
                                            Subject=subject, xMailer=x_mailer, xOriginatingIP=x_originating_ip)


def propbundle_EncodedStream(uco_object, encoding_method=Missing()):
    '''
    :param EncodingMethod: Exactly one value of type String.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(encoding_method, Missing),\
    "[propbundle_EncodedStream] encoding_method is required."
    if not isinstance(encoding_method, Missing):
        assert isinstance(encoding_method, str),\
        "[propbundle_EncodedStream] encoding_method must be of type String."

    return uco_object.create_PropertyBundle('EncodedStream', EncodingMethod=encoding_method)


def propbundle_EncryptedStream(uco_object, encryption_iv=Missing(), encryption_key=Missing(),
                               encryption_method=Missing(), encryption_mode=Missing()):
    '''
    :param EncryptionIV: At most one value of type HexBinary.
    :param EncryptionKey: At most one value of type HexBinary.
    :param EncryptionMethod: At most one occurrence of type ControlledVocabulary.
    :param EncryptionMode: At most one occurrence of type ControlledVocabulary.
    :return: A PropertyBundle object.
    '''

    #TODO:HexBinary
    #TODO:HexBinary
    if not isinstance(encryption_method, Missing):
        assert (isinstance(encryption_method, case.CoreObject) and (encryption_method.type=='ControlledVocabulary')),\
        "[propbundle_EncryptedStream] encryption_method must be of type ControlledVocabulary."
    if not isinstance(encryption_mode, Missing):
        assert (isinstance(encryption_mode, case.CoreObject) and (encryption_mode.type=='ControlledVocabulary')),\
        "[propbundle_EncryptedStream] encryption_mode must be of type ControlledVocabulary."

    return uco_object.create_PropertyBundle('EncryptedStream', EncryptionIV=encryption_iv,
                                            EncryptionKey=encryption_key, EncryptionMethod=encryption_method,
                                            EncryptionMode=encryption_mode)


def propbundle_EnvironmentVariable(uco_object, name=Missing(), value=Missing()):
    '''
    :param Name: Exactly one value of any type.
    :param Value: At most one value of any type.
    :return: A PropertyBundle object.
    '''

    #TODO:NothingElseToCheck

    return uco_object.create_PropertyBundle('EnvironmentVariable', Name=name, Value=value)


def propbundle_Event(uco_object, application_ref=Missing(), cyber_action_ref=Missing(), categories=Missing(),
                     computer_name=Missing(), created_time=Missing(), event_id=Missing(), event_text=Missing(),
                     event_type=Missing()):
    '''
    :param ApplicationRef: Exactly one occurrence of type Trace.
    :param CyberActionRef: At most one occurrence of type CyberAction.
    :param Categories: Any number of values of type String.
    :param ComputerName: At most one value of type String.
    :param CreatedTime: At most one value type Datetime.
    :param EventID: At most one value of type String.
    :param EventText: At most one value of type String.
    :param EventType: At most one value of type String.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(application_ref, Missing),\
    "[propbundle_Event] application_ref is required."
    if not isinstance(application_ref, Missing):
        assert (isinstance(application_ref, case.CoreObject) and (application_ref.type=='Trace')),\
        "[propbundle_Event] application_ref must be of type Trace."

    #TODO:CyberAction
    if not isinstance(categories, Missing):
        assert isinstance(categories, list),\
        "[propbundle_Event] categories must be of type List of String."
        assert all(isinstance(i, str) for i in categories),\
        "[propbundle_Event] categories must be of type List of String."
    if not isinstance(computer_name, Missing):
        assert isinstance(computer_name, str),\
        "[propbundle_Event] computer_name must be of type String."
    if not isinstance(created_time, Missing):
        assert isinstance(created_time, datetime.datetime),\
        "[propbundle_Event] created_time must be of type Datetime."
    if not isinstance(event_id, Missing):
        assert isinstance(event_id, str),\
        "[propbundle_Event] event_id must be of type String."
    if not isinstance(event_text, Missing):
        assert isinstance(event_text, str),\
        "[propbundle_Event] event_text must be of type String."
    if not isinstance(event_type, Missing):
        assert isinstance(event_type, str),\
        "[propbundle_Event] event_type must be of type String."

    return uco_object.create_PropertyBundle('Event', ApplicationRef=application_ref, CyberActionRef=cyber_action_ref,
                                            Categories=categories, ComputerName=computer_name, CreatedTime=created_time,
                                            EventID=event_id, EventText=event_text, EventType=event_type)


def propbundle_EXIF(uco_object, exif_data=Missing()):
    '''
    :param EXIFData: At least one occurrence of type ControlledDictionary.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(exif_data, Missing),\
    "[propbundle_EXIF] exif_data is required."
    if not isinstance(exif_data, Missing):
        assert isinstance(exif_data, list),\
        "[propbundle_EXIF] exif_data must be of type List of ControlledDictionary."
        assert all( (isinstance(i, case.DuckObject) and i.type=='ControlledDictionary') for i in exif_data),\
        "[propbundle_EXIF] exif_data must be of type List of ControlledDictionary."
        
    return uco_object.create_PropertyBundle('EXIF', EXIFData=exif_data)


def propbundle_ExtInode(uco_object, inode_id=Missing(), file_type=Missing(), deletion_time=Missing(),
                        inode_change_time=Missing(), permissions=Missing(), sgid=Missing(), suid=Missing(),
                        flags=Missing(), hard_link_count=Missing()):
    '''
    :param InodeID: At most one value of type Integer.
    :param FileType: At most one value of type Integer.
    :param DeletionTime: At most one value of type Datetime.
    :param InodeChangeTime: At most one value of type Datetime.
    :param Permissions: At most one value of type Integer.
    :param SGID: At most one value of type Integer.
    :param SUID: At most one value of type Integer.
    :param Flags: At most one value of type Integer.
    :param HardLinkCount: At most one value of type Integer.
    :return: A PropertyBundle object.
    '''

    if not isinstance(inode_id, Missing):
        assert isinstance(inode_id, int),\
        "[propbundle_ExtInode] inode_id must be of type Integer."
    if not isinstance(file_type, Missing):
        assert isinstance(file_type, int),\
        "[propbundle_ExtInode] file_type must be of type Integer."
    if not isinstance(deletion_time, Missing):
        assert isinstance(deletion_time, datetime.datetime),\
        "[propbundle_ExtInode] deletion_time must be of type Datetime."
    if not isinstance(inode_change_time, Missing):
        assert isinstance(inode_change_time, datetime.datetime),\
        "[propbundle_ExtInode] inode_change_time must be of type Datetime."
    if not isinstance(permissions, Missing):
        assert isinstance(permissions, int),\
        "[propbundle_ExtInode] permissions must be of type Integer."
    if not isinstance(sgid, Missing):
        assert isinstance(sgid, int),\
        "[propbundle_ExtInode] sgid must be of type Integer."
    if not isinstance(suid, Missing):
        assert isinstance(suid, int),\
        "[propbundle_ExtInode] suid must be of type Integer."
    if not isinstance(flags, Missing):
        assert isinstance(flags, int),\
        "[propbundle_ExtInode] flags must be of type Integer."
    if not isinstance(hard_link_count, Missing):
        assert isinstance(hard_link_count, int),\
        "[propbundle_ExtInode] hard_link_count must be of type Integer."

    return uco_object.create_PropertyBundle('ExtInode', InodeID=inode_id, FileType=file_type,
                                            DeletionTime=deletion_time, InodeChangeTime=inode_change_time,
                                            Permissions=permissions, SGID=sgid, SUID=suid, Flags=flags,
                                            HardLinkCount=hard_link_count)


def propbundle_ExtractedStrings(uco_object, strings=Missing()):
    '''
    :param Strings: At least one occurrence of type String.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(strings, Missing),\
    "[propbundle_ExtractedStrings] strings is required."
    if not isinstance(strings, Missing):
        assert isinstance(strings, list),\
        "[propbundle_ExtractedStrings] strings must be of type List of String."
        assert all(isinstance(i, str) for i in strings),\
        "[propbundle_ExtractedStrings] strings must be of type List of String."

    return uco_object.create_PropertyBundle('ExtInode', Strings=strings)


def propbundle_File(uco_object, is_directory=Missing(), filename=Missing(), filepath=Missing(),
                    filesystem_type=Missing(), created_time=Missing(), modified_time=Missing(),
                    accessed_time=Missing(), metadata_change_time=Missing(), extension=Missing(),
                    size_in_bytes=Missing()):
    '''
    :param IsDirectory: Any number of values of type Bool.
    :param Filename: Any number of values of type String.
    :param Filepath: Any number of values of type String.
    :param FilesystemType: At most one occurrence of type ControlledVocabulary.
    :param CreatedTime: At most one value of type Datetime.
    :param ModifiedTime: At most one value of type Datetime.
    :param AccessedTime: At most one value of type Datetime.
    :param MetadataChangeTime: At most one value of type Datetime.
    :param Extension: At most one value of type String.
    :param SizeInBytes: At most one value of type Integer.
    :return: A PropertyBundle object.
    '''

    if not isinstance(is_directory, Missing):
        assert isinstance(is_directory, list),\
        "[propbundle_File] is_directory must be of type List of Bool."
        assert all(isinstance(i, bool) for i in is_directory),\
        "[propbundle_File] is_directory must be of type List of Bool."
    if not isinstance(filename, Missing):
        assert isinstance(filename, list),\
        "[propbundle_File] filename must be of type List of String."
        assert all(isinstance(i, str) for i in filename),\
        "[propbundle_File] filename must be of type List of String."
    if not isinstance(filesystem_type, Missing):
        assert (isinstance(filesystem_type, case.CoreObject) and (filesystem_type.type=='ControlledVocabulary')),\
        "[propbundle_File] filesystem_type must be of type ControlledVocabulary."
    if not isinstance(created_time, Missing):
        assert isinstance(created_time, datetime.datetime),\
        "[propbundle_File] created_time must be of type Datetime."
    if not isinstance(modified_time, Missing):
        assert isinstance(modified_time, datetime.datetime),\
        "[propbundle_File] modified_time must be of type Datetime."
    if not isinstance(accessed_time, Missing):
        assert isinstance(accessed_time, datetime.datetime),\
        "[propbundle_File] accessed_time must be of type Datetime."
    if not isinstance(metadata_change_time, Missing):
        assert isinstance(metadata_change_time, datetime.datetime),\
        "[propbundle_File] metadata_change_time must be of type Datetime."
    if not isinstance(extension, Missing):
        assert isinstance(extension, str),\
        "[propbundle_File] extension must be of type String."
    if not isinstance(size_in_bytes, Missing):
        assert isinstance(size_in_bytes, int),\
        "[propbundle_File] size_in_bytes must be of type Integer."

    return uco_object.create_PropertyBundle('File', IsDirectory=is_directory, Filename=filename, Filepath=filepath,
                                            FilesystemType=filesystem_type, CreatedTime=created_time,
                                            ModifiedTime=modified_time, AccessedTime=accessed_time,
                                            MetadataChangeTime=metadata_change_time, Extension=extension,
                                            SizeInBytes=size_in_bytes)


def propbundle_FilePermissions(uco_object, owner_ref=Missing()):
    '''
    :param OwnerRef: Exactly one occurrence of type Trace.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(owner_ref, Missing),\
    "[propbundle_FilePermissions] owner_ref is required."
    if not isinstance(owner_ref, Missing):
        assert (isinstance(owner_ref, case.CoreObject) and (owner_ref.type=='Trace')),\
        "[propbundle_FilePermissions] owner_ref must be of type Trace."

    return uco_object.create_PropertyBundle('FilePermissions', OwnerRef=owner_ref)


def propbundle_Filesystem(uco_object, filesystem_type=Missing(), cluster_size=Missing()):
    '''
    :param FilesystemType: At most one occurrence of type ControlledVocabulary.
    :param ClusterSize: At most one value of type Integer.
    :return: A PropertyBundle object.
    '''

    if not isinstance(filesystem_type, Missing):
        assert (isinstance(filesystem_type, case.CoreObject) and (filesystem_type.type=='ControlledVocabulary')),\
        "[propbundle_Filesystem] filesystem_type must be of type ControlledVocabulary."
    if not isinstance(cluster_size, Missing):
        assert isinstance(cluster_size, int),\
        "[propbundle_Filesystem] cluster_size must be of type Integer."

    return uco_object.create_PropertyBundle('Filesystem', FilesystemType=filesystem_type, ClusterSize=cluster_size)


def propbundle_Fragment(uco_object, fragment_index=Missing(), total_fragments=Missing()):
    '''
    :param FragmentIndex: Any number of values of type Integer.
    :param TotalFragments: Any number of values of type Integer.
    :return: A PropertyBundle object.
    '''

    if not isinstance(fragment_index, Missing):
        assert isinstance(fragment_index, list),\
        "[propbundle_Fragment] fragment_index must be of type List of Integer."
        assert all(isinstance(i, int) for i in fragment_index),\
        "[propbundle_Fragment] fragment_index must be of type List of Integer."
    if not isinstance(total_fragments, Missing):
        assert isinstance(total_fragments, list),\
        "[propbundle_Fragment] total_fragments must be of type List of Integer."
        assert all(isinstance(i, int) for i in total_fragments),\
        "[propbundle_Fragment] total_fragments must be of type List of Integer."

    return uco_object.create_PropertyBundle('Fragment', FragmentIndex=fragment_index, TotalFragments=total_fragments)


def propbundle_GeolocationEntry(uco_object, application_ref=Missing(), created_time=Missing(), location_ref=Missing()):
    '''
    :param ApplicationRef: Exactly one occurrence of type Trace.
    :param CreatedTime: At most one value of type Datetime.
    :param LocationRef: At most one occurrence of type Location.
    '''

    assert not isinstance(application_ref, Missing),\
    "[propbundle_GeolocationLog] application_ref is required."
    if not isinstance(application_ref, Missing):
        assert (isinstance(application_ref, case.CoreObject) and (application_ref.type=='Trace')),\
        "[propbundle_GeolocationLog] application_ref must be of type Trace."

    if not isinstance(created_time, Missing):
        assert isinstance(created_time, datetime.datetime),\
        "[propbundle_GeolocationLog] created_time must be of type Datetime."
    if not isinstance(location_ref, Missing):
        assert (isinstance(location_ref, case.CoreObject) and (location_ref.type=='Location')),\
        "[propbundle_GeolocationLog] location_ref must be of type Location."

    return uco_object.create_PropertyBundle('GeolocationEntry', ApplicationRef=application_ref,
                                            CreatedTime=created_time, LocationRef=location_ref)


def propbundle_GeolocationLog(uco_object, application_ref=Missing(), created_time=Missing()):
    '''
    :param ApplicationRef: Exactly one occurrence of type Trace.
    :param CreatedTime: At most one value of type Datetime.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(application_ref, Missing),\
    "[propbundle_GeolocationLog] application_ref is required."
    if not isinstance(application_ref, Missing):
        assert (isinstance(application_ref, case.CoreObject) and (application_ref.type=='Trace')),\
        "[propbundle_GeolocationLog] application_ref must be of type Trace."

    if not isinstance(created_time, Missing):
        assert isinstance(created_time, datetime.datetime),\
        "[propbundle_GeolocationLog] created_time must be of type Datetime."

    return uco_object.create_PropertyBundle('GeolocationLog', ApplicationRef=application_ref, CreatedTime=created_time)


def propbundle_GeolocationTrack(uco_object, application_ref=Missing(), start_time=Missing(),
                                end_time=Missing(), geolocation_entry_refs=Missing()):
    '''
    :param ApplicationRef: Exactly one occurrence of type Trace.
    :param StartTime: At most one value of type Datetime.
    :param EndTime: At most one value of type Datetime.
    :param GeolocationEntryRefs: Any number of occurrences of type Trace.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(application_ref, Missing),\
    "[propbundle_GeolocationTrack] application_ref is required."
    if not isinstance(application_ref, Missing):
        assert (isinstance(application_ref, case.CoreObject) and (application_ref.type=='Trace')),\
        "[propbundle_GeolocationTrack] application_ref must be of type Trace."

    if not isinstance(start_time, Missing):
        assert isinstance(start_time, datetime.datetime),\
        "[propbundle_GeolocationTrack] start_time must be of type Datetime."
    if not isinstance(end_time, Missing):
        assert isinstance(end_time, datetime.datetime),\
        "[propbundle_GeolocationTrack] end_time must be of type Datetime."
    if not isinstance(geolocation_entry_refs, Missing):
        assert isinstance(geolocation_entry_refs, list),\
        "[propbundle_GeolocationTrack] geolocation_entry_refs must be of type List of Trace."
        assert all( (isinstance(i, case.CoreObject) and i.type=='Trace') for i in geolocation_entry_refs),\
        "[propbundle_GeolocationTrack] geolocation_entry_refs must be of type List of Trace."

    return uco_object.create_PropertyBundle('Geolocation', ApplicationRef=application_ref, EndTime=end_time,
                                            GeolocationEntryRefs=geolocation_entry_refs, StartTime=start_time)


def propbundle_GPSCoordinates(uco_object, hdop=Missing(), pdop=Missing(), tdop=Missing(), vdop=Missing()):
    '''
    :param HDOP: At most one value of type Float.
    :param PDOP: At most one value of type Float.
    :param TDOP: At most one value of type Float.
    :param VDOP: At most one value of type Float.
    :return: A PropertyBundle object.
    '''

    if not isinstance(hdop, Missing):
        assert isinstance(hdop, float),\
        "[propbundle_GPSCoordinates] hdop must be of type Float."
    if not isinstance(pdop, Missing):
        assert isinstance(pdop, float),\
        "[propbundle_GPSCoordinates] pdop must be of type Float."
    if not isinstance(tdop, Missing):
        assert isinstance(tdop, float),\
        "[propbundle_GPSCoordinates] tdop must be of type Float."
    if not isinstance(vdop, Missing):
        assert isinstance(vdop, float),\
        "[propbundle_GPSCoordinates] vdop must be of type Float."

    return uco_object.create_PropertyBundle('GPSCoordinates', HDOP=hdop, PDOP=pdop, TDOP=tdop, VDOP=vdop)


def propbundle_HTTPConnection(uco_object, request_method=Missing(), request_value=Missing(),
                              http_request_version=Missing(), http_request_header=Missing()
                              , http_message_body_length=Missing(), http_message_body_data_ref=Missing()):
    '''
    :param RequestMethod: Exactly one value of type String.
    :param RequestValue: Exactly one value of type String.
    :param RequestVersion: At most one value of type String.
    :param HTTPRequestVersion: At most one value of type String.
    :param HTTPMessageBodyLength: At most one value of type Integer.
    :param HTTPMessageBodyDataRef: At most one occurrence of type Trace.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(request_method, Missing),\
    "[propbundle_HTTPConnection] request_method is required."
    if not isinstance(request_method, Missing):
        assert isinstance(request_method, str),\
        "[propbundle_HTTPConnection] request_method must be of type String."
    assert not isinstance(request_value, Missing),\
    "[propbundle_HTTPConnection] request_value is required."
    if not isinstance(request_value, Missing):
        assert isinstance(request_value, str),\
        "[propbundle_HTTPConnection] request_value must be of type String."

    if not isinstance(http_request_header, Missing):
        assert isinstance(http_request_header, str),\
        "[propbundle_HTTPConnection] request_version must be of type String."
    if not isinstance(http_request_version, Missing):
        assert isinstance(http_request_version, str),\
        "[propbundle_HTTPConnection] http_request_version must be of type String."
    if not isinstance(http_message_body_length, Missing):
        assert isinstance(http_message_body_length, int),\
        "[propbundle_HTTPConnection] http_message_body_length must be of type Integer."
    if not isinstance(http_message_body_data_ref, Missing):
        assert (isinstance(http_message_body_data_ref, case.CoreObject) and
                (http_message_body_data_ref.type=='Trace')),\
        "[propbundle_HTTPConnection] http_message_body_data_ref must be of type Trace."

    return uco_object.create_PropertyBundle('HTTPConnection', RequestMethod=request_method,
                                            RequestValue=request_value, RequestVersion=http_request_version,
                                            HTTPRequestVersion=http_request_version,
                                            HTTPMessageBodyLength=http_message_body_length,
                                            HTTPMessageBodyDataRef=http_message_body_data_ref)


def propbundle_ICMPConnection(uco_object, icmp_type=Missing(), icmp_code=Missing()):
    '''
    :param ICMPType: Exactly one value of type HexBinary.
    :param ICMPCode: Exactly one value of tpye HexBinary.
    :return: A PropertyBundle object.
    '''

    #TODO:HexBinary
    #TODO:HexBinary

    return uco_object.create_PropertyBundle('ICMPConnection', ICMPType=icmp_type, ICMPCode=icmp_code)


def propbundle_Identity(uco_object):
    '''
    :return: A PropertyBundle object.
    '''

    #TODO:NothingElseToCheck

    return uco_object.create_PropertyBundle('Identity')


def propbundle_Image(uco_object, image_type=Missing()):
    '''
    :param ImageType: Exactly one value of type String.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(image_type, Missing),\
    "[propbundle_Image] image_type is required."
    if not isinstance(image_type, Missing):
        assert isinstance(image_type, str),\
        "[propbundle_Image] image_type must be of type String."

    return uco_object.create_PropertyBundle('Image', ImageType=image_type)


def propbundle_IPV4Address(uco_object, value=Missing()):
    '''
    :param Value: Exactly one value of type String.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(value, Missing),\
    "[propbundle_IPV4Address] value is required."
    if not isinstance(value, Missing):
        assert isinstance(value, str),\
        "[propbundle_IPV4Address] value must be of type String."

    return uco_object.create_PropertyBundle('IPV4Address', Value=value)


def propbundle_IPV6Address(uco_object, value=Missing()):
    '''
    :param Value: Exactly one value of type String.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(value, Missing),\
    "[propbundle_IPV6Address] value is required."
    if not isinstance(value, Missing):
        assert isinstance(value, str),\
        "[propbundle_IPV6Address] value must be of type String."

    return uco_object.create_PropertyBundle('IPV6Address', Value=value)


def propbundle_LatLongCoordinates(uco_object, latitude=Missing(), longitude=Missing(), altitude=Missing()):
    '''
    :param Latitude: At most one value of type Float.
    :param Longitude: At most one value of type Float.
    :param Altitude: At most one value of type Float.
    :return: A PropertyBundle object.
    '''

    if not isinstance(latitude, Missing):
        assert isinstance(latitude, float),\
        "[propbundle_LatLongCoordinates] latitude must be of type Float."
    if not isinstance(longitude, Missing):
        assert isinstance(longitude, float),\
        "[propbundle_LatLongCoordinates] longitude must be of type Float."
    if not isinstance(altitude, Missing):
        assert isinstance(altitude, float),\
        "[propbundle_LatLongCoordinates] altitude must be of type Float."

    return uco_object.create_PropertyBundle('LatLongCoordinates', Latitude=latitude,
                                            Longitude=longitude, Altitude=altitude)


def propbundle_Library(uco_object, library_type=Missing()):
    '''
    :param LibraryType: Exactly one occurrence of type ControlledVocabulary.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(library_type, Missing),\
    "[propbundle_Library] library_type is required."
    if not isinstance(library_type, Missing):
        assert (isinstance(library_type, case.CoreObject) and (library_type.type=='ControlledVocabulary')),\
        "[propbundle_Library] library_type must be of type ControlledVocabulary."

    return uco_object.create_PropertyBundle('Library', LibraryType=library_type)


def propbundle_MACAddress(uco_object, value=Missing()):
    '''
    :param Value: Exactly one value of type String.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(value, Missing),\
    "[propbundle_MACAddress] value is required."
    if not isinstance(value, Missing):
        assert isinstance(value, bool),\
        "[propbundle_MACAddress] value must be of type Bool."

    return uco_object.create_PropertyBundle('MACAddress', Value=value)


def propbundle_Memory(uco_object, is_injected=Missing(), is_mapped=Missing(), is_protected=Missing(),
                      is_volatile=Missing(), region_size=Missing(), region_start_address=Missing(),
                      region_end_address=Missing()):
    '''
    :param IsInjected: Exactly one value of type Bool.
    :param IsMapped: Exactly one value of type Bool.
    :param IsProtected: Exactly one value of type Bool.
    :param IsVolatile: Exactly one value of type Bool.
    :param RegionSize: At most one value of any type.
    :param RegionStartAddress: At most one value of type HexBinary.
    :param RegionEndAddress: At most one value of type Hexbinary.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(is_injected, Missing),\
    "[propbundle_Memory] is_injected is required."
    if not isinstance(is_injected, Missing):
        assert isinstance(is_injected, bool),\
        "[propbundle_Memory] is_injected must be of type Bool."
    assert not isinstance(is_mapped, Missing),\
    "[propbundle_Memory] is_mapped is required."
    if not isinstance(is_mapped, Missing):
        assert isinstance(is_mapped, bool),\
        "[propbundle_Memory] is_mapped must be of type Bool."
    assert not isinstance(is_protected, Missing),\
    "[propbundle_Memory] is_protected is required."
    if not isinstance(is_protected, Missing):
        assert isinstance(is_protected, bool),\
        "[propbundle_Memory] is_protected must be of type Bool."
    assert not isinstance(is_volatile, Missing),\
    "[propbundle_Memory] is_volatile is required."
    if not isinstance(is_volatile, Missing):
        assert isinstance(is_volatile, bool),\
        "[propbundle_Memory] is_volatile must be of type Bool."

    #NOCHECK:region_size
    #TODO:HexBinary
    #TODO:HexBinary

    return uco_object.create_PropertyBundle('Memory', IsInjected=is_injected, IsMapped=is_mapped,
                                            IsProtected=is_protected, IsVolatile=is_volatile, RegionSize=region_size,
                                            RegionStartAddress=region_start_address,
                                            RegionEndAddress=region_end_address)


def propbundle_Message(uco_object, application_ref=Missing(), from_ref=Missing(),
                       to_refs=Missing(), message_text=Missing(), message_id=Missing(),
                       message_type=Missing(), session_id=Missing(), sent_time=Missing(),
                       participant_refs=Missing()):
    '''
    :param ApplicationRef: At most one occurrence of type Trace.
    :param FromRef: At most one occurrence of type Trace.
    :param ToRefs: Any number of occurrences of type Trace.
    :param MessageText: At most one value of type String.
    :param MessageID: At most one value of type String.
    :param MessageType: At most one value of type String.
    :param SessionID: At most one value of type String.
    :param SentTime: At most one value of type Datetime.
    :param ParticipantRefs: Any number of occurrences of type Trace.
    :return: A PropertyBundle object.
    '''

    if not isinstance(application_ref, Missing):
        assert (isinstance(application_ref, case.CoreObject) and (application_ref.type=='Trace')),\
        "[propbundle_Message] application_ref must be of type Trace."
    if not isinstance(from_ref, Missing):
        assert (isinstance(from_ref, case.CoreObject) and (from_ref.type=='Trace')),\
        "[propbundle_Message] from_ref must be of type Trace."
    if not isinstance(to_refs, Missing):
        assert isinstance(to_refs, list),\
        "[propbundle_Message] to_refs must be of type List of Trace."
        assert all( (isinstance(i, case.CoreObject) and i.type=='Trace') for i in to_refs),\
        "[propbundle_Message] to_refs must be of type List of Trace."
    if not isinstance(message_text, Missing):
        assert isinstance(message_text, str),\
        "[propbundle_Message] message_text must be of type String."
    if not isinstance(message_id, Missing):
        assert isinstance(message_id, str),\
        "[propbundle_Message] message_id must be of type String."
    if not isinstance(message_type, Missing):
        assert isinstance(message_type, str),\
        "[propbundle_Message] message_type must be of type String."
    if not isinstance(session_id, Missing):
        assert isinstance(session_id, str),\
        "[propbundle_Message] session_id must be of type String."
    if not isinstance(sent_time, Missing):
        assert isinstance(sent_time, datetime.datetime),\
        "[propbundle_Message] sent_time must be of type Datetime."
    if not isinstance(participant_refs, Missing):
        assert isinstance(participant_refs, list),\
        "[propbundle_Message] participant_refs must be of type List of Trace."
        assert all( (isinstance(i, case.CoreObject) and i.type=='Trace') for i in participant_refs),\
        "[propbundle_Message] participant_refs must be of type List of Trace."

    return uco_object.create_PropertyBundle('Message', ApplicationRef=application_ref,
                                            FromRef=from_ref, ToRefs=to_refs, MessageText=message_text,
                                            MessageID=message_id, MessageType=message_type, SessionID=session_id,
                                            SentTime=sent_time, ParticipantRefs=participant_refs)


def propbundle_MessageThread(uco_object, message_refs=Missing(), visibility=Missing(), participant_refs=Missing()):
    '''
    :param MessageRefs: Any number of occurrences of type ArrayOfObject.
    :param Visibility: At most one value of type Bool.
    :param ParticipantRefs: Any number of occurrences of type Trace.
    '''

    if not isinstance(message_refs, Missing):
        assert isinstance(message_refs, list),\
        "[propbundle_MessageThread] message_refs must be of type List of ArrayOfObject."
        assert all( (isinstance(i, case.DuckObject) and i.type=='ArrayOfObject') for i in message_refs),\
        "[propbundle_MessageThread] message_refs must be of type List of ArrayOfObject."
    if not isinstance(visibility, Missing):
        assert isinstance(visibility, bool),\
        "[propbundle_MessageThread] visibility must be of type Bool."
    if not isinstance(participant_refs, Missing):
        assert isinstance(participant_refs, list),\
        "[propbundle_MessageThread] participant_refs must be of type List of Trace."
        assert all( (isinstance(i, case.CoreObject) and i.type=='Trace') for i in participant_refs),\
        "[propbundle_MessageThread] participant_refs must be of type List of Trace."

    return uco_object.create_PropertyBundle('MessageThread', MessageRefs=message_refs, Visibility=visibility,
                                            ParticipantRefs=participant_refs)


def propbundle_MFTRecord(uco_object, mft_file_id=Missing(), mft_parent_id=Missing(), ntfs_hard_link_count=Missing(),
                         mft_record_change_time=Missing(), ntfs_owner_sid=Missing(), ntfs_owner_id=Missing(),
                         mft_flags=Missing(), mft_filename_created_time=Missing(), mft_filename_modified_time=Missing(),
                         mft_filename_accessed_time=Missing(), mft_filename_record_change_time=Missing(),
                         mft_filename_length=Missing()):
    '''
    :param MFTFileID: At most one value of type Integer.
    :param MFTParentID: At most one value of type Integer.
    :param NTFSHardLinkCount: At most one value of type Integer.
    :param MFTRecordChangeTime: At most one value of type Datetime.
    :param NTFSOwnerSID: At most one value of type String.
    :param NTFSOwnerID: At most one value of type String.
    :param MFTFlags: At most one value of type Integer.
    :param MFTFilenameCreatedTime: At most one value of type Datetime.
    :param MFTFilenameModifiedTime: At most one value of type Datetime.
    :param MFTFilenameAccessedTime: At most one value of type Datetime.
    :param MFTFilenameRecordChangeTime: At most one value of type Datetime.
    :param MFTFilenameLength: At most one value of type Integer.
    :return: A PropertyBundle object.
    '''

    if not isinstance(mft_file_id, Missing):
        assert isinstance(mft_file_id, int),\
        "[propbundle_MFTRecord] mft_file_id must be of type Integer."
    if not isinstance(mft_parent_id, Missing):
        assert isinstance(mft_parent_id, int),\
        "[propbundle_MFTRecord] mft_parent_id must be of type Integer."
    if not isinstance(ntfs_hard_link_count, Missing):
        assert isinstance(ntfs_hard_link_count, int),\
        "[propbundle_MFTRecord] ntfs_hard_link_count must be of type Integer."
    if not isinstance(mft_record_change_time, Missing):
        assert isinstance(mft_record_change_time, datetime.datetime),\
        "[propbundle_MFTRecord] mft_record_change_time must be of type Datetime."
    if not isinstance(ntfs_owner_sid, Missing):
        assert isinstance(ntfs_owner_sid, str),\
        "[propbundle_MFTRecord] ntfs_owner_sid must be of type String."
    if not isinstance(ntfs_owner_id, Missing):
        assert isinstance(ntfs_owner_id, str),\
        "[propbundle_MFTRecord] ntfs_owner_id must be of type String."
    if not isinstance(mft_flags, Missing):
        assert isinstance(mft_flags, int),\
        "[propbundle_MFTRecord] mft_flags must be of type Integer."
    if not isinstance(mft_filename_created_time, Missing):
        assert isinstance(mft_filename_created_time, datetime.datetime),\
        "[propbundle_MFTRecord] mft_filename_created_time must be of type Datetime."
    if not isinstance(mft_filename_modified_time, Missing):
        assert isinstance(mft_filename_modified_time, datetime.datetime),\
        "[propbundle_MFTRecord] mft_filename_modified_time must be of type Datetime."
    if not isinstance(mft_filename_accessed_time, Missing):
        assert isinstance(mft_filename_accessed_time, datetime.datetime),\
        "[propbundle_MFTRecord] mft_filename_accessed_time must be of type Datetime."
    if not isinstance(mft_filename_record_change_time, Missing):
        assert isinstance(mft_filename_record_change_time, datetime.datetime),\
        "[propbundle_MFTRecord] mft_filename_record_change_time must be of type Datetime."
    if not isinstance(mft_filename_length, Missing):
        assert isinstance(mft_filename_length, int),\
        "[propbundle_MFTRecord] mft_filename_length must be of type Integer."

    return uco_object.create_PropertyBundle('MFTRecord', MFTFileID=mft_file_id, MFTParentID=mft_parent_id,
                                            NTFSHardLinkCount=ntfs_hard_link_count,
                                            MFTRecordChangeTime=mft_record_change_time, NTFSOwnerSID=ntfs_owner_sid,
                                            NTFSOwnerID=ntfs_owner_id, MFTFlags=mft_flags,
                                            MFTFileNameCreatedTime=mft_filename_created_time,
                                            MFTFileNameModifiedTime=mft_filename_modified_time,
                                            MFTFileNameAccessedTime=mft_filename_accessed_time,
                                            MFTFileNameRecordChangeTime=mft_filename_record_change_time,
                                            MFTFileNameLength=mft_filename_length)


def propbundle_Mutex(uco_object, is_named=Missing()):
    '''
    :param IsNamed: Exactly one value of type Bool.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(is_named, Missing),\
    "[propbundle_Mutex] is_named is required."
    if not isinstance(is_named, Missing):
        assert isinstance(is_named, bool),\
        "[propbundle_Mutex] is_named must be of type Bool."

    return uco_object.create_PropertyBundle('Mutex', IsNamed=is_named)


def propbundle_NetworkConnection(uco_object, is_active=Missing(), start_time=Missing(), end_time=Missing(),
                                 source_refs=Missing(), destination_refs=Missing(), source_port=Missing(),
                                 destination_port=Missing(), protocols=Missing()):
    '''
    :param IsActive: At most one value of type Bool.
    :param StartTime: At most one value of type Datetime.
    :param EndTime: At most one value of type Datetime.
    :param SourceRefs: Any number of occurrences of type CoreObject.
    :param DestinationRefs: Any number of occurrences of type CoreObject.
    :param SourcePort: At most one value of type Integer.
    :param DestinationPort: At most one value of type Integer.
    :param Protocols: At most one occurrence of type ControlledDictionary.
    :return: A PropertyBundle object.
    '''

    if not isinstance(is_active, Missing):
        assert isinstance(is_active, bool),\
        "[propbundle_NetworkConnection] is_active must be of type Bool."
    if not isinstance(start_time, Missing):
        assert isinstance(start_time, datetime.datetime),\
        "[propbundle_NetworkConnection] start_time must be of type Datetime."
    if not isinstance(end_time, Missing):
        assert isinstance(end_time, datetime.datetime),\
        "[propbundle_NetworkConnection] end_time must be of type Datetime."
    if not isinstance(source_refs, Missing):
        assert isinstance(source_refs, list),\
        "[propbundle_NetworkConnection] source_refs must be of type List of CoreObject."
        assert all(isinstance(i, case.CoreObject) for i in source_refs),\
        "[propbundle_NetworkConnection] source_refs must be of type List of CoreObject."
    if not isinstance(destination_refs, Missing):
        assert isinstance(destination_refs, list),\
        "[propbundle_NetworkConnection] destination_refs must be of type List of CoreObject."
        assert all(isinstance(i, case.CoreObject) for i in destination_refs),\
        "[propbundle_NetworkConnection] destination_refs must be of type List of CoreObject."
    if not isinstance(source_port, Missing):
        assert isinstance(source_port, int),\
        "[propbundle_NetworkConnection] source_port must be of type Integer."
    if not isinstance(destination_port, Missing):
        assert isinstance(destination_port, int),\
        "[propbundle_NetworkConnection] destination_port must be of type Integer."
    if not isinstance(protocols, Missing):
        assert (isinstance(protocols, case.DuckObject) and (protocols.type=='ControlledDictionary')),\
        "[propbundle_NetworkConnection] protocols must be of type ControlledDictionary."

    return uco_object.create_PropertyBundle('NetworkConnection', IsActive=is_active, StartTime=start_time,
                                            EndTime=end_time, SourceRefs=source_refs,
                                            DestinationRefs=destination_refs, SourcePort=source_port,
                                            DestinationPort=destination_port, Protocols=protocols)

    
def propbundle_NetworkFlow(uco_object, source_bytes=Missing(), destination_bytes=Missing(),
                           source_packets=Missing(), destination_packets=Missing(),
                           source_payload_refs=Missing(), destination_payload_refs=Missing(),
                           ipfix=Missing()):
    '''
    :param SourceBytes: At most one value of type Integer.
    :param DestinationBytes: At most one value of type Integer.
    :param SourcePackets: At most one value of type Integer.
    :param DestinationPackets: At most one value of type Integer.
    :param SourcePayloadRefs: At most one occurrence of type Trace.
    :param DestinationPayloadRefs: At most one occurrence of type Trace.
    :param IPFIX: At most one occurrence of type Dictionary.
    :return: A PropertyBundle object.
    '''
    
    if not isinstance(source_bytes, Missing):
        assert isinstance(source_bytes, int),\
        "[propbundle_NetworkFlow] source_bytes must be of type Integer."
    if not isinstance(destination_bytes, Missing):
        assert isinstance(destination_bytes, int),\
        "[propbundle_NetworkFlow] destination_bytes must be of type Integer."
    if not isinstance(source_packets, Missing):
        assert isinstance(source_packets, int),\
        "[propbundle_NetworkFlow] source_packets must be of type Integer."
    if not isinstance(destination_packets, Missing):
        assert isinstance(destination_packets, int),\
        "[propbundle_NetworkFlow] destination_packets must be of type Integer."
    if not isinstance(source_payload_refs, Missing):
        assert (isinstance(source_payload_refs, case.CoreObject) and (source_payload_refs.type=='Trace')),\
        "[propbundle_NetworkFlow] source_payload_refs must be of type Trace."
    if not isinstance(destination_payload_refs, Missing):
        assert (isinstance(destination_payload_refs, case.CoreObject) and (destination_payload_refs.type=='Trace')),\
        "[propbundle_NetworkFlow] destination_payload_refs must be of type Trace."
    if not isinstance(ipfix, Missing):
        assert (isinstance(ipfix, case.DuckObject) and (ipfix.type=='Dictionary')),\
        "[propbundle_NetworkFlow] ipfix must be of type Dictionary."

    return uco_object.create_PropertyBundle('NetworkFlow', SourceBytes=source_bytes,
                                            DestinationBytes=destination_bytes,
                                            SourcePackets=source_packets,
                                            DestinationPackets=destination_packets,
                                            SourcePayloadRefs=source_payload_refs,
                                            DestinationPayloadRefs=destination_payload_refs,
                                            IPFIX=ipfix)


def propbundle_NetworkInterface(uco_object, adapter_name=Missing(), dhcp_lease_expires=Missing(),
                                dhcp_lease_obtained=Missing(), dhcp_server_refs=Missing(),
                                ip_gateway_refs=Missing(), ip_refs=Missing(), mac_address_ref=Missing()):
    '''
    :param AdapterName: At most one value of type String.
    :param DHCPLeaseExpires: At most one value of type Datetime.
    :param DHCPLeaseObtained: At most one value of type Datetime.
    :param DHCPServerRefs: Any number of occurrences of type Trace.
    :param IPGatewayRefs: Any number of occurrences of type Trace.
    :param IPRefs: Any number of occurrences of type Trace.
    :param MACAddressRef: At most one occurrence of type Trace.
    :return: A PropertyBundle object.
    '''

    if not isinstance(adapter_name, Missing):
        assert isinstance(adapter_name, str),\
        "[propbundle_NetworkInterface] adapter_name must be of type String."
    if not isinstance(dhcp_lease_expires, Missing):
        assert isinstance(dhcp_lease_expires, datetime.datetime),\
        "[propbundle_NetworkInterface] dhcp_lease_expires must be of type Datetime."
    if not isinstance(dhcp_lease_obtained, Missing):
        assert isinstance(dhcp_lease_obtained, datetime.datetime),\
        "[propbundle_NetworkInterface] dhcp_lease_obtained must be of type Datetime."
    if not isinstance(dhcp_server_refs, Missing):
        assert isinstance(dhcp_server_refs, list),\
        "[propbundle_NetworkInterface] dhcp_server_refs must be of type List of Trace."
        assert all( (isinstance(i, case.CoreObject) and i.type=='Trace') for i in dhcp_server_refs),\
        "[propbundle_NetworkInterface] dhcp_server_refs must be of type List of Trace."
    if not isinstance(ip_gateway_refs, Missing):
        assert isinstance(ip_gateway_refs, list),\
        "[propbundle_NetworkInterface] ip_gateway_refs must be of type List of Trace."
        assert all( (isinstance(i, case.CoreObject) and i.type=='Trace') for i in ip_gateway_refs),\
        "[propbundle_NetworkInterface] ip_gateway_refs must be of type List of Trace."
    if not isinstance(ip_refs, Missing):
        assert isinstance(ip_refs, list),\
        "[propbundle_NetworkInterface] ip_refs must be of type List of Trace."
        assert all( (isinstance(i, case.CoreObject) and i.type=='Trace') for i in ip_refs),\
        "[propbundle_NetworkInterface] ip_refs must be of type List of Trace."
    if not isinstance(mac_address_ref, Missing):
        assert (isinstance(mac_address_ref, case.CoreObject) and (mac_address_ref.type=='Trace')),\
        "[propbundle_NetworkInterface] mac_address_ref must be of type Trace."

    return uco_object.create_PropertyBundle('NetworkInterface', AdapterName=adapter_name,
                                            DHCPLeaseExpires=dhcp_lease_expires, DHCPLeaseObtained=dhcp_lease_obtained,
                                            DHCPServerRefs=dhcp_server_refs, IPGatewayRefs=ip_gateway_refs,
                                            IPRefs=ip_refs, MACAddressRef=mac_address_ref)


def propbundle_Note(uco_object, application_ref=Missing(), categories=Missing(), created_time=Missing(),
                    modified_time=Missing(), labels=Missing(), text=Missing()):
    '''
    :param ApplicationRef: Exactly one occurrence of type Trace.
    :param Categories: Any number of values of type String.
    :param CreatedTime: At most one value of type Datetime.
    :param ModifiedTime: At most one value of type Datetime.
    :param Labels: Any number of values of type String.
    :param Text: At most one value of type String.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(application_ref, Missing),\
    "[propbundle_Note] application_ref is required."
    if not isinstance(application_ref, Missing):
        assert (isinstance(application_ref, case.CoreObject) and (application_ref.type=='Trace')),\
        "[propbundle_Note] application_ref must be of type Trace."

    if not isinstance(categories, Missing):
        assert isinstance(categories, list),\
        "[propbundle_Note] categories must be of type List of String."
        assert all(isinstance(i, str) for i in categories),\
        "[propbundle_Note] categories must be of type List of String."
    if not isinstance(created_time, Missing):
        assert isinstance(created_time, datetime.datetime),\
        "[propbundle_Note] created_time must be of type Datetime."
    if not isinstance(modified_time, Missing):
        assert isinstance(modified_time, datetime.datetime),\
        "[propbundle_Note] modified_time must be of type Datetime."
    if not isinstance(labels, Missing):
        assert isinstance(labels, list),\
        "[propbundle_Note] labels must be of type List of String."
        assert all(isinstance(i, str) for i in labels),\
        "[propbundle_Note] labels must be of type List of String."
    if not isinstance(text, Missing):
        assert isinstance(text, str),\
        "[propbundle_Note] text must be of type String."

    return uco_object.create_PropertyBundle('Note', ApplicationRef=application_ref, Categories=categories,
                                            CreatedTime=created_time, ModifiedTime=modified_time,
                                            Labels=labels, Text=text)


def propbundle_NTFSFilePermissions(uco_object):
    '''
    :return: A PropertyBundle object.
    '''

    #TODO:NothingElseToCheck

    return uco_object.create_PropertyBundle('NTFSFilePermission')


def propbundle_NTFSFileSystem(uco_object, sid=Missing(), alternate_data_streams=Missing(), entry_id=Missing()):
    '''
    :param SID: At most one value of type String.
    :param AlternateDataStreams: Any number of occurrences of type AlternateDataStream.
    :param EntryID: At most one value of type Long.
    :return: A PropertyBundle object.
    '''

    if not isinstance(sid, Missing):
        assert isinstance(sid, str),\
        "[propbundle_NTFSFileSystem] sid must be of type String."
    if not isinstance(alternate_data_streams, Missing):
        assert isinstance(alternate_data_streams, list),\
        "[propbundle_NTFSFileSystem] alternate_data_streams must be of type List of AlternateDataStream."
        assert all( (isinstance(i, case.DuckObject) and i.type=='AlternateDataStream') for i in alternate_data_streams),\
        "[propbundle_NTFSFileSystem] alternate_data_streams must be of type List of AlternateDataStream."
    if not isinstance(entry_id, Missing):
        assert isinstance(entry_id, long),\
        "[propbundle_NTFSFileSystem] entry_id must be of type Long."

    return uco_object.create_PropertyBundle('NTFSFileSystem', SID=sid, AlternateDataStreams=alternate_data_streams,
                                            EntryID=entry_id)


def propbundle_OperatingSystem(uco_object, manufacturer=Missing(), version=Missing(), bitness=Missing(),
                               environment_variables=Missing(), install_date=Missing()):
    '''
    :param Manufacturer: At most one value of type String.
    :param Version: At most one value of type String.
    :param Bitness: At most one occurrence of type ControlledVocabulary.
    :param EnvironmentVariables: At most one occurrence of type Dictionary.
    :param InstallDate: At most one value of type Datetime.
    :return: A PropertyBundle object.
    '''

    if not isinstance(manufacturer, Missing):
        assert isinstance(manufacturer, str),\
        "[propbundle_OperatingSystem] manufacturer must be of type String."
    if not isinstance(version, Missing):
        assert isinstance(version, str),\
        "[propbundle_OperatingSystem] version must be of type String."
    if not isinstance(bitness, Missing):
        assert (isinstance(bitness, case.DuckObject) and (bitness.type=='ControlledDictionary')),\
        "[propbundle_OperatingSystem] bitness must be of type ControlledDictionary."
    if not isinstance(environment_variables, Missing):
        assert (isinstance(environment_variables, case.DuckObject) and (environment_variables.type=='Dictionary')),\
        "[propbundle_OperatingSystem] environment_variables must be of type Dictionary."
    if not isinstance(install_date, Missing):
        assert isinstance(install_date, datetime.datetime),\
        "[propbundle_OperatingSystem] install_date must be of type Datetime."

    return uco_object.create_PropertyBundle('OperatingSystem', Manufacturer=manufacturer, Version=version,
                                            Bitness=bitness, EnvironmentVariables=environment_variables,
                                            InstallDate=install_date)


def propbundle_PathRelation(uco_object, path=Missing()):
    '''
    :param Path: At least one value of type String.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(path, Missing),\
    "[propbundle_PathRelation] path is required."
    if not isinstance(path, Missing):
        assert isinstance(path, list),\
        "[propbundle_PathRelation] path must be of type List of String."
        assert all(isinstance(i, str) for i in path),\
        "[propbundle_PathRelation] path must be of type List of String."
        
    return uco_object.create_PropertyBundle('PathRelationship', Path=path)


def propbundle_PDFFile(uco_object, version=Missing(), is_optimized=Missing(), document_information_dictionary=Missing(),
                       pdf_id_zero=Missing(), pdf_id_one=Missing()):
    '''
    :param Version: At most one value of type String.
    :param IsOptimized: At most one value of type Bool.
    :param DocumentInformationDictionary: At most one occurrence of type ControlledDictionary.
    :param PDFIDZero: Any number of values of type String.
    :param PDFIDOne: At most one value of type String.
    :return: A PropertyBundle object.
    '''

    if not isinstance(version, Missing):
        assert isinstance(version, str),\
        "[propbundle_PDFFile] version must be of type String."
    if not isinstance(is_optimized, Missing):
        assert isinstance(is_optimized, bool),\
        "[propbundle_PDFFile] is_optimized must be of type Bool."
    if not isinstance(document_information_dictionary, Missing):
        assert (isinstance(document_information_dictionary, case.DuckObject) and
                (document_information_dictionary.type=='ControlledDictionary')),\
        "[propbundle_PDFFile] document_information_dictionary must be of type ControlledDictionary."
    if not isinstance(pdf_id_zero, Missing):
        assert isinstance(pdf_id_zero, list),\
        "[propbundle_PDFFile] pdf_id_zero must be of type List of String."
        assert all(isinstance(i, str) for i in pdf_id_zero),\
        "[propbundle_PDFFile] pdf_id_zero must be of type List of String."
    if not isinstance(pdf_id_one, Missing):
        assert isinstance(pdf_id_one, str),\
        "[propbundle_PDFFile] pdf_id_one must be of type String."
    
    return uco_object.create_PropertyBundle('PDFFile', Version=version, IsOptimized=is_optimized,
                                            DocumentInformationDictionary=document_information_dictionary,
                                            PDFIDZero=pdf_id_zero, PDFIDOne=pdf_id_one)


def propbundle_PhoneAccount(uco_object, phone_number=Missing()):
    '''
    :param PhoneNumber: Exactly one value of type String.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(phone_number, Missing),\
    "[propbundle_PhoneAccount] phone_number is required."
    if not isinstance(phone_number, Missing):
        assert isinstance(phone_number, str),\
        "[propbundle_PhoneAccount] phone_number must be of type String."

    return uco_object.create_PropertyBundle('PhoneAccount', PhoneNumber=phone_number)


def propbundle_PhoneCall(uco_object, application_ref=Missing(), call_type=Missing(), duration=Missing(),
                         start_time=Missing(), end_time=Missing(), from_ref=Missing(), to_ref=Missing(),
                         participant_refs=Missing()):
    '''
    :param ApplicationRef: Exactly one occurrence of type Trace.
    :param CallType: At most one value of type String.
    :param Duration: At most one value of type Long.
    :param StartTime: At most one value of type Datetime.
    :param EndTime: At most one value of type Datetime.
    :param FromRef: At most one occurrence of type Trace.
    :param ToRef: At most one occurrence of type Trace.
    :param ParticipantRefs: Any number of occurrences of type Trace.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(application_ref, Missing),\
    "[propbundle_PhoneCall] application_ref is required."
    if not isinstance(application_ref, Missing):
        assert (isinstance(application_ref, case.CoreObject) and (application_ref.type=='Trace')),\
        "[propbundle_PhoneCall] application_ref must be of type Trace."

    if not isinstance(call_type, Missing):
        assert isinstance(call_type, str),\
        "[propbundle_PhoneCall] call_type must be of type String."
    if not isinstance(duration, Missing):
        assert isinstance(duration, long),\
        "[propbundle_PhoneCall] duration must be of type Long."
    if not isinstance(start_time, Missing):
        assert isinstance(start_time, datetime.datetime),\
        "[propbundle_PhoneCall] start_time must be of type Datetime."
    if not isinstance(end_time, Missing):
        assert isinstance(end_time, datetime.datetime),\
        "[propbundle_PhoneCall] end_time must be of type Datetime."
    if not isinstance(from_ref, Missing):
        assert (isinstance(from_ref, case.CoreObject) and (from_ref.type=='Trace')),\
        "[propbundle_PhoneCall] from_ref must be of type Trace."
    if not isinstance(to_ref, Missing):
        assert (isinstance(to_ref, case.CoreObject) and (to_ref.type=='Trace')),\
        "[propbundle_PhoneCall] to_ref must be of type Trace."
    if not isinstance(participant_refs, Missing):
        assert isinstance(participant_refs, list),\
        "[propbundle_PhoneCall] participant_refs must be of type List of Trace."
        assert all( (isinstance(i, case.CoreObject) and i.type=='Trace') for i in participant_refs),\
        "[propbundle_PhoneCall] participant_refs must be of type List of Trace."

    return uco_object.create_PropertyBundle('PhoneCall', ApplicationRef=application_ref, CallType=call_type,
                                            Duration=duration, StartTime=start_time, EndTime=end_time,
                                            FromRef=from_ref, ToRef=to_ref, ParticipantRef=participant_refs)


def propbundle_Process(uco_object, arguments=Missing(), binary_ref=Missing(), created_time=Missing(),
                       creator_user_ref=Missing(), current_working_directory=Missing(),
                       environment_variables=Missing(), exit_status=Missing(), exit_time=Missing(),
                       is_hidden=Missing(), parent_ref=Missing(), pid=Missing(), status=Missing()):
    '''
    :param Arguments: Any number of values of type String.
    :param BinaryRef: At most one occurrence of type Trace.
    :param CreatedTime: At most one value of type Datetime.
    :param CreatorUserRef: At most one occurrence of type Trace.
    :param CurrentWorkingDirectory: At most one value of type String.
    :param EnvironmentVariables: At most one occurrence of type Dictionary.
    :param ExitStatus: At most one value of type Long.
    :param ExitTime: At most one value of type Datetime.
    :param IsHidden: At most one value of type Bool.
    :param ParentRef: At most one occurrence of type Trace.
    :param PID: At most one value of type Integer.
    :param Status: At most one value of type String.
    :return: A PropertyBundle object.
    '''

    if not isinstance(arguments, Missing):
        assert isinstance(arguments, list),\
        "[propbundle_Process] arguments must be of type List of String."
        assert all(isinstance(i, str) for i in arguments),\
        "[propbundle_Process] arguments must be of type List of String."
    if not isinstance(binary_ref, Missing):
        assert (isinstance(binary_ref, case.CoreObject) and (binary_ref.type=='Trace')),\
        "[propbundle_Process] binary_ref must be of type Trace."
    if not isinstance(created_time, Missing):
        assert isinstance(created_time, datetime.datetime),\
        "[propbundle_Process] created_time must be of type Datetime."
    if not isinstance(creator_user_ref, Missing):
        assert (isinstance(creator_user_ref, case.CoreObject) and (creator_user_ref.type=='Trace')),\
        "[propbundle_Process] creator_user_ref must be of type Trace."
    if not isinstance(current_working_directory, Missing):
        assert isinstance(current_working_directory, str),\
        "[propbundle_Process] current_working_directory must be of type String."
    if not isinstance(environment_variables, Missing):
        assert (isinstance(environment_variables, case.DuckObject) and (environment_variables.type=='Dictionary')),\
        "[propbundle_Process] environment_variables must be of type Dictionary."
    if not isinstance(exit_status, Missing):
        assert isinstance(exit_status, long),\
        "[propbundle_Process] exit_status must be of type Long."
    if not isinstance(exit_time, Missing):
        assert isinstance(exit_time, datetime.datetime),\
        "[propbundle_Process] exit_time must be of type Datetime."
    if not isinstance(is_hidden, Missing):
        assert isinstance(is_hidden, bool),\
        "[propbundle_Process] is_hidden must be of type Bool."
    if not isinstance(parent_ref, Missing):
        assert (isinstance(parent_ref, case.CoreObject) and (parent_ref.type=='Trace')),\
        "[propbundle_Process] parent_ref must be of type Trace."
    if not isinstance(pid, Missing):
        assert isinstance(pid, int),\
        "[propbundle_Process] pid must be of type Integer."
    if not isinstance(status, Missing):
        assert isinstance(status, str),\
        "[propbundle_Process] status must be of type String."

    return uco_object.create_PropertyBundle('Process', Arguments=arguments, BinaryRef=binary_ref,
                                            CreatedTime=created_time, CreatorUserRef=creator_user_ref,
                                            CurrentWorkingDirectory=current_working_directory,
                                            EnvironmentVariables=environment_variables,
                                            ExitStatus=exit_status, ExitTime=exit_time, IsHidden=is_hidden,
                                            ParentRef=parent_ref, PID=pid, Status=status)


def propbundle_RasterPicture(uco_object, picture_height=Missing(), picture_width=Missing(), bits_per_pixel=Missing(),
                             image_compression_method=Missing(), camera_ref=Missing(), picture_type=Missing()):
    '''
    :param PictureHeight: At most one value of type Integer.
    :param PictureWidth: At most one value of type Integer.
    :param BitsPerPixel: At most one value of type Integer.
    :param ImageCompressionMethod: At most one value of type String.
    :param CameraRef: At most one occurrence of type Trace.
    :param PictureType: At most one value of type String.
    :return: A PropertyBundle object.
    '''

    if not isinstance(picture_height, Missing):
        assert isinstance(picture_height, int),\
        "[propbundle_RasterPicture] picture_height must be of type Integer."
    if not isinstance(picture_width, Missing):
        assert isinstance(picture_width, int),\
        "[propbundle_RasterPicture] picture_width must be of type Integer."
    if not isinstance(bits_per_pixel, Missing):
        assert isinstance(bits_per_pixel, int),\
        "[propbundle_RasterPicture] bits_per_pixel must be of type Integer."
    if not isinstance(image_compression_method, Missing):
        assert isinstance(image_compression_method, str),\
        "[propbundle_RasterPicture] image_compression_method must be of type String."
    if not isinstance(camera_ref, Missing):
        assert (isinstance(camera_ref, case.CoreObject) and (camera_ref.type=='Trace')),\
        "[propbundle_RasterPicture] camera_ref must be of type Trace."
    if not isinstance(picture_type, Missing):
        assert isinstance(picture_type, str),\
        "[propbundle_RasterPicture] picture_type must be of type String."

    return uco_object.create_PropertyBundle('RasterPicture', PictureHeight=picture_height, PictureWidth=picture_width,
                                            BitsPerPixel=bits_per_pixel,
                                            ImageCompressionMethod=image_compression_method,
                                            CameraRef=camera_ref, PictureType=picture_type)


def propbundle_SimpleAddress(uco_object, street=Missing(), locality=Missing(), region=Missing(),
                             postal_code=Missing(), country=Missing(), address_type=Missing()):
    '''
    :param Street: At most one value of type String.
    :param Locality: At most one value of type String.
    :param Region: At most one value of type String.
    :param PostalCode: At most one value of type String.
    :param Country: At most one value of type String.
    :param AddressType: At most one value of type String.
    :return: A PropertyBundle object.
    '''

    if not isinstance(street, Missing):
        assert isinstance(street, str),\
        "[propbundle_SimpleAddress] street must be of type String."
    if not isinstance(locality, Missing):
        assert isinstance(locality, str),\
        "[propbundle_SimpleAddress] locality must be of type String."
    if not isinstance(region, Missing):
        assert isinstance(region, str),\
        "[propbundle_SimpleAddress] region must be of type String."
    if not isinstance(postal_code, Missing):
        assert isinstance(postal_code, str),\
        "[propbundle_SimpleAddress] postal_code must be of type String."
    if not isinstance(country, Missing):
        assert isinstance(country, str),\
        "[propbundle_SimpleAddress] country must be of type String."
    if not isinstance(address_type, Missing):
        assert isinstance(address_type, str),\
        "[propbundle_SimpleAddress] address_type must be of type String."

    return uco_object.create_PropertyBundle('SimpleAddress', Street=street, Locality=locality,
                                            Region=region, PostalCode=postal_code, Country=country,
                                            AddressType=address_type)


def propbundle_SMSMessage(uco_object, is_read=Missing()):
    '''
    :param IsRead: Exactly one value of type Bool.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(is_read, Missing),\
    "[propbundle_SMSMessage] is_read is required."
    if not isinstance(is_read, Missing):
        assert isinstance(is_read, bool),\
        "[propbundle_SMSMessage] is_read must be of type Bool."

    return uco_object.create_PropertyBundle('SMSMessage', IsRead=is_read)


def propbundle_Software(uco_object, version=Missing(), language=Missing(), manufacturer=Missing(), swid=Missing(),
                        cpeid=Missing()):
    '''
    :param Version: At most one value of type String.
    :param Language: At most one value of type String.
    :param Manufacturer: At most one value of type String.
    :param SWID: At most one value of type String.
    :param CPEID: At most one value of type String.
    :return: A PropertyBundle object.
    '''
    
    if not isinstance(version, Missing):
        assert isinstance(version, str),\
        "[propbundle_Software] version must be of type String."
    if not isinstance(language, Missing):
        assert isinstance(language, str),\
        "[propbundle_Software] language must be of type String."
    if not isinstance(manufacturer, Missing):
        assert isinstance(manufacturer, str),\
        "[propbundle_Software] manufacturer must be of type String."
    if not isinstance(swid, Missing):
        assert isinstance(swid, str),\
        "[propbundle_Software] swid must be of type String."
    if not isinstance(cpeid, Missing):
        assert isinstance(cpeid, str),\
        "[propbundle_Software] cpeid must be of type String."

    return uco_object.create_PropertyBundle('Software', Version=version, Language=language,
                                            Manufacturer=manufacturer, SWID=swid, CPEID=cpeid)


def propbundle_SQLiteBlob(uco_object, column_name=Missing(), row_condition=Missing(), row_index=Missing(),
                          table_name=Missing()):
    '''
    :param ColumnName: At most one value of type String.
    :param RowCondition: At most one value of type String.
    :param RowIndex: At most one value of type PositiveInteger.
    :param TableName: At most one value of type String.
    :return: A PropertyBundle object.
    '''

    if not isinstance(column_name, Missing):
        assert isinstance(column_name, str),\
        "[propbundle_SQLiteBlob] column_name must be of type String."
    if not isinstance(row_condition, Missing):
        assert isinstance(row_condition, str),\
        "[propbundle_SQLiteBlob] row_condition must be of type String."
    if not isinstance(row_index, Missing):
        assert (isinstance(row_index, int) and (row_index > 0)),\
        "[propbundle_SQLiteBlob] row_index must be of type PositiveInteger."
    if not isinstance(table_name, Missing):
        assert isinstance(table_name, str),\
        "[propbundle_SQLiteBlob] table_name must be of type String."

    return uco_object.create_PropertyBundle('SQLiteBlob', ColumnName=column_name,
                                            RowCondition=row_condition, RowIndex=row_index, TableName=table_name)


def propbundle_SymbolicLink(uco_object, target_file_ref=Missing()):
    '''
    :param TargetFileRef: Exactly one occurrence of type Trace.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(target_file_ref, Missing),\
    "[propbundle_SymbolicLink] target_file_ref is required."
    if not isinstance(target_file_ref, Missing):
        assert (isinstance(target_file_ref, case.CoreObject) and (target_file_ref.type=='Trace')),\
        "[propbundle_SymbolicLink] target_file_ref must be of type Trace."

    return uco_object.create_PropertyBundle('SymbolicLink', TargetFileRef=target_file_ref)


def propbundle_TCPConnection(uco_object, source_flags=Missing(), destination_flags=Missing()):
    '''
    :param SourceFlags: At most one value of type HexBinary.
    :param DestinationFlags: At most one value of type HexBinary.
    :return: A PropertyBundle object.
    '''

    #TODO:HexBinary
    #TODO:HexBinary

    return uco_object.create_PropertyBundle('TCPConnection', SourceFlags=source_flags,
                                            DestinationFlags=destination_flags)


def propbundle_ToolConfigurationType(uco_object, configuration_settings=Missing(), dependencies=Missing(),
                                     usage_context_assumptions=Missing()):
    '''
    :param ConfigurationSettings: Any number of occurrences of type ConfigurationSettingType.
    :param Dependencies: Any number of occurrences of type DependencyType.
    :param UsageContextAssumptions: Any number of values of type StructuredText.
    :return: A PropertyBundle object.
    '''

    if not isinstance(configuration_settings, Missing):
        assert isinstance(configuration_settings, list),\
        "[propbundle_ToolConfigurationType] configuration_settings must be of type List of ConfigurationSettingType."
        assert all( (isinstance(i, case.DuckObject) and
                     i.type=='ConfigurationSettingType') for i in configuration_settings),\
        "[propbundle_ToolConfigurationType] configuration_settings must be of type List of ConfigurationSettingType."
    if not isinstance(dependencies, Missing):
        assert isinstance(dependencies, list),\
        "[propbundle_ToolConfigurationType] dependencies must be of type List of DependencyType."
        assert all( (isinstance(i, case.DuckObject) and i.type=='DependencyType') for i in dependencies),\
        "[propbundle_ToolConfigurationType] dependencies must be of type List of DependencyType."
    #TODO:StructuredType

    return uco_object.create_PropertyBundle('ToolConfigurationType', ConfigurationSettings=configuration_settings,
                                            Dependencies=dependencies,
                                            UsageContextAssumptions=usage_context_assumptions)


def propbundle_UNIXAccount(uco_object, gid=Missing(), groups=Missing(), shell=Missing()):
    '''
    :param GID: At most one value of type Integer.
    :param Groups: Any number of values of type String.
    :param Shell: At most one value of type String.
    :return: A PropertyBundle object.
    '''

    if not isinstance(gid, Missing):
        assert isinstance(gid, int),\
        "[propbundle_UNIXAccount] gid must be of type Integer."
    if not isinstance(groups, Missing):
        assert isinstance(groups, list),\
        "[propbundle_UNIXAccount] groups must be of type List of String."
        assert all(isinstance(i, str) for i in groups),\
        "[propbundle_UNIXAccount] groups must be of type List of String."
    if not isinstance(shell, Missing):
        assert isinstance(shell, str),\
        "[propbundle_UNIXAccount] shell must be of type String."

    return uco_object.create_PropertyBundle('UNIXAccount', GID=gid, Groups=groups, Shell=shell)


def propbundle_UNIXFilePermissions(uco_object):
    '''
    :return: A PropertyBundle object.
    '''

    #TODO:NothingElseToCheck

    return uco_object.create_PropertyBundle('UNIXFilePermissions')


def propbundle_UNIXProcess(uco_object, open_file_descriptor_refs=Missing(), priority=Missing(), ruid=Missing(),
                           session_id=Missing()):
    '''
    :param OpenFileDescriptorRefs: Any number of value of type Integer.
    :param Priority: At most one value of type PositiveInteger.
    :param RUID: At most one value of type PositiveInteger.
    :param SessionID: At most one value of type PositiveInteger.
    :return: A PropertyBundle object.
    '''

    if not isinstance(open_file_descriptor_refs, Missing):
        assert isinstance(open_file_descriptor_refs, list),\
        "[propbundle_UNIXProcess] open_file_descriptor_refs must be of type List of Integer."
        assert all(isinstance(i, int) for i in open_file_descriptor_refs),\
        "[propbundle_UNIXProcess] open_file_descriptor_refs must be of type List of Integer."
    if not isinstance(priority, Missing):
        assert (isinstance(priority, int) and (priority > 0)),\
        "[propbundle_UNIXProcess] priority must be of type PositiveInteger."
    if not isinstance(ruid, Missing):
        assert (isinstance(ruid, int) and (ruid > 0)),\
        "[propbundle_UNIXProcess] ruid must be of type PositiveInteger."
    if not isinstance(session_id, Missing):
        assert (isinstance(session_id, int) and (session_id > 0)),\
        "[propbundle_UNIXProcess] session_id must be of type PositiveInteger."

    return uco_object.create_PropertyBundle('UNIXProcess', OpenFileDescriptorRefs=open_file_descriptor_refs,
                                            Priority=priority, RUID=ruid, SessionID=session_id)


def propbundle_UNIXVolume(uco_object, mount_point=Missing(), options=Missing()):
    '''
    :param MountPoint: At most one value of type String.
    :param Options: At most one value of type String.
    :return: A PropertyBundle objects.
    '''

    if not isinstance(mount_point, Missing):
        assert isinstance(mount_point, str),\
        "[propbundle_UNIXVolume] mount_point must be of type String."
    if not isinstance(options, Missing):
        assert isinstance(options, str),\
        "[propbundle_UNIXVolume] options must be of type String."

    return uco_object.create_PropertyBundle('UNIXVolume', MountPoint=mount_point, Options=options)


def propbundle_URL(uco_object, full_value=Missing(), scheme=Missing(), user_name_ref=Missing(), password_ref=Missing(),
                   host_ref=Missing(), port=Missing(), path=Missing(), query=Missing(), fragment=Missing()):
    '''
    :param FullValue: Exactly one value of type String.
    :param Scheme: At most one value of type String.
    :param UserNameRef: At most one occurrence of type Trace.
    :param PasswordRef: At most one occurrence of type Trace.
    :param HostRef: At most one occurrence of type Trace.
    :param Port: At most one value of type Long.
    :param Path: At most one value of type String.
    :param Query: At most one value of type String.
    :param Fragment: At most one value of type String.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(full_value, Missing),\
    "[propbundle_URL] full_value is required."
    if not isinstance(full_value, Missing):
        assert isinstance(full_value, str),\
        "[propbundle_URL] full_value must be of type String."

    if not isinstance(scheme, Missing):
        assert isinstance(scheme, str),\
        "[propbundle_URL] scheme must be of type String."
    if not isinstance(user_name_ref, Missing):
        assert (isinstance(user_name_ref, case.CoreObject) and (user_name_ref.type=='Trace')),\
        "[propbundle_URL] user_name_ref must be of type Trace."
    if not isinstance(password_ref, Missing):
        assert (isinstance(password_ref, case.CoreObject) and (password_ref.type=='Trace')),\
        "[propbundle_URL] password_ref must be of type Trace."
    if not isinstance(host_ref, Missing):
        assert (isinstance(host_ref, case.CoreObject) and (host_ref.type=='Trace')),\
        "[propbundle_URL] host_ref must be of type Trace."
    if not isinstance(port, Missing):
        assert isinstance(port, long),\
        "[propbundle_URL] port must be of type Long."
    if not isinstance(path, Missing):
        assert isinstance(port, str),\
        "[propbundle_URL] port must be of type String."
    if not isinstance(query, Missing):
        assert isinstance(query, str),\
        "[propbundle_URL] query must be of type String."
    if not isinstance(fragment, Missing):
        assert isinstance(fragment, str),\
        "[propbundle_URL] fragment must be of type String."

    return uco_object.create_PropertyBundle('URL', FullValue=full_value, Scheme=scheme, UserNameRef=user_name_ref,
                                            PasswordRef=password_ref, HostRef=host_ref, Port=port, Path=path,
                                            Query=query, Fragment=fragment)


def propbundle_UserAccount(uco_object, home_directory=Missing(), is_service_account=Missing(), is_privileged=Missing(),
                           can_escalate_privileges=Missing()):
    '''
    :param HomeDirectory: At most one value of type String.
    :param IsServiceAccount: At most one value of type Bool.
    :param IsPrivileged: At most one value of type Bool.
    :param CanEscalatePrivileges: At most one value of type Bool.
    :return: A PropertyBundle object.
    '''

    if not isinstance(home_directory, Missing):
        assert isinstance(home_directory, str),\
        "[propbundle_UserAccount] home_directory must be of type String."
    if not isinstance(is_service_account, Missing):
        assert isinstance(is_service_account, bool),\
        "[propbundle_UserAccount] is_service_account must be of type Bool."
    if not isinstance(is_privileged, Missing):
        assert isinstance(is_privileged, bool),\
        "[propbundle_UserAccount] is_privileged must be of type Bool."
    if not isinstance(can_escalate_privileges, Missing):
        assert isinstance(can_escalate_privileges, bool),\
        "[propbundle_UserAccount] can_escalate_privileges must be of type Bool."

    return uco_object.create_PropertyBundle('UserAccount', HomeDirectory=home_directory,
                                            IsServiceAccount=is_service_account, IsPrivileged=is_privileged,
                                            CanEscalatePrivileges=can_escalate_privileges)


def propbundle_UserSession(uco_object, effective_group=Missing(), effective_group_id=Missing(),
                           effective_user_ref=Missing(), login_time=Missing(), logout_time=Missing()):
    '''
    :param EffectiveGroup: At most one value of type String.
    :param EffectiveGroupID: At most one value of type String.
    :param EffectiveUserRef: At most one occurrence of type Trace.
    :param LoginTime: At most one value of type Datetime.
    :param LogoutTime: At most one value of type Datetime.
    :return: A PropertyBundle object.
    '''

    if not isinstance(effective_group, Missing):
        assert isinstance(effective_group, str),\
        "[propbundle_UserSession] effective_group must be of type String."
    if not isinstance(effective_group_id, Missing):
        assert isinstance(effective_group_id, str),\
        "[propbundle_UserSession] effective_group_id must be of type String."
    if not isinstance(effective_user_ref, Missing):
        assert (isinstance(effective_user_ref, case.CoreObject) and (effective_user_ref.type=='Trace')),\
        "[propbundle_UserSession] effective_user_ref must be of type Trace."
    if not isinstance(login_time, Missing):
        assert isinstance(login_time, datetime.datetime),\
        "[propbundle_UserSession] login_time must be of type Datetime."
    if not isinstance(logout_time, Missing):
        assert isinstance(logout_time, datetime.datetime),\
        "[propbundle_UserSession] logout_time must be of type Datetime."

    return uco_object.create_PropertyBundle('UserSession', EffectiveGroup=effective_group,
                                            EffectiveGroupID=effective_group_id, EffectiveUserRef=effective_user_ref,
                                            LoginTime=login_time, LogoutTime=logout_time)


def propbundle_Volume(uco_object, volume_id=Missing(), sector_size=Missing()):
    '''
    :param VolumeID: At most one value of type String.
    :param SectorSize: At most one value of type Long.
    :return: A PropertyBundle object.
    '''

    if not isinstance(volume_id, Missing):
        assert isinstance(volume_id, str),\
        "[propbundle_Volume] volume_id must be of type String."
    if not isinstance(sector_size, Missing):
        assert isinstance(sector_size, str),\
        "[propbundle_Volume] sector_size must be of type String."

    return uco_object.create_PropertyBundle('Volume', VolumeID=volume_id, SectorSize=sector_size)


def propbundle_WhoIs(uco_object, lookup_date=Missing(), domain_name_ref=Missing(), domain_id=Missing(),
                     server_name_ref=Missing(), ip_address_ref=Missing(), name_server_refs=Missing(),
                     updated_date=Missing(), creation_date=Missing(), expiration_date=Missing(),
                     sponsoring_registrar=Missing(), registrar_info=Missing(), registrant_ids=Missing(),
                     contact_info=Missing(), remarks=Missing()):
    '''
    :param LookupDate: At most one value of type Datetime.
    :param DomainNameRef: At most one occurrence of type Trace.
    :param DomainID: At most one value of type String.
    :param ServerNameRef: At most one occurrence of type Trace.
    :param IPAddressRef: At most one occurrence of type Trace.
    :param NameServerRefs: Any number of occurrences of type Trace.
    :param UpdatedDate: At most one value of type Datetime.
    :param CreationDate: At most one value of type Datetime.
    :param ExpirationDate: At most one value of type Datetime.
    :param SponsoringRegistrar: At most one value of type String.
    :param RegistrarInfo: At most one occurrence of type WhoIsRegistrarInfoType.
    :param RegistrantIDs: Any number of values of type String.
    :param ContactInfo: Any number of occurrences of type WhoIsContactType.
    :param Remarks: At most one value of type String.
    :return: A PropertyBundle object.
    '''

    if not isinstance(lookup_date, Missing):
        assert isinstance(lookup_date, datetime.datetime),\
        "[propbundle_WhoIs] lookup_date must be of type Datetime."
    if not isinstance(domain_name_ref, Missing):
        assert (isinstance(domain_name_ref, case.CoreObject) and (domain_name_ref.type=='Trace')),\
        "[propbundle_WhoIs] domain_name_ref must be of type Trace."
    if not isinstance(domain_id, Missing):
        assert isinstance(domain_id, str),\
        "[propbundle_WhoIs] domain_id must be of type String."
    if not isinstance(server_name_ref, Missing):
        assert (isinstance(server_name_ref, case.CoreObject) and (server_name_ref.type=='Trace')),\
        "[propbundle_WhoIs] server_name_ref must be of type Trace."
    if not isinstance(ip_address_ref, Missing):
        assert (isinstance(ip_address_ref, case.CoreObject) and (ip_address_ref.type=='Trace')),\
        "[propbundle_WhoIs] ip_address_ref must be of type Trace."
    if not isinstance(name_server_refs, Missing):
        assert isinstance(name_server_refs, list),\
        "[propbundle_WhoIs] name_server_refs must be of type List of Trace."
        assert all( (isinstance(i, case.CoreObject) and i.type=='Trace') for i in name_server_refs),\
        "[propbundle_WhoIs] name_server_refs must be of type List of Trace."
    if not isinstance(updated_date, Missing):
        assert isinstance(updated_date, datetime.datetime),\
        "[propbundle_WhoIs] updated_date must be of type Datetime."
    if not isinstance(creation_date, Missing):
        assert isinstance(creation_date, datetime.datetime),\
        "[propbundle_WhoIs] creation_date must be of type Datetime."
    if not isinstance(expiration_date, Missing):
        assert isinstance(expiration_date, datetime.datetime),\
        "[propbundle_WhoIs] expiration_date must be of type Datetime."
    if not isinstance(sponsoring_registrar, Missing):
        assert isinstance(sponsoring_registrar, str),\
        "[propbundle_WhoIs] sponsoring_registrar must be of type String."
    if not isinstance(registrar_info, Missing):
        assert (isinstance(registrar_info, case.DuckObject) and (registrar_info.type=='WhoIsRegistrarInfoType')),\
        "[propbundle_WhoIs] registrar_info must be of type WhoIsRegistrarInfoType."
    if not isinstance(registrant_ids, Missing):
        assert isinstance(registrant_ids, list),\
        "[propbundle_WhoIs] registrant_ids must be of type List of String."
        assert all(isinstance(i, str) for i in registrant_ids),\
        "[propbundle_WhoIs] registrant_ids must be of type List of String."
    if not isinstance(contact_info, Missing):
        assert isinstance(contact_info, list),\
        "[propbundle_WhoIs] contact_info must be of type List of WhoIsContactType."
        assert all( (isinstance(i, case.DuckObject) and i.type=='WhoIsContactType') for i in contact_info),\
        "[propbundle_WhoIs] contact_info must be of type List of WhoIsContactType."
    if not isinstance(remarks, Missing):
        assert isinstance(remarks, str),\
        "[propbundle_WhoIs] remarks must be of type String."

    return uco_object.create_PropertyBundle('WhoIs', LookupDate=lookup_date, DomainNameRef=domain_name_ref,
                                            DomainID=domain_id, ServerNameRef=server_name_ref,
                                            IPAddressRef=ip_address_ref, NameServerRefs=name_server_refs,
                                            UpdatedDate=updated_date, CreationDate=creation_date,
                                            ExpirationDate=expiration_date, SponsoringRegistrar=sponsoring_registrar,
                                            RegistrarInfo=registrar_info, RegistrantIDs=registrant_ids,
                                            ContactInfo=contact_info, Remarks=remarks)


def propbundle_WindowsAccount(uco_object, groups=Missing()):
    '''
    :param Groups: At least one value of type String.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(groups, Missing),\
    "[propbundle_WindowsAccount] groups is required."
    if not isinstance(groups, Missing):
        assert isinstance(groups, list),\
        "[propbundle_WindowsAccount] groups must be of type List of String."
        assert all(isinstance(i, str) for i in groups),\
        "[propbundle_WindowsAccount] groups must be of type List of String."

    return uco_object.create_PropertyBundle('WindowsAccount', Groups=groups)


def propbundle_WindowsActiveDirectoryAccount(uco_object, object_guid=Missing(), active_directory_groups=Missing()):
    '''
    :param ObjectGUID: Exactly one value of type String.
    :param ActiveDirectoryGroups: Any number of values of type String.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(object_guid, Missing),\
    "[propbundle_WindowsActiveDirectoryAccount] object_guid is required."
    if not isinstance(object_guid, Missing):
        assert isinstance(object_guid, str),\
        "[propbundle_WindowsActiveDirectoryAccount] object_guid must be of type String."

    if not isinstance(active_directory_groups, Missing):
        assert isinstance(active_directory_groups, list),\
        "[propbundle_WindowsActiveDirectoryAccount] active_directory_groups must be of type List of String."
        assert all(isinstance(i, str) for i in active_directory_groups),\
        "[propbundle_WindowsActiveDirectoryAccount] active_directory_groups must be of type List of String."

    return uco_object.create_PropertyBundle('WindowsActiveDirectoryAccount', ObjectGUID=object_guid,
                                            ActiveDirectoryGroups=active_directory_groups)


def propbundle_WindowsComputerSpecification(uco_object, domain=Missing(), global_flag_list=Missing(),
                                            net_bios_name=Missing(), ms_product_id=Missing(),
                                            ms_product_name=Missing(), registered_organization_ref=Missing(),
                                            registered_owner_ref=Missing(), windows_directory_ref=Missing(),
                                            windows_system_directory_ref=Missing(),
                                            windows_temp_directory_ref=Missing()):
    '''
    :param Domain: Any number of values of type String.
    :param GlobalFlagList: Any number of occurrences of type GlobalFlagType.
    :param NetBIOSName: At most one value of type String.
    :param MsProductID: At most one value of type String.
    :param MsProductName: At most one value of type String.
    :param RegisteredOrganizationRef: At most one occurrence of type Identity (core).
    :param RegisteredOwnerRef: At most one occurrence of type Identity (core).
    :param WindowsDirectoryRef: Ata most one occurrence of type Trace.
    :param WindowsSystemDirectoryRef: At most one occurrence of type Trace.
    :param WindowsTempDirectoryRef: At most one occurrence of type Trace.
    :return: A PropertyBundle object.
    '''

    if not isinstance(domain, Missing):
        assert isinstance(domain, list),\
        "[propbundle_WindowsComputerSpecification] domain must be of type List of String."
        assert all(isinstance(i, str) for i in domain),\
        "[propbundle_WindowsComputerSpecification] domain must be of type List of String."
    if not isinstance(global_flag_list, Missing):
        assert isinstance(global_flag_list, list),\
        "[propbundle_WindowsComputerSpecification] global_flag_list must be of type List of GlobalFlagType."
        assert all( (isinstance(i, case.DuckObject) and i.type=='GlobalFlagType') for i in global_flag_list),\
        "[propbundle_WindowsComputerSpecification] global_flag_list must be of type List of GlobalFlagType."
    if not isinstance(net_bios_name, Missing):
        assert isinstance(net_bios_name, str),\
        "[propbundle_WindowsComputerSpecification] net_bios_name must be of type String."
    if not isinstance(ms_product_id, Missing):
        assert isinstance(ms_product_id, str),\
        "[propbundle_WindowsComputerSpecification] ms_product_id must be of type String."
    if not isinstance(ms_product_name, Missing):
        assert isinstance(ms_product_name, str),\
        "[propbundle_WindowsComputerSpecification] ms_product_name must be of type String."
    if not isinstance(registered_organization_ref, Missing):
        assert (isinstance(registered_organization_ref, case.CoreObject) and (registered_organization_ref.type=='Identity (core)')),\
        "[propbundle_WindowsComputerSpecification] registered_organization_ref must be of type Identity (core)."
    if not isinstance(windows_directory_ref, Missing):
        assert (isinstance(windows_directory_ref, case.CoreObject) and (windows_directory_ref.type=='Trace')),\
        "[propbundle_WindowsComputerSpecification] windows_directory_ref must be of type Trace."
    if not isinstance(windows_system_directory_ref, Missing):
        assert (isinstance(windows_system_directory_ref, case.CoreObject) and (windows_system_directory_ref.type=='Trace')),\
        "[propbundle_WindowsComputerSpecification] windows_system_directory_ref must be of type Trace."
    if not isinstance(windows_temp_directory_ref, Missing):
        assert (isinstance(windows_temp_directory_ref, case.CoreObject) and (windows_temp_directory_ref.type=='Trace')),\
        "[propbundle_WindowsComputerSpecification] windows_temp_directory_ref must be of type Trace."
        
    return uco_object.create_PropertyBundle('WindowsComputerSpecification', Domain=domain,
                                            GlobalFlagList=global_flag_list, NetBIOSName=net_bios_name,
                                            MsProductID=ms_product_id, MsProductName=ms_product_name,
                                            RegisteredOrganizationRef=registered_organization_ref,
                                            RegisteredOwnerRef=registered_owner_ref,
                                            WindowsDirectoryRef=windows_directory_ref,
                                            WindowsSystemDirectoryRef=windows_system_directory_ref,
                                            WindowsTempDirectoryRef=windows_temp_directory_ref)


def propbundle_WindowsPEBinaryFile(uco_object, machine=Missing(), pe_type=Missing(), imp_hash=Missing(),
                                   number_of_sections=Missing(), datetime_stamp=Missing(),
                                   pointer_to_symbol_table=Missing(), size_of_optional_header=Missing(),
                                   characteristics=Missing(), file_header_hashes=Missing(),
                                   optional_header=Missing(), sections=Missing()):
    '''
    :param Machine: Exactly one value of type HexBinary.
    :param PEType: At most one occurrence of type Controlled Vocabulary.
    :param ImpHash: At most one value of type String.
    :param NumberOfSections: At most one value of type Integer.
    :param DatetimeStamp: At most one value of type Datetime.
    :param PointerToSymbolTable: At most one value of type HexBinary.
    :param NumberOfSymbols: At most one value of type Integer.
    :param SizeOfOptionalHeader: At most one value of type Integer.
    :param Characteristics: At most one value of type HexBinary.
    :param FileHeaderHashes: Any number of occurrences of type Hash.
    :param OptionalHeader: At most once occurrence of type WindowsPEOptionalHeader.
    :param Sections: Any number of occurrences of type WindowsPESection.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(machine, Missing),\
    "[propbundle_WindowsPEBinaryFile] machine is required."
    #TODO:HexBinary

    if not isinstance(pe_type, Missing):
        assert (isinstance(pe_type, case.CoreObject) and (pe_type.type=='ControlledVocabulary')),\
        "[propbundle_WindowsPEBinaryFile] pe_type must be of type ControlledVocabulary."
    if not isinstance(imp_hash, Missing):
        assert isinstance(imp_hash, str),\
        "[propbundle_WindowsPEBinaryFile] imp_hash must be of type String."
    if not isinstance(number_of_sections, Missing):
        assert isinstance(number_of_sections, int),\
        "[propbundle_WindowsPEBinaryFile] number_of_sections must be of type Integer."
    if not isinstance(datetime_stamp, Missing):
        assert isinstance(datetime_stamp, datetime.datetime),\
        "[propbundle_WindowsPEBinaryFile] datetime_stamp must be of type Datetime."
    #TODO:HexBinary
    if not isinstance(pointer_to_symbol_table, Missing):
        assert isinstance(pointer_to_symbol_table, int),\
        "[propbundle_WindowsPEBinaryFile] number_of_symbols must be of type Integer."
    if not isinstance(size_of_optional_header, Missing):
        assert isinstance(size_of_optional_header, int),\
        "[propbundle_WindowsPEBinaryFile] size_of_optional_header must be of type Integer."
    #TODO:HexBinary
    if not isinstance(file_header_hashes, Missing):
        assert isinstance(file_header_hashes, list),\
        "[propbundle_WindowsPEBinaryFile] file_header_hashes must be of type List of Hash."
        assert all( (isinstance(i, case.DuckObject) and i.type=='Hash') for i in file_header_hashes),\
        "[propbundle_WindowsPEBinaryFile] file_header_hashes must be of type List of Hash."
    if not isinstance(optional_header, Missing):
        assert (isinstance(optional_header, case.DuckObject) and (optional_header.type=='WindowsPEOptionalHeader')),\
        "[propbundle_WindowsPEBinaryFile] pe_type must be of type WindowsPEOptionalHeader."
    if not isinstance(sections, Missing):
        assert isinstance(sections, list),\
        "[propbundle_WindowsPEBinaryFile] sections must be of type List of WindowsPESection."
        assert all( (isinstance(i, case.DuckObject) and i.type=='WindowsPESection') for i in sections),\
        "[propbundle_WindowsPEBinaryFile] sections must be of type List of WindowsPESection."

    return uco_object.create_PropertyBundle('WindowsPEBinaryFile', Machine=machine, PEType=pe_type,
                                            ImpHash=imp_hash, NumberOfSections=number_of_sections,
                                            DatetimeStamp=datetime_stamp, PointerToSymbolTable=pointer_to_symbol_table,
                                            NumberOfSymbols=pointer_to_symbol_table,
                                            SizeOfOptionalHeader=size_of_optional_header,
                                            Characteristics=characteristics,
                                            FileHeaderHashes=file_header_hashes, OptionalHeader=optional_header,
                                            Sections=sections)


def propbundle_WindowsPrefetch(uco_object, application_file_name=Missing(), prefetch_hash=Missing(),
                               times_executed=Missing(), first_run=Missing(), last_run=Missing(),
                               volume_ref=Missing(), accessed_file_refs=Missing(),
                               accessed_directory_refs=Missing()):
    '''
    :param ApplicationFileName: At most one value of type String.
    :param PrefetchHash: At most one value of type String.
    :param TimesExecuted: At most one value of type Long.
    :param FirstRun: At most one value of type Datetime.
    :param LastRun: At most one value of type Datetime.
    :param VolumeRef: At most one occurrence of type Trace.
    :param AccessedFileRefs: Any number of occurrences of type Trace.
    :param AccessedDirectoryRefs: Any number of occurrences of type Trace.
    :return: A PropertyBundle object.
    '''

    if not isinstance(application_file_name, Missing):
        assert isinstance(application_file_name, str),\
        "[propbundle_WindowsPrefetch] application_file_name must be of type String."
    if not isinstance(prefetch_hash, Missing):
        assert isinstance(prefetch_hash, str),\
        "[propbundle_WindowsPrefetch] prefetch_hash must be of type String."
    if not isinstance(times_executed, Missing):
        assert isinstance(times_executed, long),\
        "[propbundle_WindowsPrefetch] times_executed must be of type Long."
    if not isinstance(first_run, Missing):
        assert isinstance(first_run, long),\
        "[propbundle_WindowsPrefetch] first_run must be of type Datetime."
    if not isinstance(last_run, Missing):
        assert isinstance(last_run, datetime.datetime),\
        "[propbundle_WindowsPrefetch] last_run must be of type Datetime."
    if not isinstance(volume_ref, Missing):
        assert (isinstance(volume_ref, case.CoreObject) and (volume_ref.type=='Trace')),\
        "[propbundle_WindowsPrefetch] volume_ref must be of type Trace."
    if not isinstance(accessed_file_refs, Missing):
        assert isinstance(accessed_file_refs, list),\
        "[propbundle_WindowsPrefetch] accessed_file_refs must be of type List of Trace."
        assert all( (isinstance(i, case.CoreObject) and i.type=='Trace') for i in accessed_file_refs),\
        "[propbundle_WindowsPrefetch] accessed_file_refs must be of type List of Trace."
    if not isinstance(accessed_directory_refs, Missing):
        assert isinstance(accessed_directory_refs, list),\
        "[propbundle_WindowsPrefetch] accessed_directory_refs must be of type List of Trace."
        assert all( (isinstance(i, case.CoreObject) and i.type=='Trace') for i in accessed_directory_refs),\
        "[propbundle_WindowsPrefetch] accessed_directory_refs must be of type List of Trace."

    return uco_object.create_PropertyBundle('WindowsPrefetch', ApplicationFileName=application_file_name,
                                            PrefetchHash=prefetch_hash, TimesExecuted=times_executed,
                                            FirstRun=first_run, LastRun=last_run,
                                            VolumeRef=volume_ref, AccessedFileRefs=accessed_file_refs,
                                            AccessedDirectoryRefs=accessed_directory_refs)


def propbundle_WindowsProcess(uco_object, aslr_enabled=Missing(), dep_enabled=Missing(), priority=Missing(),
                              owner_sid=Missing(), window_title=Missing(), startup_info=Missing()):
    '''
    :param ASLREnabled: At most one value of type Bool.
    :param DEPEnabled: At most one value of type Bool.
    :param Priority: At most one value of type String.
    :param OwnerSID: At most one value of type String.
    :param WindowTitle: At most one value of type String.
    :param StartupInfo: At most one occurrence of type Dictionary.
    :return: A PropertyBundle object.
    '''

    if not isinstance(aslr_enabled, Missing):
        assert isinstance(aslr_enabled, bool),\
        "[propbundle_WindowsProcess] aslr_enabled must be of type Bool."
    if not isinstance(dep_enabled, Missing):
        assert isinstance(dep_enabled, bool),\
        "[propbundle_WindowsProcess] dep_enabled must be of type Bool."
    if not isinstance(priority, Missing):
        assert isinstance(priority, str),\
        "[propbundle_WindowsProcess] priority must be of type String."
    if not isinstance(owner_sid, Missing):
        assert isinstance(owner_sid, str),\
        "[propbundle_WindowsProcess] priority must be of type String."
    if not isinstance(window_title, Missing):
        assert isinstance(window_title, str),\
        "[propbundle_WindowsProcess] window_title must be of type String."
    if not isinstance(startup_info, Missing):
        assert (isinstance(startup_info, case.DuckObject) and (startup_info.type=='Dictionary')),\
        "[propbundle_WindowsProcess] startup_info must be of type Dictionary."

    return uco_object.create_PropertyBundle('WindowsProcess', ASLREnabled=aslr_enabled, DEPEnabled=dep_enabled,
                                            Priority=priority, OwnerSID=owner_sid, WindowTitle=window_title,
                                            StartupInfo=startup_info)


def propbundle_WindowsRegistryHive(uco_object, hive_type=Missing()):
    '''
    :param HiveType: Exactly one value of type String.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(hive_type, Missing),\
    "[propbundle_WindowsRegistryHive] hive_type is required."
    if not isinstance(hive_type, Missing):
        assert isinstance(hive_type, str),\
        "[propbundle_WindowsRegistryHive] hive_type must be of type String."

    return uco_object.create_PropertyBundle('WindowsRegistryHive', HiveType=hive_type)


def propbundle_WindowsRegistryKey(uco_object, key=Missing(), values=Missing(), modified_time=Missing(),
                                  creator_ref=Missing(), number_of_subkeys=Missing()):
    '''
    :param Key: Exactly one value of type String.
    :param Values: Any number of occurrences of type WindowsRegistryHive.
    :param ModifiedTime: At most one value of type Datetime.
    :param CreatorRef: At most one occurrence of type Trace.
    :param NumberOfSubkeys: At most one value of type Integer.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(key, Missing),\
    "[propbundle_WindowsRegistryKey] key is required."
    if not isinstance(key, Missing):
        assert isinstance(key, str),\
        "[propbundle_WindowsRegistryKey] key must be of type String."

    if not isinstance(values, Missing):
        assert isinstance(values, list),\
        "[propbundle_WindowsRegistryKey] values must be of type List of WindowsRegistryHive."
        assert all( (isinstance(i, case.PropertyBundle) and i.type=='WindowsRegistryHive') for i in values),\
        "[propbundle_WindowsRegistryKey] values must be of type List of WindowsRegistryHive."
    if not isinstance(modified_time, Missing):
        assert isinstance(modified_time, datetime.datetime),\
        "[propbundle_WindowsRegistryKey] modified_time must be of type Datetime."
    if not isinstance(creator_ref, Missing):
        assert (isinstance(creator_ref, case.CoreObject) and (creator_ref.type=='Trace')),\
        "[propbundle_WindowsRegistryKey] creator_ref must be of type Trace."
    if not isinstance(number_of_subkeys, Missing):
        assert isinstance(number_of_subkeys, int),\
        "[propbundle_WindowsRegistryKey] number_of_subkeys must be of type Integer."

    return uco_object.create_PropertyBundle('WindowsRegistryKey', Key=key, Values=values, ModifiedTime=modified_time,
                                            CreatorRef=creator_ref, NumberOfSubkeys=number_of_subkeys)


def propbundle_WindowsService(uco_object, service_name=Missing(), descriptions=Missing(), display_name=Missing(),
                              group_name=Missing(), start_command_line=Missing(), start_type=Missing(),
                              service_type=Missing(), service_status=Missing()):
    '''
    :param ServiceName: Exactly one value of type String.
    :param Descriptions: Any number of values of type String.
    :param DisplayName: At most one value of type String.
    :param GroupName: At most one value of type String.
    :param StartCommandLine: At most one value of type String.
    :param StartType: At most one occurrence of type ControlledVocabulary.
    :param ServiceType: At most one occurrence of type ControlledVocabulary.
    :param ServiceStatus: At most one occurrence of type ControlledVocabulary.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(service_name, Missing),\
    "[propbundle_WindowsService] service_name is required."
    if not isinstance(service_name, Missing):
        assert isinstance(service_name, str),\
        "[propbundle_WindowsService] service_name must be of type String."

    if not isinstance(descriptions, Missing):
        assert isinstance(descriptions, list),\
        "[propbundle_WindowsService] descriptions must be of type List of String."
        assert all(isinstance(i, str) for i in descriptions),\
        "[propbundle_WindowsService] descriptions must be of type List of String."
    if not isinstance(display_name, Missing):
        assert isinstance(display_name, str),\
        "[propbundle_WindowsService] display_name must be of type String."
    if not isinstance(group_name, Missing):
        assert isinstance(group_name, str),\
        "[propbundle_WindowsService] group_name must be of type String."
    if not isinstance(start_command_line, Missing):
        assert isinstance(start_command_line, str),\
        "[propbundle_WindowsService] start_command_line must be of type String."
    if not isinstance(start_type, Missing):
        assert (isinstance(start_type, case.CoreObject) and (start_type.type=='ControlledVocabulary')),\
        "[propbundle_WindowsTask] start_type must be of type ControlledVocabulary."
    if not isinstance(service_type, Missing):
        assert (isinstance(service_type, case.CoreObject) and (service_type.type=='ControlledVocabulary')),\
        "[propbundle_WindowsTask] service_type must be of type ControlledVocabulary."
    if not isinstance(service_status, Missing):
        assert (isinstance(service_status, case.CoreObject) and (service_status.type=='ControlledVocabulary')),\
        "[propbundle_WindowsTask] service_status must be of type ControlledVocabulary."

    return uco_object.create_PropertyBundle('WindowsService', ServiceName=service_name, Descriptions=descriptions,
                                            DisplayName=display_name, GroupName=group_name,
                                            StartCommandLine=start_command_line, StartType=start_type,
                                            ServiceType=service_type, ServiceStatus=service_status)


def propbundle_WindowsTask(uco_object, image_name=Missing(), application_ref=Missing(), parameters=Missing(),
                           account_ref=Missing(), account_run_level=Missing(), account_logon_type=Missing(),
                           creator=Missing(), created_time=Missing(), most_recent_run_time=Missing(),
                           exit_code=Missing(), max_run_time=Missing(), next_run_time=Missing(),
                           action_list=Missing(), trigger_list=Missing(), comment=Missing(),
                           working_directory=Missing(), work_item_data_ref=Missing()):
    '''
    :param ImageName: At most one value of type String.
    :param ApplicationRef: At most one occurrence of type Trace.
    :param Parameters: At most one value of type String.
    :param AccountRef: At most one occurrence of type Trace.
    :param AccountRunLevel: At most one value of type String.
    :param AccountLogonType: At most one value of type String.
    :param Creator: At most one value of type String.
    :param CreatedTime: At most one value of type Datetime.
    :param MostRecentRunTime: At most one value of type Datetime.
    :param ExitCode: At most one value of type Long.
    :param MaxRunTime: At most one value of type Long.
    :param NextRunTime: At most one value of type Datetime.
    :param ActionList: Any number of occurrences of type TaskActionType.
    :param TriggerList: Any number of occurrences of type TriggerType.
    :param Comment: At most one value of type String.
    :param WorkingDirectory: At most one occurrence of type Trace.
    :param WorkItemDataRef: At most one occurrence of type Trace.
    :return: A PropertyBundle object.
    '''

    if not isinstance(image_name, Missing):
        assert isinstance(image_name, str),\
        "[propbundle_WindowsTask] image_name must be of type String."
    if not isinstance(application_ref, Missing):
        assert (isinstance(application_ref, case.CoreObject) and (application_ref.type=='Trace')),\
        "[propbundle_WindowsTask] application_ref must be of type Trace."
    if not isinstance(parameters, Missing):
        assert isinstance(parameters, str),\
        "[propbundle_WindowsTask] parameters must be of type String."
    if not isinstance(account_ref, Missing):
        assert (isinstance(account_ref, case.CoreObject) and (account_ref.type=='Trace')),\
        "[propbundle_WindowsTask] account_ref must be of type Trace."
    if not isinstance(account_run_level, Missing):
        assert isinstance(account_run_level, str),\
        "[propbundle_WindowsTask] account_run_level must be of type String."
    if not isinstance(account_logon_type, Missing):
        assert isinstance(account_logon_type, str),\
        "[propbundle_WindowsTask] account_logon_type must be of type String."
    if not isinstance(creator, Missing):
        assert isinstance(creator, str),\
        "[propbundle_WindowsTask] creator must be of type String."
    if not isinstance(created_time, Missing):
        assert isinstance(created_time, datetime.datetime),\
        "[propbundle_WindowsTask] created_time must be of type Datetime."
    if not isinstance(most_recent_run_time, Missing):
        assert isinstance(most_recent_run_time, datetime.datetime),\
        "[propbundle_WindowsTask] most_recent_run_time must be of type Datetime."
    if not isinstance(exit_code, Missing):
        assert isinstance(exit_code, long),\
        "[propbundle_WindowsTask] exit_code must be of type Long."
    if not isinstance(max_run_time, Missing):
        assert isinstance(max_run_time, long),\
        "[propbundle_WindowsTask] max_run_time must be of type Long."
    if not isinstance(next_run_time, Missing):
        assert isinstance(next_run_time, datetime.datetime),\
        "[propbundle_WindowsTask] next_run_time must be of type Datetime."
    if not isinstance(action_list, Missing):
        assert isinstance(action_list, list),\
        "[propbundle_WindowsTask] action_list must be of type List of TaskActionType."
        assert all( (isinstance(i, case.DuckObject) and i.type=='TaskActionType') for i in action_list),\
        "[propbundle_WindowsTask] action_list must be of type List of TaskActionType."
    if not isinstance(trigger_list, Missing):
        assert isinstance(trigger_list, list),\
        "[propbundle_WindowsTask] trigger_list must be of type List of TriggerType."
        assert all( (isinstance(i, case.DuckObject) and i.type=='TriggerType') for i in trigger_list),\
        "[propbundle_WindowsTask] trigger_list must be of type List of TriggerType."
    if not isinstance(comment, Missing):
        assert isinstance(comment, str),\
        "[propbundle_WindowsTask] comment must be of type String."
    if not isinstance(working_directory, Missing):
        assert (isinstance(working_directory, case.CoreObject) and (working_directory.type=='Trace')),\
        "[propbundle_WindowsTask] working_directory must be of type Trace."
    if not isinstance(work_item_data_ref, Missing):
        assert (isinstance(work_item_data_ref, case.CoreObject) and (application_ref.type=='Trace')),\
        "[propbundle_WindowsTask] work_item_data_ref must be of type Trace."

    return uco_object.create_PropertyBundle('WindowsTask', ImageName=image_name, ApplicationRef=application_ref,
                                            Parameters=parameters, AccountRef=account_ref,
                                            AccountRunLevel=account_run_level,
                                            AccountLogonType=account_logon_type, Creator=creator,
                                            CreatedTime=created_time, MostRecentRunTime=most_recent_run_time,
                                            ExitCode=exit_code, MaxRunTime=max_run_time, NextRunTime=next_run_time,
                                            ActionList=action_list, TriggerList=trigger_list, Comment=comment,
                                            WorkingDirectory=working_directory, WorkItemDataRef=work_item_data_ref)


def propbundle_WindowsThread(uco_object, thread_id=Missing(), running_status=Missing(), context=Missing(),
                             priority=Missing(), creation_flags=Missing(), creation_time=Missing(),
                             start_address=Missing(), parameter_address=Missing(), security_attributes=Missing(),
                             stack_size=Missing()):
    '''
    :param ThreadID: At most one value of type PositiveInteger.
    :param RunningStatus: At most one occurence of type ControlledVocabulary.
    :param Context: At most one value of type String.
    :param Priority: At most one value of type Integer.
    :param CreationFlags: At most one value of type HexBinary.
    :param CreationTime: At most one value of type Datetime.
    :param StartAddress: At most one value of type HexBinary.
    :param ParameterAddress: At most one value of type HexBinary.
    :param SecurityAttributes: At most one value of type String.
    :param StackSize: At most one value of type PositiveInteger.
    :return: A PropertyBundle object.
    '''

    if not isinstance(thread_id, Missing):
        assert (isinstance(thread_id, int) and (thread_id > 0)),\
        "[propbundle_WindowsThread] thread_id must be of type PositiveInteger."
    if not isinstance(running_status, Missing):
        assert (isinstance(running_status, case.CoreObject) and (running_status.type=='ControlledVocabulary')),\
        "[propbundle_WindowsThread] running_status must be of type Hash."
    if not isinstance(context, Missing):
        assert isinstance(context, str),\
        "[propbundle_WindowsThread] context must be of type String."
    if not isinstance(priority, Missing):
        assert isinstance(priority, int),\
        "[propbundle_WindowsThread] priority must be of type Integer."
    #TODO:HexBinary
    if not isinstance(creation_time, Missing):
        assert isinstance(creation_time, datetime.datetime),\
        "[propbundle_WindowsThread] creation_time must be of type Datetime."
    #TODO:HexBinary
    #TODO:HexBinary
    if not isinstance(security_attributes, Missing):
        assert isinstance(security_attributes, str),\
        "[propbundle_WindowsThread] security_attributes must be of type String."
    if not isinstance(stack_size, Missing):
        assert (isinstance(stack_size, int) and (thread_id > 0)),\
        "[propbundle_WindowsThread] stack_size must be of type PositiveInteger."

    return uco_object.create_PropertyBundle('WindowsThread', ThreadID=thread_id, RunningStatus=running_status,
                                            Context=context, Priority=priority, CreationFlags=creation_flags,
                                            CreationTime=creation_time, StartAddress=start_address,
                                            ParameterAddress=parameter_address, SecurityAttributes=security_attributes,
                                            StackSize=stack_size)


def propbundle_WindowsVolume(uco_object, drive_letter=Missing()):
    '''
    :param DriveLetter: Exactly one value of type String.
    :return: A PropertyBundle object.
    '''

    assert not isinstance(drive_letter, Missing),\
    "[propbundle_WindowsVolume] drive_letter is required."
    if not isinstance(drive_letter, Missing):
        assert isinstance(drive_letter, str),\
        "[propbundle_WindowsVolume] drive_letter must be of type String."

    return uco_object.create_PropertyBundle('WindowsVolume', DriveLetter=drive_letter)


def propbundle_WirelessNetworkConnection(uco_object, base_station=Missing(), ssid=Missing()):
    '''
    :param BaseStation: At most one value of type String.
    :param SSID: At most one value of type String.
    :return: A PropertyBundle object.
    '''

    if not isinstance(base_station, Missing):
        assert isinstance(base_station, str),\
        "[propbundle_WirelessNetworkConnection] base_station must be of type String."
    if not isinstance(ssid, Missing):
        assert isinstance(ssid, str),\
        "[propbundle_WirelessNetworkConnection] ssid must be of type String."

    return uco_object.create_PropertyBundle('WirelessNetworkConnection', BaseStation=base_station, SSID=ssid)


def propbundle_X509Certificate(uco_object, is_self_signed=Missing(), version=Missing(), serial_number=Missing(),
                               signature_algorithm=Missing(), signature=Missing(), issuer=Missing(),
                               issuer_hash=Missing(), validity_not_before=Missing(), validity_not_after=Missing(),
                               subject=Missing(), subject_hash=Missing(), subject_public_key_algorithm=Missing(),
                               subject_public_key_modulus=Missing(), subject_public_key_exponent=Missing(),
                               x509V3Extensions=Missing(), thumbprint_hash=Missing()):
    '''
    :param IsSelfSigned: At most one value of type Bool.
    :param Version: At most one value of type String.
    :param SerialNumber: At most one value of type String.
    :param SignatureAlgorithm: At most one value of type String.
    :param Signature: At most one value of type String.
    :param Issuer: At most one value of type String.
    :param IssuerHash: At most one occurrence of type Hash.
    :param ValidityNotBefore: At most one value of type Datetime.
    :param ValidityNotAfter: At most one value of type Datetime.
    :param Subject: At most one value of type String.
    :param SubjectHash: At most one occurrence of type Hash.
    :param SubjectPublicKeyAlgorithm: At most one value of type String.
    :param SubjectPublicKeyModulus: At most one value of type String.
    :param SubjectPublicKeyExponent: At most one value of type Integer.
    :param Extensions: At most one occurrence of type X509V3Extensions.
    :param ThumbprintHash: At most one occurrence of type Hash.
    :return: A PropertyBundle object.
    '''

    if not isinstance(is_self_signed, Missing):
        assert isinstance(is_self_signed, bool),\
        "[propbundle_X509Certificate] is_self_signed must be of type Bool."
    if not isinstance(version, Missing):
        assert isinstance(version, str),\
        "[propbundle_X509Certificate] version must be of type String."
    if not isinstance(serial_number, Missing):
        assert isinstance(serial_number, str),\
        "[propbundle_X509Certificate] serial_number must be of type String."
    if not isinstance(signature_algorithm, Missing):
        assert isinstance(signature_algorithm, str),\
        "[propbundle_X509Certificate] signature_algorithm must be of type String."
    if not isinstance(signature, Missing):
        assert isinstance(signature, str),\
        "[propbundle_X509Certificate] signature must be of type String."
    if not isinstance(issuer, Missing):
        assert isinstance(issuer, str),\
        "[propbundle_X509Certificate] issuer must be of type String."
    if not isinstance(issuer_hash, Missing):
        assert (isinstance(issuer_hash, str) and (issuer_hash.type=='Hash')),\
        "[propbundle_X509Certificate] issuer_hash must be of type Hash."
    if not isinstance(validity_not_before, Missing):
        assert isinstance(validity_not_before, datetime.datetime),\
        "[propbundle_X509Certificate] validity_not_before must be of type Datetime."
    if not isinstance(validity_not_after, Missing):
        assert isinstance(validity_not_after, datetime.datetime),\
        "[propbundle_X509Certificate] validity_not_after must be of type Datetime."
    if not isinstance(subject, Missing):
        assert isinstance(subject, str),\
        "[propbundle_X509Certificate] subject must be of type String."
    if not isinstance(subject_hash, Missing):
        assert (isinstance(subject_hash, case.DuckObject) and (subject_hash.type=='Hash')),\
        "[propbundle_X509Certificate] subject_hash must be of type Hash."
    if not isinstance(subject_public_key_algorithm, Missing):
        assert isinstance(subject_public_key_algorithm, str),\
        "[propbundle_X509Certificate] subject_public_key_algorithm must be of type String."
    if not isinstance(subject_public_key_modulus, Missing):
        assert isinstance(subject_public_key_modulus, str),\
        "[propbundle_X509Certificate] subject_public_key_modulus must be of type String."
    if not isinstance(subject_public_key_exponent, Missing):
        assert isinstance(subject_public_key_exponent, int),\
        "[propbundle_X509Certificate] subject_public_key_exponent must be of type Integer."
    if not isinstance(x509V3Extensions, Missing):
        assert (isinstance(x509V3Extensions, case.DuckObject) and (subject_hash.type=='X509V3Extensions')),\
        "[propbundle_X509Certificate] extensions must be of type X509V3Extensions."
    if not isinstance(thumbprint_hash, Missing):
        assert (isinstance(thumbprint_hash, case.DuckObject) and (subject_hash.type=='Hash')),\
        "[propbundle_X509Certificate] thumbprint_hash must be of type Hash."

    return uco_object.create_PropertyBundle('X509Certificate', IsSelfSigned=is_self_signed, Version=version,
                                            SerialNumber=serial_number, SignatureAlgorithm=signature_algorithm,
                                            Signature=signature, Issuer=issuer, IssuerHash=issuer_hash,
                                            ValidityNotBefore=validity_not_before, ValidityNotAfter=validity_not_after,
                                            Subject=subject, SubjectHash=subject_hash,
                                            SubjectPublicKeyAlgorithm=subject_public_key_algorithm,
                                            SubjectPublicKeyModulus=subject_public_key_modulus,
                                            SubjectPublicKeyExponent=subject_public_key_exponent,
                                            Extensions=x509V3Extensions, ThumbprintHash=thumbprint_hash)


#====================================================
#-- PROPERTYBUNDLE CHILDREN IN ALPHABETICAL ORDER

def propbundle_sub_Address(uco_document, uco_object_propbundle, address_ref=Missing()):
    '''
    :param AddressRef: Exactly one occurrence of type Location.
    :return: A SubObject object.
    '''

    assert (isinstance(uco_object_propbundle, case.PropertyBundle) and (uco_object_propbundle.type=='Identity')),\
    "[propbundle_sub_Address] uco_object_propbundle must be of type Identity."

    assert not isinstance(address_ref, Missing),\
    "[propbundle_sub_Address] address_ref is required."
    if not isinstance(address_ref, Missing):
        assert (isinstance(address_ref, case.CoreObject) and (address_ref.type=='Location')),\
        "[propbundle_sub_Address] address_ref must be of type Location."

    return uco_document.create_SubObject('Address')


def propbundle_sub_Affiliation(uco_document, uco_object_propbundle):
    '''
    :return: A SubObject object.
    '''

    assert (isinstance(uco_object_propbundle, case.PropertyBundle) and (uco_object_propbundle.type=='Identity')),\
    "[propbundle_sub_Affiliation] uco_object_propbundle must be of type Identity."

    #TODO:NothingElseToCheck

    return uco_document.create_SubObject('Affiliation')


def propbundle_sub_BirthInformation(uco_document, uco_object_propbundle, birth_date=Missing()):
    '''
    :param BirthDate: Exactly one value of type Datetime.
    :return: A SubObject object.
    '''

    assert (isinstance(uco_object_propbundle, case.PropertyBundle) and (uco_object_propbundle.type=='Identity')),\
    "[propbundle_sub_BirthInformation] uco_object_propbundle must be of type Identity."

    assert not isinstance(birth_date, Missing),\
    "[propbundle_sub_BirthInformation] birth_date is required."
    if not isinstance(birth_date, Missing):
        assert isinstance(birth_date, datetime.datetime),\
        "[propbundle_sub_BirthInformation] birth_date must be of type Datetime."

    return uco_document.create_SubObject('BirthInformation')


def propbundle_sub_CountriesOfResidence(uco_document, uco_object_propbundle):
    '''
    :return: A SubObject object.
    '''

    assert (isinstance(uco_object_propbundle, case.PropertyBundle) and (uco_object_propbundle.type=='Identity')),\
    "[propbundle_sub_CountriesOfResidence] uco_object_propbundle must be of type Identity."

    #TODO:NothingElseToCheck

    return uco_document.create_SubObject('CountriesOfResidence')


def propbundle_sub_Events(uco_document, uco_object_propbundle):
    '''
    :return: A SubObject object.
    '''

    assert (isinstance(uco_object_propbundle, case.PropertyBundle) and (uco_object_propbundle.type=='Identity')),\
    "[propbundle_sub_Events] uco_object_propbundle must be of type Identity."

    #TODO:NothingElseToCheck

    return uco_document.create_SubObject('Events')


def propbundle_sub_Identifier(uco_document, uco_object_propbundle):
    '''
    :return: A SubObject object.
    '''

    assert (isinstance(uco_object_propbundle, case.PropertyBundle) and (uco_object_propbundle.type=='Identity')),\
    "[propbundle_sub_Identifier] uco_object_propbundle must be of type Identity."

    #TODO:NothingElseToCheck

    return uco_document.create_SubObject('Identifier')


def propbundle_sub_Languages(uco_document, uco_object_propbundle):
    '''
    :return: A SubObject object.
    '''

    assert (isinstance(uco_object_propbundle, case.PropertyBundle) and (uco_object_propbundle.type=='Identity')),\
    "[propbundle_sub_Languages] uco_object_propbundle must be of type Identity."

    #TODO:NothingElseToCheck

    return uco_document.create_SubObject('Languages')


def propbundle_sub_Nationality(uco_document, uco_object_propbundle):
    '''
    :return: A SubObject object.
    '''

    assert (isinstance(uco_object_propbundle, case.PropertyBundle) and (uco_object_propbundle.type=='Identity')),\
    "[propbundle_sub_Nationality] uco_object_propbundle must be of type Identity."

    #TODO:NothingElseToCheck

    return uco_document.create_SubObject('Nationality')


def propbundle_sub_Occupation(uco_document, uco_object_propbundle):
    '''
    :return: A SubObject object.
    '''

    assert (isinstance(uco_object_propbundle, case.PropertyBundle) and (uco_object_propbundle.type=='Identity')),\
    "[propbundle_sub_Occupation] uco_object_propbundle must be of type Identity."

    #TODO:NothingElseToCheck

    return uco_document.create_SubObject('Occupation')


def propbundle_sub_OrganizationDetails(uco_document, uco_object_propbundle):
    '''
    :return: A SubObject object.
    '''

    assert (isinstance(uco_object_propbundle, case.PropertyBundle) and (uco_object_propbundle.type=='Identity')),\
    "[propbundle_sub_OrganizationDetails] uco_object_propbundle must be of type Identity."

    #TODO:NothingElseToCheck

    return uco_document.create_SubObject('OrganizationDetails')


def propbundle_sub_PersonalDetails(uco_document, uco_object_propbundle):
    '''
    :return: A SubObject object.
    '''

    assert (isinstance(uco_object_propbundle, case.PropertyBundle) and (uco_object_propbundle.type=='Identity')),\
    "[propbundle_sub_PersonalDetails] uco_object_propbundle must be of type Identity."

    #TODO:NothingElseToCheck

    return uco_document.create_SubObject('PhysicalInfo')


def propbundle_sub_Qualification(uco_document, uco_object_propbundle):
    '''
    :return: A SubObject object.
    '''

    assert (isinstance(uco_object_propbundle, case.PropertyBundle) and (uco_object_propbundle.type=='Identity')),\
    "[propbundle_sub_Qualification] uco_object_propbundle must be of type Identity."

    #TODO:NothingElseToCheck

    return uco_document.create_SubObject('Qualification')


def propbundle_sub_Relationship(uco_document, uco_object_propbundle):
    '''
    :return: A SubObject object.
    '''

    assert (isinstance(uco_object_propbundle, case.PropertyBundle) and (uco_object_propbundle.type=='Identity')),\
    "[propbundle_sub_Relationship] uco_object_propbundle must be of type Identity."

    #TODO:NothingElseToCheck

    return uco_document.create_SubObject('Relationship')


def propbundle_sub_SimpleName(uco_document, uco_object_propbundle, family_name=Missing(), given_name=Missing(),
                              honorific_prefix=Missing(), honorific_suffix=Missing()):
    '''
    :param FamilyName: Any number of values of any type.
    :param GivenName: Any number of values of any type.
    :param HonorificPrefix: Any number of values of any type.
    :param HonorificSuffix: Any number of values of any type.
    :return: A SubObject object.
    '''

    assert (isinstance(uco_object_propbundle, case.PropertyBundle) and (uco_object_propbundle.type=='Identity')),\
    "[propbundle_sub_SimpleName] uco_object_propbundle must be of type Identity."

    #TODO:NothingElseToCheck

    return uco_document.create_SubObject('ForensicAction', FamilyName=family_name, GivenName=given_name,
                                         HonorificPrefix=honorific_prefix, HonorificSuffix=honorific_suffix)


def propbundle_sub_Visa(uco_document, uco_object_propbundle):
    '''
    :return: A SubObject object.
    '''

    assert (isinstance(uco_object_propbundle, case.PropertyBundle) and (uco_object_propbundle.type=='Identity')),\
    "[propbundle_sub_Visa] uco_object_propbundle must be of type Identity."

    #TODO:NothingElseToCheck

    return uco_document.create_SubObject('Visa')


#====================================================
#-- DUCK IN ALPHABETICAL ORDER

def duck_AlternateDataStream(uco_document, name=Missing(), hashes=Missing(), size=Missing()):
    '''
    :param Name: Exactly one value of type String.
    :param Hashes: At most one occurrence of type ArrayOfHash.
    :param Size: At most one value of type Integer.
    :return: A DuckObject object.
    '''

    assert not isinstance(name, Missing),\
    "[duck_AltnerateDataStream] name is required."
    if not isinstance(name, Missing):
        assert isinstance(name, str),\
        "[duck_AlternateDataStream] name must be of type String."

    if not isinstance(hashes, Missing):
        assert (isinstance(hashes, case.DuckObject) and (hashes.type=='AlternateDataStream')),\
        "[duck_AlternateDataStream] hashes must be of type AlternateDataStream."
    if not isinstance(size, Missing):
        assert isinstance(size, int),\
        "[duck_AlternateDataStream] size must be of type Integer."

    return uco_document.create_DuckObject('AlternateDataStream', Name=name, Hashes=hashes, size=size)


def duck_ArrayOfHash(uco_document, hashes=Missing()):
    '''
    :param Hashes: At least one occurrence of type Hash.
    :return: A DuckObject object.
    '''

    assert not isinstance(hashes, Missing),\
    "[duck_ArrayOfHash] hashes is required."
    if not isinstance(hashes, Missing):
        assert isinstance(hashes, list),\
        "[duck_ArrayOfHash] hashes must be of type List of Hash."
        assert all( (isinstance(i, case.DuckObject) and i.type=='Hash') for i in hashes),\
        "[duck_ArrayOfHash] hashes must be of type List of Hash."

    return uco_document.create_DuckObject('ArrayOfHash', Hashes=hashes)


def duck_ArrayOfObject(uco_document, objects=Missing()):
    '''
    :param Objects: At least one occurrence of type CoreObject.
    :return: A DuckObject object.
    '''
    
    assert not isinstance(objects, Missing),\
    "[duck_ArrayOfObject] objects is required."
    if not isinstance(objects, Missing):
        assert isinstance(objects, list),\
        "[duck_ArrayOfObject] objects must be of type List of CoreObject."
        assert all(isinstance(i, case.CoreObject) for i in objects),\
        "[duck_ArrayOfObject] objects must be of type List of CoreObject."

    return uco_document.create_DuckObject('ArrayOfObject', Objects=objects)


def duck_ArrayOfString(uco_document, strings=Missing()):
    '''
    :param strings: At least one value of type String.
    :return: A DuckObject object.
    '''
    
    assert not isinstance(strings, Missing),\
    "[duck_ArrayOfString] strings is required."
    if not isinstance(strings, Missing):
        assert isinstance(strings, list),\
        "[duck_ArrayOfString] strings must be of type List of String."
        assert all(isinstance(i, str) for i in strings),\
        "[duck_ArrayOfString] strings must be of type List of String."

    return uco_document.create_DuckObject('ArrayOfString', Strings=strings)


def duck_BuildConfigurationType(uco_document, configuration_setting_description=Missing(),
                                configuration_settings=Missing()):
    '''
    :param ConfigurationSettingDescription: At most one value of type String.
    :param ConfigurationSettings: Any number of occurrences of type ConfigurationSettingType.
    :return: A DuckObject object.
    '''
    
    if not isinstance(configuration_setting_description, Missing):
        assert isinstance(configuration_setting_description, str),\
        "[duck_BuildConfigurationType] configuration_setting_description must be of type String."
    if not isinstance(configuration_settings, Missing):
        assert isinstance(configuration_settings, list),\
        "[duck_BuildConfigurationType] configuration_settings must be of type List of ConfigurationSettingType."
        assert all( (isinstance(i, case.DuckObject) and
                     i.type=='ConfigurationSettingType') for i in configuration_settings),\
        "[duck_BuildConfigurationType] configuration_settings must be of type List of ConfigurationSettingType."

    return uco_document.create_DuckObject('BuildConfigurationType',
                                          ConfigurationSettingDescription=configuration_setting_description,
                                          ConfigurationSettings=configuration_settings)


def duck_BuildInformationType(uco_document, build_id=Missing(), build_project=Missing(), build_utility=Missing(),
                              build_version=Missing(), build_label=Missing(), compilers=Missing(),
                              compilation_date=Missing(), build_configuration=Missing(), build_script=Missing(),
                              libraries=Missing(), build_output_log=Missing()):
    '''
    :param BuildID: At most one value of type String.
    :param BuildProject: At most one value of type String.
    :param BuildUtility: At most one occurrence of type BuildUtilityType.
    :param BuildVersion: At most one value of type String.
    :param BuildLabel: At most one value of type String.
    :param Compilers: Any number of occurrences of type CompilerType.
    :param CompilationDate: At most one value of type Datetime.
    :param BuildConfiguration: At most one occurrence of type BuildConfigurationType.
    :param BuildScript: At most one value of type String.
    :param Libraries: Any number of occurrences of type LibraryType.
    :param BuildOutputLog: At most one value of type String.
    :return: A DuckObject object.
    '''
 
    if not isinstance(build_id, Missing):
        assert isinstance(build_id, str),\
        "[duck_BuildInformationType] build_id must be of type String."
    if not isinstance(build_project, Missing):
        assert isinstance(build_project, str),\
        "[duck_BuildInformationType] build_project must be of type String."
    if not isinstance(build_utility, Missing):
        assert (isinstance(build_utility, case.DuckObject) and (build_utility.type=='BuildUtilityType')),\
        "[duck_BuildInformationType] build_utility must be of type BuildUtilityType."
    if not isinstance(build_version, Missing):
        assert isinstance(build_version, str),\
        "[duck_BuildInformationType] build_version must be of type String."
    if not isinstance(build_label, Missing):
        assert isinstance(build_label, str),\
        "[duck_BuildInformationType] build_label must be of type String."
    if not isinstance(compilers, Missing):
        assert isinstance(compilers, list),\
        "[duck_BuildInformationType] compilers must be of type List of CompilerType."
        assert all( (isinstance(i, case.DuckObject) and i.type=='CompilerType') for i in compilers),\
        "[duck_BuildInformationType] compilers must be of type List of CompilerType."
    if not isinstance(compilation_date, Missing):
        assert isinstance(compilation_date, datetime.datetime),\
        "[duck_BuildInformationType] compilation_date must be of type Datetime."
    if not isinstance(build_configuration, Missing):
        assert isinstance(build_configuration, list),\
        "[duck_BuildInformationType] build_configuration must be of type List of BuildConfigurationType."
        assert all( (isinstance(i, case.DuckObject) and i.type=='BuildConfigurationType') for i in build_configuration),\
        "[duck_BuildInformationType] build_configuration must be of type List of BuildConfigurationType."
    if not isinstance(build_script, Missing):
        assert isinstance(build_script, str),\
        "[duck_BuildInformationType] build_script must be of type String."
    if not isinstance(libraries, Missing):
        assert isinstance(libraries, list),\
        "[duck_BuildInformationType] libraries must be of type List of LibraryType."
        assert all( (isinstance(i, case.DuckObject) and i.type=='LibraryType') for i in libraries),\
        "[duck_BuildInformationType] libraries must be of type List of LibraryType."
    if not isinstance(build_output_log, Missing):
        assert isinstance(build_output_log, str),\
        "[duck_BuildInformationType] build_output_log must be of type String."

    return uco_document.create_DuckObject('BuildInformationType', BuildID=build_id, BuildProject=build_project,
                                          BuildUtilities=build_utility, BuildVersion=build_version,
                                          BuildLabel=build_label, Compilers=compilers,
                                          CompilationDate=compilation_date, BuildConfiguration=build_configuration,
                                          BuildScript=build_script, Libraries=libraries,
                                          BuildOutputLog=build_output_log)


def duck_BuildUtilityType(uco_document, build_utility_name=Missing(), swid=Missing(), cpeid=Missing()):
    '''
    :param BuildUtilityName: Exactly one value of type String.
    :param SWID: At most one value of type String.
    :param CPEID: At most one value of type String.
    :return: A DuckObject object.
    '''

    assert not isinstance(build_utility_name, Missing),\
    "[duck_BuildUtility] build_utility_name is required."
    if not isinstance(build_utility_name, Missing):
        assert isinstance(build_utility_name, str),\
        "[duck_BuildUtility] build_utility_name must be of type String."

    if not isinstance(swid, Missing):
        assert isinstance(swid, str),\
        "[duck_BuildUtility] swid must be of type String."
    if not isinstance(cpeid, Missing):
        assert isinstance(cpeid, str),\
        "[duck_BuildUtility] cpeid must be of type String."
    
    return uco_document.create_DuckObject('BuildUtilityType', BuildUtilityName=build_utility_name, SWID=swid,
                                          CPEID=cpeid)


def duck_CompilerType(uco_document, compiler_informal_description=Missing(), swid=Missing(), cpeid=Missing()):
    '''
    :param CompilerInformalDescription: At most one value of any type.
    :param SWID: At most one value of type String.
    :param CPEID: At most one value of type String.
    :return: A DuckObject object.
    '''

    #NOCHECK:compiler_informal_description
    if not isinstance(swid, Missing):
        assert isinstance(swid, str),\
        "[duck_CompilerType] swid must be of type String."
    if not isinstance(cpeid, Missing):
        assert isinstance(cpeid, str),\
        "[duck_CompilerType] cpeid must be of type String."
    
    return uco_document.create_DuckObject('CompilerType', CompilerInformalDescription=compiler_informal_description,
                                          SWID=swid, CPEID=cpeid)


def duck_ConfigurationSettingType(uco_document, item_name=Missing(), item_value=Missing(), item_type=Missing(),
                                  item_description=Missing()):
    '''
    :param ItemName: Exactly one value of type String.
    :param ItemValue: Exactly one value of type String.
    :param ItemType: At most one value of type String.
    :param ItemDescriptipn: At most one value of type String.
    :return: A DuckObject object.
    '''
   
    assert not isinstance(item_name, Missing),\
    "[duck_ConfigurationSettingType] item_name is required."
    if not isinstance(item_name, Missing):
        assert isinstance(item_name, str),\
        "[duck_ConfigurationSettingType] item_name must be of type String."
    assert not isinstance(item_value, Missing),\
    "[duck_ConfigurationSettingType] item_value is required."
    if not isinstance(item_value, Missing):
        assert isinstance(item_value, str),\
        "[duck_ConfigurationSettingType] item_value must be of type String."

    if not isinstance(item_type, Missing):
        assert isinstance(item_type, str),\
        "[duck_ConfigurationSettingType] item_type must be of type String."
    if not isinstance(item_description, Missing):
        assert isinstance(item_description, str),\
        "[duck_ConfigurationSettingType] item_description must be of type String."

    return uco_document.create_DuckObject('ConfigurationSettingType', ItemName=item_name, ItemValue=item_value,
                                          ItemType=item_type, ItemDescription=item_description)


def duck_ControlledDictionary(uco_document, entry=Missing()):
    '''
    :param Entry: At least one occurrence of type ControlledDictionaryEntry.
    :return: A DuckObject object.
    '''
    
    assert not isinstance(entry, Missing),\
    "[duck_ControlledDictionary] entry is required."
    if not isinstance(entry, Missing):
        assert isinstance(entry, list),\
        "[duck_ControlledDictionary] entry must be of type List of ControlledDictionaryEntry."
        assert all( (isinstance(i, case.DuckObject) and i.type=='ControlledDictionaryEntry') for i in entry),\
        "[duck_ControlledDictionary] entry must be of type List of ControlledDictionaryEntry."

    return uco_document.create_DuckObject('ControlledDictionary', Entry=entry)


def duck_ControlledDictionaryEntry(uco_document, key=Missing(), value=Missing()):
    '''
    :param Key: Exactly one occurrence of type ControlledVocabulary.
    :param Value: Exactly one value of type String.
    :return: A DuckObject object.
    '''

    assert not isinstance(key, Missing),\
    "[duck_ControlledDictionaryEntry] key is required."
    if not isinstance(key, Missing):
        assert (isinstance(key, case.CoreObject) and (key.type=='ControlledVocabulary')),\
        "[duck_ControlledDictionaryEntry] key must be of type ControlledVocabulary."
    assert not isinstance(value, Missing),\
    "[duck_ControlledDictionaryEntry] value is required."
    if not isinstance(value, Missing):
        assert isinstance(value, str),\
        "[duck_ControlledDictionaryEntry] value must be of type String."

    return uco_document.create_DuckObject('ControlledDictionaryEntry', Key=key, Value=value)


def duck_DataRange(uco_document, range_offset_type=Missing(), range_offset=Missing(), range_size=Missing()):
    '''
    :param RangeOffsetType: At most one value of type String.
    :param RangeOffset: At most one value of type Integer.
    :param RangeSize: At most one value of type Long.
    :return: A DuckObject object.
    '''

    if not isinstance(range_offset_type, Missing):
        assert isinstance(range_offset_type, str),\
        "[duck_DataRange] range_offset_type must be of type String."
    if not isinstance(range_offset, Missing):
        assert isinstance(range_offset, int),\
        "[duck_DataRange] range_offset must be of type Integer."
    if not isinstance(range_size, Missing):
        assert isinstance(range_size, long),\
        "[duck_DataRange] range_size must be of type Long."
    
    return uco_document.create_DuckObject('DataRange', RangeOffsetType=range_offset_type, RangeOffset=range_offset,
                                          RangeSize=range_size)


def duck_DependencyType(uco_document, dependency_description=Missing(), dependency_type=Missing()):
    '''
    :param DependencyDescription: Exactly one value of any type.
    :param DependencyType: At most one value of type String.
    :return: A DuckObject object.
    '''

    #NOCHECK:dependency_description
    if not isinstance(dependency_type, Missing):
        assert isinstance(dependency_type, str),\
        "[duck_DependencyType] dependency_type must be of type String."
    
    return uco_document.create_DuckObject('DependencyType', DependencyDescription=dependency_description,
                                          DependencyType=dependency_type)


def duck_Dictionary(uco_document, entry=Missing()):
    '''
    :param Entry: At least one occurrence of type DictionaryEntry.
    :return: A DuckObject object.
    '''
    
    assert not isinstance(entry, Missing),\
    "[duck_Dictionary] entry is required."
    if not isinstance(entry, Missing):
        assert (isinstance(entry, case.DuckObject) and (entry.type=='DictionaryEntry')),\
        "[duck_Dictionary] entry must be of type DictionaryEntry."

    return uco_document.create_DuckObject('Dictionary', Entry=entry)


def duck_DictionaryEntry(uco_document, key=Missing(), value=Missing()):
    '''
    :param Key: Exactly one value of type String.
    :param Value: Exactly one value of type String.
    :return: A DuckObject object.
    '''
    
    assert not isinstance(key, Missing),\
    "[duck_DictionaryEntry] key is required."
    if not isinstance(key, Missing):
        assert isinstance(key, str),\
        "[duck_DictionaryEntry] key must be of type String."
    assert not isinstance(value, Missing),\
    "[duck_DictionaryEntry] value is required."
    if not isinstance(value, Missing):
        assert isinstance(value, str),\
        "[duck_DictionaryEntry] value must be of type String."

    return uco_document.create_DuckObject('DictionaryEntry', Key=key, Value=value)


def duck_GlobalFlagType(uco_document, abbreviation=Missing(), destination=Missing(), hexadecimal_value=Missing(),
                        symbolic_name=Missing()):
    '''
    :param Abbrevation: At most one value of type String.
    :param Destination: At most one value of type String.
    :param HexadecimalValue: At most one value of type HexBinary.
    :param SymbolicName: At most one value of type String.
    :return: A DuckObject object.
    '''
    
    if not isinstance(abbreviation, Missing):
        assert isinstance(abbreviation, str),\
        "[duck_GlobalFlagType] abbreviation must be of type String."
    if not isinstance(destination, Missing):
        assert isinstance(destination, str),\
        "[duck_GlobalFlagType] destination must be of type String."
    #TODO:HexBinary
    if not isinstance(symbolic_name, Missing):
        assert isinstance(symbolic_name, str),\
        "[duck_GlobalFlagType] symbolic_name must be of type String."

    return uco_document.create_DuckObject('GlobalFlagType', Abbreviation=abbreviation, Destination=destination,
                                          HexadecimalValue=hexadecimal_value, SymbolicName=symbolic_name)


def duck_GranularMarking(uco_document, content_selectors=Missing(), marking_references=Missing()):
    '''
    :param ContentSelectors: Any number of values of type String.
    :param MarkingReferences: Any number of occurrences of type MarkingDefinition.
    :return: A DuckObject object.
    '''
    
    if not isinstance(content_selectors, Missing):
        assert isinstance(content_selectors, list),\
        "[duck_GranularMarking] content_selectors must be of type List of String."
        assert all(isinstance(i, str) for i in content_selectors),\
        "[duck_GranularMarking] content_selectors must be of type List of String."
    if not isinstance(marking_references, Missing):
        assert isinstance(marking_references, list),\
        "[duck_GranularMarking] marking_references must be of type List of MarkingDefinition."
        assert all( (isinstance(i, case.CoreObject) and i.type=='MarkingDefinition') for i in marking_references),\
        "[duck_GranularMarking] marking_references must be of type List of MarkingDefinition."

    return uco_document.create_DuckObject('GranularMarking', ContentSelectors=content_selectors,
                                          MarkingReferences=marking_references)


def duck_Hash(uco_document, hash_method=Missing(), hash_value=Missing()):
    '''
    :param HashMethod: Exactly one occurrence of type ControlledVocabulary.
    :param HashValue: Exactly one value of type HexBinary.
    :return: A DuckObject object.
    '''
    
    assert not isinstance(hash_method, Missing),\
    "[duck_Hash] hash_method is required."
    if not isinstance(hash_method, Missing):
        assert (isinstance(hash_method, case.CoreObject) and (hash_method.type=='ControlledVocabulary')),\
        "[duck_Hash] hash_method must be of type ControlledVocabulary."
    #TODO:HexBinary

    return uco_document.create_DuckObject('Hash', HashMethod=hash_method, HashValue=hash_value)


def duck_IComHandlerActionType(uco_document, com_data=Missing(), com_class_id=Missing()):
    '''
    :param ComData: At most one value of type String.
    :param ComClassID: At most one value of type String.
    :return: A DuckObject object.
    '''

    if not isinstance(com_data, Missing):
        assert isinstance(com_data, str),\
        "[duck_IComHandlerActionType] com_data must be of type String."
    if not isinstance(com_class_id, Missing):
        assert isinstance(com_class_id, str),\
        "[duck_IComHandlerActionType] com_class_id must be of type String."
    
    return uco_document.create_DuckObject('IComHandlerActionType', ComData=com_data, ComClassID=com_class_id)


def duck_LibraryType(uco_document, library_name=Missing(), library_version=Missing()):
    '''
    :param LibraryName: Exactly one value of type String.
    :param LibraryVersion: Exactly one value of type String.
    :return: A DuckObject object.
    '''
    
    assert not isinstance(library_name, Missing),\
    "[duck_LibraryType] library_name is required."
    if not isinstance(library_name, Missing):
        assert isinstance(library_name, str),\
        "[duck_LibraryType] library_name must be of type String."
    assert not isinstance(library_version, Missing),\
    "[duck_LibraryType] library_version is required."
    if not isinstance(library_version, Missing):
        assert isinstance(library_version, str),\
        "[duck_LibraryType] library_version must be of type String."

    return uco_document.create_DuckObject('LibraryType', LibraryName=library_name, LibraryVersion=library_version)


def duck_MarkingModel(uco_document):
    '''
    :return: A DuckObject object.
    '''

    #TODO:NothingElseToCheck

    return uco_document.create_DuckObject('MarkingModel')


def duck_MIMEPartType(uco_document, body=Missing(), content_type=Missing(), body_raw_ref=Missing(),
                      content_disposition=Missing()):
    '''
    :param Body: At most one value of type String.
    :param ContentType: At most one value of type String.
    :param BodyRawRef: At most one occurrence of type Trace.
    :param ContentDisposition: At most one value of type String.
    :return: A DuckObject object.
    '''
    
    if not isinstance(body, Missing):
        assert isinstance(body, str),\
        "[duck_MIMEPartType] body must be of type String."
    if not isinstance(content_type, Missing):
        assert isinstance(content_type, str),\
        "[duck_MIMEPartType] content_type must be of type String."
    if not isinstance(body_raw_ref, Missing):
        assert (isinstance(body_raw_ref, case.CoreObject) and (body_raw_ref.type=='Trace')),\
        "[duck_MIMEPartType] body_raw_ref must be of type Trace."
    if not isinstance(content_disposition, Missing):
        assert isinstance(content_disposition, str),\
        "[duck_MIMEPartType] content_disposition must be of type String."

    return uco_document.create_DuckObject('MIMEPartType', Body=body, ContentType=content_type, BodyRawRef=body_raw_ref,
                                          ContentDisposition=content_disposition)


def duck_TaskActionType(uco_document, action_id=Missing(), iemail_action_ref=Missing(), icom_handler_action=Missing(),
                        iexec_action=Missing(), ishow_message_action=Missing()):
    '''
    :param ActionID: At most one value of type String.
    :param iEmailActionRef: At most one occurrence of type Trace.
    :param iComHandlerAction: At most one occurrence of type IComHandlerActionType.
    :param iExecAction: At most one occurrence of type IExecActionType.
    :param iShowMessageAction: At most one occurrence of type IShowMessageActionType.
    :return: A DuckObject object.
    '''
    
    if not isinstance(action_id, Missing):
        assert isinstance(action_id, str),\
        "[duck_TaskActionType] action_id must be of type String."
    if not isinstance(iemail_action_ref, Missing):
        assert (isinstance(iemail_action_ref, case.CoreObject) and (iemail_action_ref.type=='Trace')),\
        "[duck_TaskActionType] iemail_action_ref must be of type Trace."
    if not isinstance(icom_handler_action, Missing):
        assert (isinstance(icom_handler_action, case.DuckObject) and (icom_handler_action.type=='IComHandlerActionType')),\
        "[duck_TaskActionType] icom_handler_action must be of type IComHandlerActionType."
    if not isinstance(iexec_action, Missing):
        assert (isinstance(iexec_action, case.DuckObject) and (iexec_action.type=='IExecActionType')),\
        "[duck_TaskActionType] iexec_action must be of type IExecActionType."
    if not isinstance(ishow_message_action, Missing):
        assert (isinstance(ishow_message_action, case.DuckObject) and (ishow_message_action.type=='IShowMessageActionType')),\
        "[duck_TaskActionType] ishow_message_action must be of type IShowMessageActionType."

    return uco_document.create_DuckObject('TaskActionType', ActionID=action_id, iEmailActionRef=iemail_action_ref,
                                          iComHandlerAction=icom_handler_action, iExecAction=iexec_action,
                                          iShowMessageAction=ishow_message_action)


def duck_TriggerType(uco_document, is_enabled=Missing(), trigger_begin_time=Missing(), trigger_delay=Missing(),
                     trigger_end_time=Missing(), trigger_max_run_time=Missing(),
                     trigger_session_change_type=Missing()):
    '''
    :param IsEnabled: At most one value of type Bool.
    :param TriggerBeginTime: At most one value of type Datetime.
    :param TriggerDelay: At most one value of type String.
    :param TriggerEndTime: At most one value of type Datetime.
    :param TriggerMaxRunTime: At most one value of type String.
    :param TriggerSessionChangeType: At most one value of type String.
    :return: A DuckObject object.
    '''

    if not isinstance(is_enabled, Missing):
        assert isinstance(is_enabled, bool),\
        "[duck_TriggerType] is_enabled must be of type Bool."
    if not isinstance(trigger_begin_time, Missing):
        assert isinstance(trigger_begin_time, datetime.datetime),\
        "[duck_TriggerType] trigger_begin_time must be of type Datetime."
    if not isinstance(trigger_delay, Missing):
        assert isinstance(trigger_delay, str),\
        "[duck_TriggerType] trigger_delay must be of type String."
    if not isinstance(trigger_end_time, Missing):
        assert isinstance(trigger_end_time, datetime.datetime),\
        "[duck_TriggerType] trigger_end_time must be of type Datetime."
    if not isinstance(trigger_max_run_time, Missing):
        assert isinstance(trigger_max_run_time, str),\
        "[duck_TriggerType] trigger_max_run_time must be of type String."
    if not isinstance(trigger_session_change_type, Missing):
        assert isinstance(trigger_session_change_type, str),\
        "[duck_TriggerType] trigger_session_change_type must be of type String."
    
    return uco_document.create_DuckObject('TriggerType', IsEnabled=is_enabled, TriggerBeginTime=trigger_begin_time,
                                          TriggerDelay=trigger_delay, TriggerEndTime=trigger_end_time,
                                          TriggerMaxRunTime=trigger_max_run_time,
                                          TriggerSessionChangedTime=trigger_session_change_type)


def duck_WhoIsContactType(uco_document, contact_id=Missing(), contact_name=Missing(), email_address_ref=Missing(),
                          phone_number_ref=Missing(), fax_number_ref=Missing(), address_ref=Missing(),
                          contact_organization=Missing()):
    '''
    :param ContactID: At most one value of type String.
    :param ContactName: At most one value of type String.
    :param EmailAddressRef: At most one occurrence of type Trace.
    :param PhoneNumberRef: At most one occurrence of type Trace.
    :param FaxNumberRef: At most one occurrence of type Trace.
    :param AddressRef: At most one occurrence of type Location.
    :param ContactOrganization: At most one occurrence of type Identity (core).
    :return: A DuckObject object.
    '''
    
    if not isinstance(contact_id, Missing):
        assert isinstance(contact_id, str),\
        "[duck_WhoIsContactType] contact_id must be of type String."
    if not isinstance(contact_name, Missing):
        assert isinstance(contact_name, str),\
        "[duck_WhoIsContactType] contact_name must be of type String."
    if not isinstance(email_address_ref, Missing):
        assert (isinstance(email_address_ref, case.CoreObject) and (email_address_ref.type=='Trace')),\
        "[duck_WhoIsContactType] email_address_ref must be of type Trace."
    if not isinstance(phone_number_ref, Missing):
        assert (isinstance(phone_number_ref, case.CoreObject) and (phone_number_ref.type=='Trace')),\
        "[duck_WhoIsContactType] phone_number_ref must be of type Trace."
    if not isinstance(fax_number_ref, Missing):
        assert (isinstance(fax_number_ref, case.CoreObject) and (fax_number_ref.type=='Trace')),\
        "[duck_WhoIsContactType] fax_number_ref must be of type Trace."
    if not isinstance(address_ref, Missing):
        assert (isinstance(address_ref, case.CoreObject) and (address_ref.type=='Location')),\
        "[duck_WhoIsContactType] address_ref must be of type Location."
    if not isinstance(contact_organization, Missing):
        assert (isinstance(contact_organization, case.CoreObject) and (contact_organization.type=='Identity')),\
        "[duck_WhoIsContactType] contact_organization must be of type Identity."

    return uco_document.create_DuckObject('WhoIsContactType', ContactID=contact_id, ContactName=contact_name,
                                          EmailAddressRef=email_address_ref, PhoneNumberRef=phone_number_ref,
                                          FaxNumberRef=fax_number_ref, ContactOrganization=contact_organization)


def duck_WhoIsRegistrarInfoType(uco_document, registrar_id=Missing(), registrar_guid=Missing(),
                                who_is_server_ref=Missing(), referral_url_ref=Missing(),
                                registrar_name=Missing(), email_address_ref=Missing(), phone_number_ref=Missing(),
                                address_ref=Missing(), contact_info_refs=Missing()):
    '''
    :param RegistrarID: At most one value of type String.
    :param RegistrarGUID: At most one value of type String.
    :param WhoIsServerRef: At most one occurrence of type Trace.
    :param ReferralURLRef: At most one occurrence of type Trace.
    :param RegistrarName: At most one value of type String.
    :param EmailAddressRef: At most one occurrence of type Trace.
    :param PhoneNumberRef: At most one occurrence of type Trace.
    :param AddressRef: At most one occurrence of type Location.
    :param ContactInfoRefs: Any number of occurrences of type WhoIsContactType.
    :return: A DuckObject object.
    '''
    
    if not isinstance(registrar_id, Missing):
        assert isinstance(registrar_id, str),\
        "[duck_WhoIsRegistrarInfoType] registrar_id must be of type String."
    if not isinstance(registrar_guid, Missing):
        assert isinstance(registrar_guid, str),\
        "[duck_WhoIsRegistrarInfoType] registrar_guid must be of type String."
    if not isinstance(who_is_server_ref, Missing):
        assert (isinstance(who_is_server_ref, case.CoreObject) and (who_is_server_ref.type=='Trace')),\
        "[duck_WhoIsRegistrarInfoType] who_is_server_ref must be of type Trace."
    if not isinstance(referral_url_ref, Missing):
        assert (isinstance(referral_url_ref, case.CoreObject) and (referral_url_ref.type=='Trace')),\
        "[duck_WhoIsRegistrarInfoType] referral_url_ref must be of type Trace."
    if not isinstance(registrar_name, Missing):
        assert isinstance(registrar_name, str),\
        "[duck_WhoIsRegistrarInfoType] registrar_name must be of type String."
    if not isinstance(email_address_ref, Missing):
        assert (isinstance(email_address_ref, case.CoreObject) and (email_address_ref.type=='Trace')),\
        "[duck_WhoIsRegistrarInfoType] email_address_ref must be of type Trace."
    if not isinstance(phone_number_ref, Missing):
        assert (isinstance(phone_number_ref, case.CoreObject) and (phone_number_ref.type=='Trace')),\
        "[duck_WhoIsRegistrarInfoType] phone_number_ref must be of type Trace."
    if not isinstance(address_ref, Missing):
        assert (isinstance(address_ref, case.CoreObject) and (address_ref.type=='Location')),\
        "[duck_WhoIsRegistrarInfoType] address_ref must be of type Location."
    if not isinstance(contact_info_refs, Missing):
        assert isinstance(contact_info_refs, list),\
        "[duck_WhoIsRegistrarInfoType] contact_info_refs must be of type List of WhoIsContactType."
        assert all( (isinstance(i, case.DuckObject) and i.type=='WhoIsContactType') for i in contact_info_refs),\
        "[duck_WhoIsRegistrarInfoType] contact_info_refs must be of type List of WhoIsContactType."

    return uco_document.create_DuckObject('WhoIsRegistrarInfoType', RegistrarID=registrar_id,
                                          RegistrarGUID=registrar_guid, WhoIsServerRef=who_is_server_ref,
                                          ReferralURLRef=referral_url_ref, RegistrarName=registrar_name,
                                          EmailAddress=email_address_ref, PhoneNumberRef=phone_number_ref,
                                          AddressRef=address_ref, ContactInfoRefs=contact_info_refs)


def duck_WindowsPEFileHeader(uco_document, machine=Missing(), number_of_sections=Missing(), time_date_stamp=Missing(),
                             pointer_to_symbol_table=Missing(), number_of_symbols=Missing(),
                             size_of_optional_header=Missing(), characteristics=Missing(),
                             hashes=Missing()):
    '''
    :param Machine: Exactly one value of type HexBinary.
    :param NumberOfSections: At most one value of type HexBinary.
    :param TimeDateStamp: At most one value of any type.
    :param PointerToSymbolTable: At most one value of type HexBinary.
    :param NumberOfSymbols: At most one value of type HexBinary.
    :param SizeOfOptionalHeader: At most one value ot type HexBinary.
    :param Characteristics: At most one value of type HexBinary.
    :param Hashes: Any number of occurences of type Hash.
    :return: A DuckObject object.
    '''
    
    #TODO:HexBinary #REQUIRED

    #TODO:HexBinary
    #NOCHECK:time_date_stamp
    #TODO:HexBinary
    #TODO:HexBinary
    #TODO:HexBinary
    #TODO:HexBinary
    if not isinstance(hashes, Missing):
        assert isinstance(hashes, list),\
        "[duck_WindowsPEFileHeader] hashes must be of type List of Hash."
        assert all( (isinstance(i, case.DuckObject) and i.type=='Hash') for i in hashes),\
        "[duck_WindowsPEFileHeader] hashes must be of type List of Hash."

    return uco_document.create_DuckObject('WindowsPEFileHeader', Machine=machine, NumberOfSections=number_of_sections,
                                          TimeDateStamp=time_date_stamp, PointerToSymbolTable=pointer_to_symbol_table,
                                          NumberOfSymbols=number_of_symbols,
                                          SizeOfOptionalHeader=size_of_optional_header,
                                          Characteristics=characteristics, Hashes=hashes)


def duck_WindowsPEOptionalHeader(uco_document, magic=Missing(), major_linker_version=Missing(),
                                 minor_linker_version=Missing(), size_of_code=Missing(),
                                 size_of_initialized_data=Missing(), size_of_uninitialized_data=Missing(),
                                 address_of_entry_point=Missing(), base_of_code=Missing(), image_base=Missing(),
                                 section_alignment=Missing(), file_alignment=Missing(), major_os_version=Missing(),
                                 minor_os_version=Missing(), major_image_version=Missing(),
                                 minor_image_version=Missing(), major_subsystem_version=Missing(),
                                 minor_subsystem_version=Missing(), win32_version_value=Missing(),
                                 size_of_image=Missing(), size_of_headers=Missing(), checksum=Missing(),
                                 subsystem=Missing(), dll_characteristics=Missing(), size_of_stack_reserve=Missing(),
                                 size_of_stack_commit=Missing(), size_of_heap_reserve=Missing(),
                                 size_of_heap_commit=Missing(), loader_flags=Missing(),
                                 number_of_rva_and_sizes=Missing(), hashes=Missing()):
    '''
    :param Magic: At most one value of type HexBinary.
    :param MajorLinkerVersion: At most one value of type HexBinary.
    :param MinorLinkerVersion: At most one value of type HexBinary.
    :param SizeOfCode: At most one value of type HexBinary.
    :param SizeOfInitializedData: At most one value of type HexBinary.
    :param SizeOfUninitializedData: At most one value of type HexBinary.
    :param AddressOfEntryPoint: At most one value of type HexBinary.
    :param BaseOfCode: At most one value of type HexBinary.
    :param ImageBase: At most one value of type HexBinary.
    :param SectionAlignment: At most one value of type HexBinary.
    :param FileAlignment: At most one value of type HexBinary.
    :param MajorOSVersion: At most one value of type HexBinary.
    :param MinorOSVersion: At most one value of type HexBinary.
    :param MajorImageVersion: At most one value of type HexBinary.
    :param MinorImageVersion: At most one value of type HexBinary.
    :param MajorSubsystemVersion: At most one value of type HexBinary.
    :param MinorSubsystemVersion: At most one value of type HexBinary.
    :param Win32VersionValue: At most one value of type HexBinary.
    :param SizeOfImage: At most one value of type HexBinary.
    :param SizeOfHeaders: At most one value of type HexBinary.
    :param Checksum: At most one value of type HexBinary.
    :param Subsystem: At most one value of type HexBinary.
    :param DLLCharacteristics: At most one value of type HexBinary.
    :param SizeOfStackReserve: At most one value of type HexBinary.
    :param SizeOfStackCommit: At most one value of type HexBinary.
    :param SizeOfHeapReserve: At most one value of type HexBinary.
    :param SizeOfHeapCommit: At most one value of type HexBinary.
    :param LoaderFlags: At most one value of type HexBinary.
    :param NumberOfRVAAndSizes: At most one value of type HexBinary.
    :param Hashes: Any number of occurrences of type Hash.
    :return: A DuckObject object.
    '''
    
    # ALL THE HEXBINARY
    #TODO:HexBinary

    if not isinstance(hashes, Missing):
        assert isinstance(hashes, list),\
        "[duck_WindowsPEOptionalHeader] hashes must be of type List of Hash."
        assert all( (isinstance(i, case.DuckObject) and i.type=='Hash') for i in hashes),\
        "[duck_WindowsPEOptionalHeader] hashes must be of type List of Hash."

    return uco_document.create_DuckObject('WindowsPEOptionalHeader', Magic=magic,
                                          MajorLinkerVersion=major_linker_version,
                                          MinorLinkerVersion=minor_linker_version, SizeOfCode=size_of_code,
                                          SizeOfInitializedData=size_of_initialized_data,
                                          SizeOfUninitializedData=size_of_uninitialized_data,
                                          AddressOfEntryPoint=address_of_entry_point,
                                          BaseOfCode=base_of_code, ImageBase=image_base,
                                          SectionAlignment=section_alignment, FileAlignment=file_alignment,
                                          MajorOSVersion=major_os_version, MinorOSVersion=minor_os_version,
                                          MajorImageVersion=major_image_version, MinorImageVersion=minor_image_version,
                                          MajorSubsystemVersion=major_subsystem_version,
                                          MinorSubsystemVersion=minor_subsystem_version,
                                          Win32VersionValue=win32_version_value, SizeOfImage=size_of_image,
                                          SizeOfHeaders=size_of_headers, Checksum=checksum, Subsystem=subsystem,
                                          DLLCharacteristics=dll_characteristics,
                                          SizeOfStackReserve=size_of_stack_reserve,
                                          SizeOfStackCommit=size_of_stack_commit,
                                          SizeOfHeapReserve=size_of_heap_reserve,
                                          SizeOfHeapCommit=size_of_heap_commit, LoaderFlags=loader_flags,
                                          NumberOfRVAAndSizes=number_of_rva_and_sizes, Hashes=hashes)


def duck_WindowsPESection(uco_document, name=Missing(), size=Missing(), entropy=Missing(), hashes=Missing()):
    '''
    :param Name: Exactly one value of type String.
    :param Size: At most one value of type Integer.
    :param Entropy: At most one value of type Float.
    :param Hashes: Any number of occurrences of type Hash.
    :return: A DuckObject object.
    '''
    
    assert not isinstance(name, Missing),\
    "[duck_WindowsPESection] name is required."
    if not isinstance(name, Missing):
        assert isinstance(name, str),\
        "[duck_WindowsPESection] name must be of type String."

    if not isinstance(size, Missing):
        assert isinstance(size, int),\
        "[duck_WindowsPESection] size must be of type Integer."
    if not isinstance(entropy, Missing):
        assert isinstance(entropy, float),\
        "[duck_WindowsPESection] entropy must be of type Float."
    if not isinstance(hashes, Missing):
        assert isinstance(hashes, list),\
        "[duck_WindowsPESection] hashes must be of type List of Hash."
        assert all( (isinstance(i, case.DuckObject) and i.type=='Hash') for i in hashes),\
        "[duck_WindowsPESection] hashes must be of type List of Hash."

    return uco_document.create_DuckObject('WindowsPESection', Name=name, Size=size, Entropy=entropy, Hashes=hashes)


def duck_WindowsRegistryValue(uco_document, name=Missing(), data=Missing(), data_type=Missing()):
    '''
    :param Name: Exactly one value of type String.
    :param Data: At most one value of type String.
    :param DataType: At most one occurrence of type ControlledVocabulary.
    :return: A DuckObject object.
    '''
    
    assert not isinstance(name, Missing),\
    "[duck_WindowsRegistryValue] name is required."
    if not isinstance(name, Missing):
        assert isinstance(name, str),\
        "[duck_WindowsRegistryValue] name must be of type String."

    if not isinstance(data, Missing):
        assert isinstance(data, str),\
        "[duck_WindowsRegistryValue] data must be of type String."
    if not isinstance(data_type, Missing):
        assert (isinstance(data_type, case.CoreObject) and (data_type.type=='ControlledVocabulary')),\
        "[duck_WindowsRegistryValue] data_type must be of type ControlledVocabulary."

    return uco_document.create_DuckObject('WindowsRegistryValue', Name=name, Data=data, DataType=data_type)


def duck_X509V3Extensions(uco_document, basic_constraints=Missing(), name_constraints=Missing(),
                          policy_constraints=Missing(), key_usage=Missing(), extended_key_usage=Missing(),
                          subject_key_identifier=Missing(), authority_key_identifier=Missing(),
                          subject_alternative_name=Missing(), issuer_alternative_name=Missing(),
                          subject_directory_attributes=Missing(), crl_distribution_points=Missing(),
                          inhibit_any_policy=Missing(), private_key_usage_period_not_before=Missing(),
                          private_key_usage_period_not_after=Missing(), certificate_policies=Missing(),
                          policy_mappings=Missing()):
    '''
    :param BasicConstraints: At most one value of type String.
    :param NameConstraints: At most one value of type String.
    :param PolicyConstraints: At most one value of type String.
    :param KeyUsage: At most one value of type String.
    :param ExtendedKeyUsage: At most one value of type String.
    :param SubjectKeyIdentifier: At most one value of type String.
    :param AuthorityKeyIdentifier: At most one value of type String.
    :param SubjectAlternativeName: At most one value of type String.
    :param IssuerAlternativeName: At most one value of type String.
    :param SubjectDirectoryAttributes: At most one value of type String.
    :param CRLDistributionPoints: At most one value of type String.
    :param InhibitAnyPolicy: At most one value of type String.
    :param PrivateKeyUsagePeriodNotBefore: At most one value of type Datetime.
    :param PrivateKeyUsagePeriodNotAfter: At most one value of type Datetime.
    :param CertificatePolicies: At most one value of type String.
    :param PolicyMappings: At most one value of type String.
    :return: A DuckObject object.
    '''
    
    if not isinstance(basic_constraints, Missing):
        assert isinstance(basic_constraints, str),\
        "[duck_X509V3Extensions] basic_constraints must be of type String."
    if not isinstance(name_constraints, Missing):
        assert isinstance(name_constraints, str),\
        "[duck_X509V3Extensions] name_constraints must be of type String."
    if not isinstance(policy_constraints, Missing):
        assert isinstance(policy_constraints, str),\
        "[duck_X509V3Extensions] policy_constraints must be of type String."
    if not isinstance(key_usage, Missing):
        assert isinstance(key_usage, str),\
        "[duck_X509V3Extensions] key_usage must be of type String."
    if not isinstance(extended_key_usage, Missing):
        assert isinstance(extended_key_usage, str),\
        "[duck_X509V3Extensions] extended_key_usage must be of type String."
    if not isinstance(subject_key_identifier, Missing):
        assert isinstance(subject_key_identifier, str),\
        "[duck_X509V3Extensions] subject_key_identifier must be of type String."
    if not isinstance(authority_key_identifier, Missing):
        assert isinstance(authority_key_identifier, str),\
        "[duck_X509V3Extensions] authority_key_identifier must be of type String."
    if not isinstance(subject_alternative_name, Missing):
        assert isinstance(subject_alternative_name, str),\
        "[duck_X509V3Extensions] subject_alternative_name must be of type String."
    if not isinstance(issuer_alternative_name, Missing):
        assert isinstance(issuer_alternative_name, str),\
        "[duck_X509V3Extensions] issuer_alternative_name must be of type String."
    if not isinstance(subject_directory_attributes, Missing):
        assert isinstance(subject_directory_attributes, str),\
        "[duck_X509V3Extensions] subject_directory_attributes must be of type String."
    if not isinstance(crl_distribution_points, Missing):
        assert isinstance(crl_distribution_points, str),\
        "[duck_X509V3Extensions] crl_distribution_points must be of type String."
    if not isinstance(inhibit_any_policy, Missing):
        assert isinstance(inhibit_any_policy, str),\
        "[duck_X509V3Extensions] inhibit_any_policy must be of type String."
    if not isinstance(private_key_usage_period_not_before, Missing):
        assert isinstance(private_key_usage_period_not_before, datetime.datetime),\
        "[duck_X509V3Extensions] private_key_usage_period_not_before must be of type Datetime."
    if not isinstance(private_key_usage_period_not_after, Missing):
        assert isinstance(private_key_usage_period_not_after, datetime.datetime),\
        "[duck_X509V3Extensions] private_key_usage_period_not_after must be of type Datetime."
    if not isinstance(certificate_policies, Missing):
        assert isinstance(certificate_policies, str),\
        "[duck_X509V3Extensions] certificate_policies must be of type String."
    if not isinstance(policy_mappings, Missing):
        assert isinstance(policy_mappings, str),\
        "[duck_X509V3Extensions] policy_mappings must be of type String."

    return uco_document.create_DuckObject('X509V3Extensions', BasicConstraints=basic_constraints,
                                          NameConstraints=name_constraints, PolicyConstraints=policy_constraints,
                                          KeyUsage=key_usage, ExtendedKeyUsage=extended_key_usage,
                                          SubjectKeyIdentifier=subject_key_identifier,
                                          AuthorityKeyIdentifier=authority_key_identifier,
                                          SubjectAlternativeName=subject_alternative_name,
                                          IssuerAlternativeName=issuer_alternative_name,
                                          SubjectDirectoryAttributes=subject_alternative_name,
                                          CRLDistributionPoints=crl_distribution_points,
                                          InhibitAnyPolicy=inhibit_any_policy,
                                          PrivateKeyUsagePeriodNotBefore=private_key_usage_period_not_before,
                                          PrivateKeyUsagePeriodNotAfter=private_key_usage_period_not_after,
                                          CertificatePolicies=certificate_policies,
                                          PolicyMappings=policy_mappings)


#====================================================
#-- DUCK CHILDREN IN ALPHABETICAL ORDER

def duck_sub_ArrayOfAction(uco_document, duck_object):
    '''
    :return: A SubObject object.
    '''

    assert (isinstance(duck_object, case.DuckObject) and (duck_object.type=='ArrayOfObject')),\
    "[duck_sub_ArrayOfAction] duck_object must be of type ArrayOfObject."
    
    #TODO:NothingElseToCheck

    return uco_document.create_SubObject('ArrayOfAction')


#====================================================
#-- SPECIAL TYPE-CHECKING FUNCTIONS

    # URI, HexBinary, CyberAction, StructureText

