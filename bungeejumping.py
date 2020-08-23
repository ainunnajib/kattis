import math
k, l, s, w = map(float, input().split())
while k + l + s + w > 0:
    g = 9.81

    if l >= s: # free fall, rope longer than height
        t = math.sqrt(2*s/g)
        v = g*t
        if v > 10:
            print("Killed by the impact.")
        else:
            print("James Bond survives.")
    else: # rope is stretched
        energy = w*g*s
        kinetic = energy - k*(s-l)*(s-l)/2
        if kinetic < 0:
            print("Stuck in the air.")
        else:
            v = math.sqrt(2*kinetic/w)
            if v > 10:
                print("Killed by the impact.")
            else:
                print("James Bond survives.")

    k, l, s, w = map(float, input().split())
