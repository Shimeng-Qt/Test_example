# -*- coding: utf-8 -*-

import names


def main():
    startApplication("addressbook")
    activateItem(waitForObjectItem(names.address_Book_QMenuBar, "Help"))
    activateItem(waitForObjectItem(names.address_Book_Help_QMenu, "About"))
    # ***** The application CRASHED at this point! *****
