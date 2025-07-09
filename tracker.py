import json
import os
from datetime import datetime
from utils.summary import get_summary

DATA_FILE = "storage/sessions.json"

def load_sessions():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_sessions(sessions):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(sessions, f, indent=4)

def log_session():
    game = input("Enter game name: ").strip()
    duration = int(input("Duration (minutes): ").strip())
    kills = int(input("Kills: ").strip())
    deaths = int(input("Deaths: ").strip())
    notes = input("Notes: ").strip()

    session = {
        "game": game,
        "timestamp": datetime.now().isoformat(),
        "duration": duration,
        "kills": kills,
        "deaths": deaths,
        "notes": notes
    }

    sessions = load_sessions()
    sessions.append(session)
    save_sessions(sessions)

    print("✅ Session logged successfully!\n")

def list_sessions():
    sessions = load_sessions()
    if not sessions:
        print("No sessions logged yet.")
        return

    for i, s in enumerate(sessions, 1):
        print(f"{i}. {s['game']} - {s['duration']} mins - {s['timestamp']}")
        print(f"   Kills: {s['kills']} | Deaths: {s['deaths']}")
        print(f"   Notes: {s['notes']}\n")

def main():
    print("🎮 Welcome to AI Game Tracker")
    print("1. Log session")
    print("2. View session history")
    print("3. View 7-Day Summary")
    print("0. Exit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        log_session()
    elif choice == "2":
        list_sessions()
    elif choice == "3":
        game = input("Enter your game name: ")
        print(get_summary(game))
    elif choice == "0":
        print("Bye.")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    while True:
        main()
        break
