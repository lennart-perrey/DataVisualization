'''
1. 
visualization answers questions related to the distribution of time spent on iOS and Android devices, distinguishing between the time spent on apps and browsers. It provides a detailed breakdown of the time spent on various app categories and browsers.
2. 
Marks: The marks used are slices in a pie chart.
Channels: The channels used include color (for distinguishing categories), angle/area (for representing proportions), and labels (for providing additional information about each category).
3.
Violation of Tufte's principle of maximizing the data-ink ratio:
detailed breakdown of the "Apps" category could potentially lead to information overload, making it challenging for viewers to extract meaningful insights at a glance. Also pie charts have limited ability to accurately represent proportions, especially when there are many categories.
4. 
Like: 
visualization provides a clear overview of the dominant categories (Apps vs. Browser) and the subcategories within each. The use of color helps differentiate between the categories, and the labels provide additional context.
Dislike: Pie charts can be less effective for precise comparisons, especially when there are many categories. The detailed breakdown of the "Apps" category might be overwhelming, and the use of multiple colors could make it challenging for users with color vision deficiencies to interpret.
5.
replaced pie chart with a grouped bar chart, where each category ("Apps" and "Browser") is represented by a separate bar;
applied distinct colors for each major category and shades within each major category for subcategories;
included labels and percentages for each major category and subcategory.
provided a clear title and key takeaways to guide the viewer's understanding.
grouped bar chart is more effective for comparing proportions between major categories ("Apps" and "Browser") and within each major category.
'''
import matplotlib.pyplot as plt

# Data for the original pie chart
categories = ['Apps', 'Browser']
colors = ['#3498db', '#2ecc71']  # Blue for Apps, Green for Browser
sizes = [86, 14]  # Percentage of time spent

# Subcategories for Apps and Browser
app_subcategories = ['Gaming', 'Facebook', 'Utilities', 'Productivity', 'Social Messaging', 'Others', 'Entertainment', 'Youtube', 'News', 'Twitter']
app_sub_sizes = [32, 17, 8, 4, 9.5, 3, 4, 4, 3, 1]
app_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#17becf', '#ff0000']  # Different colors for app subcategories

browser_subcategories = ['Apple Safari', 'Google Browsers', 'Others']
browser_sub_sizes = [7, 5, 2]
browser_colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # Different colors for browser subcategories

# Create a stacked bar chart
fig, ax = plt.subplots()

# Plotting the Apps category
ax.bar(categories[0], sizes[0], color=colors[0], label='Total', alpha=0.7)

# Plotting the subcategories for Apps
bottom = [0]
for i, (subcat, subsize, color) in enumerate(zip(app_subcategories, app_sub_sizes, app_colors)):
    ax.bar(categories[0], subsize, color=color, bottom=bottom[-1], label=subcat, alpha=0.7)
    bottom.append(bottom[-1] + subsize)

# Plotting the Browser category
ax.bar(categories[1], sizes[1], color=colors[1], label='Total', alpha=0.7)

# Plotting the subcategories for Browser
bottom = [0]
for i, (subcat, subsize, color) in enumerate(zip(browser_subcategories, browser_sub_sizes, browser_colors)):
    ax.bar(categories[1], subsize, color=color, bottom=bottom[-1], label=subcat, alpha=0.7)
    bottom.append(bottom[-1] + subsize)

# Adding labels and legend
ax.set_ylabel('% of Time Spent')
ax.set_title('Mobile Experience: Apps vs. Browser')
ax.legend()

# Display the plot
plt.show()
