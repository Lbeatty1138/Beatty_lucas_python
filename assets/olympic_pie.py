import matplotlib.pyplot as plt


labels = 'Skiing', 'Bobsleigh', 'Curling', 'Ice Hockey', 'Luge', 'Skating', 'Biathalon'
sizes = [60.230, 30.56, 80, 560, 0, 250.69,0.520]
explode = (0, 0, 0, 0.1, 0, 0, 0)
colors = ["midnightblue", "tomato", "darkgreen", "hotpink", "ivory", "darkmagenta", "sienna"]

fig1, ax1 = plt.subplots()
ax1.set_title('Canadian Winter Olympic Sports Popularity')
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
    colors=colors, shadow=True, startangle=90)
ax1.axis('equal')

plt.show()
