import pytest
from onboarding import Netshoes
import pathlib
import json


class TestOnboarding():
    def setup_method(self):
        self.netshoes = Netshoes()

    def teardown_method(self):
        pass

    '''Testar se foi feita alguma query / existe produtos no db'''

    def test_db(self):
        assert len(self.netshoes.produtos) > 0

    def test_report(self):
        self.netshoes.generate_report()
        assert pathlib.Path('report.json').exists

    def test_report_not_empty(self):
        with open('report.json', 'r') as obj:
            report = json.load(obj)
            assert isinstance(report, list)
            assert len(report) > 0
