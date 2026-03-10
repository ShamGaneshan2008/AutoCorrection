# 🤖 AI Autocorrect — Windows
### System-wide spell, caps, grammar & space correction — powered by Groq AI

Works in **every app on Windows** — Chrome, Word, Notepad, VS Code, Discord, anything.  
Runs silently in the background. No setup per-app needed.

---

## ✨ Features

| Feature | How it triggers | What it fixes |
|---|---|---|
| **Spell Correction** | Spacebar | `recieve` → `receive`, `teh` → `the` |
| **Caps Fix** | Spacebar | `hELLO` → `Hello`, `wOrLd` → `world`, `HELLO` → `hello` |
| **Space Fixer** | Auto (0.9s pause) + Tab | `he llo` → `hello`, `wor ld` → `world` |
| **Grammar Fix** | Tab key | `i has went` → `I have gone`, subject-verb, tense, punctuation |
| **Change Popup** | After grammar fix | Shows before → after in bottom-right corner |

---

## 📁 Files

```
ai_autocorrect.py     ← main Python script (run this)
autocorrect_ui.html   ← control panel UI (open in browser)
README.md             ← this file
```

---

## ⚡ Quick Start

### 1. Install Python
Download from https://python.org  
> ⚠️ During install, tick **"Add Python to PATH"**

### 2. Install dependencies
Open **Command Prompt** and run:
```bash
pip install pynput pyperclip groq pystray pillow
```

### 3. Get your Groq API key (Free!)
1. Go to **https://console.groq.com** and sign up
2. Navigate to **API Keys** → click **Create API Key**
3. Copy the key
4. Open `ai_autocorrect.py` in any text editor
5. Find line 34 and paste your key:
```python
GROQ_API_KEY = "gsk_your_actual_key_here"
```

### 4. Run it
```bash
python ai_autocorrect.py
```
An **orange "Ac" icon** appears in your system tray (bottom-right of taskbar).  
When grammar mode is ON, the icon turns **green**.

---

## 🎮 How to Use

| You do this | App does this |
|---|---|
| Type normally | Nothing changes, works as usual |
| Press `Space` | Last word is spell-checked + caps fixed instantly |
| Stop typing for 0.9s | Adjacent fragments checked for unwanted spaces |
| Press `Tab` | Entire sentence fixed (spaces + grammar) |
| `Ctrl+Z` | Undo any correction |

### Example workflow writing a formal email:
```
You type:   i has went to teh STORE yesteday
→ Space fixes as you go:  I → I, teh → the, STORE → store, yesteday → yesterday
→ Press Tab: "I have gone to the store yesterday"
→ Popup shows what changed
```

---

## 🖥️ Control Panel UI

Open `autocorrect_ui.html` in your browser for a visual dashboard:

- Toggle each feature on/off (Spell, Caps, Grammar, Space Fixer, Popup)
- Adjust timing with sliders (space-check delay, popup duration)
- Live demo box — test corrections right in the browser
- Session stats — see how many fixes were made
- Save your Groq API key

> The UI is a visual companion. To fully connect it to the Python script, wire it via a local Flask server (optional advanced setup).

---

## ⚙️ Configuration

All settings are at the top of `ai_autocorrect.py`:

```python
GROQ_API_KEY      = "YOUR_GROQ_API_KEY_HERE"  # your Groq key
GROQ_MODEL        = "llama3-8b-8192"          # AI model to use
POPUP_DURATION    = 4000                       # popup visible time (ms)
SPACE_CHECK_DELAY = 0.9                        # seconds before auto space-fix
```

### Available Groq Models

| Model | Speed | Quality |
|---|---|---|
| `llama3-8b-8192` | ⚡ Fastest | Good — recommended default |
| `llama3-70b-8192` | 🔶 Medium | Best accuracy |
| `mixtral-8x7b-32768` | 🔶 Medium | Great balance |
| `gemma2-9b-it` | ⚡ Fast | Google's model |

---

## 🔧 System Tray Menu

Right-click the **"Ac"** icon in the taskbar:

| Option | What it does |
|---|---|
| **Pause / Resume** | Stops or starts all corrections |
| **Toggle Grammar (Tab)** | Turns grammar mode ON 🟢 / OFF 🔴 |
| **Quit** | Exits the app completely |

---

## 🚀 Run on Windows Startup (Optional)

1. Press `Win + R`, type `shell:startup`, press **Enter**
2. Create a shortcut to `ai_autocorrect.py` in that folder
3. The app will now launch automatically when Windows starts

---

## 🛠️ Troubleshooting

| Problem | Fix |
|---|---|
| Nothing happens | Check your Groq API key is set correctly |
| Bad correction | Press `Ctrl+Z` to undo immediately |
| App freezes | Restart the script; check your internet connection |
| Tab not working | Make sure grammar mode is ON (green icon in tray) |
| Acronyms getting lowercased | Words ≤4 all-caps are protected (NASA, HTML, etc.) |

---

## 📦 Dependencies

```
pynput      — global keyboard listener
pyperclip   — clipboard save/restore
groq        — Groq AI API client
pystray     — system tray icon
pillow      — tray icon image rendering
tkinter     — correction popup (built into Python)
```

---

## 💡 Tips

- Use `llama3-70b-8192` for more accurate grammar on long formal letters
- Keep `SPACE_CHECK_DELAY` above `0.5s` or it may interfere with fast typing
- The app only corrects — it never reads or stores what you type
- Press `Tab` only at the **end of a sentence**, not mid-sentence

---

*Built with Python · Groq AI · pynput · runs on Windows 10/11*
