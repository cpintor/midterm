def greeting():
    print("Welcome to the beam inertia program")

def beamA(b, b2, h, h2):
    i = (b*h ** 3) - (b2*h2 ** 3)/12
    return (i)

def beamD(b, h):
    i = (b*h ** 3)/12
    return (i)

def beamC(r):
    i = (3.14 * r ** 4) / 4
    return(i)

