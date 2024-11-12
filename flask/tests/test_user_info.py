import unittest
from services.user_info import generate_upn, get_groups

class TestUserInfo(unittest.TestCase):
    def test_generate_upn(self):
        self.assertEqual(generate_upn("John", "Doe", "Staff"), "john.doe@sofwerx.org")
        self.assertEqual(generate_upn("Mary Jane", "Smith", "Intern"), "mary.jane.smith.intern@sofwerx.org")

    def test_get_groups(self):
        group_data = get_groups("Nerd Herd", "EWI")
        self.assertIn("SWX_Trainual", group_data["groups"])
        self.assertIn("SWX_All", group_data["distribution_groups"])

if __name__ == "__main__":
    unittest.main()
