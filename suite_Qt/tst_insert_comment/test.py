# -*- coding: utf-8 -*-

import names


def main():
    startApplication("_addressbook")
    test.breakpoint()
    clickButton(waitForObject(names.address_Book_New_QToolButton))
    # create a new table
    mouseClick(waitForObject(names.address_Book_Unnamed_QStatusBar), 164, 10, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.address_Book_Unnamed_Add_QToolButton))
    # add a new entry
    # first name
    # last name
    type(waitForObject(names.email_LineEdit), "<Backspace>")
    type(waitForObject(names.email_LineEdit), "<CapsLock>")
    type(waitForObject(names.email_LineEdit), "@example.com")
    # email
    # phone
