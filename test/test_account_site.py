import unittest

from auth_system import Account, Site


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account1 = Account(
            "Ali_Babaei",
            "5Dj:xKBA",
            "0030376459",
            "09121212121",
            "SAliB_SAliB@gmail.com",
        )

    def test_init(self):
        self.assertEqual(
            self.account1.username,
            "Ali_Babaei",
            "\nThe username attribute was not initialized correctly.",
        )

        self.assertIn(
            "_",
            self.account1.username,
            "\nThe username must contain an underscore (_).",
        )

        self.assertEqual(
            self.account1.username.count("_"),
            1,
            "\nThe username must contain exactly one underscore (_).",
        )

        self.assertEqual(
            self.account1.password,
            "aca87bf6767f2dbb19d1d5b5d01e3d07eab8ea0f16741bd70e7c0784f0b3916d",
            "\nThe password attribute was not initialized correctly.",
        )

        self.assertEqual(
            self.account1.national_id,
            "0030376459",
            "\nThe national_id attribute was not initialized correctly.",
        )

        self.assertEqual(
            self.account1.phone,
            "09121212121",
            "\nThe phone attribute was not initialized correctly.",
        )

        self.assertEqual(
            self.account1.email,
            "SAliB_SAliB@gmail.com",
            "\nThe email attribute was not initialized correctly.",
        )


class TestSite(unittest.TestCase):
    def setUp(self):
        self.site1 = Site("salib.net")

    def test_init_site(self):
        self.assertEqual(
            self.site1.url,
            "salib.net",
            "\nThe url attribute was not initialized correctly.",
        )

        self.assertListEqual(
            self.site1.registered_users,
            [],
            "\nThe registered_users list was not initialized correctly.",
        )

        self.assertListEqual(
            self.site1.active_users,
            [],
            "\nThe active_users list was not initialized correctly.",
        )


if __name__ == "__main__":
    unittest.main()
