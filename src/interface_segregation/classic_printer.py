from .printer import Printer

class ClassicPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

    # def fax(self, document):
    #     raise NotImplementedError("Fax functionality not supported")

    # def scan(self, document):
    #     raise NotImplementedError("Scan functionality not supported")
