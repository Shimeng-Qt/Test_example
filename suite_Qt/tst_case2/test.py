# -*- coding: utf-8 -*-

import names
from screen import Screen
import traceback

def main():
    startApplication("addressbook")

    screen = Screen.byIndex(0)  # Get the first screen
    geometry = screen.geometry
 
    test.log(f"Screen width: {geometry.width}")
    test.log(f"Screen height: {geometry.height}")
     
    pos = waitForObject(names.address_Book_New_QToolButton).mapToGlobal(QPoint(0, 0))
    test.log("x/y: %d/%d" % (pos.x, pos.y))
     
     
    mouseClick(waitForObjectItem(names.address_Book_QMenuBar, "File"))
    mouseClick(waitForObjectItem(names.address_Book_File_QMenu, "New"))
    clickButton(waitForObject(names.address_Book_Unnamed_Add_QToolButton))
    mouseClick(waitForObject(names.forename_LineEdit), 31, 19, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.forename_LineEdit), "a")
    mouseClick(waitForObject(names.surname_LineEdit), 22, 8, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.surname_LineEdit), "b")
    mouseClick(waitForObject(names.email_LineEdit), 14, 8, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.email_LineEdit), "t")
    mouseClick(waitForObject(names.phone_LineEdit), 13, 4, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.phone_LineEdit), "d")
    clickButton(waitForObject(names.address_Book_Add_OK_QPushButton))

    test.vp("VP5")

    test.vp("VP6")