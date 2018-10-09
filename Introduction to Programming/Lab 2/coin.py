from random import choice

coin_faces = ("Heads", "Tails")
times_per_face = {"Heads":0, "Tails":0}

for i in range(100):
    if choice(coin_faces) == "Heads":
        times_per_face["Heads"] += 1
    else:
        times_per_face["Tails"] += 1

print("Heads: {}, Tails: {}".format(times_per_face["Heads"], times_per_face["Tails"]))
