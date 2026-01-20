# 🕵️‍♂️ Secret Code Language (Encoder-Decoder)

A Python-based CLI tool that converts normal text into a "Secret Language" using a custom encryption algorithm. This project demonstrates proficiency in **String Manipulation**, **Conditional Logic**, and **List Comprehensions** in Python.

## 🚀 How It Works (The Logic)

This tool applies specific rules to encrypt and decrypt messages, ensuring secure communication between users who know the logic.

### 🔒 Encoding Rules:
1.  **Short Words (Length < 3):** The word is simply **reversed**.
    * *Example:* `is` -> `si`
2.  **Long Words (Length ≥ 3):**
    * The **first letter** is moved to the **end**.
    * **Random characters** are appended at the start and end to obfuscate the text.
    * *Example:* `Amit` -> `mitA` -> `(random)mitA(random)`

### 🔓 Decoding Rules:
The tool reverses the encryption process:
1.  **Short Words:** Reversed back to original.
2.  **Long Words:** The random characters (7 from start, 7 from end) are removed, and the last character is moved back to the front.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Concepts Used:** String Slicing, Control Flow (If-Else), Loops, Lists.

## 💻 How to Run
1.  Clone this repository:
    ```bash
    git clone [https://github.com/MyStIc-mY/Secret-Code-Language.git](https://github.com/MyStIc-mY/Secret-Code-Language.git)
    ```
2.  Run the script:
    ```bash
    python main.py
    ```
3.  Follow the on-screen prompts to Encode or Decode a message.

## 📝 Example Usage

```text
Enter your message: hello world
Do you want to encode (yes/no): yes

Encoded Message: adcncnjellohjnrjrfn adcncnjorldwjnrjrfn
