from .printer import Printer

class ModernPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
         print(f"Faxing {document}...")

    def scan(self, document):
         print(f"Scanning {document}...")