# Open Food Facts: the carbon “food-print” we do not eat

## Abstract

Everything we do has a carbon footprint, and our diet is no exception. From growing, farming, processing and packaging our food, energy and organic resources are consumed and released, which reflects in the emission of greenhouse gases, like CO<sub>2</sub>. In our project, we analyse the processed foods industry - its manufacturing, product composition, and sales - for the main sources of carbon emissions, using the Open Food Facts dataset. We explain the carbon footprint repartition, starting on an understanding of the products, followed by the breakdown of production countries as well as point of sales and evaluating trends in diet composition, with a special focus on nutritionally high marked products in France and the UK. With this study, we want to provide a better understanding of the agri-food industry, and eventually help reducing carbon emissions.

## Research questions
Part 1 - Production/manufacture impact:
> Which are the dominant global food producers and manufacturers? How is this distribution impacted when we consider neutral and large carbon footprint products? For instance, considering the specific case of palm oil, can we observe any trend in the number of products including this oil (assuming a strong dependence between date the product was added to the database and data the product was invented)? Which countries use it the most for production?


Part 2 - Good nutrition impact:
> Next, consider the case of France/UK, for which a nutritional index is available (nutrition_grade_fr/nutrition_grade_uk). Has there been a surge in high graded products in the last years? Where do these product come from and where are they manufactured? What is the composition? Do they contain many additives?  Where are these products sold? 

> Common sense would suggest most nutritionally-high graded products are organic (plant, fruit, vegetables, …) and are therefore not manufactured, thus having a small footprint. Can we establish a meaningful correlation between these product and the carbon footprint  or an estimated price (using another dataset or creating our own with web scraping)? Are expansive and polluting products performing more poorly in the nutrition mark? Is there a general correlation between high carbon footprint and price? 

## Dataset

For our data project, we are going to leverage on the [Open Food Facts](https://world.openfoodfacts.org/) data set, a rich database on food items and their manufacturer, composition, carbon footprint, and points of sale. Each data point is indexed by the product name and barcode, categorised into food type categories and various data entries additionally are assigned a carbon footprint and a Nutri Score (a grade from A to E reflecting their nutritional value).
We compare the food items based on their manufacturing and sales location and set the carbon footprints into relation. Furthermore, we are going to make the assumption that the timestamp, when the food item was added and modified, is a relevant indicator on the diet trend of people at that time. 
In order to enrich the dataset, we are going to crawl the online food shops for the actual price of products in the dataset, and approximate missing carbon footprints with the food items CO<sub>2</sub>-database provided by [Eaternity](http://www.eaternity.org/foodprint/database?fbclid=IwAR2OF0hWBCky6sBc79pzHo2QXKPUMJpDk-it2etXbGH-HbD1cje0Qd-EYPI).

## A list of internal milestones up until project milestone 2

Project roadmap until project milestone 2, November 25th:
- [ ] Set up environment - Access the clusters and datasets, describe the statistics and properties of the data; 
- [ ] Data cleansing - brush up the data, complete missing carbon footprints, extract suitable categories;
- [ ] Enrich dataset with missing price information - implement and launch a web crawler for online food shops;
- [ ] Present the data - visualise geographical patterns of production and sales of processed foods. 


## Questions for TAs
- Is there a known database given consumption level of each product for a given country ? 
- Is there a more efficient way to get prices of products than doing web scraping? 



