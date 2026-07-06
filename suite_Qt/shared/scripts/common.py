# -*- coding: utf-8 -*-
import names

def step1():
    activateItem(waitForObjectItem(names.address_Book_QMenuBar, "File"))
    activateItem(waitForObjectItem(names.address_Book_File_QMenu, "Open..."))
    scrollTo(waitForObject(names.treeView_QScrollBar), 15)
    mouseClick(waitForObjectItem(names.stackedWidget_treeView_QTreeView, "MyAddresses\\.adr"), 94, 10, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.qFileDialog_Open_QPushButton))

