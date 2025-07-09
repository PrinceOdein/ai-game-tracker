# 🎮 AI Game Tracker (MVP)

**AI Game Tracker** is a simple Python-based CLI tool to log your gaming sessions, track performance (like K/D ratios), and generate intelligent summaries over time. 

It’s built to help gamers analyze their play habits and self-improve — perfect for FPS grinders, RPG explorers, and competitive warriors alike.

---

## 🚀 Features

- 📜 Log gameplay sessions: game name, duration, kills, deaths, notes
- 🕒 Track session history with timestamps
- 📊 Generate 7-day summaries per game
- ⚖️ Calculates your K/D ratio over time
- 💬 Personalized motivational feedback
- 🧱 Ready for future G-Assist plug-in integration

---

## 🛠️ Tech Stack

- Python 3.x
- JSON (for local session storage)
- CLI-based interface

---

## 📦 Installation

```bash
git clone https://github.com/PrinceOdein/ai-game-tracker.git
cd ai-game-tracker
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the main script:

```bash
python tracker.py
```

From there, you'll be guided to:
- Log new game sessions
- View session history
- View 7-day summary for any game

---

## 📁 Project Structure

```
ai-game-tracker/
├── tracker.py              # CLI entry point
├── storage/
│   └── sessions.json       # Local data store
├── utils/
│   └── summary.py          # Game summary logic
├── README.md
└── requirements.txt
```

---

## 🧠 Future Plans

- Discord webhook to share stats
- Voice-command interface simulation
- Visualization (KD chart, session heatmap)
- OpenAI summary generator
- Full NVIDIA G-Assist plug-in conversion (RTX)

---

## 🤝 Contributing

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/foo`)
3. Commit your changes (`git commit -m 'Add some foo'`)
4. Push to the branch (`git push origin feature/foo`)
5. Open a Pull Request

---

## 📝 License

MIT License

---

## 🙏 Credits

Built by [Anyanwu Jedidiah Tamunodein](https://github.com/princeodein)  
Inspired by the spirit of self-improvement, gamedev, and AI productivity.

---

> "In every session, a gamer evolves."
