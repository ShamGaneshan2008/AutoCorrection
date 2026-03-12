# debug_test.py
# Run this to check what's broken: python debug_test.py

import os
print("=" * 40)
print("STEP 1 — Checking .env file")
print("=" * 40)
if os.path.exists(".env"):
    print("[OK] .env file found")
    with open(".env") as f:
        content = f.read().strip()
    if "GROQ_API_KEY" in content:
        print("[OK] GROQ_API_KEY found in .env")
    else:
        print("[FAIL] GROQ_API_KEY not found in .env")
        print("       Make sure your .env looks like:")
        print('       GROQ_API_KEY="gsk_yourkey"')
else:
    print("[FAIL] .env file NOT found in this folder")
    print("       Create a file named .env with:")
    print('       GROQ_API_KEY="gsk_yourkey"')

print()
print("=" * 40)
print("STEP 2 — Checking API key loads")
print("=" * 40)
try:
    from dotenv import load_dotenv
    load_dotenv()
    key = os.getenv("GROQ_API_KEY")
    if key:
        print(f"[OK] API key loaded: {key[:8]}...{key[-4:]}")
    else:
        print("[FAIL] API key is empty after loading .env")
except Exception as e:
    print(f"[FAIL] dotenv error: {e}")

print()
print("=" * 40)
print("STEP 3 — Testing Groq connection")
print("=" * 40)
try:
    from groq import Groq
    from dotenv import load_dotenv
    load_dotenv()
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": "Reply with just: OK"}]
    )
    print(f"[OK] Groq responded: {response.choices[0].message.content.strip()}")
except Exception as e:
    print(f"[FAIL] Groq error: {e}")

print()
print("=" * 40)
print("STEP 4 — Testing ghost text window")
print("=" * 40)
try:
    import tkinter as tk
    root = tk.Tk()
    root.withdraw()
    print("[OK] tkinter works")
    root.destroy()
except Exception as e:
    print(f"[FAIL] tkinter error: {e}")

try:
    import pyperclip
    pyperclip.copy("test")
    print("[OK] pyperclip works")
except Exception as e:
    print(f"[FAIL] pyperclip error: {e}")

print()
print("=" * 40)
print("STEP 5 — Testing keyboard listener")
print("=" * 40)
try:
    from pynput import keyboard
    print("[OK] pynput works")
except Exception as e:
    print(f"[FAIL] pynput error: {e}")

print()
print("=" * 40)
print("All checks done! Share the output above.")
print("=" * 40)