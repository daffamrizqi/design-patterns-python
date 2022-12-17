"""
perspective of a data engineer who needs to extract text from
various different unstructured file types like pdf and emails.
You'll create an informal interface that defines methods that will be in both the
pdfParser and EmlParser concrete classes
"""


"""
methods are defined but not implemented. The implementation will occur once you create
concrete classes that INHERIT from InformalParserInterface
"""
class InformalParserInterface:
    def load_data_source(self, path: str, file_name: str) -> str:
        """Load in the file for extracting text"""
        pass

    def extract_text(self, full_file_name: str) -> dict:
        """Extract text fromo the currently loaded file"""
        pass


"""
The concrete implementation of InformalParserInterface now allows you to extract text
from PDF files
"""
class PdfParser(InformalParserInterface):
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_name: str) -> dict:
        """Overrides InformalParserInterface.extract_text()"""
        pass


class EmlParser(InformalParserInterface):
    """Extract text from an email"""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override InformalParserInterface.extract_text()
        """
        pass


"""
So far you've defined concrete implementation of the InformalPythoninterface.
However, note that EmlParser fails to properly define .extract_text().
If you were to check whether EmlParser implements InformalParserInterface, then you’d get the following result
"""
# Check if both classes implement from InformalParsesInterface
print(issubclass(PdfParser, InformalParserInterface))
print(issubclass(EmlParser, InformalParserInterface))