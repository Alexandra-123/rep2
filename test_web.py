import os
import pytest
from action_tests import ActionTests


@pytest.mark.usefixtures("setup")
class Tests:
    def test_title(self):
        self.driver.get("https://ficbook.net")
        assert self.driver.title == "Книга Фанфиков - более 25000 фэндомов, ориджиналы от популярных авторов"
