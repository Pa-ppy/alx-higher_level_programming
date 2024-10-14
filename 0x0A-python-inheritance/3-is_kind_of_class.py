#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance, or an instance that inherited from the specified class
    """
    return isinstance(obj, a_class)
