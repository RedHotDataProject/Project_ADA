# Open Food Facts: The Carbon “Food-print” We Do Not Eat
<b> By Christopher Lang, Nina Tubau and Maxence Draguet </b> 

<b> Data Story Website: </b>https://redhotdataproject.github.io/Project_ADA/

## Abstract

Everything we do possess a certain carbon footprint, and our diet is of course no exception. From growing, farming, processing and packaging our food, energy and organic resources are consumed and released, which reflects in the emission of greenhouse gases, such as CO2. In this story, we explore the arcane of the food industry, such as its manufacturing, product composition and sales, and delve into its carbon emission as well as its nutrition standards of quality. Using the Open Food Facts dataset as well as Eaternity's, we present the carbon footprint repartition, starting on an understanding of the products, followed by the breakdown of production countries as well as point of sales and evaluating trends in diet composition, with a special focus on nutritionally high marked products in France and the UK. With this study, we want to provide a better understanding of the agri-food industry, and eventually help reducing carbon emissions by promoting a healthier product base for our consumption.

## Member Contributions

- Christopher: Problem formulation, cleansing the data tags, web crawler for online shops, categorization of food products, data visualisation, analysis and visualisation of manufacturer/ purchasing countries and carbon footprints, code maintenance. 

- Nina: Getting, cleansing, exploring and scraping Eaternity database, study and vizualisation of palm oil case study.

- Maxence: Problem formulation, writing the website, standardisation of country names, analysis of nutrition grade/mark/category and distribution over countries. 

## Research questions [Updated]
Part 1 - Production/manufacture impact:
> - [x] Which are the dominant global food producers and manufacturers? <b>Answered</b>
> - [ ] How is this distribution impacted when we consider neutral and large carbon footprint products? For instance, considering the specific case of palm oil, can we observe any trend in the number of products including this oil (assuming a strong dependence between date the product was added to the database and data the product was invented)?  <b>Not answered due to lack of information</b>
> - [x] Which countries use it the most for production? <b>Answered</b>


Part 2 - Good nutrition impact:
> Next, consider the case of France, for which a nutritional index is available (nutrition_grade_fr). 
> - [x] Has there been a surge in high graded products in the last years? <b>Answered</b>
> - [x] Where do these product come from and where are they manufactured? <b>Answered</b>
> - [x] What is the composition/category? <b>Answered</b>
> - [x] Where are these products sold? <b>Answered</b>
> - [x] Is there any link with price apparent? > <b>Answered</b>

Common sense would suggest most nutritionally-high graded products are organic (plant, fruit, vegetables, …) and are therefore not manufactured, thus having a small footprint. 

> - [x] Can we establish a meaningful correlation between these products and the carbon footprint or an estimated price (using another dataset or creating our own with web scraping)? <b>Answered</b>
> - [x] Are expansive and polluting products performing more poorly in the nutrition mark? <b>Answered</b>
> - [x] Is there a general correlation between high carbon footprint and price? <b>Answered</b>

## Dataset

For our data project, we are going to leverage on the [Open Food Facts](https://world.openfoodfacts.org/) dataset, a rich database on food items and their manufacturer, composition, carbon footprint and points of sale. Each data point is indexed by the product name and barcode, categorised into food type categories and various data entries additionally are assigned a carbon footprint and a Nutri Score (a grade from A to E reflecting their nutritional value).
We compare the food items based on their manufacturing and sales location and set the carbon footprints into relation. Furthermore, we are going to make the assumption that the timestamp, when the food item was added and modified, is a relevant indicator on the diet trend of people at that time. 
In order to enrich the dataset, we are going to crawl the online food shops for the actual price of products in the dataset, and approximate missing carbon footprints with the food items CO<sub>2</sub>-database provided by [Eaternity](http://www.eaternity.org/foodprint/database?fbclid=IwAR2OF0hWBCky6sBc79pzHo2QXKPUMJpDk-it2etXbGH-HbD1cje0Qd-EYPI). To harmonise the country names that appear in the purchase, manufacturing and originating places, we use the database provided by https://mledoze.github.io/countries/ . 

## List of internal milestones up until project milestone 2

Project roadmap until project milestone 2, November 25th:
- [x] Set up environment - Access the clusters and datasets, describe the statistics and properties of the data; 
- [x] Data cleansing - brush up the data, complete missing carbon footprints, extract suitable categories;
- [x] Enrich dataset with missing price information - implement and launch a web crawler for online food shops;
- [x] Present the data - visualise geographical patterns of production and sales of processed foods. 

## List of internal milestones up until project milestone 3
- [x] Aggregate carbon-footprints and product prices in categories.
- [x] Perform part of the analysis requiring the footprint.
- [x] Perform precise study on the high-nutritional index food products (may require to derive a personal index based on the content)
- [x] Make plots more appealing - Standardize colormaps, make maps and clusters plots interactive.
- [x] Write report


## Additional libraries used
conda install webdriver fuzzyset py-translate 


## Questions for TAs
Will you really enjoy your christmas knowing we have to study? 
