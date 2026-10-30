"""RPS-001 rule and request checks."""

# pytest injects fixtures by their function names; test names document behavior.
# pylint: disable=redefined-outer-name,missing-function-docstring

import pytest

import app as web
import game


@pytest.fixture
def client():
    web.app.config.update(TESTING=True)
    return web.app.test_client()


@pytest.mark.unit
@pytest.mark.parametrize(
    ("player", "computer", "expected"),
    [
        ("rock", "rock", "tie"),
        ("rock", "paper", "lose"),
        ("rock", "scissors", "win"),
        ("paper", "rock", "win"),
        ("paper", "paper", "tie"),
        ("paper", "scissors", "lose"),
        ("scissors", "rock", "lose"),
        ("scissors", "paper", "win"),
        ("scissors", "scissors", "tie"),
    ],
)
def test_determine_winner_matches_all_nine_outcomes(player, computer, expected):
    assert game.determine_winner(player, computer) == expected


@pytest.mark.integration
def test_valid_round_uses_real_rules_and_displays_result(client, monkeypatch):
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")

    response = client.post("/", data={"move": "rock"})
    page = response.get_data(as_text=True)

    assert response.status_code == 200
    assert 'data-outcome="lose"' in page
    assert "Computer wins" in page
    assert "You chose" in page and "Computer chose" in page
    assert "Rock" in page and "Paper" in page
