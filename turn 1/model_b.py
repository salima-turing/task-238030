import unittest
from unittest.mock import patch, Mock


# Your data quality management system function
def personalize_data(data, consent_manager):
    personalized_data = []
    for entry in data:
        if consent_manager.is_consented(entry['user_id']):
            personalized_data.append(entry)
    return personalized_data


# Consent management class (you can replace this with your actual implementation)
class ConsentManagement:
    def is_consented(self, user_id):
        # Replace this with your actual consent logic
        return True


class TestPersonalizeData(unittest.TestCase):

    @patch('__main__.ConsentManagement')
    def test_personalize_data_with_consent(self, MockConsentManagement):
        # Mock the consent management instance
        mock_consent_manager = MockConsentManagement.return_value
        mock_consent_manager.is_consented.return_value = True

        # Sample data
        data = [
            {'user_id': 1, 'name': 'Alice'},
            {'user_id': 2, 'name': 'Bob'},
            {'user_id': 3, 'name': 'Charlie'}
        ]

        # Call the function under test
        result = personalize_data(data, mock_consent_manager)

        # Assert the expected result
        self.assertEqual(result, data)

    @patch('__main__.ConsentManagement')
    def test_personalize_data_without_consent(self, MockConsentManagement):
        # Mock the consent management instance
        mock_consent_manager = MockConsentManagement.return_value
        mock_consent_manager.is_consented.return_value = False

        # Sample data
        data = [
            {'user_id': 1, 'name': 'Alice'},
            {'user_id': 2, 'name': 'Bob'},
            {'user_id': 3, 'name': 'Charlie'}
        ]

        # Call the function under test
        result = personalize_data(data, mock_consent_manager)

        # Assert the expected result
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
