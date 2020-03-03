/*
# © 2020 The MITRE Corporation
#This software (or technical data) was produced for the U. S. Government under contract SB-1341-14-CQ-0010, and is subject to the Rights in Data-General Clause 52.227-14, Alt. IV (DEC 2007)
#Released under MITRE PRE #18-4297.
*/

#include <stdio.h>
#include <string.h>
#include <python2.7/Python.h>

/* This is a test for calling the CASE-Python-API modules
and creating RDF nodes for tools written in C. The Python
API must be pip installed first; case.py & NLG.py will be
accessible via the Python environment for imports below.*/

//================================================================

/*
PyObject* c_to_python(void* param_to_convert);
void py_script_manager(const char* module, const char* function, const char* format, ...);
*/

//================================================================

static PyObject *my_callback = NULL;
static PyObject *my_set_callback(PyObject* dummy, PyObject* args)
{
    printf("CALLBACK FUNCTION\n");

    PyObject *result = NULL;
    PyObject *temp;
    
    if (PyArg_ParseTuple(args, "0:set_callback", &temp)){
        if (!PyCallable_Check(temp)) {
            PyErr_SetString(PyExc_TypeError, "parameter must be callable");
            return NULL;
        }
        Py_XINCREF(temp);
        Py_XDECREF(my_callback);
        my_callback = temp;

        Py_INCREF(Py_None);
        result = Py_None;
    }
    return result;
}

//================================================================

/*
void py_script_manager(const char* module, const char* function, const char* format, ...)
{
    va_list arguments;
    int i;
    int argc = 0;
    PyObject* arglist;
    PyObject* result;
    PyObject* pModule, *func;
    PyObject* pArgs;
    PyObject* pValue;
    PyObject* pName;

    //args = last argumente specified; all others are accessed via variable-argument macros (e.g. va_start).
    va_start(arguments, format);
    pArgs = Py_VaBuild((char*)format, arguments);
    if (pArgs == NULL)
    {
        //
    }
}
*/










//================================================================

int main()
{
    printf("START\n");
    Py_Initialize();

//================================================================

    //1. Export function in tool will gather together all objects by calling conversion function to translate
    //   C objects to Python. PyObjects will be added to an array during this.
    //2. Python translator script will be called and the array of PyObjects passed to it for use.


    // Create main Python module/environment.
    PyObject *main_module = PyImport_ImportModule("__main__");
    PyObject *main_dict = PyModule_GetDict(main_module);

    // Import case.py and NLG.py and insert into main module's namespace.
    PyObject *case_module = PyImport_ImportModule("case");
    PyObject *case_dict = PyModule_GetDict(case_module);
    PyDict_SetItemString(main_dict, "case", case_module);
    PyObject *nlg_module = PyImport_ImportModule("NLG");
    PyObject *nlg_dict = PyModule_GetDict(nlg_module);
    PyDict_SetItemString(main_dict, "NLG", nlg_module);

    // Import ctypes.
    PyObject *ctypes_module = PyImport_ImportModule("ctypes");
    PyObject *ctypes_dict = PyModule_GetDict(ctypes_module);
    PyDict_SetItemString(main_dict, "ctypes", ctypes_module);

//================================================================
    // Get passed all export objects from the tool.
    // Iterate through them and call the conversion function for each.
    // The conversion function will do conversion and then inject each into a PyObject variable.
    // PyObjects will then be used as parameters when calling the appropriate NLG function here in the tool.

    // Fake exports from tool.
    char object_name[] = "core_Tool";
    long int param_1 = 4;
    double param_2 = 6.35;

    //Call export function.

    // Create Document for export data.
//    PyObject* doc = PyDict_GetItemString(main_dict, (char*)"Document.init");
//    PyObject* call_doc = PyObject_CallFunction(doc, "s", NULL);

//================================================================
    // OPTION 1 FOR CALLING PYTHON TRANSLATOR
    FILE* trans = fopen("case_translator.py", "r");
    PyRun_File(trans, "case_translator.py",
               Py_file_input,
               main_dict, main_dict);

    // CALL python functions from NLG for each object.

//================================================================
    // OPTION 2 FOR CALLING PYTHON TRANSLATOR

/*
    int num_objects = 3;
    PyObject* exports[num_objects];

    int num_params = 2;
    char** p_list[num_params];

    char* param_1 = "param_1";
    p_list[0] = &param_1;

    char* param_2 = "param_2";
    p_list[1] = &param_2;

    // get length of incoming parameters to set cmd string length
    char cmd[1000] = "python /home/case/Documents/mitre/DC3DD/integration-tst/case_translator.py";
    int cmd_len = strlen(cmd);
    for (int i=0; i<num_params; i++){
        char** curr_str = p_list[i];
        cmd_len = cmd_len + strlen(*curr_str);
        sprintf(cmd, "%s %s", cmd, *p_list[i]);
    }
    printf("%i\n", cmd_len);
    printf("%s\n", cmd);

    system(cmd);
*/

//================================================================
    Py_Finalize();
    printf("STOP\n");
}
