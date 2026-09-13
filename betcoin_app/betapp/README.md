# Betcoin Prediction Pool

A local-only Python/Tkinter fictional-points prediction pool.

## Requirements
- Python 3.9+ recommended
- No third-party packages required

## Run in VS Code
1. Open this folder in VS Code.
2. Open `betcoin_app.py`.
3. Run:
   python betcoin_app.py

## Data
The app automatically creates `betcoin_data.json` in the same folder.
That file stores:
- players and balances
- all questions
- all bets
- resolution results
- transaction history

Betcoins are fictional, non-redeemable points with no cash value.

## How the odds work
For an open question:

odds = total pool / side pool

Example:
YES = 600 BC
NO = 400 BC
Total = 1000 BC

YES = 1.67x
NO = 2.50x

When resolved, winners split the total pool in proportion to their winning bet.
