import unittest
from unittest.mock import patch
from flask import Flask, request, json, jsonify
import app.controllers.voting_controller as controller
from app.dto.vote import Vote


class TestVotingController(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)

    def test_create_vote(self):
        with self.app.test_request_context(
            "/api/v1/create_vote",
            method="POST",
            json={"user_id": "user_123", "vote_value": "up_vote"},
        ):
            with patch("app.services.voting_service.cast_vote") as mock_cast_vote:
                # arrange
                mock_vote = Vote(vote_id="1", user_id="user_123", vote_value="up_vote")
                mock_cast_vote.return_value = mock_vote

                # act
                response, status_code = controller.create_vote()  # unpack the tuple

                # assert
                self.assertEqual(status_code, 201)  # check status code
                response_data = json.loads(
                    response.get_data(as_text=True)
                )  # get json data from response
                self.assertEqual(
                    response_data,
                    {
                        "vote_id": "1",
                        "user_id": "user_123",
                        "vote_value": "up_vote",
                    },  # this should match your mock
                )


if __name__ == "__main__":
    unittest.main()
