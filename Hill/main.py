import numpy as np

from Hill import matrix
import break_key
import Hill

plain_text = "XY[LER5HI;:LMOPQR81911SBJ"
chiper = "[WQ:9B0A81911CUQ<ANY1IMTD"

plain_matrix = matrix.text_to_number(plain_text, Hill.dict, 5)
chiper_matrix = matrix.text_to_number(chiper, Hill.dict, 5)

key = break_key.get_key(plain_matrix, chiper_matrix)
chip = np.dot(key, plain_matrix) % 41
decrip = Hill.reverse_key(key)
print(decrip)
str = "A8VS3,XRDEO,N6JEV,XGJID,13C07,L4C1R,4Q965,XWRA5,DQGYW,TNHYO,4ND8Z"
li = str.split(",")
for i in li:
    Hill.decrypt(i, decrip)
