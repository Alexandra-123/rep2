import os
import pytest


@pytest.mark.usefixtures("setup")
class Tests:
    def test_title(self):
        self.driver.get("https://ru.wikipedia.org/wiki/Заглавная_страница")
        assert self.driver.title == "Википедия — свободная энциклопедия"
