# -*- coding: utf-8 -*-

import names
import os

source(findFile("scripts", "wrapsquishfunction.py"))


def addLoggingToClickButton(clickButtonFunction):  # Add this function
    def wrappedFunction(button, logText="clickButton() called"):
        test.log(logText, str(button))
        clickButtonFunction(button)
    return wrappedFunction


def main():
    startApplication('"' + os.environ["SQUISH_PREFIX"] + '/examples/qt/addressbook/addressbook"')
    wrapSquishFunction("clickButton", addLoggingToClickButton)  # Add this line
    # ...
    activateItem(waitForObjectItem(names.address_Book_QMenuBar, "File"))
    activateItem(waitForObjectItem(names.address_Book_File_QMenu, "Open..."))
    clickButton(waitForObject(names.qFileDialog_detailModeButton_QToolButton))
    waitForObjectItem(names.stackedWidget_treeView_QTreeView, "MyAddresses\\.adr")
    clickItem(names.stackedWidget_treeView_QTreeView, "MyAddresses\\.adr", 112, 9, 0, Qt.LeftButton)
    clickButton(waitForObject(names.qFileDialog_Open_QPushButton), "File Open clicked")
    waitForObjectItem(names.address_Book_MyAddresses_adr_File_QTableWidget, "1/1")
    clickItem(names.address_Book_MyAddresses_adr_File_QTableWidget, "1/1", 55, 20, 0, Qt.LeftButton)
    table = waitForObject(names.address_Book_MyAddresses_adr_File_QTableWidget)
    test.verify(table.rowCount == 125)
    activateItem(waitForObjectItem(names.address_Book_MyAddresses_adr_QMenuBar, "Edit"))
    activateItem(waitForObjectItem(names.address_Book_MyAddresses_adr_Edit_QMenu, "Add..."))
    type(waitForObject(names.forename_LineEdit), "Jane")
    type(waitForObject(names.forename_LineEdit), "<Tab>")
    type(waitForObject(names.surname_LineEdit), "Doe")
    type(waitForObject(names.surname_LineEdit), "<Tab>")
    type(waitForObject(names.email_LineEdit), "jane.doe@nowhere.com")
    type(waitForObject(names.email_LineEdit), "<Tab>")
    type(waitForObject(names.phone_LineEdit), "555 123 4567")
    clickButton(waitForObject(names.address_Book_Add_OK_QPushButton))
    waitForObjectItem(names.address_Book_MyAddresses_adr_File_QTableWidget, "3/1")
    clickItem(names.address_Book_MyAddresses_adr_File_QTableWidget, "3/1", 64, 11, 0, Qt.LeftButton)
    type(waitForObject(names.address_Book_MyAddresses_adr_File_QTableWidget), "<Shift>")
    type(waitForObject(names.address_Book_MyAddresses_adr_File_QTableWidget), "D")
    type(waitForObject(names.address_Book_MyAddresses_adr_3_1_LineEdit), "oe")
    type(waitForObject(names.address_Book_MyAddresses_adr_3_1_LineEdit), "<Return>")
    waitForObjectItem(names.address_Book_MyAddresses_adr_File_QTableWidget, "0/1")
    test.verify(table.rowCount == 126)
    clickItem(names.address_Book_MyAddresses_adr_File_QTableWidget, "0/1", 42, 6, 0, Qt.LeftButton)
    activateItem(waitForObjectItem(names.address_Book_MyAddresses_adr_QMenuBar, "Edit"))
    activateItem(waitForObjectItem(names.address_Book_MyAddresses_adr_Edit_QMenu, "Remove..."))
    clickButton(waitForObject(names.address_Book_Yes_QPushButton))
    test.verify(table.rowCount == 125)
    test.compare(waitForObjectExists(names.file_0_0_QModelIndex).text, "Jane")
    test.compare(waitForObjectExists(names.file_0_1_QModelIndex).text, "Doe")
    test.compare(waitForObjectExists(names.file_0_2_QModelIndex).text, "jane.doe@nowhere.com")
    test.compare(waitForObjectExists(names.file_0_3_QModelIndex).text, "555 123 4567")
    sendEvent("QCloseEvent", waitForObject(names.mainWindow))
    clickButton(waitForObject(names.address_Book_No_QPushButton))
