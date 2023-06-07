

import matplotlib.pyplot as plt
alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text = 'PRAVALIKA BOLLAM'
vertical = []
for x in alphabet:
    m = text.count(x)
    vertical.append(m)
    
print(vertical)
plt.bar(list(alphabet), vertical)
plt.show()

