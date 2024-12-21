import unittest
from src.Encode import Encoder
from src.utils.helper import validate_floor, validate_side, validate_direction, validate_camera_id

class TestEncoder(unittest.TestCase):

    def setUp(self):
        """Create an instance of Encoder for testing."""
        self.encoder = Encoder()

    def test_validate_floor(self):
        """Test valid and invalid floor inputs."""
        self.assertEqual(validate_floor("0"), 0)
        self.assertEqual(validate_floor("255"), 255)
        with self.assertRaises(ValueError):
            validate_floor("-1")
        with self.assertRaises(ValueError):
            validate_floor("abc")

    def test_validate_side(self):
        """Test valid and invalid side inputs."""
        self.assertEqual(validate_side("N"), "N")
        self.assertEqual(validate_side("SW"), "SW")
        with self.assertRaises(ValueError):
            validate_side("X")

    def test_validate_direction(self):
        """Test valid and invalid direction inputs."""
        self.assertEqual(validate_direction("E"), "E")
        self.assertEqual(validate_direction("NW"), "NW")
        with self.assertRaises(ValueError):
            validate_direction("Z")

    def test_validate_camera_id(self):
        """Test valid and invalid camera ID inputs."""
        self.assertEqual(validate_camera_id("0"), 0)
        self.assertEqual(validate_camera_id("9999"), 9999)
        with self.assertRaises(ValueError):
            validate_camera_id("10000")
        with self.assertRaises(ValueError):
            validate_camera_id("abc")

    def test_encode_camera_location(self):
        """Test the encoding of camera location."""
        encoded = self.encoder.encode_camera_location(1, "N", "E", 1234)
        self.assertIn("binary_code", encoded)
        self.assertIn("decimal_code", encoded)
        self.assertEqual(encoded["binary_code"].count(' '), 3)  # Check format
        self.assertEqual(len(encoded["decimal_code"]), 12)  # Check length

if __name__ == "__main__":
    unittest.main()