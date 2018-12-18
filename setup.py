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
      package_data={'': ['elstruct/writer/*/templates/*.mako', 
                         'elstruct/runner/*/templates/*.mako']},
      include_package_data=True,
      scripts=["scripts/sblues"])
