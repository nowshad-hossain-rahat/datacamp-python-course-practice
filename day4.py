import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(123)

# random_walk = [0]

# for x in range(100):
#   step = random_walk[-1]
#   dice = np.random.randint(1, 7)

#   if dice <= 2:
#     step = max(0, step - 1)
#   elif dice <= 5:
#     step = step + 1
#   else:
#     step = step + np.random.randint(1, 7)

#   random_walk = np.append(random_walk, step)

# plt.plot(random_walk)

# plt.show()

# final_steps = []

# for x in range(100):
#   tails = [0]

#   for y in range(10):
#     step = tails[-1]
#     coin = np.random.randint(0, 2)

#     tails.append(tails[y] + coin)

#   # final_steps.append(tails[-1])
#   final_steps.extend(tails)

# print(final_steps)

# plt.plot(final_steps)

# plt.show()

netflix_df = pd.read_csv("netflix_data.csv")

duration = netflix_df["duration"].value_counts().idxmax()

print(duration)

action_movies = netflix_df[
    np.logical_and(netflix_df["type"] == "Movie", netflix_df["genre"] == "Action")
]

short_movies = action_movies[action_movies["duration"] < 90]
movies_after_1990s = short_movies[short_movies["release_year"] >= 1990]
movies_before_2000s = movies_after_1990s[movies_after_1990s["release_year"] < 2000]

short_movie_count = len(movies_before_2000s)

print(short_movie_count)
