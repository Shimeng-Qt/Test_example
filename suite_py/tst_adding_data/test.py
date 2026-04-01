# -*- coding: utf-8 -*-

import names
import os


def main():
    startApplication('"' + os.environ["SQUISH_PREFIX"] + '/examples/qt/addressbook/addressbook"')
    invokeMenuItem("File", "New")
    table = waitForObject({"type": "QTableWidget"})
    test.verify(table.rowCount == 0)
    limit = 10  # To avoid testing 100s of rows since that would be boring
    for row, record in enumerate(testData.dataset("MyAddresses.tsv")):
        forename = testData.field(record, "Forename")
        surname = testData.field(record, "Surname")
        email = testData.field(record, "Email")
        phone = testData.field(record, "Phone")
        table.setCurrentCell(0, 0)  # always insert at the start
        addNameAndAddress((forename, surname, email, phone))  # pass as a single tuple
        checkNameAndAddress(table, record)
        if row > limit:
            break
    test.compare(table.rowCount, row + 1, "table contains as many rows as added data")
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


def checkNameAndAddress(table, record):
    for column in range(len(testData.fieldNames(record))):
        test.compare(table.item(0, column).text(),  # New addresses are inserted at the start
                     testData.field(record, column))
