import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    print(initial_tx, file=sys.stderr, flush=True)
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    while(initial_tx==light_x and initial_ty>light_y):
        initial_ty-=1
        print("N")

    while(initial_tx==light_x and initial_ty<light_y):
        initial_ty+=1
        print("S")
    
    while(initial_ty==light_y and initial_tx<light_x):
        initial_tx+=1
        print("E")

    while(initial_ty==light_y and initial_tx>light_x):
        initial_tx-=1
        print("W")

    while(initial_tx<light_x and initial_ty<light_y):
        initial_tx+=1
        initial_ty+=1
        print("SE")

    while(initial_tx>light_x and initial_ty<light_y):
        initial_tx-=1
        initial_ty+=1
        print("SW")

    while(initial_tx<light_x and initial_ty>light_y):
        initial_tx+=1
        initial_ty-=1
        print("NE")

    while(initial_tx>light_x and initial_ty>light_y):
        initial_tx-=1
        initial_ty-=1
        print("NW")

    # A single line providing the move to be made: N NE E SE S SW W or NW
