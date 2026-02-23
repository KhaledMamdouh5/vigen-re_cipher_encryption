Here is a clean, professional README.md file designed for direct use on GitHub.

Vigenère Cipher Implementation in Python
This repository contains a Python implementation of the Vigenère Cipher, a polyalphabetic substitution method. It uses a keyword and a 2D encryption table (Tabula Recta) to encrypt and decrypt messages while preserving the original space structure.

📁 Project Structure
encrypt.py: Script to convert plain text into encrypted ciphertext.

decrypt.py: Script to convert ciphertext back into the original plain text.

encrypt_table.xlsx: An Excel spreadsheet containing the 26x26 character substitution grid (required for the code to run).

⚙️ How It Works
The algorithm follows a specific 8-step process for both encryption and decryption:

Key Definition: A keyword (e.g., TUNIS) is defined to determine the shifts.

Message Input: The user provides the target string (e.g., MEET ME AT PARK).

Space Preservation: The script records the indices of spaces, removes them for calculation, and re-inserts them at the end.

Discretization: Both the key and message are broken into individual characters.

Index Mapping: The code maps characters to their corresponding coordinates in the encrypt_table.xlsx.

Key Wrapping: The key is repeated to match the length of the message (e.g., TUNISTUNISTUNIS).

Table Transformation:

Encryption: Finds the intersection of the key row and message column.

Decryption: Searches the key row to find the ciphertext letter and identifies the corresponding header column.

Reconstruction: Spaces are added back, and the list of characters is joined into a string.
