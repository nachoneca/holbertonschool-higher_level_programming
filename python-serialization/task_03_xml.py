#!/usr/bin/python3

"""
Try
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    
    """
    Serialize a Python dictionary to an XML file.
    
    Args:
    dictionary (dict): The dictionary to serialize.
    filename (str): The name of the file to save the XML data to.
    """
    
    root = ET.Element('data')
    
    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = value
        root.append(child)

    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    
    cons_dict = {}
    
    tree = ET.parse(filename)
    root = tree.getroot()
    
    for child in root:
        cons_dict[child.tag] = child.text
    
    return cons_dict
