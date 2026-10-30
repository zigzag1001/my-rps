"""Real-browser coverage for an RPS-001 round and replay."""

import pytest
from playwright.sync_api import Page, expect

import app as web

pytestmark = pytest.mark.e2e


def test_real_round_and_replay(page: Page, live_server, monkeypatch):
    """Play two rounds through the real app and rules."""
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")
    page.goto(live_server)

    page.get_by_role("button", name="Rock", exact=True).click()
    choices = page.get_by_label("This round’s choices")
    expect(choices).to_contain_text("Rock")
    expect(choices).to_contain_text("Paper")
    expect(page.locator('[data-outcome="lose"]')).to_be_visible()
    expect(page.get_by_role("heading", name="Computer wins")).to_be_visible()

    page.get_by_role("button", name="Scissors", exact=True).click()
    expect(choices).to_contain_text("Scissors")
    expect(choices).to_contain_text("Paper")
    expect(page.locator('[data-outcome="win"]')).to_be_visible()
    expect(page.get_by_role("heading", name="You win!")).to_be_visible()
