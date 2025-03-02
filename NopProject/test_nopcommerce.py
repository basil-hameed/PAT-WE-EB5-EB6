from automate_nopcommerce import NopAutomation


url = "https://demo.nopcommerce.com/login"
myNopCommerce = NopAutomation(url)

class TestNopCommerce:

    def test_valid_login(self):
        expected_url = "https://demo.nopcommerce.com/"
        actual_url = myNopCommerce.perform_login()
        assert expected_url == actual_url
        print("SUCCESS: Test Case Passed - Logged in!")
