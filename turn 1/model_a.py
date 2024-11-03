import unittest
from unittest.mock import patch, Mock


class DataQualityManagement:
    def __init__(self, consent_manager):
        self.consent_manager = consent_manager

    def process_data_with_consent(self, data):
        if self.consent_manager.check_consent(data['user_id']):
            # Perform data processing with consent
            return "Data processed with consent"
        else:
            # Handle data without consent
            return "Data processing blocked by consent"


class TestDataQualityManagement(unittest.TestCase):

    @patch('__main__.ConsentManagement')
    def test_consent_management_functioning(self, MockConsentManagement):
        # Create a mock consent manager instance
        mock_cm = MockConsentManagement.return_value

        # Configure the mock to return True for user_id 1
        mock_cm.check_consent.return_value = True

        dqm = DataQualityManagement(mock_cm)
        test_data = {'user_id': 1, 'email': 'test@example.com'}
        result = dqm.process_data_with_consent(test_data)

        self.assertEqual(result, "Data processed with consent")

        # Configure the mock to return False for user_id 2
        mock_cm.check_consent.return_value = False
        test_data = {'user_id': 2, 'email': 'test2@example.com'}
        result = dqm.process_data_with_consent(test_data)
        self.assertEqual(result, "Data processing blocked by consent")


if __name__ == '__main__':
    unittest.main()
