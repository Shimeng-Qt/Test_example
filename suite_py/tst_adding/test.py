# -*- coding: utf-8 -*-

import names
import os


def main():
    startApplication('"' + os.environ["SQUISH_PREFIX"] + '/examples/qt/addressbook/addressbook"')
    invokeMenuItem("File", "New")
    table = waitForObject({"type": "QTableWidget"})
    test.verify(table.rowCount == 0)
    data = [("Andy", "Beach", "andy.beach@nowhere.com", "555 123 6786"),
            ("Candy", "Deane", "candy.deane@nowhere.com", "555 234 8765"),
            ("Ed", "Fernleaf", "ed.fernleaf@nowhere.com", "555 876 4654")]
    for oneNameAndAddress in data:
        addNameAndAddress(oneNameAndAddress)
    waitForObject(table)
    test.compare(table.rowCount, len(data), "table contains as many rows as added data")

    test.ocrTextPresent("Beach")
    closeWithoutSaving()


def invokeMenuItem(menu, item):
    activateItem(waitForObjectItem({"type": "QMenuBar"}, menu))
    activateItem(waitForObjectItem({'type': 'QMenu', 'title': menu}, item))


def addNameAndAddress(oneNameAndAddress):
    invokeMenuItem("Edit", "Add...")
    type(waitForObject(names.forename_LineEdit), oneNameAndAddress[0])
    type(waitForObject(names.surname_LineEdit), oneNameAndAddress[1])
    type(waitForObject(names.email_LineEdit), oneNameAndAddress[2])
    type(waitForObject(names.phone_LineEdit), oneNameAndAddress[3])
    clickButton(waitForObject(names.address_Book_Add_OK_QPushButton))


def closeWithoutSaving():
    sendEvent("QCloseEvent", waitForObject(names.mainWindow))
    clickButton(waitForObject(names.address_Book_No_QPushButton))
