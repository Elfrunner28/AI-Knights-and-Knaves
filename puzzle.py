from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnave,AKnight),
    Not(And(AKnight,AKnave)),
    Implication(AKnight,And(AKnight,AKnave)))

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnave,AKnight),
    Not(And(AKnight,AKnave)),
    #A is not a knight and a knave
    Or(BKnave,BKnight),
    Not(And(BKnight,BKnave)),
    Implication(AKnave,Not(And(AKnave,BKnave))),
    # If A is a knave, A and B cannot both be knaves 
    Implication(AKnight,And(AKnave,BKnave)),
    # if A is a knight, A is a knave and B is a knight
    
)



# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnave,AKnight),
    Not(And(AKnight,AKnave)),
    #A is not a knight and a knave
    Or(BKnave,BKnight),
    Not(And(BKnight,BKnave)),
    Implication(AKnave,BKnight),
    Implication(AKnight,BKnight),
    Implication(BKnight,AKnave),
    Implication(BKnave,AKnave)


)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnave,AKnight),
    Not(And(AKnight,AKnave)),
    #A is not a knight and a knave
    Or(BKnave,BKnight),
    Not(And(BKnight,BKnave)),

    Or(CKnave,CKnight),
    Not(And(CKnight,CKnave)),

    Implication(AKnave,Not(Or(AKnave,AKnight))),
    Implication(BKnight,And(AKnave,CKnave)),
    Implication(BKnave,CKnight),
    Implication(CKnave,AKnave)
    
    #if A is a knave, he is lying about the statement: I am either a knight or a knave. A = a or i. Contradiction to that is 

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
