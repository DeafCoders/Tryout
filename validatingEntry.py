from tkinter import *
from apply import *


class ValidatingEntry(Entry):
    """base class for validating entry widgets"""

    def __init__(self, master, value="", **kw):
        apply(Entry.__init__, (self, master), kw)
        self.__value = value
        self.__variable = StringVar()
        self.__variable.set(value)
        self.__variable.trace("w", self.__callback)
        self.config(textvariable=self.__variable)

    def __callback(self, *dummy):
        value = self.__variable.get()
        new_value = self.validate(value)
        if new_value is None:
            self.__variable.set(self.__value)
        elif new_value != value:
            self.__value = new_value
            self.__variable.set(new_value)
        else:
            self.__value = value

    def validate(self, value):
        """override: return value, new value, or None if invalid"""
        return value


class IntegerEntry(ValidatingEntry):
    def validate(self, value):
        try:
            if value:
                v = int(value)
            return value
        except ValueError:
            return None


class FloatEntry(ValidatingEntry):
    def validate(self, value):
        try:
            if value:
                v = float(value)
            return value
        except ValueError:
            return None


class MaxLengthEntry(ValidatingEntry):
    def __init__(self, master, maxlength=None, **kw):
        self.maxlength = maxlength
        apply(ValidatingEntry.__init__, (self, master), kw)

    def validate(self, value):
        if self.maxlength is None or len(value) <= self.maxlength:
            return value
        return None  # new value too long
