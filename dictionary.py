# These are the custom words that prevents the Ai from treating it.
CUSTOM_WORDS = {
    "sham",
    "pytorch",
    "tensorflow",
    "ollama",
    "numpy",
    "pandas"
}

# The value "word" comes from keyboard_listener.py
def is_custom(word):
    return word.lower() in CUSTOM_WORDS