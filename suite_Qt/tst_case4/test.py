# -*- coding: utf-8 -*-

import names
import json

def main():
    startApplication("calqlatrexample")
    obj = waitForObject(names.o_QQuickWindowQmlImpl)
    #listView = waitForObject({"container": names.o_QQuickWindowQmlImpl, "objectName": "digitalOutputsListView", "type": "ListView"})
    listView = waitForObject(names.digitalOutputsListView_ListView)
    count = listView.count
    test.log("Count: " + str(count))
    test.breakpoint()
    
    for i in range(count):
        item = waitForObject({"container": names.digitalOutputsListView_ListView, "index": i, "type": "Text"})
        test.log("Item text: " + str(item.text))


    json_str = obj.property("digitalOutputsDataJson")
    
    json_str1 = str(json_str)
    
    data = json.loads(json_str1)
    
    for item in data:
        test.log(item["name"])

    
    
    names.digitalOutputsListView_delegate_0_Text
    digitalOutputsListView_delegate_0_Text = {"container": digitalOutputsListView_ListView, "index": 0, "objectName": "delegate_0", "type": "Text", "visible": True}
    names.digitalOutputsListView_delegate_1_Text

    #===========================================================================
    # activateItem(waitForObjectItem(names.address_Book_QMenuBar, "File"))
    # activateItem(waitForObjectItem(names.address_Book_File_QMenu, "Open..."))
    # scrollTo(waitForObject(names.treeView_QScrollBar), 16)
    # mouseClick(waitForObjectItem(names.stackedWidget_treeView_QTreeView, "MyAddresses\\.adr"), 90, 8, Qt.NoModifier, Qt.LeftButton)
    # clickButton(waitForObject(names.qFileDialog_Open_QPushButton))
    # 
    # obj = waitForObject(names.o30_HeaderViewItem)
    # rect = object.globalBounds(obj)
    # 
    #===========================================================================
    #scrollTo(waitForObject(names.file_QScrollBar), 24)
    #mouseClick(waitForObject(names.o30_HeaderViewItem), 8, 11, Qt.NoModifier, Qt.LeftButton)

    test.breakpoint()
    
    
#===============================================================================
#     clickButton(waitForObject(names.address_Book_New_QToolButton))
# 
#     clickButton(waitForObject(names.address_Book_Unnamed_New_QToolButton))
#     
#     ok = waitFor(lambda: object.exists(names.address_Book_Unnamed_New_QToolButton) and object.exists(names.address_Book_Unnamed_Add_QToolButton), 5000)
#     
#     if not ok:
#         test.log("waitFor function no work")
#     else:
#         test.log("waitFor function works")
#     
#     clickButton(waitForObject(names.address_Book_Unnamed_Add_QToolButton))
#     clickButton(waitForObject(names.address_Book_Add_Cancel_QPushButton))
#     
#     ok_1 = waitFor(lambda: object.exists(names.address_Book_Add_Cancel_QPushButton) and object.exists(names.address_Book_Unnamed_Add_QToolButton), 5000)
#     
#     if not ok_1:
#         test.log("waitFor function no work")
#     else:
#         test.log("waitFor function works")
# 
#     test.breakpoint()
#===============================================================================
