""" install elstruct
"""
from distutils.core import setup


setup(name="elstruct",
      packages=["elstruct",
                "elstruct.writer",
                "elstruct.writer.psi4",
                "elstruct.writer.molpro",
                "elstruct.runner",
                "elstruct.runner.bebop",
                "elstruct.runner.blues",
                "elstruct.reader",
                "elstruct.reader.psi4",
                "elstruct.reader.molpro",
                "elstruct.reader.rere"],
      scripts=["scripts/sblues"])
