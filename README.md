# ShopEase Ecommerce Analysis

## Background and Overview

### Problem Statement

Our e-commerce store has been operational for several years, accumulating a vast amount of data on customer behavior, preferences, and purchasing habits. However, this data has not been thoroughly analyzed to identify trends, patterns, and insights that can inform business decisions. The e-commerce market is experiencing rapid growth, and our company is facing increased competition. To stay ahead, our stakeholders have requested a comprehensive analysis of our online store to better understand our customer segments, their preferences, and the overall workflow of our store.

### Objectives

The primary objectives of this project are:

    1. Identify customer segments based on behavior, preferences, and purchasing habits.
    2. Analyze the workflow of our entire store to identify areas for improvement.
    3. Develop a detailed report summarizing our findings, providing insights to support the marketing team in developing strategies to bolster sales.

### Methodology

To achieve these objectives, we will employ a combination of data analysis and RFM (Recency, Frequency, Monetary) analysis techniques. Our analysis will focus on 2 months of e-commerce store data to identify trends, patterns, and insights that can inform business decisions.

### Deliverables

The project deliverables will include:

    1. Customer Segmentation Model: A machine learning model that segments our customers into distinct groups based on their behavior, preferences, and purchasing habits. The model will be trained on our e-commerce         store data and will provide insights into customer characteristics.
    2. Detailed Report: A comprehensive report summarizing our findings and providing insights to support the marketing team in developing strategies to bolster sales.
    
---> Interactive platform showcasing data analysis findings and customer segmentation model results can be found [here](https://shopease.streamlit.app/home).
<br>
---> Detailed documentation of project methodology, results, and insights can be found here [here](https://shopease-analysis.readthedocs.io/en/latest/).
<br>
---> Step-by-step guide to data analysis, modeling, and customer segmentation model building can be found here [here](https://github.com/Sherwin-14/shopease_analysis/blob/master/eda-on-ecommerce-dataset.ipynb).



## Data Structure Overview
The dataset used for this project consists of over 10 crore records, providing a comprehensive view of customer behavior and purchasing habits. The data is structured into 9 columns, each containing unique information about the customers and their interactions with the e-commerce platform.

![Data Looks Like This](https://github.com/Sherwin-14/shopease_analysis/blob/master/strucutre.png)

## Executive Summary

### Overview Of Findings

#### Insight 1: Category Dominance 

Our analysis of Shopease's sales data reveals that Electronics and Appliances emerge as the clear market leaders, commanding the largest share of sales. Specifically, Electronics account for 22.1%, Computers comprise 20.6%, Apparel represents 21.1%, and Appliances make up 12.6% of total sales. Conversely, Medicine trails behind, representing a mere 0.0466% of sales, indicating opportunities for growth and expansion in this segment.

![Data Looks Like This](https://github.com/Sherwin-14/shopease_analysis/blob/master/docs/images/main_categories.png)

#### Insight 2: Brand Dominance and Opportunities

A closer examination of the word cloud reveals that Bertoni, Cube,Ariston, Audio are the dominant brands driving sales and customer engagement on Shopease. To capitalize on this trend, store owners should prioritize inventory management and marketing efforts for these brands. Conversely, smaller brands like Concept Club, JVC, Denzel, and Candy, which have a relatively weaker presence, may require reevaluation or targeted promotions to increase their visibility and appeal to customers.

![Data Looks Like This](https://github.com/Sherwin-14/shopease_analysis/blob/master/docs/images/top_10_most_popular_brands_by_revenue.png)

#### Insight 3: Peak Customer Activity Hours

Our analysis of hourly data reveals that customers are most active during specific time windows, indicating opportunities for targeted marketing and promotions. The top four peak hours are:

    1.16:00-17:00: This hour sees a peak in views (850,156) and carts (14,056), with purchases (10,570) remaining strong.
    2.15:00-16:00: High activity is observed in views (828,353) and carts (15,168), with purchases (11,288) significant.
    3.14:00-15:00: Continued high activity is seen in views (764,775) and carts (15,629), with purchases (11,837) still notable.
    4.7:00-8:00: This early morning hour experiences high activity in views (638,503) and carts (19,415), with purchases (16,216) strong.

![Data Looks Like This](https://github.com/Sherwin-14/shopease_analysis/blob/master/docs/images/hour_eventtype.png)
  
By understanding these peak hours, Shopease can optimize its marketing efforts, promotions, and inventory management to cater to customer demand and maximize sales.

#### Insight 4: Customer Segmentation

Our analysis has revealed a customer segmentation model that categorizes customers into five distinct clusters based on their recency, frequency, and monetary value. These clusters provide valuable insights into customer behavior and preferences, enabling targeted marketing strategies and personalized recommendations.

    1.Recent One-Time Buyers (Cluster 0): Customers who have recently made a purchase, but don't buy frequently and don't spend much.
    2.Inactive Customers (Cluster 1): Customers who haven't made a purchase recently, don't buy frequently, and don't spend much.
    3.Frequent Low-Spenders (Cluster 2): Customers who don't make purchases recently, but when they do, they buy frequently and don't spend much.
    4.Moderate Value Customers (Cluster 3): Customers who don't make purchases recently, but when they do, they spend a moderate amount of money.
    5.High-Value Frequent Buyers (Cluster 4): Customers who don't make purchases recently, but when they do, they spend a lot of money and buy frequently.

This customer segmentation model provides a framework for understanding customer behavior and preferences, enabling targeted marketing strategies and personalized recommendations.

***To explore these insights in more detail, please visit the Background and Overview section, where you can find links to additional resources and visualizations.***

## Recommendations

As the primary objective of this project was to analyze the data and present insights to stakeholders, no specific recommendations are made in this report. Instead, the insights and findings presented here are intended to inform the marketing team's decision-making process.


The marketing team can use these insights to develop targeted marketing strategies, optimize product offerings, and improve customer engagement. The specific actions and recommendations will be determined by the marketing team based on their expertise and business objectives.

## Caveats and Assumptions

While our analysis provides valuable insights into customer behavior and preferences, there are several caveats and assumptions that should be considered when interpreting the results.

    1. Data quality and completeness: Our analysis assumes that the data is accurate, complete, and free from errors. However, in reality, data quality issues may exist, which could impact the accuracy of our findings.
    2. Sampling bias: Our analysis is based on a sample of data, which may not be representative of the entire population. This could lead to biased results and conclusions.
    3. Assumptions about customer behavior: Our analysis assumes that customers behave in a consistent manner, which may not always be the case. Customers may exhibit different behavior patterns over time, which could impact the accuracy of our findings.
    4. Limited data scope: Our analysis is limited to the data provided, which may not capture all aspects of customer behavior and preferences. Additional data sources or variables may be necessary to gain a more comprehensive understanding of customer behavior.
    5. Assumptions about product categories: Our analysis assumes that product categories are mutually exclusive and exhaustive, which may not always be the case. Products may belong to multiple categories or have ambiguous categorization, which could impact the accuracy of our findings.
    6. Assumptions about user behavior: Our analysis assumes that users behave in a consistent manner, which may not always be the case. Users may exhibit different behavior patterns over time, which could impact the accuracy of our findings.


