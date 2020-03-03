# © 2020 The MITRE Corporation
#This software (or technical data) was produced for the U. S. Government under contract SB-1341-14-CQ-0010, and is subject to the Rights in Data-General Clause 52.227-14, Alt. IV (DEC 2007)
#Released under MITRE PRE #18-4297.


#====================================================
# CASE API
#!/usr/bin/env python

import datetime
import uuid

import rdflib
from rdflib import RDF

CASE = rdflib.Namespace('http://case.example.org/core#')


#====================================================
#-- CREATE A CASE DOCUMENT FOR A SINGLE REPORT

class Document(object):

    def __init__(self, graph=None):
        """
        Initializes the CASE document.
        Args:
            graph: The graph to populate (instance of rdflib.Graph)
                   If not provided, a graph in memory will be used.
        """

        if not graph:
            graph = rdflib.Graph()
        graph.namespace_manager.bind('case', CASE)
        self.graph = graph


    def _sanitize_triple(self, triple):
        """Santizes the triple to contains pure rdflib terms."""

        s, p, o = triple
        if isinstance(s, Node):
            s = s._node
        if isinstance(o, Node):
            o = o._node
        elif o is not None and not isinstance(o, rdflib.term.Node):
            o = rdflib.Literal(o)
        if p is not None and not isinstance(p, rdflib.term.Node):
            p = CASE[p]

        return s, p, o


    def __iter__(self):
        """Wrapper for iterating over all triples in the graph"""
        return iter(self.graph)


    def __contains__(self, triple):
        """Wrapper for checking if triple is contained in the graph."""
        return self._sanitize_triple(triple) in self.graph


    def triples(self, triple):
        """Generator over the triple store in graph."""
        return self.graph.triples(self._sanitize_triple(triple))


    def _json_ld_context(self):
        context = dict(
            (pfx, str(ns))
            for (pfx, ns) in self.graph.namespaces() if pfx and
            str(ns) != u"http://www.w3.org/XML/1998/namespace")
        context['@vocab'] = str(CASE)
        return context


    # Manually specify properties to help inforce both properties are supplied.
    def create_hash(self, hashMethod, hashValue):
        return self.create_Node(
                CASE.Hash, bnode=True, hashMethod=hashMethod, hashValue=hashValue)


    # We are going to default to json-ld instead of rdflib's default of xml.
    def serialize(self, format='json-ld', **kwargs):
        """Serializes the document's graph to a destination.
        (Follows same arguments as rdflib.Graph().serialize())"""
        if format == 'json-ld':
            if 'context' not in kwargs:
                kwargs['context'] = self._json_ld_context()
            if 'auto_compact' not in kwargs:
                kwargs['auto_compact'] = True
        return self.graph.serialize(format=format, **kwargs)


#    def serialize_append(self, format='json-ld', destination="new-api_output.json", **kwargs):
#        """
#        Serializes the document's graph to append to a  destination file.
#        """
#        if format == 'json-ld':
#            if 'context' not in kwargs:
#                kwargs['context'] = self._json_ld_context()
#            if 'auto_compact' not in kwargs:
#                kwargs['auto_compact'] = True
#        graph = self.graph.serialize(format=format, **kwargs)
#        with open(destination, "a") as fin:
#            fin.write(graph)
#        fin.close()


#====================================================
#-- CREATE A CASE OBJECT

    def create_Node(self, rdf_type=None, uri=None, bnode=False, **kwargs):
        return Node(self.graph, rdf_type=rdf_type, uri=uri, bnode=bnode,  **kwargs)

    def create_CoreObject(self, _type=None, **kwargs):
        """
        Creates and returns a CoreObject.
        """
        return CoreObject(self.graph, rdf_type=_type, **kwargs)

    def create_ContextObject(self, _type=None, **kwargs):
        """
        Creates and returns a Context.
        This class may not have PropertyBundles.
        """
        return ContextObject(self.graph, rdf_type=_type, **kwargs)

    def create_DuckObject(self, _type=None, **kwargs):
        """
        Creates and returns a Duck.
        These lonely Ducks have no CASE class parents and are fully duck-typed.
        This class may not have PropertyBundles.
        """
        return DuckObject(self.graph, rdf_type=_type, **kwargs)

    def create_SubObject(self, _type=None, **kwargs):
        """
        Creates and returns a Sub.
        This class is for children of one of the above CASE classes.
        This class may not have PropertyBundles.
        """
        return SubObject(self.graph, rdf_type=_type, **kwargs)

#====================================================
#-- CASE OBJECT CLASSES

class Node(object):
    """Implements a generic node in the graph."""

    RDF_TYPE = None
    # Namespace to use when adding properties that are not of type rdflib.URIRef.
    NAMESPACE = CASE

    def __init__(self, graph, uri=None, bnode=False, rdf_type=None, **kwargs):
        """Initializes and adds a node to the graph.

        NOTE: At least the type or a property must be supplied for the Node
        to exist in the graph.

        Args:
            graph: The graph to add this node to. (instance of rdflib.Graph)
            uri: Optional string to set th URI to. (If not provided a UUID will be generated.)
            bnode: Whether to create a blank node or a uri reference.
            rdf_type: The RDF type to set this node to.
            properties: Extra properties to add to this node.
            (More properties can be set after initialization by using the add() function.)
        """

        super(Node, self).__init__()
        if uri:
            self.uri = uri
        else:
            self.uri = str(uuid.uuid4())
        if bnode:
            self._node = rdflib.BNode(self.uri)
        else:
            self._node = rdflib.URIRef(self.uri)
        self._graph = graph
        if not rdf_type:
            rdf_type = self.RDF_TYPE

        # Add namespace prefix to non URIRef to allow abstraction from rdflib.
        if not isinstance(rdf_type, rdflib.term.Node):
            rdf_type = self.NAMESPACE[rdf_type]
        self.add(RDF.type, rdf_type)
        for key, value in iter(kwargs.items()):
            self.add(key, value)


    def add(self, property, value):
        """Adds a property and its value to the node."""
        # type: (object, object) -> object

        # Ignore setting properties with a None value.
        if value is None:
            return

        # Lists and other iterables as values are the equivelent of having multiple properties.
        # NOTE: Lists obviously lose their order.
        # TODO: Add support for ordered lists.
        if isinstance(value, (list, tuple, set)):
            for item in value:
                self.add(property, item)
            return
        if isinstance(value, Node):
            value = value._node

        # Convert basic python datatypes to literals.
        elif not isinstance(value, rdflib.term.Node):
            value = rdflib.Literal(value)

        # Automatically convert non-node properties to URIRef using default prefix.
        if not isinstance(property, rdflib.term.Node):
            property = self.NAMESPACE[property]

        self._graph.add((self._node, property, value))


class CoreObject(Node):

    RDF_TYPE = CASE.CoreObject

    def __init__(self, graph, rdf_type=None, **kwargs):
        """Initializes and adds a node to the graph.
        NOTE: At least the type or a property must be supplied for the Node
        to exist in the graph.

        Args:
            graph: The graph to add this node to. (instance of rdflib.Graph)
            rdf_type: The RDF type to set this node to.
            properties: Extra properties to add to this node.
            (More properties can be set after initialization by using the add() function.)
        """

        self.type = rdf_type

        super(CoreObject, self).__init__(graph, rdf_type=rdf_type, **kwargs)
        self.add('CoreObjectCreationTime', datetime.datetime.utcnow())
        self.pb = ""


    def create_PropertyBundle(self, prop_type=None, **kwargs):
        """Convenience function for adding property bundles to this Trace.

        Args:
            type: The @type of property bundle (can be of type rdflib.URIRef or string).
            properties: Properties to add to the created property bundle.

        Returns:
            The property bundle created (instance of PropertyBundle).
        """

        self.pb = PropertyBundle(self._graph, rdf_type=prop_type, **kwargs)
        self.add(CASE.propertyBundle, self.pb)

        return self.pb


class PropertyBundle(Node):

    RDF_TYPE = CASE.PropertyBundle

    def __init__(self, graph, rdf_type=None, **kwargs):
        """Initializes and adds a node to the graph.
        NOTE: At least the type or a property must be supplied for the Node
        to exist in the graph.

        Args:
            graph: The graph to add this node to. (instance of rdflib.Graph)
            rdf_type: The RDF type to set this node to.
            properties: Extra properties to add to this node.
            (More properties can be set after initialization by using the add() function.)
        """

        self.type = rdf_type

        # Property bundles should be blank nodes because we should be referencing them
        # through CoreObjects.
        self.propObj = kwargs

        super(PropertyBundle, self).__init__(
                graph, bnode=True, rdf_type=rdf_type, **kwargs)


class ContextObject(Node):

    RDF_TYPE = CASE.ContextObject

    def __init__(self, graph, rdf_type=None, **kwargs):
        """Initializes and adds a node to the graph.
        NOTE: At least the type must be supplied for the Node
        to exist in the graph.

        Args:
            graph: The graph to add this node to. (instance of rdflib.Graph)
            rdf_type: The RDF type to set this node to.
            properties: Extra properties to add to this node.
            (More properties can be set after initialization by using the add() function.)
        """

        self.type = rdf_type

        super(ContextObject, self).__init__(graph, rdf_type=rdf_type, **kwargs)
        self.add('ContextObjectCreationTime', datetime.datetime.utcnow())


class DuckObject(Node):

    RDF_TYPE = CASE.DuckObject

    def __init__(self, graph, rdf_type=None, **kwargs):
        """Initializes and adds a node to the graph.
        NOTE: At least the type must be supplied for the Node
        to exist in the graph.

        Args:
            graph: The graph to add this node to. (instance of rdflib.Graph)
            rdf_type: The RDF type to set this node to.
            properties: Extra properties to add to this node.
            (More properties can be set after initialization by using the add() function.)
        """

        self.type = rdf_type

        super(DuckObject, self).__init__(graph, rdf_type=rdf_type, **kwargs)
        self.add('DuckObjectCreationTime', datetime.datetime.utcnow())


class SubObject(Node):

    RDF_TYPE = CASE.SubObject

    def __init__(self, graph, rdf_type=None, **kwargs):
        """Initializes and adds a node to the graph.
        NOTE: At least the type must be supplied for the Node
        to exist in the graph.

        Args:
            graph: The graph to add this node to. (instance of rdflib.Graph)
            rdf_type: The RDF type to set this node to.
            properties: Extra properties to add to this node.
            (More properties can be set after initialization by using the add() function.)
        """

        self.type = rdf_type

        super(SubObject, self).__init__(graph, rdf_type=rdf_type, **kwargs)
        self.add('SubObjectCreationTime', datetime.datetime.utcnow())
