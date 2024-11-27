README.md
# 911 Calls Analysis Project

## Topic
Analysis of Emergency 911 Calls to Uncover Patterns and Insights using google colab

## Table of Contents
1. [Project Scope](#project-scope)
2. [Project Objectives](#project-objectives)
3. [Expected Outcome](#expected-outcome)
4. [Document Purpose](#document-purpose)
5. [Use Case](#use-case)
6. [Data Source](#data-source)
7. [Data Cleaning and Processing](#data-cleaning-and-processing)
8. [Data Analysis](#data-analysis)
9. [Data Visualization](#data-visualization)
10. [Recommendation](#recommendation)
11. [Conclusion](#conclusion)

## Project Scope
This project involves a comprehensive analysis of 911 emergency call data to identify patterns, trends, and insights that could potentially improve emergency response systems and resource allocation.

## Project Objectives
- Analyze the frequency and types of emergency calls
- Identify temporal patterns in emergency calls (daily, weekly, monthly trends)
- Examine geographical distribution of calls
- Investigate correlations between call types and specific times or locations

## Expected Outcome
The analysis aims to provide actionable insights that can help emergency services optimize resource allocation, improve response times, and enhance overall emergency management strategies.

## Document Purpose
This document serves as a comprehensive guide to the 911 Calls Analysis project, outlining its scope, objectives, methodologies, and findings.

## Use Case
The insights derived from this analysis can be used by emergency service departments to:
- Optimize staffing levels based on call volume patterns
- Improve resource allocation in high-call areas
- Develop targeted prevention strategies for specific types of emergencies
- Enhance public safety education programs

## Data Source
The dataset used in this analysis is sourced from Kaggle and contains detailed information about 911 emergency calls, including timestamps, locations, and call descriptions.

## Data Cleaning and Processing
### Handling Missing Values:
* The dataset contained some missing values in the zip, twp, and addr columns.
* We did not fill missing values as they were minimal and did not significantly impact the analysis.
### Data Type Conversion:
* The timeStamp column, initially in string format, was converted to DateTime objects using pd.to_datetime() to allow for time-based analysis.
### Feature Extraction:
* Extracted new features from the timeStamp column: Hour, Month, Day of Week, and Date.
* Created a Reasons column by extracting the emergency type (EMS, Fire, Traffic) from the title column.

## Data Analysis
This analysis was performed using Google Colab, leveraging libraries such as pandas, seaborn, and matplotlib.

### Key Questions Explored:
1. Top 5 Zip Codes for 911 Calls:
* Identified the top zip codes where the most 911 calls originated.
2. Top 5 Townships for 911 Calls:
* Explored which townships had the highest volume of emergency calls.
3. Common Reasons for 911 Calls:
* Using the Reasons column, we found that the most common reason for 911 calls was EMS (Emergency Medical Services).
4. Time-Based Analysis:
* Grouped the data by Hour, Month, and Day of Week to identify trends over time.
* Investigated patterns by day of the week and month to understand peak times for calls.


## Data Visualization
Several visualizations were created to represent the analysis findings:

1. Countplot of 911 Calls by Reason:
A bar chart using seaborn to show the frequency of 911 calls for each reason (EMS, Fire, Traffic).
[Countplot of 911 Calls By Reasons]![image](https://github.com/user-attachments/assets/e6ccef33-a2e9-4907-9dbd-4fbc43cb5c57)

2. Countplot of Calls by Day of Week:
Visualized the number of calls each day of the week, broken down by emergency reason.
[Countplot of Calls by Day of Week]![image](https://github.com/user-attachments/assets/25a0fb6d-b57d-4c86-a436-6ec0650695c9)

3. Monthy Calls Trend:
Created line plots to visualize the number of calls per month, revealing that some months had missing data.
[Monthy Calls Trend]![image](https://github.com/user-attachments/assets/78c30b02-88c1-4f9a-aabe-4f1cd8732537)

4. Heatmaps:
Used heatmaps to show the distribution of 911 calls by day of the week and hour, as well as by day of the week and month.
[heatmap day-of-week]![image](https://github.com/user-attachments/assets/a58b1241-a296-437d-9710-c0dbf869ff99)

[heatmap day-hour]![image](https://github.com/user-attachments/assets/e3c9d460-6ba7-486f-b9db-7969484392dd)

[heatmap day-month]![image](https://github.com/user-attachments/assets/8ee01765-9e0b-495b-bc65-583ba8c13816)


5. Clustermaps:
Generated clustermaps to identify patterns in the data and cluster similar time periods based on call volume.
[clustermap of day-month]![image](https://github.com/user-attachments/assets/2404cdac-f915-4d0b-b6a4-2f9272450703)


## Recommendation
It is recommended that emergency services use this data to optimize resource allocation by focusing on high-call periods and geographical hotspots.

## Conclusion
The analysis of 911 emergency calls provides key insights into how emergency services operate and where their resources are most needed. The high volume of EMS calls points to a strong need for medical-related emergency preparedness. 

## LINK
https://drive.google.com/file/d/10KfbNkBAfoK4p0-I7hxjOl3GynrePZ1b/view?usp=sharing
