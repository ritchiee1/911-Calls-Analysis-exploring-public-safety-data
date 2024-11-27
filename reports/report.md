#911 Calls Analysis: Exploring Public Safety Data

##Introduction
This project explores a comprehensive analysis of 911 emergency call data from Kaggle. The main objective is to uncover patterns, trends, and insights that can improve the efficiency of emergency response systems. By analyzing call reasons, temporal trends, and geographical distributions, this project aims to provide valuable insights into the dynamics of emergency services.

##Data Overview
The dataset contains the following fields:

* lat: Latitude of the call
* lng: Longitude of the call
* desc: Description of the emergency
* zip: Zipcode
* title: Title (which includes the reason for the call)
* timeStamp: Time of the call in YYYY-MM-DD HH:MM format
* twp: Township of the call
* addr: Address
* e: Dummy variable (always 1)
The data includes information on when, where, and why calls were made, providing a rich source for analysis.

 ## Data Cleaning and Preprocessing
Before analyzing the data, several steps were taken to clean and preprocess it:

1. Datetime Conversion: The timeStamp column was converted from string format to a datetime object for easier manipulation of time-based features.
2. New Features: Additional features such as Hour, Month, and Day of Week were extracted from the timeStamp for temporal analysis.
3. Categorizing Call Reasons: A new column, Reason, was created from the title column, which categorizes the calls into EMS, Fire, and Traffic.
## Exploratory Data Analysis (EDA)
 ### Top Zipcodes for 911 Calls
The top 5 zip codes for 911 calls are:

19446: 6,979 calls
19401: 6,643 calls
19464: 4,853 calls
19403: 4,748 calls
19002: 3,174 calls

### Most Common Reasons for 911 Calls
Calls are classified into three main reasons:

* EMS (Emergency Medical Services) is the most frequent reason for calls.
* Traffic is the second most common.
* Fire accounts for the least number of calls.

### Temporal Trends
* Day of the Week: 911 calls are more frequent during weekdays, especially on Mondays.
* Hour of the Day: Calls peak during late morning and early afternoon, with a dip in the early hours of the morning.
* Month: A monthly trend indicates some months have missing data, but most calls occur during the summer months.

### Geographical Analysis
* Zipcodes: Geographical distribution of the calls shows that certain zip codes receive a significantly higher volume of calls than others.
* Townships: Similarly, townships like Norristown and Lower Merion have the highest number of calls.


## Insights & Findings
* Emergency Medical Services (EMS) calls are the most common, highlighting the importance of quick response to medical emergencies.
* Temporal Patterns: Calls peak during weekdays and certain hours of the day, suggesting that staffing and resource allocation for emergency services should focus on these high-demand periods.
* Geographical Hotspots: Zip codes and townships like Norristown and Lower Merion consistently have higher emergency call volumes, indicating a potential need for localized resources or response strategies.
## Conclusion & Recommendations
The analysis of 911 emergency calls provides key insights into how emergency services operate and where their resources are most needed. The high volume of EMS calls points to a strong need for medical-related emergency preparedness. It is recommended that emergency services use this data to optimize resource allocation by focusing on high-call periods and geographical hotspots.

Further analysis could explore seasonal trends more deeply, and additional datasets could provide insights into response times and outcomes.