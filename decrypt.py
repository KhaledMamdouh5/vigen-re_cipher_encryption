import pandas as pd
import numpy as np

encryption_table = pd.read_excel("encrypt_table.xlsx", header=None)

# Step 1: Define the key
key = 'FALCON'

# Step 2: Input the encrypted message
encrypted_message = 'FYRB EX UG XSKE'

# Step 3: Remove spaces from the encrypted message
spaces = [i for i, ch in enumerate(encrypted_message) if ch == " "]
cleaned_encrypted_message = encrypted_message.replace(" ", "")

# Step 4: Discretize the key and encrypted message
encrypted_message_disc = list(cleaned_encrypted_message)
key_disc = list(key)

# Step 5: Assign indexes to key letters
r = np.zeros(len(key_disc), dtype=int)
for index in range (1,encryption_table.shape[1]):
    for key_let in range (0,len(key_disc)):
        if encryption_table.iloc[1,index] == key_disc [key_let]:
            r [key_let] = index

# Step 6: Match each letter in the encrypted message with a letter in the key in the correct order
match = np.zeros(len(encrypted_message_disc), dtype=int)
for c in range(1,(len(encrypted_message_disc)+1)):
    if c % len(key_disc) != 0:
        i = c % len(key_disc)

    else:
        i = len(key_disc)
    
    match [c-1] = r[i-1]
    
# Step 7: Decrypt
message_disc = []
for m in range(0,(len(encrypted_message_disc))):
    for j in range (1,encryption_table.shape[1]):
        if encryption_table.iloc[match[m],j] == encrypted_message_disc[m]:
            message_disc.append(encryption_table.iloc[0,j])

# Step 8: Add the spaces back to the message
for pos in spaces:
    message_disc.insert(pos, " ")
    
message = "".join(message_disc)
print(message)
