# -*- coding: utf-8 -*-
#
# Copyright © 2009-2010 CEA
# Pierre Raybaut
# Licensed under the terms of the CECILL License
# (see guidata/__init__.py for details)

"""
ActivableDataSet example

Warning: ActivableDataSet objects were made to be integrated inside GUI layouts.
So this example with dialog boxes may be confusing.
--> see tests/editgroupbox.py to understand the activable dataset usage
"""

# When editing, all items are shown.
# When showing dataset in read-only mode (e.g. inside another layout), all items
# are shown except the enable item.

from guidata.dataset.dataitems import BoolItem, ChoiceItem, ColorItem, FloatItem
from guidata.dataset.datatypes import ActivableDataSet
from guidata.env import execenv
from guidata.qthelpers import qt_app_context

# guitest: show


class ExampleDataSet(ActivableDataSet):
    """
    Example
    <b>Activable dataset example</b>
    """

    def __init__(self, title=None, comment=None, icon=""):
        ActivableDataSet.__init__(self, title, comment, icon)

    enable = BoolItem(
        "Enable parameter set",
        help="If disabled, the following parameters will be ignored",
        default=False,
    )
    param0 = ChoiceItem("Param 0", ["choice #1", "choice #2", "choice #3"])
    param1 = FloatItem("Param 1", default=0, min=0)
    param2 = FloatItem("Param 2", default=0.93)
    color = ColorItem("Color", default="red")


ExampleDataSet.active_setup()


def test():
    with qt_app_context():
        prm = ExampleDataSet()
        prm.set_writeable()
        prm.edit()
        prm.set_readonly()
        prm.view()
        execenv.print("OK")


if __name__ == "__main__":
    test()
