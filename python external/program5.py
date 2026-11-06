import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Create a pie chart
plt.pie(popularity, labels=languages, autopct='%1.1f%%')

# Add title
plt.title("Popularity of Programming Languages")

# Display the chart
plt.show()