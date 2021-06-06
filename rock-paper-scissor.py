import random
import sys

print("Do you want to play a new match?")
print("1- Yes")
print("2- No")
opcion=int(input())
jug=0
pc=0
while opcion!=1 and opcion!=2:
    print("Error")
    print("Invalid option")
    print("Do you want to play a new match?")
    print("1- Yes")
    print("2- No")
    opcion=int(input())
while opcion==1:
    print("Choose: rock, paper, scissor") 
    op_jug=input()
    if op_jug=="rock": # rock=1 paper=2 scissor=3
        mano_jug=1
    elif op_jug=="paper":
        mano_jug=2
    elif op_jug=="scissor":
        mano_jug=3
    else:
        print("Error")
        print("End of program")
        sys.exit()
    mano_pc=random.randint(1,3)
    if mano_pc==1:
        print("PC chooses rock")
    elif mano_pc==2:
        print("PC chooses paper")
    elif mano_pc==3:
        print("PC chooses scissor")
    # jug - pc #
    # rock - paper -> pc  #
    # rock - scissor -> player #
    # paper - rock -> player #
    # paper - scissor -> pc #
    # scissor - paper -> player #
    # scissor - rock -> pc #
    # same option -> tie #
    if mano_jug==1 and mano_pc==2:
        jug=jug
        pc=pc+1
    elif mano_jug==1 and mano_pc==3:
        jug=jug+1
        pc=pc
    elif mano_jug==2 and mano_pc==1:
        jug=jug+1
        pc=pc
    elif mano_jug==2 and mano_pc==3:
        jug=jug
        pc=pc+1
    elif mano_jug==3 and mano_pc==2:
        jug=jug+1
        pc=pc
    elif mano_jug==3 and mano_pc==1:
        jug=jug
        pc=pc+1
    else:
        # empate
        jug=jug
        pc=pc
    print("Play another round?")
    print("1- Yes")
    print("2- No")
    opcion=int(input())
if jug>pc:
    print("Player wins ", jug, " to ", pc)
elif jug<pc:
    print("PC wins ", pc, " to ", jug)
else:
    print("Tie ", pc, " to ", jug)
