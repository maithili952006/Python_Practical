import matplotlib.pyplot as plt

languages = ['java','python','cpp','c#']
popurlarity = [22, 17, 35, 29]

plt.barh(languages, popurlarity)

plt.title("Popularity of programming language")
plt.xlabel("Popularity")
plt.ylabel("Languages")

plt.show()
