import squish
import names

def main():
    # Start the address book application
    app_path = "C:\\Users\\shhuang\\squish_packages\\squish-9.2.0-qt68x-win64-msvc143\\examples\\qt\\addressbook\\addressbook.exe"
    squish.startApplication(app_path)

    # Click the New button to create a new (unnamed) address book
    squish.mouseClick(squish.waitForObject(names.address_Book_New_QToolButton))

    # Click the Add button to open the Add person dialog
    squish.mouseClick(squish.waitForObject(names.address_Book_Unnamed_Add_QToolButton))

    # Fill in the Forename field
    squish.mouseClick(squish.waitForObject(names.forename_LineEdit))
    squish.type(squish.waitForObject(names.forename_LineEdit), "vivi")

    # Fill in the Surname field
    squish.mouseClick(squish.waitForObject(names.surname_LineEdit))
    squish.type(squish.waitForObject(names.surname_LineEdit), "zhang")

    # Fill in the Email field
    squish.mouseClick(squish.waitForObject(names.email_LineEdit))
    squish.type(squish.waitForObject(names.email_LineEdit), "vivi.zhang@qt.io")

    # Fill in the Phone field
    squish.mouseClick(squish.waitForObject(names.phone_LineEdit))
    squish.type(squish.waitForObject(names.phone_LineEdit), "12345657")

    # Click OK to confirm adding the person
    squish.mouseClick(squish.waitForObject(names.address_Book_Add_OK_QPushButton))

    # Verify the person was added successfully
    squish.test.passes("New person 'vivi zhang' added successfully")
