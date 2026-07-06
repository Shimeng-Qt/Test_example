# -*- coding: utf-8 -*-
import names
# -*- coding: utf-8 -*-

@mbt.step("Create new address book")
def step():
    startApplication("addressbook")

    activateItem(waitForObjectItem(names.address_Book_QMenuBar, "File"))
    activateItem(waitForObjectItem(names.address_Book_File_QMenu, "New"))
    
@mbt.step("Open Add view")
def step():
    clickButton(waitForObject(names.address_Book_Unnamed_Add_QToolButton))

    
@mbt.step("Fill in contact information")
def step():

    type(waitForObject(names.forename_LineEdit), "a")
    mouseClick(waitForObject(names.surname_LineEdit), 20, 13, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.surname_LineEdit), "b")
    mouseClick(waitForObject(names.email_LineEdit), 22, 7, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.email_LineEdit), "v")
    mouseClick(waitForObject(names.address_Book_Add_Dialog), 90, 93, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.phone_LineEdit), 17, 5, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.phone_LineEdit), "c")

@mbt.step("Confirm")
def step():
    clickButton(waitForObject(names.address_Book_Add_OK_QPushButton))

@mbt.step("Verify new entry has been added")
def step():

    test.compare(waitForObjectExists(names.address_Book_Unnamed_File_QTableWidget).rowCount, 1)

@mbt.step("Abort")
def step():
    clickButton(waitForObject({"type":"QPushButton", "text":"Cancel"}))

@mbt.step("Verify no new entry has been added")
def step():
    test.compare(
        waitForObjectExists({"type": "QTableWidget"}).rowCount,
        0,
        "There should be 0 entries in the address book"
        )
