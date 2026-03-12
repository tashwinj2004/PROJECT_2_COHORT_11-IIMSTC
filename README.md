# Disaster Relief Allocation

## Overview

This project focuses on building a machine learning system to help prioritize emergency supply requests during disasters. The model analyzes disaster-related data and classifies relief requests into **Critical**, **Moderate**, and **Low** priority levels so that authorities can distribute resources efficiently.

The goal of this project is to support better disaster management by using data-driven decision-making for relief allocation.

---

## Problem Statement

During natural disasters such as floods, earthquakes, and cyclones, many regions request emergency supplies like food, water, medicine, and shelter. However, relief resources are limited and cannot be distributed everywhere at the same time.

Therefore, it becomes necessary to **prioritize requests based on urgency and severity of the disaster**. This project implements machine learning models that analyze disaster data and determine the **priority tier** for relief allocation.

---

## Objectives

* Develop a machine learning model to classify disaster relief requests.
* Categorize requests into **Critical, Moderate, and Low priority tiers**.
* Assist disaster management authorities in efficient resource distribution.
* Support faster decision-making during emergency situations.

---

## Dataset Description

The dataset used in this project contains information about disaster events and the conditions affecting relief distribution.

### Parameters Used in the Dataset

| Parameter         | Description                                                                                   |
| ----------------- | --------------------------------------------------------------------------------------------- |
| **iso3**          | A three-letter country code used internationally to identify countries (e.g., IND for India). |
| **country**       | Name of the country where the disaster occurred.                                              |
| **disaster_type** | Type of disaster such as Flood, Earthquake, Cyclone, or Fire.                                 |
| **year**          | The year in which the disaster occurred.                                                      |
| **deaths**        | Number of people who died due to the disaster, indicating severity.                           |
| **affected**      | Number of people affected or impacted by the disaster.                                        |
| **mng_cap**       | Management capacity or emergency response capability available in the affected region.        |
| **inventory**     | Amount of relief supplies available in nearby warehouses.                                     |
| **distance**      | Distance between the disaster area and the supply warehouse or relief center.                 |
| **priority_tier** | Target variable representing the urgency of relief allocation (Critical, Moderate, Low).      |

---

## Data Preprocessing

Before training the machine learning models, several preprocessing steps were performed:

* Cleaning the dataset
* Handling missing values
* Encoding categorical variables such as disaster type and country
* Normalizing or scaling numerical features
* Splitting the dataset into **training and testing sets**

These steps ensure that the dataset is suitable for machine learning algorithms.

---

## Feature Engineering

Feature engineering helps improve model performance by selecting and transforming relevant features.

Examples include:

* Analyzing disaster severity using **deaths and affected population**
* Considering **inventory levels** to understand supply availability
* Using **distance** to estimate logistical difficulty in delivering aid
* Evaluating **management capacity** to determine local response strength

These features help determine the urgency of disaster relief allocation.

---

## Machine Learning Models Implemented

The following machine learning models were implemented in this project:

### Decision Tree

Decision Tree models create rule-based structures that split data based on feature values. This model helps identify decision paths such as disaster severity and resource availability.

### Random Forest

Random Forest is an ensemble learning method that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

### Linear Regression

Linear Regression was used to analyze relationships between disaster impact factors and the priority level for relief allocation.

---

## Model Evaluation

The models were evaluated to determine how accurately they classify the priority level of disaster relief requests.

Evaluation methods include:

* Accuracy
* Precision
* Recall
* F1 Score

These metrics help measure the performance and reliability of each model.

---

## Results

After training and testing the models, their performance was compared to identify the model that provides the most accurate classification of disaster relief priority levels.

The model with the best evaluation performance can assist disaster response teams in prioritizing relief efforts effectively.

---

## Conclusion

This project demonstrates how machine learning techniques can support disaster management by automatically prioritizing relief requests. By analyzing disaster severity, population impact, resource availability, and logistics, the system can recommend which areas require immediate attention.

Such systems can help improve emergency response efficiency and ensure that limited resources are distributed where they are needed the most.

---


## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib

---
