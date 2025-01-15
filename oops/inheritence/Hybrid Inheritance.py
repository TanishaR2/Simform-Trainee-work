# Hybrid Inheritance (Combination of Multiple & Multilevel Inheritance)
class Printer:
    def print_doc(self):
        print("Printing document")

class Scanner:
    def scan_doc(self):
        print("Scanning document")

class Copier(Printer, Scanner):
    def copy_doc(self):
        print("Copying document")

def main():
    print("\nHybrid Inheritance:")
    copier = Copier()
    copier.print_doc()  # Inherited from Printer
    copier.scan_doc()  # Inherited from Scanner
    copier.copy_doc()  # Copier's own method

if __name__ == "__main__":
    main()
