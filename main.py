"""
Author: Cristian Pintor
This program prompts the user to enter the type of beam and the necessary data (based on the input), and then computes
and displays the beam’s rectangular moment of inertia.
"""

from beamProgram import *

def main():
    greeting()
    beamType = input("Please enter the type of beam (A=I-Beam, D=rectangular beam, C=cylindrical beam, X=quit): ")

    while beamType != 'X':
        if(beamType == 'A'):
            b = eval(input("Enter large base: "))
            b2 = eval(input("Enter small base: "))
            h = eval(input("Enter large height: "))
            h2 = eval(input("Enter small height: "))
            x = beamA(b, b2, h, h2)
            print(x)
        elif (beamType == 'D'):
            b = eval(input("Enter base: "))
            h = eval(input("Enter height: "))
            x = beamD(b, h)
            print(x)
        elif (beamType == 'C'):
            r = eval(input("Enter radius: "))
            x = beamC(r)
            print(x)
        # Program repeats same question at the end of while loop
        beamType = input("Please enter the type of beam (A=I-Beam, D=rectangular beam, C=cylindrical beam, X=quit): ")

main()
