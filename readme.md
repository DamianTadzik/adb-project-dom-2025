

# Advanced Databases – Project Description
1. List of participants
Damian Brzana

Marek Janaszkiewicz

Oskar Brandys


2. Project concept
Our project aims to build a complete data collection, storage, and visualization system based on environmental air quality data. We will periodically fetch real-time measurement data from the OpenAQ API (v3), which provides information about air quality from thousands of cities and measurement stations around the world.

The collected data will be logged into a MySQL database hosted on the AGH University database infrastructure. Once the data is stored, we will build a web-based visualization system that allows users to analyze the data in three different statistical ways:

Time series analysis – displaying changes in air quality over time

Quantitative analysis – comparing average, min/max, and other statistical metrics across cities or pollutants

Spatial analysis – visualizing data geographically on a map with measurement station locations

Each analysis view will include at least five filtering options, such as:

Date range

Country

City

Type of pollutant (e.g. PM2.5, CO, NO₂)

Measurement unit

3. Data sources
We will use the official OpenAQ Platform API v3 as our primary data source. This API offers open access to real-time and historical air quality data from government and research stations across the globe.

Key endpoints we plan to use:

/measurements – for latest air quality data

/locations – to retrieve metadata about stations

/parameters – to get available pollutant types

Website: https://www.openaq.org/
API documentation: https://docs.openaq.org/

