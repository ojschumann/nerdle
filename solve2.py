from nerdle import entropy2, result

EQN = [s.strip() for s in open("eqn.dat", "rt")]

def filter(test, x):
  global EQN

  EQN = [ eq for eq in EQN if result(eq, test) == x ]


  SOL = [ (entropy2(EQN, eq), eq) for eq in EQN ]

  T = min(SOL)[0]
  T = [eq for s,eq in SOL if s==T]


  test = random.choice(T)
  print ("left", len(EQN), min(SOL), len(T), test)

  return SOL




