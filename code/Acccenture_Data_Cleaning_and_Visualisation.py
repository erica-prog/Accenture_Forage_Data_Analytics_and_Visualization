#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
content = pd.read_csv('Content.csv')
reactions = pd.read_csv('Reactions.csv')
reactiontypes = pd.read_csv('ReactionTypes.csv')

content.head()
content.info()

def clean_content(content):
    content.drop(columns=['Unnamed: 0', 'User ID', 'URL'], inplace= True)
    content.dropna(inplace=True)
    content.rename(columns={'Type':'Content Type'}, inplace=True)
    content['Category'] = content['Category'].str.lower()
    content['Category'] = content['Category'].str.replace('"', '')

    return content

content_cleaned = clean_content(content)

content_cleaned.head()

reactions.head()
reactions.info()

def cleaned_reactions(reactions):
    reactions.drop(columns=['Unnamed: 0', 'User ID'], inplace=True)
    reactions.dropna(inplace=True)
    reactions.rename(columns={'Type':'Reaction Type'}, inplace=True)
    reactions['Datetime'] = pd.to_datetime(reactions['Datetime'])
    reactions['Reaction Type'] = reactions['Reaction Type'].str.lower()
    return reactions

reactions_cleaned = cleaned_reactions(reactions)

reactions_cleaned.head()

reactiontypes.head()
reactiontypes.info()

def clean_reactiontypes(reactiontypes):
    reactiontypes.drop(columns=['Unnamed: 0'], inplace=True)
    reactiontypes.rename(columns={'Type':'Reaction Type'}, inplace=True)
    reactiontypes['Reaction Type'] = reactiontypes['Reaction Type'].str.lower()
    return reactiontypes

reactiontypes_cleaned = clean_reactiontypes(reactiontypes)

reactiontypes_cleaned.head()

# Merge the datasets
# - merge content and reactions data based on Content ID
# - merge reactions and reactiontypes data based on Reaction Type
merged_one = pd.merge(content_cleaned, reactions_cleaned, on='Content ID')
merged_one.head()

merged_full_cleaned_data = pd.merge(merged_one, reactiontypes_cleaned, on='Reaction Type')
merged_full_cleaned_data.head()

#export the merged data to csv file
merged_full_cleaned_data.to_csv('merged_full_cleaned_data.csv', index=False)

# Top 5 Scores per Category
top_scores_per_category = merged_full_cleaned_data.groupby('Category')['Score'].sum().sort_values(ascending=False)
top_scores_per_category.head()

len(top_scores_per_category)

# bar chart
plt.figure(figsize=(10,10))
plt.barh(top_scores_per_category.index, top_scores_per_category.values)
plt.xlabel('Score')
plt.ylabel('Category')
plt.title('Scores per category')
plt.show()

# bar chart for top 5 scores per category
top_5_scores = top_scores_per_category.head()

plt.figure(figsize=(10,10))
# Create a color array
colors = ['lightgray'] * len(top_5_scores)
# Set a different color for the top category
colors[0] = 'purple'
bars = plt.barh(top_5_scores.index, top_5_scores.values, color=colors)
plt.xlabel('Score')
plt.ylabel('Category')
plt.title('Top 5 Scores per category')
plt.gca().invert_yaxis() # descending order


# Add labels to the end of the bars
for bar in bars:
    plt.text(bar.get_width() - (bar.get_width() * 0.05),  # Position the text slightly before the end of the bar
             bar.get_y() + bar.get_height()/2,  # Position the text vertically centered in the bar
             f'{bar.get_width():.0f}',  # Format the label as an integer
             va='center', ha='right', color='white', fontsize=12) # Align and color the text

plt.show()

# How many reactions are there to most popular category?
reactions_per_category = merged_full_cleaned_data.groupby('Category')['Reaction Type'].count().sort_values(ascending=False)
reactions_per_category.head()

# bar chart for top 5 scores per category
top_5_reaction = reactions_per_category.head()

plt.figure(figsize=(10,10))
# Create a color array
colors = ['lightgray'] * len(top_5_reaction)
# Set a different color for the top category
colors[0] = 'darkviolet'
plt.barh(top_5_reaction.index, top_5_reaction.values, color=colors)
plt.xlabel('Reactions Count')
plt.ylabel('Category')
plt.title('Top 5 Reactions per category')
plt.gca().invert_yaxis() # descending order
plt.show()

# bar chart for top 5 scores per category
top_5_reaction = reactions_per_category.head()

plt.figure(figsize=(10,10))
# Create a color array
colors = ['lightgray'] * len(top_5_reaction)
# Set a different color for the top category
colors[0] = 'purple'
bars = plt.barh(top_5_reaction.index, top_5_reaction.values, color=colors)
plt.xlabel('Reactions Count')
plt.ylabel('Category')
plt.title('Top 5 Reactions per category')
plt.gca().invert_yaxis() # descending order

# Add labels to the end of the bars
for bar in bars:
    plt.text(bar.get_width() - (bar.get_width() * 0.05),  # Position the text slightly before the end of the bar
             bar.get_y() + bar.get_height()/2,  # Position the text vertically centered in the bar
             f'{bar.get_width():.0f}',  # Format the label as an integer
             va='center', ha='right', color='white', fontsize=12) # Align and color the text

plt.show()

# What was the month with the most posts?
# - time series plot using month and year
merged_full_cleaned_data['Datetime'] = pd.to_datetime(merged_full_cleaned_data['Datetime'])
merged_full_cleaned_data['Datetime'] = merged_full_cleaned_data['Datetime'].dt.strftime('%b, %Y')
merged_full_cleaned_data.head()

total_post_per_datetime = merged_full_cleaned_data.groupby('Datetime')['Content ID'].count()
total_post_per_datetime

plt.figure(figsize=(10,10))
plt.plot(total_post_per_datetime.index, total_post_per_datetime.values)
plt.xlabel('Datetime')
plt.ylabel('Total Posts')
plt.xticks(rotation=90)
plt.title('Total Posts per Month')

fig, ax = plt.subplots(figsize=(10,10))
ax.plot(total_post_per_datetime.index, total_post_per_datetime.values, color = 'violet')
ax.set_xlabel('Datetime')
ax.set_ylabel('Total Posts')
ax.set_xticklabels(total_post_per_datetime.index, rotation=90)
ax.set_title('Total Posts per Month')
# Find the month with the most posts
max_posts_month = total_post_per_datetime.idxmax()
max_posts_count = total_post_per_datetime.max()
# Annotate the highest point with bolder text, purple background and box shape
ax.annotate(f'Highest: {max_posts_month} ({max_posts_count} posts)',
            xy=(max_posts_month, max_posts_count),
            xytext=(max_posts_month, max_posts_count * 0.9),
            arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle="arc3,rad=-0.2"),
            ha='center',
            fontsize=10,
            fontweight='bold', # Make text bolder
            color='white', # Set text color to white
            bbox=dict(boxstyle="square,pad=0.3", fc="purple", ec="black", lw=2)) # Add purple background and box shape
plt.show()

# Pivot Table of Category vs DateTime
datetime_vs_category = pd.pivot_table(merged_full_cleaned_data, values='Content ID', index='Category', columns='Datetime', aggfunc='count', fill_value=0)
datetime_vs_category

# pie chart of the May 2021 vs category using datetime_vs_category
may_2021 = datetime_vs_category.loc[:, 'May, 2021']
may_2021

plt.figure(figsize=(10,10))
plt.pie(may_2021, labels=may_2021.index, autopct='%1.1f%%')
plt.title('Post category\'s popularity in May 2021')
plt.show()

# Moving the animals's pie slightly away from the chart
may_2021 = datetime_vs_category.loc[:, 'May, 2021']
may_2021

# Explode the "animals" slice
explode = [0] * len(may_2021)
# Find the index of 'animals'
try:
  animals_index = may_2021.index.get_loc('animals')
  explode[animals_index] = 0.1 # Adjust this value to control how much the slice is moved
except KeyError:
  # Handle the case where 'animals' is not in the data
  print("Category 'animals' not found in May, 2021 data.")
  explode = [0] * len(may_2021) # Reset explode if 'animals' is not found

plt.figure(figsize=(10,10))
plt.pie(may_2021, labels=may_2021.index, autopct='%1.1f%%', explode=explode)
plt.title('Post category\'s popularity in May 2021')
plt.show()
