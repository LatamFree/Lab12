import unittest
from src.interface_segregation.printer import Printer
from src.interface_segregation.classic_printer import ClassicPrinter
from src.interface_segregation.modern_printer import ModernPrinter

class TestSuite(unittest.TestCase):
    def setUp(self):
       self.classic_printer = ClassicPrinter()
       self.modern_printer = ModernPrinter()
       
    def test_printers(self):
        assert self.classic_printer.__class__.__base__ == Printer
        assert self.modern_printer.__class__.__base__ == Printer

    def test_classic_printer(self):
        assert hasattr(self.classic_printer, "fax") == False
        assert hasattr(self.classic_printer, "scan") == False

    def test_modern_printer(self):
        assert hasattr(self.modern_printer, "fax") == True
        assert hasattr(self.modern_printer, "scan") == True
