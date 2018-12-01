import matplotlib.pyplot as plt
import numpy as np

n_groups = 10

men = (20, 32, 17, 34, 41, 8, 75, 76, 57, 152)

women = (0, 0, 2, 2, 6, 7, 50, 49, 85, 88)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.3

opacity = 1

ax.bar(index, men, bar_width, alpha=opacity, color='#89cff0', label='Men')
ax.bar(index + bar_width, women, bar_width, alpha=opacity, color='#32CD32', label='Women')

ax.set_xlabel('Decades')
ax.set_ylabel('Genders')
ax.set_title('Men and Women Olympic Participation in Canada Per Decade')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('1920s', '1930s', '1940s', '1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s'))
ax.legend()

fig.tight_layout()
plt.show()
