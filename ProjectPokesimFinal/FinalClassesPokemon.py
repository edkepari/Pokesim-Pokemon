import random

class Pokemon:
    def generateMoves(Movepool, Atk, SpAtk):
        MoveSet=[]
        PhysicalSTAB1=[]
        PhysicalSTAB2=[]
        PhysicalCoverage=[]
        SpecialSTAB1=[]
        SpecialSTAB2=[]
        SpecialCoverage=[]
        for i in range(3,len(Movepool)):
            if Movepool[i]=="-":
                k = i+2
                break
            PhysicalSTAB1.append(Movepool[i])
        for i in range(k,len(Movepool)):
            if Movepool[i]=="-":
                k = i+2
                break
            PhysicalSTAB2.append(Movepool[i])
        for i in range(k,len(Movepool)):
            if Movepool[i]=="-":
                k = i+3
                break
            PhysicalCoverage.append(Movepool[i])
        for i in range(k,len(Movepool)):
            if Movepool[i]=="-":
                k = i+2
                break
            SpecialSTAB1.append(Movepool[i])
        for i in range(k,len(Movepool)):
            if Movepool[i]=="-":
                k = i+2
                break
            SpecialSTAB2.append(Movepool[i])
        for i in range(k,len(Movepool)-1):
            SpecialCoverage.append(Movepool[i])
        k = Atk-SpAtk+50
        randomNumber = random.random()*100
        if randomNumber<=k and len(PhysicalCoverage)+len(PhysicalSTAB1)+ len(PhysicalSTAB2)>=4:
            setType = "Physical"
        elif randomNumber>k and len(SpecialCoverage) + len(SpecialSTAB1) + len(SpecialSTAB2)>=4:
            setType = "Special"
        elif len(PhysicalCoverage)+len(PhysicalSTAB1)+ len(PhysicalSTAB2)>len(SpecialCoverage) + len(SpecialSTAB1) + len(SpecialSTAB2):
            setType = "Physical"
        else:
            setType = "Special"
        if setType=="Physical":
            MoveSet.append(random.choice(PhysicalSTAB1))
            PhysicalSTAB1.remove(MoveSet[0])
            if len(PhysicalSTAB2)!=0:
                MoveSet.append(random.choice(PhysicalSTAB2))
                PhysicalSTAB2.remove(MoveSet[1])
            k = 4-len(MoveSet)
            if len(PhysicalCoverage)>=k:
                for i in range(0,k):
                    MoveSet.append(random.choice(PhysicalCoverage))
                    PhysicalCoverage.remove(MoveSet[-1])
                return MoveSet
            MoveSet = MoveSet + PhysicalCoverage
            PhysicalSTAB1 = PhysicalSTAB1 + PhysicalSTAB2
            while len(MoveSet)<4:
                MoveSet.append(random.choice(PhysicalSTAB1))
                PhysicalSTAB1.remove(MoveSet[-1])
            return MoveSet
        MoveSet.append(random.choice(SpecialSTAB1))
        SpecialSTAB1.remove(MoveSet[0])
        if len(SpecialSTAB2)!=0:
            MoveSet.append(random.choice(SpecialSTAB2))
            SpecialSTAB2.remove(MoveSet[1])
        k = 4-len(MoveSet)
        if len(SpecialCoverage)>=k:
            for i in range(0,k):
                MoveSet.append(random.choice(SpecialCoverage))
                SpecialCoverage.remove(MoveSet[-1])
            return MoveSet
        MoveSet = MoveSet + SpecialCoverage
        SpecialSTAB1 = SpecialSTAB1 + SpecialSTAB2
        while len(MoveSet)<4:
            MoveSet.append(random.choice(SpecialSTAB1))
            SpecialSTAB1.remove(MoveSet[-1])
        return MoveSet

    def __init__(self, Name, Type1, Type2, HP, Attack, Defense, SpAttack, SpDefense, Speed, Movepool, Front, Back):
        self.Name = Name
        self.Type1 = Type1
        self.Type2 = Type2
        self.HP = HP
        self.OriginalHP = HP
        self.Attack = Attack
        self.Defense = Defense
        self.SpAttack = SpAttack
        self.SpDefense = SpDefense
        self.Speed = Speed
        self.MoveSet = Pokemon.generateMoves(Movepool, int(Attack), int(SpAttack))
        self.Front = Front
        self.Back = Back

class Moves:
    def __init__(self, Name, Type, PP, Power, Accuracy, Catagory):
        self.Name = Name
        self.Type = Type
        self.PP = PP
        self.Power = Power
        self.Accuracy = Accuracy
        self.Catagory = Catagory

class TypeAdvantages:
    def __init__(self, MoveType, StrongAgainst, WeakAgainst, ImmuneAgainst):
        self.MoveType = MoveType
        self.StrongAgainst = StrongAgainst[:]
        self.WeakAgainst = WeakAgainst[:]
        self.ImmuneAgainst = ImmuneAgainst[:]

class Trainer:
    def __init__(self, Name, Party):
        self.Name = Name
        self.Party = Party[:]