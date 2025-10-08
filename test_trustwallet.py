# test_trustwallet.py
"""
Tests for TrustWallet module.
"""

import unittest
from trustwallet import TrustWallet

class TestTrustWallet(unittest.TestCase):
    """Test cases for TrustWallet class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TrustWallet()
        self.assertIsInstance(instance, TrustWallet)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TrustWallet()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
