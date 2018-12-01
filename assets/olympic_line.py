import matplotlib.pyplot as plt

n_gorups = 10
years = ('1920s', '1930s', '1940s', '1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s')
medals = (20, 32, 19, 36, 47, 4, 12, 125, 142, 180)

plt.plot(years, medals, c='r')
plt.title('Medals Earned For Canada Per Decade')
plt.xlabel('Olympics in Decades')
plt.ylabel('Medals earned for Canada')
plt.show()
