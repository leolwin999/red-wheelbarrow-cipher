# 🎡 red-wheelbarrow-cipher

> *"So much depends upon a red wheelbarrow..."*

A fun little Python CLI tool inspired by that iconic Season 2 scene in **Mr. Robot** (`eps2.9_pyth0n-pt1.p7z`) where Mr. Robot decodes Tyrell Wellick's encrypted message using **ROT13** + **A1Z26** (letter-to-number substitution).

**Note**: Built with assistance from Google Gemini to enhance the tool's functionality and give the code a cleaner, cooler structure.

---

## 🛠️ How It Works

The cipher runs a classic two-step transformation with a couple of custom tweaks so your messages don't get mangled:

1. **Encryption (`Plaintext -> Ciphertext`)**
   - Runs **ROT13** on your text first.
   - Converts each letter to its **A1Z26** alphabet position (`1–26`), tagging uppercase with `U` and lowercase with `L` (e.g., `B -> O -> U15`).
   - Wraps actual numbers in brackets (like `[6]`) so they don't get confused with letter codes during decryption.
2. **Decryption (`Ciphertext -> Plaintext`)**
   - Maps `U`/`L` number tokens back to their exact uppercase or lowercase letters, unwraps bracketed digits, and runs **ROT13** again to bring back your original message.

---

## 🚀 Getting Started

No external libraries or `pip install` needed, just standard Python 3.

1. **Clone the repo:**
   ```bash
   git clone https://github.com/leolwin999/red-wheelbarrow-cipher.git
   cd red-wheelbarrow-cipher
   ```

2. **Run the script:**
   ```bash
   python red-wheelbarrow-cipher.py
   ```

---

## 💻 Example Output

When you boot it up, it runs a quick demo before dropping you into an interactive `fsociety` prompt:

```text
=======================================================
  RED WHEELBARROW CIPHER UTILITY (ROT13+A1Z26)
=======================================================

[DEMO] Original Message : Bonsoir Elliot 6
[DEMO] Encrypted Output : U15-L2-L1-L6-L2-L22-L5 U18-L25-L25-L22-L2-L7 [6]
[DEMO] Decrypted Output : Bonsoir Elliot 6
-------------------------------------------------------

Select an operation:
  [1] Encrypt (Plaintext -> ROT13 -> Numbers)
  [2] Decrypt (Numbers -> Letters -> ROT13)
  [3] Exit

fsociety@mrrobot:~$
```

---

## ⚠️ Disclaimer

Obviously, don't use ROT13 + A1Z26 to hide real secrets from prying eyes. This is purely for fun and nostalgia. 
