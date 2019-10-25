import matplotlib.pyplot as plt

x = [5,7,11,17,19,25]
k1 = [0.8222,0.918,0.9344,0.9262,0.9371,0.9353]
k2 = [0.8988,0.9334,0.9435,0.9407,0.9453,0.9453]
plt.plot(x,k1,'s-',color = 'r',label="ATT-RLSTM")
plt.plot(x,k2,'o-',color = 'g',label="CNN-RLSTM")
plt.xlabel("region length")
plt.ylabel("accuracy")
plt.legend(loc = "best")
plt.show()