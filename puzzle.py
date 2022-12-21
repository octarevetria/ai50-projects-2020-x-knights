from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

premise_A = And(Or(AKnight,AKnave),Not(And(AKnight,AKnave)))
premise_B = And(Or(BKnight,BKnave),Not(And(BKnight,BKnave)))
premise_C = And(Or(CKnight,CKnave),Not(And(CKnight,CKnave)))
statement_0A = And(AKnight,AKnave)
statement_1A = And(AKnave, BKnave)
statement_2A = Or(And(AKnight,BKnight),And(BKnight,BKnave))
statement_2B = Not(statement_2A)
statement_3A = Or(AKnight,AKnave)
statement0_3B = AKnave
statement1_3B = CKnave
statement_3C = AKnight

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(premise_A,
    Implication(AKnight,statement_0A),
    Implication(AKnave,Not(statement_0A))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(premise_A,
    premise_B,
    Implication(AKnave,Not(statement_1A)),
    Implication(AKnight,statement_1A)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(premise_A,
    premise_B,
    Implication(AKnight,statement_2A),
    Implication(AKnave,Not(statement_2A)),
    Implication(BKnight,statement_2B),
    Implication(BKnave,Not(statement_2B)),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(premise_A,
    premise_B,
    premise_C,
    Implication(AKnight,statement_3A),
    Implication(AKnave,Not(statement_3A)),
    Implication(BKnight,statement0_3B),
    Implication(BKnight,statement1_3B),
    Implication(BKnave,(Not(statement0_3B))),
    Implication(BKnave,(Not(statement1_3B))),
    Implication(CKnight,statement_3C),
    Implication(CKnave,Not(statement_3C)) 
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
