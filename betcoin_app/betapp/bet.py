import json
import os
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime

APP_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(APP_DIR, "betcoin_data.json")

DEFAULT_STARTING_BALANCE = 1000


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def load_data():
    if not os.path.exists(DATA_FILE):
        return {
            "players": {},
            "games": [],
            "transactions": []
        }

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        data.setdefault("players", {})
        data.setdefault("games", [])
        data.setdefault("transactions", [])
        return data
    except (json.JSONDecodeError, OSError):
        messagebox.showwarning(
            "Data file problem",
            "The local data file could not be read. A new one will be created."
        )
        return {"players": {}, "games": [], "transactions": []}


def save_data(data):
    temp_file = DATA_FILE + ".tmp"
    with open(temp_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    os.replace(temp_file, DATA_FILE)


class BetcoinApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Betcoin Prediction Pool")
        self.geometry("1050x720")
        self.minsize(900, 620)

        self.data = load_data()
        self.current_game_id = None

        self.configure(padx=12, pady=12)
        self.build_ui()
        self.refresh_all()

    # ---------- UI ----------
    def build_ui(self):
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure("Title.TLabel", font=("Segoe UI", 20, "bold"))
        style.configure("Heading.TLabel", font=("Segoe UI", 13, "bold"))
        style.configure("Big.TLabel", font=("Segoe UI", 18, "bold"))

        title = ttk.Label(self, text="Betcoin Prediction Pool", style="Title.TLabel")
        title.pack(anchor="w", pady=(0, 12))

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True)

        self.players_tab = ttk.Frame(notebook, padding=12)
        self.market_tab = ttk.Frame(notebook, padding=12)
        self.history_tab = ttk.Frame(notebook, padding=12)

        notebook.add(self.players_tab, text="Players")
        notebook.add(self.market_tab, text="Current Question")
        notebook.add(self.history_tab, text="History / Ledger")

        self.build_players_tab()
        self.build_market_tab()
        self.build_history_tab()

    def build_players_tab(self):
        top = ttk.Frame(self.players_tab)
        top.pack(fill="x")

        ttk.Button(top, text="Add Player", command=self.add_player).pack(side="left")
        ttk.Button(top, text="Remove Player", command=self.remove_player).pack(side="left", padx=8)
        ttk.Button(top, text="Reset Player Balance", command=self.reset_player).pack(side="left")

        columns = ("player", "balance", "net", "bets")
        self.player_tree = ttk.Treeview(
            self.players_tab, columns=columns, show="headings", height=16
        )
        headings = {
            "player": "Player",
            "balance": "Balance (BC)",
            "net": "Net Earnings (BC)",
            "bets": "Resolved Bets"
        }
        widths = {"player": 250, "balance": 150, "net": 180, "bets": 150}
        for col in columns:
            self.player_tree.heading(col, text=headings[col])
            self.player_tree.column(col, width=widths[col], anchor="center")
        self.player_tree.pack(fill="both", expand=True, pady=(12, 0))

        self.player_info = ttk.Label(
            self.players_tab,
            text="Betcoins are fictional, local-only points and have no cash value.",
            foreground="#555555"
        )
        self.player_info.pack(anchor="w", pady=(10, 0))

    def build_market_tab(self):
        header = ttk.Frame(self.market_tab)
        header.pack(fill="x")

        ttk.Button(header, text="New Question", command=self.new_question).pack(side="left")
        ttk.Button(header, text="Refresh", command=self.refresh_market).pack(side="left", padx=8)
        ttk.Button(header, text="Resolve Question", command=self.resolve_question).pack(side="left")

        self.question_label = ttk.Label(
            self.market_tab,
            text="No active question",
            style="Heading.TLabel",
            wraplength=900
        )
        self.question_label.pack(anchor="w", pady=(18, 8))

        pools = ttk.Frame(self.market_tab)
        pools.pack(fill="x", pady=8)

        self.yes_pool_label = ttk.Label(pools, text="YES pool: 0 BC", style="Big.TLabel")
        self.yes_pool_label.grid(row=0, column=0, padx=(0, 35), sticky="w")

        self.no_pool_label = ttk.Label(pools, text="NO pool: 0 BC", style="Big.TLabel")
        self.no_pool_label.grid(row=0, column=1, padx=(0, 35), sticky="w")

        self.total_pool_label = ttk.Label(pools, text="Total: 0 BC", style="Big.TLabel")
        self.total_pool_label.grid(row=0, column=2, sticky="w")

        odds = ttk.Frame(self.market_tab)
        odds.pack(fill="x", pady=(0, 14))

        self.yes_odds_label = ttk.Label(odds, text="YES odds: —")
        self.yes_odds_label.grid(row=0, column=0, padx=(0, 35), sticky="w")

        self.no_odds_label = ttk.Label(odds, text="NO odds: —")
        self.no_odds_label.grid(row=0, column=1, sticky="w")

        self.probability_label = ttk.Label(
            self.market_tab,
            text="Implied split: —",
            foreground="#555555"
        )
        self.probability_label.pack(anchor="w", pady=(0, 12))

        bet_frame = ttk.LabelFrame(self.market_tab, text="Place a Bet", padding=12)
        bet_frame.pack(fill="x")

        ttk.Label(bet_frame, text="Player").grid(row=0, column=0, padx=5, pady=5)
        self.bet_player = ttk.Combobox(bet_frame, state="readonly", width=24)
        self.bet_player.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(bet_frame, text="Side").grid(row=0, column=2, padx=5, pady=5)
        self.bet_side = ttk.Combobox(
            bet_frame, values=["YES", "NO"], state="readonly", width=10
        )
        self.bet_side.set("YES")
        self.bet_side.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(bet_frame, text="Betcoins").grid(row=0, column=4, padx=5, pady=5)
        self.bet_amount = ttk.Entry(bet_frame, width=14)
        self.bet_amount.grid(row=0, column=5, padx=5, pady=5)

        ttk.Button(bet_frame, text="Place Bet", command=self.place_bet).grid(
            row=0, column=6, padx=10, pady=5
        )

        self.current_bets_tree = ttk.Treeview(
            self.market_tab,
            columns=("player", "side", "amount", "time"),
            show="headings",
            height=11
        )
        for col, heading, width in [
            ("player", "Player", 220),
            ("side", "Side", 100),
            ("amount", "Amount (BC)", 140),
            ("time", "Placed", 220),
        ]:
            self.current_bets_tree.heading(col, text=heading)
            self.current_bets_tree.column(col, width=width, anchor="center")
        self.current_bets_tree.pack(fill="both", expand=True, pady=(14, 0))

    def build_history_tab(self):
        buttons = ttk.Frame(self.history_tab)
        buttons.pack(fill="x")

        ttk.Button(buttons, text="Refresh History", command=self.refresh_history).pack(side="left")
        ttk.Button(buttons, text="Open Data Folder", command=self.show_data_location).pack(
            side="left", padx=8
        )

        self.history_tree = ttk.Treeview(
            self.history_tab,
            columns=("time", "player", "question", "side", "amount", "result", "delta"),
            show="headings",
            height=22
        )

        for col, heading, width in [
            ("time", "Time", 150),
            ("player", "Player", 130),
            ("question", "Question", 300),
            ("side", "Side", 70),
            ("amount", "Bet (BC)", 100),
            ("result", "Result", 80),
            ("delta", "Net (BC)", 100),
        ]:
            self.history_tree.heading(col, text=heading)
            self.history_tree.column(col, width=width, anchor="center")
        self.history_tree.pack(fill="both", expand=True, pady=(12, 0))

    # ---------- Data helpers ----------
    def get_current_game(self):
        if self.current_game_id is None:
            return None
        for game in self.data["games"]:
            if game["id"] == self.current_game_id:
                return game
        return None

    def ensure_current_game(self):
        game = self.get_current_game()
        if not game:
            messagebox.showinfo("No question", "Create a new YES/NO question first.")
            return None
        if game["status"] != "open":
            messagebox.showinfo("Question closed", "This question has already been resolved.")
            return None
        return game

    def player_list(self):
        return sorted(self.data["players"].keys(), key=str.lower)

    def calculate_pools(self, game):
        yes_pool = sum(b["amount"] for b in game["bets"] if b["side"] == "YES")
        no_pool = sum(b["amount"] for b in game["bets"] if b["side"] == "NO")
        return yes_pool, no_pool

    # ---------- Player actions ----------
    def add_player(self):
        name = simpledialog.askstring("Add Player", "Player name:")
        if name is None:
            return
        name = name.strip()

        if not name:
            messagebox.showerror("Invalid name", "Enter a player name.")
            return
        if name in self.data["players"]:
            messagebox.showerror("Already exists", "That player already exists.")
            return

        self.data["players"][name] = {
            "balance": DEFAULT_STARTING_BALANCE,
            "starting_balance": DEFAULT_STARTING_BALANCE,
            "resolved_bets": 0,
            "created": now()
        }
        save_data(self.data)
        self.refresh_all()

    def remove_player(self):
        selected = self.player_tree.selection()
        if not selected:
            messagebox.showinfo("Select player", "Select a player first.")
            return

        name = self.player_tree.item(selected[0], "values")[0]

        open_bets = []
        for game in self.data["games"]:
            if game["status"] == "open":
                for bet in game["bets"]:
                    if bet["player"] == name:
                        open_bets.append(game["question"])

        if open_bets:
            messagebox.showerror(
                "Cannot remove player",
                "This player has an open bet. Resolve the question first."
            )
            return

        if not messagebox.askyesno(
            "Remove player",
            f"Remove {name}? Their historical transactions will remain."
        ):
            return

        del self.data["players"][name]
        save_data(self.data)
        self.refresh_all()

    def reset_player(self):
        selected = self.player_tree.selection()
        if not selected:
            messagebox.showinfo("Select player", "Select a player first.")
            return

        name = self.player_tree.item(selected[0], "values")[0]
        if not messagebox.askyesno(
            "Reset balance",
            f"Reset {name}'s balance to {DEFAULT_STARTING_BALANCE} BC?"
        ):
            return

        player = self.data["players"][name]
        player["balance"] = DEFAULT_STARTING_BALANCE
        player["starting_balance"] = DEFAULT_STARTING_BALANCE
        player["resolved_bets"] = 0

        # Record a reset event without changing the historical bet ledger.
        self.data["transactions"].append({
            "time": now(),
            "type": "RESET",
            "player": name,
            "question": "Balance reset",
            "side": "",
            "amount": 0,
            "result": "",
            "net": 0
        })

        save_data(self.data)
        self.refresh_all()

    # ---------- Question / bet actions ----------
    def new_question(self):
        # Don't allow a second open question at the same time.
        open_game = next(
            (g for g in self.data["games"] if g["status"] == "open"),
            None
        )
        if open_game:
            messagebox.showerror(
                "Question already open",
                "Resolve the current question before creating another."
            )
            self.current_game_id = open_game["id"]
            self.refresh_market()
            return

        question = simpledialog.askstring(
            "New Question",
            "Enter a YES/NO question:\n\nExample: Will Team A win?"
        )
        if question is None:
            return

        question = question.strip()
        if not question:
            messagebox.showerror("Invalid question", "Enter a question.")
            return

        game_id = str(len(self.data["games"]) + 1)
        existing_ids = {g["id"] for g in self.data["games"]}
        while game_id in existing_ids:
            game_id = str(int(game_id) + 1)

        game = {
            "id": game_id,
            "question": question,
            "created": now(),
            "status": "open",
            "result": None,
            "bets": []
        }

        self.data["games"].append(game)
        self.current_game_id = game_id
        save_data(self.data)
        self.refresh_all()

    def place_bet(self):
        game = self.ensure_current_game()
        if not game:
            return

        player = self.bet_player.get().strip()
        side = self.bet_side.get().strip().upper()

        if not player:
            messagebox.showerror("Missing player", "Choose a player.")
            return
        if side not in ("YES", "NO"):
            messagebox.showerror("Missing side", "Choose YES or NO.")
            return

        try:
            amount = int(self.bet_amount.get().strip())
        except ValueError:
            messagebox.showerror("Invalid amount", "Enter a whole number of Betcoins.")
            return

        if amount <= 0:
            messagebox.showerror("Invalid amount", "Betcoins must be greater than 0.")
            return

        balance = self.data["players"][player]["balance"]
        if amount > balance:
            messagebox.showerror(
                "Not enough Betcoins",
                f"{player} has only {balance} BC."
            )
            return

        self.data["players"][player]["balance"] -= amount

        game["bets"].append({
            "player": player,
            "side": side,
            "amount": amount,
            "time": now()
        })

        self.data["transactions"].append({
            "time": now(),
            "type": "BET",
            "player": player,
            "question": game["question"],
            "side": side,
            "amount": amount,
            "result": "OPEN",
            "net": -amount
        })

        self.bet_amount.delete(0, tk.END)

        save_data(self.data)
        self.refresh_all()

    def resolve_question(self):
        game = self.ensure_current_game()
        if not game:
            return

        if not game["bets"]:
            messagebox.showerror("No bets", "There are no bets to resolve.")
            return

        result = simpledialog.askstring(
            "Resolve Question",
            f"Question:\n{game['question']}\n\nEnter YES or NO:"
        )
        if result is None:
            return

        result = result.strip().upper()
        if result not in ("YES", "NO"):
            messagebox.showerror("Invalid result", "Enter YES or NO.")
            return

        yes_pool, no_pool = self.calculate_pools(game)
        winning_pool = yes_pool if result == "YES" else no_pool
        total_pool = yes_pool + no_pool

        if winning_pool == 0:
            messagebox.showerror(
                "Cannot resolve",
                "The winning side has no pool, so there is nothing to distribute."
            )
            return

        # Parimutuel-style fictional points:
        # winners split the full pool according to their share of the winning pool.
        resolved = []

        for bet in game["bets"]:
            player = self.data["players"][bet["player"]]

            if bet["side"] == result:
                payout = int(round(total_pool * bet["amount"] / winning_pool))
                net = payout - bet["amount"]
                player["balance"] += payout
                player["resolved_bets"] += 1
            else:
                payout = 0
                net = -bet["amount"]
                player["resolved_bets"] += 1

            # Replace the BET transaction's OPEN result with a RESOLVED transaction.
            self.data["transactions"].append({
                "time": now(),
                "type": "RESOLVE",
                "player": bet["player"],
                "question": game["question"],
                "side": bet["side"],
                "amount": bet["amount"],
                "result": result,
                "net": net
            })

            resolved.append(
                f"{bet['player']}: {payout} BC returned (net {net:+d} BC)"
            )

        game["status"] = "resolved"
        game["result"] = result
        game["resolved"] = now()

        save_data(self.data)
        self.refresh_all()

        messagebox.showinfo(
            "Question resolved",
            "Result: " + result + "\n\n" + "\n".join(resolved)
        )

    # ---------- Refresh ----------
    def refresh_all(self):
        self.refresh_players()
        self.refresh_market()
        self.refresh_history()

    def refresh_players(self):
        for item in self.player_tree.get_children():
            self.player_tree.delete(item)

        for name in self.player_list():
            p = self.data["players"][name]
            net = p["balance"] - p.get("starting_balance", DEFAULT_STARTING_BALANCE)
            self.player_tree.insert(
                "",
                "end",
                values=(name, p["balance"], f"{net:+d}", p.get("resolved_bets", 0))
            )

        values = self.player_list()
        self.bet_player["values"] = values
        if values and self.bet_player.get() not in values:
            self.bet_player.current(0)

    def refresh_market(self):
        open_game = next(
            (g for g in reversed(self.data["games"]) if g["status"] == "open"),
            None
        )

        if open_game:
            self.current_game_id = open_game["id"]

        game = self.get_current_game()
        if not game:
            self.question_label.config(text="No active question")
            self.yes_pool_label.config(text="YES pool: 0 BC")
            self.no_pool_label.config(text="NO pool: 0 BC")
            self.total_pool_label.config(text="Total: 0 BC")
            self.yes_odds_label.config(text="YES odds: —")
            self.no_odds_label.config(text="NO odds: —")
            self.probability_label.config(text="Implied split: —")
            for item in self.current_bets_tree.get_children():
                self.current_bets_tree.delete(item)
            return

        self.question_label.config(
            text=f"Question #{game['id']}: {game['question']}"
        )

        yes_pool, no_pool = self.calculate_pools(game)
        total = yes_pool + no_pool

        self.yes_pool_label.config(text=f"YES pool: {yes_pool:,} BC")
        self.no_pool_label.config(text=f"NO pool: {no_pool:,} BC")
        self.total_pool_label.config(text=f"Total: {total:,} BC")

        if yes_pool > 0 and total > 0:
            yes_probability = yes_pool / total
            yes_odds = total / yes_pool
            self.yes_odds_label.config(text=f"YES odds: {yes_odds:.2f}x")
            yes_pct = yes_probability * 100
        else:
            self.yes_odds_label.config(text="YES odds: —")
            yes_pct = 0

        if no_pool > 0 and total > 0:
            no_probability = no_pool / total
            no_odds = total / no_pool
            self.no_odds_label.config(text=f"NO odds: {no_odds:.2f}x")
            no_pct = no_probability * 100
        else:
            self.no_odds_label.config(text="NO odds: —")
            no_pct = 0

        self.probability_label.config(
            text=f"Implied split: YES {yes_pct:.1f}%  |  NO {no_pct:.1f}%"
        )

        for item in self.current_bets_tree.get_children():
            self.current_bets_tree.delete(item)

        for bet in game["bets"]:
            self.current_bets_tree.insert(
                "",
                "end",
                values=(bet["player"], bet["side"], bet["amount"], bet["time"])
            )

    def refresh_history(self):
        for item in self.history_tree.get_children():
            self.history_tree.delete(item)

        for tx in reversed(self.data["transactions"]):
            self.history_tree.insert(
                "",
                "end",
                values=(
                    tx.get("time", ""),
                    tx.get("player", ""),
                    tx.get("question", ""),
                    tx.get("side", ""),
                    tx.get("amount", ""),
                    tx.get("result", ""),
                    f"{tx.get('net', 0):+d}"
                )
            )

    def show_data_location(self):
        messagebox.showinfo(
            "Local data file",
            f"Your Betcoin ledger is stored here:\n\n{DATA_FILE}\n\n"
            "This file contains players, questions, bets and transaction history."
        )


if __name__ == "__main__":
    app = BetcoinApp()
    app.mainloop()
