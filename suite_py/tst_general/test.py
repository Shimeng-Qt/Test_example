# -*- coding: utf-8 -*-

import names
import os


def main():
    startApplication('"' + os.environ["SQUISH_PREFIX"] + '/examples/qt/addressbook/addressbook"')
    #attachToApplication("addressbook")
    activateItem(waitForObjectItem(names.address_Book_QMenuBar, "File"))
    activateItem(waitForObjectItem(names.address_Book_File_QMenu, "Open..."))
    clickButton(waitForObject(names.qFileDialog_detailModeButton_QToolButton))
    mouseClick(waitForObjectItem(names.stackedWidget_treeView_QTreeView, "MyAddresses\\.adr"), 104, 12, 0, Qt.LeftButton)
    clickButton(waitForObject(names.qFileDialog_Open_QPushButton))
    table = waitForObject(names.address_Book_MyAddresses_adr_File_QTableWidget)
    test.compare(table.rowCount, 125)
    clickButton(waitForObject(names.address_Book_MyAddresses_adr_Add_QToolButton))
    snooze(.5)  # qt4/linux workaround
    type(waitForObject(names.forename_LineEdit), "Jane")
    type(waitForObject(names.forename_LineEdit), "<Tab>")
    type(waitForObject(names.surname_LineEdit), "Doe")
    type(waitForObject(names.surname_LineEdit), "<Tab>")
    type(waitForObject(names.email_LineEdit), "jane.doe@nowhere.com")
    type(waitForObject(names.email_LineEdit), "<Tab>")
    type(waitForObject(names.phone_LineEdit), "123 555 1212")
    clickButton(waitForObject(names.address_Book_Add_OK_QPushButton))
    test.compare(table.rowCount, 126)
    doubleClick(waitForObjectItem(names.address_Book_MyAddresses_adr_File_QTableWidget, "3/1"), 19, 16, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.file_LineEdit), "Doe")
    type(waitForObject(names.file_LineEdit), "<Return>")
    mouseClick(waitForObjectItem(names.address_Book_MyAddresses_adr_File_QTableWidget, "4/1"), 72, 21, 0, Qt.LeftButton)
    clickButton(waitForObject(names.address_Book_MyAddresses_adr_Remove_QToolButton))
    clickButton(waitForObject(names.address_Book_Yes_QPushButton))
    test.compare(waitForObjectExists(names.file_0_0_QModelIndex).text, "Jane")
    test.compare(waitForObjectExists(names.file_0_1_QModelIndex).text, "Doe")
    test.compare(waitForObjectExists(names.file_0_2_QModelIndex).text, "jane.doe@nowhere.com")
    test.compare(waitForObjectExists(names.file_0_3_QModelIndex).text, "123 555 1212")
    test.compare(table.rowCount, 125)
    sendEvent("QCloseEvent", waitForObject(names.mainWindow))
    clickButton(waitForObject(names.address_Book_No_QPushButton))
