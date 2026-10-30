# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** one person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server. Name/color changes can wait until the rules work.

### Expected results

Results are from the **player’s perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

| Player | Computer | Expected return |
| --- | --- | --- |
| rock | rock | tie |
| rock | paper | lose |
| rock | scissors | win |
| paper | rock | win |
| paper | paper | tie |
| paper | scissors | lose |
| scissors | rock | lose |
| scissors | paper | win |
| scissors | scissors | tie |

### Agreed plan

Implement one independent round using the supplied interface and server; do not add scoring or saved history. `determine_winner(player, computer)` returns `win`, `lose`, or `tie` from the player's perspective. For example, Rock versus Paper is a player loss. Reject unsupported moves such as `lizard` with HTTP 400 and a helpful error. Verify all nine matchups, a real valid request and invalid request, and a real-browser round plus replay, fixing only the computer choice in request and browser tests.

### Checks

Before coding, agree this small test plan with AI:

| Level | Cases and evidence |
| --- | --- |
| Unit — positive | All nine literal expected results above, including valid losses and ties. |
| Integration — positive | A submitted round uses the real rule function and displays both choices and the correct result. Fix the computer choice for the test. |
| Integration — negative | Reuse supplied missing/unsupported-move tests: HTTP 400 and a helpful explanation, without calling the rules. A crash is not the intended result. |
| E2E — positive | Add a real-browser round and replay in tests/e2e/test_round.py using the supplied live_server/page fixtures. Fix only the computer choice; use real rules and real HTTP. |

Use `unit`, `integration`, and `e2e` pytest markers. Run `.venv/bin/python check.py` for Black, Pylint, fast tests, and browser checks; then review the diff. Keep shared settings and meaningful assertions intact. The student still plays, inspects a rule and its test, and gives feedback. Browser automation does not establish every aspect of usability or application performance.

### Work record

- Issue: https://github.com/zigzag1001/my-rps/issues/1
- Pull request / CI: add actual URLs when they exist.
- Implementation: [game.py](game.py), [tests/test_game.py](tests/test_game.py), and [tests/e2e/test_round.py](tests/e2e/test_round.py).
- Checks: `.venv/bin/python check.py` passed: Black, Pylint, 23 non-browser tests, and 6 Chromium tests. Browser observation: player chose scissors, computer chose paper, and the game displayed “You win!”; scissors beats paper.
