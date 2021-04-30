import pytest
from ..utils.contact_info import ContactInfo
from ..page.app import App



@pytest.fixture()
def initcalc_class():
    app = App()
    main = app.start()
    yield main
    app.stop()


@pytest.fixture()
def initcalc_fake():
    contactinfo = ContactInfo()
    yield contactinfo




