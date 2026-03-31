# -*- coding: utf-8 -*-

import names
import os


def tableItemChangedHandler(obj, item):
    test.log('itemChanged emitted by object "%s" on item "%s"' % (
        objectMap.symbolicName(obj), item.text()))


def fileMenuHandler(obj, action):
    test.log('triggered emitted by object "%s" for action "%s"' % (
        objectMap.symbolicName(obj), action.text))


def modelIndexClickedHandler(obj, index):
    test.log('clicked emitted by object "%s" on index "%s"' % (
        objectMap.symbolicName(obj), index.text))


def cellClickedHandler(obj, row, column):
    test.log('clicked emitted by object "%s" on cell (%d, %d)' % (
        objectMap.symbolicName(obj), row, column))


def main():
    startApplication('"' + os.environ["SQUISH_PREFIX"] + '/examples/qt/addressbook/addressbook"')
    activateItem(waitForObjectItem(names.address_Book_QMenuBar, "File"))
    fileMenu = waitForObject(names.address_Book_File_QMenu)
    installSignalHandler(fileMenu, "triggered(QAction*)", "fileMenuHandler")
    activateItem(waitForObjectItem(names.address_Book_File_QMenu, "Open..."))
    clickButton(waitForObject(names.qFileDialog_detailModeButton_QToolButton))
    waitForObjectItem(names.stackedWidget_treeView_QTreeView, "MyAddresses\\.adr")
    clickItem(names.stackedWidget_treeView_QTreeView, "MyAddresses\\.adr", 81, 4, 0, Qt.LeftButton)
    clickButton(waitForObject(names.qFileDialog_Open_QPushButton))

    table = waitForObject(names.address_Book_MyAddresses_adr_File_QTableWidget)
    installSignalHandler(table, "itemChanged(QTableWidgetItem*)", "tableItemChangedHandler")
    installSignalHandler(table, "clicked(QModelIndex)", "modelIndexClickedHandler")
    installSignalHandler(table, "cellClicked(int, int)", "cellClickedHandler")

    mouseClick(waitForObjectItem(names.address_Book_MyAddresses_adr_File_QTableWidget, "2/1"))
    type(waitForObject(names.address_Book_MyAddresses_adr_File_QTableWidget), "<F2>")
    type(waitForObject(names.address_Book_MyAddresses_adr_2_1_LineEdit), "Doe")
    type(waitForObject(names.address_Book_MyAddresses_adr_2_1_LineEdit), "<Return>")

    mouseClick(waitForObjectItem(names.address_Book_MyAddresses_adr_File_QTableWidget, "3/3"))
    type(waitForObject(names.address_Book_MyAddresses_adr_File_QTableWidget), "<F2>")
    type(waitForObject(names.address_Book_MyAddresses_adr_3_3_LineEdit), "<Backspace>")
    type(waitForObject(names.address_Book_MyAddresses_adr_3_3_LineEdit), "<Return>")

    activateItem(waitForObjectItem(names.address_Book_MyAddresses_adr_QMenuBar, "File"))
    activateItem(waitForObjectItem(names.address_Book_MyAddresses_adr_File_QMenu, "Quit"))
    clickButton(waitForObject(names.address_Book_No_QPushButton))
