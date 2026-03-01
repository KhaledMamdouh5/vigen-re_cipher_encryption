# Vigenère Cipher Implementation in Python

A Python-based cryptographic tool for encrypting and decrypting messages using the **Vigenère Cipher** algorithm. This implementation maintains the original message's space structure and uses an external Excel-based transformation table for character mapping.



## 🛠️ Project Features
* **Space Preservation**: Records space indices before processing and re-injects them into the final output to maintain readability.
* **Excel Integration**: Utilizes `pandas` to read the substitution matrix from `encrypt_table.xlsx`.
* **Modular Scripts**: Dedicated files for encryption and decryption workflows.
* **NumPy Support**: Uses vectorized arrays for efficient index mapping.

## 📂 File Structure
* `encrypt.py`: Logic for converting plaintext to ciphertext using a keyword.
* `decrypt.py`: Logic for reverting ciphertext to plaintext using a keyword.
* `encrypt_table.xlsx`: The 26x26 character reference grid (Required for execution).


## ⚙️ How It Works
The algorithm follows a specific 8-step process for both encryption and decryption:

1. Key Definition: A keyword (e.g., FALCON) is defined to determine the shifts.

2. Message Input: The user provides the target string (e.g., MEET ME AT PARK).

3. Space Preservation: The script records the indices of spaces, removes them for calculation, and re-inserts them at the end.

4. Discretization: Both the key and message are broken into individual characters.

5. Index Mapping: The code maps characters to their corresponding coordinates in the encrypt_table.xlsx.

6. Key Wrapping: The key is repeated to match the length of the message (e.g., TUNISTUNISTUNIS).

7. Table Transformation:

    - Encryption: Finds the intersection of the key row and message column.

    - Decryption: Searches the key row to find the ciphertext letter and identifies the corresponding header column.

8. Reconstruction: Spaces are added back, and the list of characters is joined into a string.
