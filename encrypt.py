import pandas as pd
import numpy as np

encryption_table = pd.read_excel("encrypt_table.xlsx", header=None)

# Step 1: Define the key
key = 'FALCON'

# Step 2: Input the message
message = 'MEET ME AT PARK'

# Step 3: Remove spaces from the message
spaces = [i for i, ch in enumerate(message) if ch == " "]
cleaned_message = message.replace(" ", "")

# Step 4: Discretize the key and message
message_disc = list(cleaned_message)
key_disc = list(key)

# Step 5: Assign indexes to key and message letters
r = np.zeros(len(key_disc), dtype=int)
j = np.zeros(len(message_disc), dtype=int)
for index in range (1,encryption_table.shape[1]):
    for key_let in range (0,len(key_disc)):
        if encryption_table.iloc[1,index] == key_disc [key_let]:
            r [key_let] = index
    
    for mes_let in range(0,len(message_disc)):
        if encryption_table.iloc[1,index] == message_disc [mes_let]:
            j [mes_let] = index

# Step 6: Match each letter in the message with a letter in the key in the correct order
match = pd.DataFrame(columns=['row', 'col'])
for c in range(1,(len(message_disc)+1)):
    if c % len(key_disc) != 0:
        i = c % len(key_disc)

    else:
        i = len(key_disc)
    
    match.loc[c-1]=[r[i-1],j[c-1]]
    
# Step 7: Encrypt
encrypt_message_disc = []
for m, n in match.iterrows():
    row_index = n['row']
    col_index = n['col']
    encrypt_message_disc.append(encryption_table.iloc[row_index, col_index]) 
    
# Step 8: Add the spaces back to the message
for pos in spaces:
    encrypt_message_disc.insert(pos, " ")
    
encrypt_message = "".join(encrypt_message_disc)
print(encrypt_message)
