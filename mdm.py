import matplotlib.pyplot as plt
import numpy as np

# Create a 2x2 subplot figure for the 4 advanced chart types
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# 1. Box Plot (`plt.boxplot`)
data_box = [np.random.normal(0, std, 100) for std in range(1, 4)]
axs[0, 0].boxplot(data_box, tick_labels=['Group A', 'Group B', 'Group C'])
axs[0, 0].set_title('Box Plot (Quartiles & Outliers)')
axs[0, 0].grid(True, linestyle='--', alpha=0.6)

# 2. Stacked Area Plot (`plt.stackplot`)
x_time = np.arange(1, 6)
y_stack = np.array([
    [1, 4, 3, 2, 5],
    [2, 2, 7, 3, 4],
    [3, 5, 2, 6, 8]
])
axs[0, 1].stackplot(x_time, y_stack, labels=['Series 1', 'Series 2', 'Series 3'], colors=['#ff9999', '#66b3ff', '#99ff99'])
axs[0, 1].set_title('Stacked Area Plot')
axs[0, 1].legend(loc='upper left')

# 3. Violin Plot (`plt.violinplot`)
data_violin = [np.random.normal(0, 1, 100), np.random.normal(2, 1.5, 100)]
axs[1, 0].violinplot(data_violin, showmeans=True)
axs[1, 0].set_title('Violin Plot (Probability Density)')
axs[1, 0].set_xticks([1, 2])
axs[1, 0].set_xticklabels(['Dataset 1', 'Dataset 2'])

# 4. Contour Plot (`plt.contourf`)
x_c = np.linspace(-3, 3, 100)
y_c = np.linspace(-3, 3, 100)
X_c, Y_c = np.meshgrid(x_c, y_c)
Z_c = np.exp(-X_c**2 - Y_c**2)
contour = axs[1, 1].contourf(X_c, Y_c, Z_c, levels=20, cmap='viridis')
fig.colorbar(contour, ax=axs[1, 1], shrink=0.8)
axs[1, 1].set_title('Contour Plot (Surface Elevation)')

# Adjust layout to prevent overlap and render the plots
plt.tight_layout()
plt.show()