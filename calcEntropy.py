import pickle

EQN = [s.strip() for s in open("eqn.dat", "rt")]

from nerdle import entropy2
 
SOL=[]
for eq in EQN:
  S = entropy2(EQN, eq)
  SOL.append((S, eq))

  print(eq, S, min(SOL), max(SOL))

pickle.dump(SOL, open("entropy.dat", "wb"))


