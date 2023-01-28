# PyQT

[pip package](https://pypi.org/project/PyQt5/)

The UI is made with a python integration of [QT](https://www.qt.io/), is works but i strongly believe that "heavy-client" ui should not be a thing anymore and that a web UI would be a lot better, for this short project, I chosed to still use QT as there was no mention of it being web at all.

The Ui is defined in a [XML file](../ui/ui.xml) and then loaded by QT in [ui.py](../ui/ui.py) with `loadUi("ui/ui.xml", self)`