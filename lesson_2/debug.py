# debug.py
import pdb


counter = 1

pdb.set_trace()

while counter <= 5:
    pdb.set_trace()
    print(counter)
    counter += 1


