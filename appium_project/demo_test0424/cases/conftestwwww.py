import pytest
from ..utils.contact_info import ContactInfo
from ..page.app import App

@pytest.fixture(scope='class')
def initcalc_class():
    # setup
    print("setup")
    contactinfo = ContactInfo()
    app = App()
    yield app
    # teardown
    print("teardown")
    app.stop()

def initcalc_def():
    app = App()
    main = app.start().goto_main()
    yield main
    app.restart()

