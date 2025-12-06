import unittest
from pathlib import Path
from pyonix_core.parsing.parser import parse_onix_stream
from pyonix_core.facade.product import ProductFacade

class TestParsing(unittest.TestCase):
    def test_parse_short_tags(self):
        xml_path = Path(__file__).parent / "sample_short.xml"
        products = list(parse_onix_stream(xml_path))
        
        self.assertEqual(len(products), 1)
        product = products[0]
        
        facade = ProductFacade(product)
        
        self.assertEqual(facade.record_reference, "REF001")
        self.assertEqual(facade.isbn13, "9781234567890")
        self.assertEqual(facade.title, "Test Book Title")
        self.assertIn("F. Scott Fitzgerald", facade.contributors)
        self.assertEqual(facade.price_amount, 10.99)

if __name__ == "__main__":
    unittest.main()
