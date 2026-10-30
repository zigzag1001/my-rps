"""RPS-001 game rules. See SPEC.md."""


def determine_winner(player: str, computer: str) -> str:
    """Return 'win', 'lose', or 'tie' from the player's perspective.

    Inputs are lowercase 'rock', 'paper', or 'scissors' moves.
    """
    if player == computer:
        return "tie"

    winning_matchups = {
        ("rock", "scissors"),
        ("paper", "rock"),
        ("scissors", "paper"),
    }
    if (player, computer) in winning_matchups:
        return "win"

    return "lose"
