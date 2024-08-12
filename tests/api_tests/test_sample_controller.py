import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, json
import app.controllers.voting_controller as controller
from parameterized import parameterized


class TestVotingController(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)

    @patch("app.services.voting_service.votes_collection.insert_one")
    @patch("app.services.voting_service.votes_collection.find_one")
    @patch("app.services.voting_service.kafka_wrapper.publish_message")
    def test_create_vote_valid_data(
        self, mock_publish_message, mock_find_one, mock_insert_one
    ):
        """Test create_vote with valid data and get 201"""
        with self.app.test_request_context(
            "/api/v1/create_vote",
            method="POST",
            json={"user_id": "user_123", "vote_value": "up_vote"},
        ):
            # Arrange
            mock_vote_data = {
                "_id": "1",
                "vote_id": "1",
                "user_id": "user_123",
                "vote_value": "up_vote",
            }
            mock_find_one.return_value = mock_vote_data
            mock_insert_one.return_value = MagicMock(acknowledged=True, inserted_id="1")

            # Act
            response, status_code = controller.create_vote()
            response_data = json.loads(response.get_data(as_text=True))

            # Assert
            self.assertEqual(status_code, 201)
            self.assertEqual(
                response_data,
                {
                    "vote_id": "1",
                    "user_id": "user_123",
                    "vote_value": "up_vote",
                },
            )

            # # Verify Kafka publish_message was called
            # mock_publish_message.assert_called_once_with(
            #     topic="votes_topic", key="1", value=mock_vote_data
            # )

    @parameterized.expand(
        [
            ({"vote_value": "up_vote"}, "user_id has to be minimum 5 characters"),
            (
                {"user_id": "user", "vote_value": "up_vote"},
                "user_id has to be minimum 5 characters",
            ),
            (
                {"user_id": "user1", "vote_value": " "},
                "vote_value has to be minimum 1 character",
            ),
            (
                {"user_id": "user1"},
                "vote_value has to be minimum 1 character",
            ),
        ]
    )
    def test_create_vote_invalid_inputs(self, json_data, expected_error_message):
        """Test create_vote with various invalid inputs"""
        with self.app.test_request_context(
            "/api/v1/create_vote",
            method="POST",
            json=json_data,
        ):
            # Act & Assert
            with self.assertRaises(ValueError) as context:
                controller.create_vote()

            # Check if the correct message is raised
            self.assertTrue(expected_error_message in str(context.exception))


if __name__ == "__main__":
    unittest.main()
