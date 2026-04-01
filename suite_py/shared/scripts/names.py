# encoding: UTF-8

from objectmaphelper import *

# See the chapter 'Script-Based Object Map API' in the Squish manual for
# documentation of the functionality offered by the 'objectmaphelper' module.

# address_Book_MainWindow = {"type": "MainWindow", "unnamed": 1, "visible": 1, "windowTitle": "Address Book"}
# address_Book_Open_QToolButton = {"text": "Open", "type": "QToolButton", "unnamed": 1, "visible": 1, "window": address_Book_MainWindow}
# qFileDialog_QFileDialog = {"name": "QFileDialog", "type": "QFileDialog", "visible": 1}
# qFileDialog_splitter_QSplitter = {"name": "splitter", "type": "QSplitter", "visible": 1, "window": qFileDialog_QFileDialog}
# splitter_frame_QFrame = {"container": qFileDialog_splitter_QSplitter, "name": "frame", "type": "QFrame", "visible": 1}
# frame_stackedWidget_QStackedWidget = {"container": splitter_frame_QFrame, "name": "stackedWidget", "type": "QStackedWidget", "visible": 1}
# stackedWidget_treeView_QTreeView = {"container": frame_stackedWidget_QStackedWidget, "name": "treeView", "type": "QTreeView", "visible": 1}
# address_Book_MyAddresses_adr_MainWindow = {"type": "MainWindow", "unnamed": 1, "visible": 1, "windowTitle": "Address Book - MyAddresses.adr"}
# address_Book_MyAddresses_adr_File_QToolBar = {"type": "QToolBar", "unnamed": 1, "visible": 1, "window": address_Book_MyAddresses_adr_MainWindow, "windowTitle": "File"}
# address_Book_MyAddresses_adr_File_QTableWidget = {"aboveWidget": address_Book_MyAddresses_adr_File_QToolBar, "type": "QTableWidget", "unnamed": 1, "visible": 1, "window": address_Book_MyAddresses_adr_MainWindow}
# address_Book_MyAddresses_adr_Add_QToolButton = {"text": "Add", "type": "QToolButton", "unnamed": 1, "visible": 1, "window": address_Book_MyAddresses_adr_MainWindow}
# address_Book_Add_Dialog = {"type": "Dialog", "unnamed": 1, "visible": 1, "windowTitle": "Address Book - Add"}
# address_Book_Add_Forename_QLabel = {"text": "Forename:", "type": "QLabel", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
# forename_LineEdit = {"buddy": address_Book_Add_Forename_QLabel, "type": "LineEdit", "unnamed": 1, "visible": 1}
# address_Book_Add_Surname_QLabel = {"text": "Surname:", "type": "QLabel", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
# surname_LineEdit = {"buddy": address_Book_Add_Surname_QLabel, "type": "LineEdit", "unnamed": 1, "visible": 1}
# address_Book_Add_Email_QLabel = {"text": "Email:", "type": "QLabel", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
# email_LineEdit = {"buddy": address_Book_Add_Email_QLabel, "type": "LineEdit", "unnamed": 1, "visible": 1}
# address_Book_Add_Phone_QLabel = {"text": "Phone:", "type": "QLabel", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
# phone_LineEdit = {"buddy": address_Book_Add_Phone_QLabel, "type": "LineEdit", "unnamed": 1, "visible": 1}
# address_Book_Add_OK_QPushButton = {"text": "OK", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
# address_Book_MyAddresses_adr_Remove_QToolButton = {"text": "Remove", "type": "QToolButton", "unnamed": 1, "visible": 1, "window": address_Book_MyAddresses_adr_MainWindow}
# address_Book_QMessageBox = {"type": "QMessageBox", "unnamed": 1, "visible": 1}
# address_Book_No_QPushButton = {"text": "No", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": address_Book_QMessageBox}
# address_Book_Yes_QPushButton = {"text": "Yes", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": address_Book_QMessageBox}
# file_2_3_QModelIndex = {"column": 3, "container": address_Book_MyAddresses_adr_File_QTableWidget, "row": 2, "type": "QModelIndex"}
# file_2_2_QModelIndex = {"column": 2, "container": address_Book_MyAddresses_adr_File_QTableWidget, "row": 2, "type": "QModelIndex"}
# file_2_1_QModelIndex = {"column": 1, "container": address_Book_MyAddresses_adr_File_QTableWidget, "row": 2, "type": "QModelIndex"}
# file_2_0_QModelIndex = {"column": 0, "container": address_Book_MyAddresses_adr_File_QTableWidget, "row": 2, "type": "QModelIndex"}
# address_Book_MyAddresses_adr_QMenuBar = {"type": "QMenuBar", "unnamed": 1, "visible": 1, "window": address_Book_MyAddresses_adr_MainWindow}
# address_Book_MyAddresses_adr_File_QMenu = {"title": "File", "type": "QMenu", "unnamed": 1, "visible": 1, "window": address_Book_MyAddresses_adr_MainWindow}
# address_Book_QMenuBar = {"type": "QMenuBar", "unnamed": 1, "visible": 1, "window": address_Book_MainWindow}
# address_Book_File_QMenu = {"title": "File", "type": "QMenu", "unnamed": 1, "visible": 1, "window": address_Book_MainWindow}
# qFileDialog_Open_QPushButton = {"text": "Open", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": qFileDialog_QFileDialog}
# qFileDialog_detailModeButton_QToolButton = {"name": "detailModeButton", "type": "QToolButton", "visible": 1, "window": qFileDialog_QFileDialog}
# file_LineEdit = {"columnIndex": 1, "container": address_Book_MyAddresses_adr_File_QTableWidget, "rowIndex": 3, "type": "LineEdit", "unnamed": 1, "visible": 1}
# file_0_3_QModelIndex = {"column": 3, "container": address_Book_MyAddresses_adr_File_QTableWidget, "row": "0", "type": "QModelIndex"}
# file_0_2_QModelIndex = {"column": 2, "container": address_Book_MyAddresses_adr_File_QTableWidget, "row": "0", "type": "QModelIndex"}
# file_0_1_QModelIndex = {"column": 1, "container": address_Book_MyAddresses_adr_File_QTableWidget, "row": "0", "type": "QModelIndex"}
# file_0_0_QModelIndex = {"column": "0", "container": address_Book_MyAddresses_adr_File_QTableWidget, "row": "0", "type": "QModelIndex"}
# address_Book_MyAddresses_adr_Edit_QMenu = {"title": "Edit", "type": "QMenu", "unnamed": 1, "visible": 1, "window": address_Book_MyAddresses_adr_MainWindow}
# address_Book_MyAddresses_adr_3_1_LineEdit = {"column": 1, "row": 3, "type": "LineEdit", "unnamed": 1, "visible": 1, "window": address_Book_MyAddresses_adr_MainWindow}
# address_Book_MyAddresses_adr_3_3_LineEdit = {"column": 3, "row": 3, "type": "LineEdit", "unnamed": 1, "visible": 1, "window": address_Book_MyAddresses_adr_MainWindow}
# address_Book_MyAddresses_adr_2_1_LineEdit = {"column": 1, "row": 2, "type": "LineEdit", "unnamed": 1, "visible": 1, "window": address_Book_MyAddresses_adr_MainWindow}
#--------------- mainWindow = {"type": "MainWindow", "unnamed": 1, "visible": 1}
# address_Book_Add_QToolButton = {"text": "Add", "type": "QToolButton", "unnamed": 1, "visible": 1, "window": address_Book_MainWindow}

