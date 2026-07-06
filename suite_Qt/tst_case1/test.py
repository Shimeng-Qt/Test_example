# -*- coding: utf-8 -*-

import names
from common import step1


def main():
    startApplication("addressbook")
    source(findFile("scripts", "common.py"))
    step1()


    mouseClick(waitForObject(names.address_Book_MyAddresses_adr_File_QTableWidget), 533, 205, Qt.NoModifier, Qt.LeftButton)

    setWindowState(waitForObject(names.address_Book_MyAddresses_adr_MainWindow), WindowState.Normal)

    mouseClick(waitForObject(names.address_Book_MyAddresses_adr_File_QTableWidget), 497, 237, Qt.NoModifier, Qt.LeftButton)

    mouseClick(waitForObjectItem(names.address_Book_MyAddresses_adr_File_QTableWidget, "9/2"), 158, 4, Qt.NoModifier, Qt.LeftButton)

    mouseClick(waitForObject(names.address_Book_MyAddresses_adr_File_QTableWidget), 505, 145, Qt.NoModifier, Qt.LeftButton)
    test.ocrTextPresent("ad.crisp@beadsworth.net")

    mouseClick(waitForObject(names.address_Book_MyAddresses_adr_File_QTableWidget), 547, 265, Qt.NoModifier, Qt.LeftButton)
    test.imagePresent("image")

    test.vp("VP2")

    mouseClick(waitForObject(names.address_Book_MyAddresses_adr_File_QTableWidget), 552, 196, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.address_Book_MyAddresses_adr_File_QTableWidget, "0/0"), 22, 15, Qt.NoModifier, Qt.LeftButton)
    snooze(3)
    mouseClick(waitForObject(names.o1_HeaderViewItem), 16, 8, Qt.NoModifier, Qt.LeftButton)
    snooze(3)
    #mouseClick(waitForObject(names.o6_HeaderViewItem), 9, 9, Qt.ShiftModifier, Qt.LeftButton)
    mousePress(waitForObject(names.o6_HeaderViewItem), 9, 9, MouseButton.LeftButton, Modifier.Shift)
    mouseRelease(waitForObject(names.o6_HeaderViewItem), 9, 9, MouseButton.LeftButton, Modifier.Shift)
    snooze(3)
    clickButton(waitForObject(names.address_Book_MyAddresses_adr_Remove_QToolButton))
    clickButton(waitForObject(names.address_Book_Delete_No_QPushButton))
    clickButton(waitForObject(names.address_Book_MyAddresses_adr_Remove_QToolButton))
    clickButton(waitForObject(names.address_Book_Delete_Yes_QPushButton))
    sendEvent("QCloseEvent", waitForObject(names.address_Book_MyAddresses_adr_MainWindow))
    clickButton(waitForObject(names.address_Book_No_QPushButton))
    
