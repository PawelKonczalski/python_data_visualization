import matplotlib.pylab as plt


labels = 'JavaScript', 'Python', 'Java', 'Ruby', 'PHP', 'C++'
sizes = [230, 100, 98.6, 87.0, 55.9, 4.13]
separated = (0, .1, 0, 0, 0, 0)

plt.pie(sizes, labels=labels, autopct='%1.2f%%', explode=separated)
plt.axis('equal')
plt.show()
