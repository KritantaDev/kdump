#
#  ktool | ktool
#  exceptions.py
#
#  Custom Exceptions for internal (and occasionally external) usage
#
#  This does not include the exceptions used in the interrupt model in the GUI.
#
#  This file is part of ktool. ktool is free software that
#  is made available under the MIT license. Consult the
#  file "LICENSE" that is distributed together with this file
#  for the exact licensing terms.
#
#  Copyright (c) 0cyn 2021.
#

class MalformedMachOException(Exception):
    """
    """


class MachOAlignmentError(Exception):
    """
    """


class VMAddressingError(ValueError):
    """
    """


class UnsupportedFiletypeException(Exception):
    """
    """


class NoObjCMetadataException(Exception):
    """
    """
