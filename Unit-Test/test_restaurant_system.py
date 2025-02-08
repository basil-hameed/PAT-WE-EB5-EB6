import unittest
from restaurant_system import SpecialMenuItem

class TestRestaurant(unittest.TestCase):
    def test_special_menu_item(self):
        item = SpecialMenuItem("Pasta", 300, 20, "Vegan")
        # print(item.display_item())
        self.assertEqual(item.display_item(), "Name :Pasta, Price : 300")

if __name__ == "__main__":
    unittest.main()