import json
from datetime import datetime, timedelta
from collections import defaultdict

DATA_FILE = "storage/sessions.json"

def load_sessions():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def filter_by_game(sessions, game):
    return [s for s in sessions if s['game'].lower() == game.lower()]

def filter_by_days(sessions, days):
    cutoff = datetime.now() - timedelta(days=days)
    return [
        s for s in sessions 
        if datetime.fromisoformat(s['timestamp']) >= cutoff
    ]

def get_summary(game_name="Apex Legends", days=7):
    sessions = load_sessions()
    game_sessions = filter_by_game(sessions, game_name)
    recent_sessions = filter_by_days(game_sessions, days)

    if not recent_sessions:
        return f"No data for {game_name} in the past {days} days."

    total_duration = sum(s["duration"] for s in recent_sessions)
    total_kills = sum(s["kills"] for s in recent_sessions)
    total_deaths = sum(s["deaths"] for s in recent_sessions)
    kd_ratio = round(total_kills / total_deaths, 2) if total_deaths > 0 else total_kills

    response = f"""
🎮 Game: {game_name}
📅 Days Tracked: {days}
🕒 Total Time Played: {total_duration} minutes
🔫 Total Kills: {total_kills}
💀 Total Deaths: {total_deaths}
📊 K/D Ratio: {kd_ratio}
💬 Insight: {"You're improving!" if kd_ratio > 1 else "Keep grinding, you got this!"}
"""

    return response
