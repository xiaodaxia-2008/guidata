# -*- coding: utf-8 -*-
#
# Copyright © 2009-2010 CEA
# Pierre Raybaut
# Licensed under the terms of the CECILL License
# (see guidata/__init__.py for details)

"""
JSON I/O demo

DataSet objects may be saved in JSON files.
This script shows how to save in and then reload data from a JSON file.
"""

# guitest: show

import os

from guidata.env import execenv
from guidata.jsonio import JSONReader, JSONWriter
from guidata.qthelpers import qt_app_context
from guidata.tests.test_all_items import TestParameters


def test():
    with qt_app_context():
        if os.path.exists("test.json"):
            os.unlink("test.json")

        e = TestParameters()
        if execenv.unattended or e.edit():
            writer = JSONWriter("test.json")
            e.serialize(writer)
            writer.save()

            e = TestParameters()
            reader = JSONReader("test.json")
            e.deserialize(reader)
            e.edit()
        execenv.print("OK")


if __name__ == "__main__":
    test()
