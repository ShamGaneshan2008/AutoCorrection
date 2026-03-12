# ghost_text.py

import tkinter as tk
import threading
import pyperclip
import time
from pynput import keyboard as kb
from pynput.keyboard import Key, Controller

_controller = Controller()

GHOST_BG    = "#1e1e2e"
GHOST_FG    = "#6c7086"
GHOST_HINT  = "#a6adc8"
GHOST_FONT  = ("Segoe UI", 11)
HINT_FONT   = ("Segoe UI", 9)

# Module state — one ghost at a time
_ghost_root        = None
_ghost_lock        = threading.Lock()
_current_original  = ""
_current_suggestion = ""
_is_showing        = False   # True while a ghost window is alive


def _get_cursor_pos():
    try:
        import ctypes
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]
        pt = POINT()
        ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
        return pt.x + 12, pt.y + 24
    except Exception:
        return 800, 500


def _destroy_ghost():
    """Destroy ghost window safely from any thread."""
    global _ghost_root, _is_showing
    with _ghost_lock:
        if _ghost_root is not None:
            try:
                _ghost_root.after(0, _ghost_root.destroy)
            except Exception:
                pass
            _ghost_root = None
        _is_showing = False


def _accept_suggestion(original: str, suggestion: str):
    """Erase original text and type the suggestion."""
    _destroy_ghost()
    time.sleep(0.08)

    old_clip = ""
    try:
        old_clip = pyperclip.paste()
    except Exception:
        pass

    # Erase original
    for _ in range(len(original)):
        _controller.press(Key.backspace)
        _controller.release(Key.backspace)
        time.sleep(0.007)

    # Type correction
    _controller.type(suggestion)

    try:
        pyperclip.copy(old_clip)
    except Exception:
        pass

    print(f"[ghost] accepted: '{original}' -> '{suggestion}'")


def show_ghost(original: str, suggestion: str):
    """Show grey ghost text popup near cursor. Safe to call repeatedly."""
    global _ghost_root, _current_original, _current_suggestion, _is_showing

    if not suggestion or suggestion.strip() == original.strip():
        return

    # Always destroy previous ghost before showing new one
    _destroy_ghost()
    time.sleep(0.05)   # small gap so old window is fully gone

    _current_original   = original
    _current_suggestion = suggestion

    def _run():
        global _ghost_root, _is_showing

        x, y = _get_cursor_pos()

        root = tk.Tk()
        root.overrideredirect(True)
        root.attributes("-topmost", True)
        root.attributes("-alpha", 0.93)
        root.configure(bg=GHOST_BG)

        outer = tk.Frame(root, bg=GHOST_BG, padx=12, pady=8)
        outer.pack()

        tk.Label(
            outer,
            text=suggestion,
            fg=GHOST_FG,
            bg=GHOST_BG,
            font=GHOST_FONT,
            anchor="w",
        ).pack(anchor="w")

        tk.Label(
            outer,
            text="Tab to accept  ·  Esc to dismiss",
            fg=GHOST_HINT,
            bg=GHOST_BG,
            font=HINT_FONT,
            anchor="w",
        ).pack(anchor="w", pady=(3, 0))

        # Left accent border
        tk.Frame(root, bg="#45475a", width=3).place(x=0, y=0, relheight=1)

        root.update_idletasks()
        w = root.winfo_reqwidth()
        h = root.winfo_reqheight()
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        if x + w > sw - 20: x = sw - w - 20
        if y + h > sh - 60: y = y - h - 30
        root.geometry(f"{w}x{h}+{x}+{y}")

        with _ghost_lock:
            _ghost_root = root
            _is_showing = True

        root.after(6000, _destroy_ghost)  # auto dismiss after 6s
        root.mainloop()

        # mainloop exited — clean up
        with _ghost_lock:
            _ghost_root = None
            _is_showing = False

    threading.Thread(target=_run, daemon=True).start()


def dismiss_ghost():
    _destroy_ghost()


def handle_key_for_ghost(key) -> bool:
    """
    Returns True if the key was consumed by ghost (Tab = accept, Esc = dismiss).
    Returns False if ghost isn't showing or key should pass through normally.
    """
    global _current_original, _current_suggestion

    if not _is_showing:
        return False

    if key == Key.tab:
        original   = _current_original
        suggestion = _current_suggestion
        threading.Thread(
            target=_accept_suggestion,
            args=(original, suggestion),
            daemon=True
        ).start()
        return True

    elif key == Key.esc:
        dismiss_ghost()
        return True

    else:
        # Any other key — dismiss ghost, let key pass through
        dismiss_ghost()
        return False