/*
# © 2020 The MITRE Corporation
#This software (or technical data) was produced for the U. S. Government under contract SB-1341-14-CQ-0010, and is subject to the Rights in Data-General Clause 52.227-14, Alt. IV (DEC 2007)
#Released under MITRE PRE #18-4297.
*/

#include <stdio.h>
#include <string.h>
#include <python2.7/Python.h>

/* This is a test for calling the CASE-Python-API modules
and creating RDF nodes for tools written in C.*/



static PyObject *
c_converter(PyObject *self, PyObject *args)
{
    const char *cmd;
    int sts;

    if (!PyArg_ParseTuple(args, "s", &cmd)){
        return NULL;
    }
    sts = system(cmd);
//    if (sts < 0){
//        PyErr_SetString(CaseTranslatorError, "System command failed");
//        return NULL;
//    }
//    return PyLong_FromLong(sts);
    return Py_BuildValue("i", sts);
}






int main()
{
}
