# Accenture Forage Data Analytics and Visualization Job Simulation: Social Buzz Content Popularity Data Analysis 

This project simulates a real-world data analytics engagement with Accenture, in partnership with the fast-growing social media platform Social Buzz. The objective was to analyze the platform’s massive volume of user-generated content and determine the top-performing content categories based on aggregate popularity scores.

## Executive Summary

As part of a three-month simulated analytics initiative, the Accenture team was tasked with helping Social Buzz prepare for a successful IPO by leveraging its content engagement data. With over **100,000 pieces** of content generated daily, the platform faced challenges in identifying which themes or categories resonated most with its users.

Using exploratory data analysis and data modeling, this project identifies the **top 5 most popular content categories** across the platform, with a focus on user reactions, post frequency, and content scores. The final recommendations guide marketing strategy, brand partnerships, and campaign timing based on real-time engagement patterns.

## Business Challenge

**Problem Statement:**
Social Buzz’s content library exceeds 36 million posts per year. The company needed to understand which types of content drive the most engagement to inform monetization, brand deals, and campaign planning.

**Client Goal:**
Analyze historical engagement data to uncover the most popular categories of content, measured by aggregated reaction scores, and deliver business-ready insights for marketing and product strategy.

## Analytical Approach

The analysis followed a structured data science workflow:

1. **Business Understanding:** Clarified the business objective, which is to determine the 5 most popular content categories using engagement metrics.
2. **Data Understanding:** Reviewed 7 datasets and a relational data model. Selected three core datasets: `Reaction`, `Content`, and `Reaction Types`.
3. **Data Cleaning & Modeling:** Merged datasets using content and reaction IDs. Aggregated reaction scores by category to determine relative popularity.

<p align="center">
  <img src="/assets/data_model.png" alt="Social Buzz Data Model" width="500">
</p>

4. **Analysis & Visualization:** Used content score summation to rank categories. Identified spikes in posting behavior and key engagement trends.

5. **Insight Delivery:** Developed visualizations to communicate findings, including content distribution by month and category-level performance.

##  Key Insights

- “Animals” was the most popular content category, generating 1,897 reactions and outperforming other themes such as Science and Cooking.

<p align="center">
  <img src="/assets/top_scores_per_category.png" alt="Top Scores per Category" width="600">
</p>

- Content volumes surged by 35% in May 2021, which had the highest number of posts (~2,138). This suggests strong seasonality that can inform campaign timing.

<p align="center">
  <img src="/assets/total_posts_per_month.png" alt="Total Posts per Month" width="600">
</p>

- Real-life content performed best, with “Lifestyle,” “Food,” and “Cooking” categories dominating the top 5.

<p align="center">
  <img src="/assets/top_reactions_per_category.png" alt="Top Reactions per Category" width="600">
</p>

- User engagement favors factual and relatable content, indicating a strong opportunity for partnerships with health, wellness, and education brands.

<p align="center">
  <img src="/assets/category_popularity_may_2021.png" alt="Category Popularity in May 2021" width="600">
</p>

## Recommendations

- Double down on high-performing categories such as Animals, Science, and Lifestyle when allocating promotion or ad inventory.

- Leverage May posting surge as a timing cue for future campaign launches or platform announcements.

- Partner with healthy eating brands to capitalize on interest in Food and Cooking categories.

- Automate content categorization and engagement tracking to monitor trends in real-time and scale insights across markets.

## Tools & Techniques

- Excel (Pivot Tables and SUMIFs)
- Python (Data cleaning and Data visualisation)

You can click here to view the [**slides**](https://github.com/erica-prog/Accenture_Forage_Data_Analytics_and_Visualization/blob/main/Accenture-%20Strategic%20Content%20Insights%20for%20Scaling%20User%20Engagement%20at%20Social%20Buzz.pdf). 

