
# Open Food Facts: the carbon “food-print” we do not eat

## Abstract
<i>Everything we do has a carbon footprint, and our diet is no exception. From growing, farming, processing and packaging our food, energy and organic resources are consumed and released, which reflects in the emission of greenhouse gases, like CO<sub>2</sub>. In our project, we analyze the processed foods industry - its manufacturing, product composition, and sales - for the main sources of carbon emissions, using the Open Food Facts dataset. We explain the carbon footprint repartition, starting on an understanding of the products, followed by the breakdown of production countries as well as point of sales and evaluating trends in diet composition, with a special focus on nutritionally high marked products in France and the UK. 

With this study, we want to provide a better understanding of the agri-food industry, and eventually help reducing carbon emissions.</i>

In this notebook, we are performingt the above analysis on the OpenFoodFacts database, which we pre-processed using the __Open Food Facts - Cleanse Data__ notebook in the main directory.

<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Abstract" data-toc-modified-id="Abstract-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Abstract</a></span></li><li><span><a href="#Import-cleansed-data" data-toc-modified-id="Import-cleansed-data-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Import cleansed data</a></span></li><li><span><a href="#Analyse-data" data-toc-modified-id="Analyse-data-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Analyse data</a></span><ul class="toc-item"><li><span><a href="#Production-/-manufacture-impact" data-toc-modified-id="Production-/-manufacture-impact-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Production / manufacture impact</a></span><ul class="toc-item"><li><span><a href="#Global-distribution-of-global-food-producers" data-toc-modified-id="Global-distribution-of-global-food-producers-3.1.1"><span class="toc-item-num">3.1.1&nbsp;&nbsp;</span>Global distribution of global food producers</a></span><ul class="toc-item"><li><span><a href="#Which-are-the-dominant-global-food-producers-and-manufacturers?" data-toc-modified-id="Which-are-the-dominant-global-food-producers-and-manufacturers?-3.1.1.1"><span class="toc-item-num">3.1.1.1&nbsp;&nbsp;</span>Which are the dominant global food producers and manufacturers?</a></span></li><li><span><a href="#How-is-this-distribution-impacted-when-we-consider-neutral-and-large-carbon-footprint-products?" data-toc-modified-id="How-is-this-distribution-impacted-when-we-consider-neutral-and-large-carbon-footprint-products?-3.1.1.2"><span class="toc-item-num">3.1.1.2&nbsp;&nbsp;</span>How is this distribution impacted when we consider neutral and large carbon footprint products?</a></span></li></ul></li><li><span><a href="#Case-study:-Palm-oil" data-toc-modified-id="Case-study:-Palm-oil-3.1.2"><span class="toc-item-num">3.1.2&nbsp;&nbsp;</span>Case study: Palm oil</a></span><ul class="toc-item"><li><span><a href="#Can-we-observe-any-trend-in-the-number-of-products-including-this-oil-(assuming-a-strong-dependence-between-date-the-product-was-added-to-the-database-and-data-the-product-was-invented)?" data-toc-modified-id="Can-we-observe-any-trend-in-the-number-of-products-including-this-oil-(assuming-a-strong-dependence-between-date-the-product-was-added-to-the-database-and-data-the-product-was-invented)?-3.1.2.1"><span class="toc-item-num">3.1.2.1&nbsp;&nbsp;</span>Can we observe any trend in the number of products including this oil (assuming a strong dependence between date the product was added to the database and data the product was invented)?</a></span></li><li><span><a href="#Which-country-use-palm-oils-for-production?" data-toc-modified-id="Which-country-use-palm-oils-for-production?-3.1.2.2"><span class="toc-item-num">3.1.2.2&nbsp;&nbsp;</span>Which country use palm oils for production?</a></span></li></ul></li></ul></li><li><span><a href="#Good-nutrition-impact" data-toc-modified-id="Good-nutrition-impact-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Good nutrition impact</a></span><ul class="toc-item"><li><span><a href="#High-nutrional-products" data-toc-modified-id="High-nutrional-products-3.2.1"><span class="toc-item-num">3.2.1&nbsp;&nbsp;</span>High-nutrional products</a></span><ul class="toc-item"><li><span><a href="#Has-there-been-a-surge-in-high-graded-Products-in-the-UK-/-France-over-the-past-years?" data-toc-modified-id="Has-there-been-a-surge-in-high-graded-Products-in-the-UK-/-France-over-the-past-years?-3.2.1.1"><span class="toc-item-num">3.2.1.1&nbsp;&nbsp;</span>Has there been a surge in high graded Products in the UK / France over the past years?</a></span></li></ul></li><li><span><a href="#High-nutrional-products" data-toc-modified-id="High-nutrional-products-3.2.2"><span class="toc-item-num">3.2.2&nbsp;&nbsp;</span>High-nutrional products</a></span><ul class="toc-item"><li><span><a href="#What-are-those-products-made-of?" data-toc-modified-id="What-are-those-products-made-of?-3.2.2.1"><span class="toc-item-num">3.2.2.1&nbsp;&nbsp;</span>What are those products made of?</a></span></li><li><span><a href="#Where-do-these-product-come-from-and-where-are-they-manufactured?" data-toc-modified-id="Where-do-these-product-come-from-and-where-are-they-manufactured?-3.2.2.2"><span class="toc-item-num">3.2.2.2&nbsp;&nbsp;</span>Where do these product come from and where are they manufactured?</a></span></li><li><span><a href="#Where-are-those-products-sold?" data-toc-modified-id="Where-are-those-products-sold?-3.2.2.3"><span class="toc-item-num">3.2.2.3&nbsp;&nbsp;</span>Where are those products sold?</a></span></li></ul></li><li><span><a href="#Carbon-footprint-of-nutrionally-high-graded-products" data-toc-modified-id="Carbon-footprint-of-nutrionally-high-graded-products-3.2.3"><span class="toc-item-num">3.2.3&nbsp;&nbsp;</span>Carbon footprint of nutrionally-high graded products</a></span><ul class="toc-item"><li><span><a href="#Is-there-a-general-correlation-between-high-carbon-footprint-and-price?" data-toc-modified-id="Is-there-a-general-correlation-between-high-carbon-footprint-and-price?-3.2.3.1"><span class="toc-item-num">3.2.3.1&nbsp;&nbsp;</span>Is there a general correlation between high carbon footprint and price?</a></span></li></ul></li></ul></li></ul></li></ul></div>


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium
from scipy import stats
from datetime import datetime

import json
import pickle

import os
import sys
nb_dir = os.path.split(os.getcwd())[0]
if nb_dir not in sys.path:
    sys.path.append(nb_dir)
    
%load_ext autoreload
%autoreload 2
    
import libs.exploring as explore
import libs.visualising as visualize
import libs.cleansing as cleanse

# Set up plotly environment
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
import plotly.tools as tls
init_notebook_mode(connected=True)
```


<script type="text/javascript">window.PlotlyConfig = {MathJaxConfig: 'local'};</script><script type="text/javascript">if (window.MathJax) {MathJax.Hub.Config({SVG: {font: "STIX-Web"}});}</script><script>requirejs.config({paths: { 'plotly': ['https://cdn.plot.ly/plotly-latest.min']},});if(!window._Plotly) {require(['plotly'],function(plotly) {window._Plotly=plotly;});}</script>



<script type="text/javascript">window.PlotlyConfig = {MathJaxConfig: 'local'};</script><script type="text/javascript">if (window.MathJax) {MathJax.Hub.Config({SVG: {font: "STIX-Web"}});}</script><script>requirejs.config({paths: { 'plotly': ['https://cdn.plot.ly/plotly-latest.min']},});if(!window._Plotly) {require(['plotly'],function(plotly) {window._Plotly=plotly;});}</script>


Command to import the link for the website


```python
tls.get_embed('https://plot.ly/~maxencedraguet/25/')
```




    '<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~maxencedraguet/25.embed" height="525" width="100%"></iframe>'



## Import cleansed data


```python
# Import data
open_food_facts_csv_file = "./data/openfoodfacts_clean.csv"

food_facts_pd = pd.read_csv(open_food_facts_csv_file,
                            delimiter="\t")
```


```python
# Change column data types
food_facts_pd['carbon-footprint_100g'] = food_facts_pd['carbon-footprint_100g'].apply(pd.to_numeric, args=('coerce',))
food_facts_pd['energy_100g'] = food_facts_pd['energy_100g'].apply(pd.to_numeric, args=('coerce',))
food_facts_pd['price_per_100g'] = food_facts_pd['price_per_100g'].apply(pd.to_numeric, args=('coerce',))
food_facts_pd['created_datetime'] = food_facts_pd['created_datetime'].apply(pd.to_datetime, args=('coerce',))
```


```python
food_facts_pd.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>code</th>
      <th>created_t</th>
      <th>created_datetime</th>
      <th>product_name</th>
      <th>quantity</th>
      <th>packaging</th>
      <th>brands</th>
      <th>categories_en</th>
      <th>origins</th>
      <th>...</th>
      <th>ingredients_text</th>
      <th>main_category</th>
      <th>energy_100g</th>
      <th>carbon-footprint_100g</th>
      <th>nutrition-score-fr_100g</th>
      <th>nutrition-score-uk_100g</th>
      <th>price_per_100g</th>
      <th>store_currency</th>
      <th>manufacturing_place</th>
      <th>purchase_places</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0000000274722</td>
      <td>1514659309</td>
      <td>2017-12-30 18:41:49</td>
      <td>Blanquette de Volaille et son Riz</td>
      <td>NaN</td>
      <td>carton,plastique</td>
      <td>Comme J’aime</td>
      <td>Meals,Meat-based products,Meals with meat,Poul...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Riz précuit 40,4 % (eau, riz, huile de colza, ...</td>
      <td>Meats</td>
      <td>450.0</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>France</td>
      <td>France</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0000000394710</td>
      <td>1484497370</td>
      <td>2017-01-15 16:22:50</td>
      <td>Danoises à la cannelle roulées</td>
      <td>1.150 kg</td>
      <td>Frais</td>
      <td>Kirkland Signature</td>
      <td>Sugary snacks,Biscuits and cakes,Pastries</td>
      <td>France</td>
      <td>...</td>
      <td>Ingrédients: Pâte (farine, eau, beurre, sucre,...</td>
      <td>Sugary snacks</td>
      <td>1520.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>France</td>
      <td>France</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>0000001071894</td>
      <td>1409411252</td>
      <td>2014-08-30 15:07:32</td>
      <td>Flute</td>
      <td>NaN</td>
      <td>Paper,plastic film</td>
      <td>Waitrose</td>
      <td>Plant-based foods and beverages,Plant-based fo...</td>
      <td>Canada</td>
      <td>...</td>
      <td>Wheat</td>
      <td>Plant-based</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Unknown</td>
      <td>Canada</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>0000001938067</td>
      <td>1484501528</td>
      <td>2017-01-15 17:32:08</td>
      <td>Chaussons tressés aux pommes</td>
      <td>1.200 kg</td>
      <td>Frais</td>
      <td>Kirkland Signature</td>
      <td>Sugary snacks,Biscuits and cakes,Pastries</td>
      <td>France</td>
      <td>...</td>
      <td>Ingrédients : Pâte (farine, margarines d'huile...</td>
      <td>Sugary snacks</td>
      <td>1090.0</td>
      <td>NaN</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>United Kingdom</td>
      <td>United Kingdom</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>0000004302544</td>
      <td>1488464896</td>
      <td>2017-03-02 14:28:16</td>
      <td>Pain Burger Artisan</td>
      <td>1.008 kg / 12 pain</td>
      <td>Frais,plastique</td>
      <td>Kirkland Signature</td>
      <td>boulange</td>
      <td>Canada</td>
      <td>...</td>
      <td>Ingrédients : Farine, eau, sel, levure, orge m...</td>
      <td>Boulange</td>
      <td>1160.0</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Unknown</td>
      <td>Canada</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 23 columns</p>
</div>



Additionally to the OpenFoodFact dataset, we obtained an extract of the Eaternity dataset hosted by the ETH Zurich, which contains 692 more products and their CO2 footprint. Unfortunately, these products are not contained in the OpenFoodFacts database, so we lack manufacturing and purchasing information as well as the OpenFoodFacts categories for this set.


```python
# Import data
carbon_footprint_csv_file = "./data/carbon_footprint_categories.csv"

carbon_footprint_pd = pd.read_csv(carbon_footprint_csv_file, delimiter=",")
carbon_footprint_pd.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 682 entries, 0 to 681
    Data columns (total 13 columns):
    Unnamed: 0                      682 non-null int64
    ID                              682 non-null int64
    Title                           682 non-null object
    Weight [gram/serving]           682 non-null int64
    CO2-Value [gram CO2/serving]    682 non-null float64
    CO2 rating                      682 non-null float64
    FAT                             682 non-null float64
    WATER                           682 non-null float64
    ENERC                           682 non-null float64
    PROT                            682 non-null float64
    category                        682 non-null object
    parent_category                 682 non-null object
    category_en                     682 non-null object
    dtypes: float64(6), int64(3), object(4)
    memory usage: 69.3+ KB



```python
carbon_footprint_pd.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>ID</th>
      <th>Title</th>
      <th>Weight [gram/serving]</th>
      <th>CO2-Value [gram CO2/serving]</th>
      <th>CO2 rating</th>
      <th>FAT</th>
      <th>WATER</th>
      <th>ENERC</th>
      <th>PROT</th>
      <th>category</th>
      <th>parent_category</th>
      <th>category_en</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>4300175162708</td>
      <td>K Classic - Junger Gemüsemais</td>
      <td>100</td>
      <td>9.0</td>
      <td>20.812</td>
      <td>3.480252</td>
      <td>52.999834</td>
      <td>765.655520</td>
      <td>8.601195</td>
      <td>Gemüsekonserven</td>
      <td>gemuese_pilze</td>
      <td>vegetable mushrooms</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>4388840231829</td>
      <td>ja! Gemüsemais</td>
      <td>100</td>
      <td>17.0</td>
      <td>37.941</td>
      <td>2.312597</td>
      <td>35.218431</td>
      <td>1070.401621</td>
      <td>5.715417</td>
      <td>Gemüsekonserven</td>
      <td>gemuese_pilze</td>
      <td>vegetable mushrooms</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>8690777653008</td>
      <td>Sera Ajvar</td>
      <td>100</td>
      <td>44.0</td>
      <td>61.076</td>
      <td>11.526800</td>
      <td>22.286400</td>
      <td>1276.524000</td>
      <td>12.058200</td>
      <td>Gemüsaufstriche &amp;amp; -salate</td>
      <td>gemuese_pilze</td>
      <td>vegetable mushrooms</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>4311527608225</td>
      <td>Edeka Ackergold Mehligkochend</td>
      <td>100</td>
      <td>11.0</td>
      <td>67.383</td>
      <td>0.100000</td>
      <td>78.700000</td>
      <td>320.000000</td>
      <td>2.000000</td>
      <td>Kartoffeln</td>
      <td>gemuese_pilze</td>
      <td>vegetable mushrooms</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>7610632971826</td>
      <td>Bio Kartoffeln festkochend</td>
      <td>100</td>
      <td>11.0</td>
      <td>67.383</td>
      <td>0.100000</td>
      <td>78.700000</td>
      <td>320.000000</td>
      <td>2.000000</td>
      <td>Kartoffeln</td>
      <td>gemuese_pilze</td>
      <td>vegetable mushrooms</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>4316268432429</td>
      <td>Botato Kartoffel Wedges</td>
      <td>100</td>
      <td>20.0</td>
      <td>71.343</td>
      <td>4.032246</td>
      <td>70.485923</td>
      <td>512.666890</td>
      <td>3.501101</td>
      <td>Kartoffelbeilagen &amp;amp; Pommes Frites</td>
      <td>gemuese_pilze</td>
      <td>vegetable mushrooms</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>4032600122055</td>
      <td>Pfanni Kartoffel Püree besonders locker 3 x 80 g</td>
      <td>100</td>
      <td>12.0</td>
      <td>73.344</td>
      <td>0.099000</td>
      <td>77.913000</td>
      <td>316.800000</td>
      <td>1.980000</td>
      <td>Kartoffelbeilagen &amp;amp; Pommes Frites</td>
      <td>gemuese_pilze</td>
      <td>vegetable mushrooms</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>4005009101204</td>
      <td>Kartoffelpüree</td>
      <td>100</td>
      <td>14.0</td>
      <td>82.441</td>
      <td>0.197999</td>
      <td>75.754800</td>
      <td>310.801700</td>
      <td>2.129955</td>
      <td>Knödel &amp;amp; Pürees</td>
      <td>gemuese_pilze</td>
      <td>vegetable mushrooms</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>4003880685257</td>
      <td>Agrarfrost Germany Knusper Frites</td>
      <td>100</td>
      <td>22.0</td>
      <td>84.098</td>
      <td>5.488000</td>
      <td>73.978000</td>
      <td>500.600000</td>
      <td>1.880000</td>
      <td>Kartoffelbeilagen &amp;amp; Pommes Frites</td>
      <td>gemuese_pilze</td>
      <td>vegetable mushrooms</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>4311596464074</td>
      <td>Backofen Rösti Ecken - aus Qualitätskartoffeln</td>
      <td>100</td>
      <td>23.0</td>
      <td>87.815</td>
      <td>5.393437</td>
      <td>72.587372</td>
      <td>488.711426</td>
      <td>1.947783</td>
      <td>Kartoffelbeilagen &amp;amp; Pommes Frites</td>
      <td>gemuese_pilze</td>
      <td>vegetable mushrooms</td>
    </tr>
  </tbody>
</table>
</div>



## Analyse data

Before we analyse the data, we have to some confesssions to make:

The data that we loaded into this notebook was already preprocessed in the "Open Food Facts - Cleanse data" notebook, that can be found in the same directory. In there we translated countries, labels, and categories and formatted and matched tags. However, we also droped more than 90% of the data set, because the data points were not complete for the purpose of our analysis.

OpenFoodFacts was initiated in France, and products sold in france are dominantly represented in this data set. Moreover, most of the products are sold in Europe or industrial nations, and we have no or only sparse data about the African, Asian, Australian, and South-american continent, which excludes the majority of the world population and especially the societes in Asia and Africa, that undergo the most decisive transformations at the moment.

Further, we only have qualitative data about the products, but no quantities that are produced and purchased world wide, hence we cannot provide a scale for all the insights that we gain throughout this notebook.

What we are trying to say is, that the data is under no circumstances representive to analyse the the research questions that we have posed. However, we will provide the methods to perform this analysis on this comprised dataset, and see what kind of insights we can already squeek out of it.

### Production / manufacture impact

#### Global distribution of global food producers


```python
countries_label = pd.read_csv("./data/country_lookup.csv")[['name', 'cca3']]     
```

##### Which are the dominant global food producers and manufacturers?

- From where are those products originating?


```python
visualize.plot_occurences_on_map(df=food_facts_pd, 
                                 column_key='origins',
                                 show_distances=False,
                                 title='Countries of origin for products')
```


<div id="fd18e856-186f-45e1-91ce-05c991aca31a" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("fd18e856-186f-45e1-91ce-05c991aca31a", [{"type": "choropleth", "locations": ["SEN", "GRL", "LTU", "VNM", "PRT", "TWN", "MAR", "TUR", "ZAF", "GLP", "NFK", "DZA", "SGP", "RWA", "CYP", "PYF", "PNG", "MKD", "REU", "JAM", "NOR", "SRB", "ROU", "MYS", "NER", "GEO", "UKR", "KOR", "GBR", "SYC", "ARG", "WSM", "NZL", "NAM", "AZE", "LUX", "HTI", "LSO", "UGA", "FRA", "ISR", "CHE", "FRO", "BGD", "LAO", "SLV", "CHL", "MEX", "TZA", "TGO", "DMA", "PAN", "NLD", "CAN", "GUF", "IND", "GRC", "CIV", "BGR", "PRY", "COM", "BIH", "BOL", "BES", "SWE", "NCL", "SVK", "USA", "LBN", "NPL", "ESP", "GHA", "BRB", "ECU", "BFA", "TTO", "IMN", "COL", "PER", "ETH", "VEN", "MTQ", "IDN", "BDI", "COD", "PHL", "NIC", "JPN", "MHL", "POL", "FIN", "KEN", "LKA", "THA", "SJM", "AUT", "SDN", "URY", "HKG", "BRA", "MDG", "DOM", "HND", "JEY", "MDA", "ISL", "AUS", "HUN", "IOT", "STP", "RUS", "DNK", "MMR", "GIN", "EGY", "PAK", "CUB", "CMR", "SVN", "BEL", "GTM", "DEU", "TUN", "IRN", "BLR", "UMI", "CHN", "EST", "ITA", "IRL", "GUY", "CRI", "HRV"], "z": [1.3862943611198906, 0.0, 1.3862943611198906, 4.2626798770413155, 3.5553480614894135, 3.295836866004329, 3.7612001156935624, 4.30406509320417, 3.9318256327243257, 1.3862943611198906, 0.6931471805599453, 2.70805020110221, 0.6931471805599453, 0.0, 1.3862943611198906, 2.302585092994046, 2.5649493574615367, 1.3862943611198906, 3.2188758248682006, 0.6931471805599453, 5.0106352940962555, 0.6931471805599453, 2.302585092994046, 1.3862943611198906, 2.3978952727983707, 1.3862943611198906, 0.6931471805599453, 2.302585092994046, 6.439350371100098, 0.6931471805599453, 4.477336814478207, 1.6094379124341003, 3.367295829986474, 0.0, 0.0, 0.6931471805599453, 1.6094379124341003, 0.0, 1.3862943611198906, 9.099297073182859, 2.0794415416798357, 4.189654742026425, 3.091042453358316, 0.6931471805599453, 1.0986122886681098, 1.0986122886681098, 3.9889840465642745, 5.484796933490655, 2.0794415416798357, 0.6931471805599453, 3.6888794541139363, 0.0, 4.74493212836325, 5.062595033026967, 0.0, 4.007333185232471, 4.454347296253507, 2.70805020110221, 1.9459101490553132, 2.8903717578961645, 0.0, 0.6931471805599453, 3.5553480614894135, 0.0, 2.302585092994046, 1.0986122886681098, 0.0, 5.752572638825633, 0.6931471805599453, 0.0, 6.214608098422191, 2.0794415416798357, 0.0, 3.7612001156935624, 0.6931471805599453, 1.3862943611198906, 0.0, 2.4849066497880004, 5.093750200806762, 1.6094379124341003, 2.302585092994046, 2.1972245773362196, 3.4657359027997265, 0.6931471805599453, 0.6931471805599453, 3.4657359027997265, 1.791759469228055, 3.1780538303479458, 0.6931471805599453, 3.7612001156935624, 1.0986122886681098, 2.302585092994046, 3.4011973816621555, 4.5217885770490405, 0.0, 3.332204510175204, 0.0, 2.995732273553991, 1.0986122886681098, 4.060443010546419, 4.454347296253507, 3.6635616461296463, 1.791759469228055, 0.0, 0.6931471805599453, 3.2188758248682006, 4.882801922586371, 2.70805020110221, 3.2188758248682006, 1.9459101490553132, 3.8501476017100584, 3.332204510175204, 0.0, 2.6390573296152584, 2.3978952727983707, 2.302585092994046, 2.3978952727983707, 2.0794415416798357, 1.3862943611198906, 4.955827057601261, 1.6094379124341003, 5.988961416889864, 2.995732273553991, 2.4849066497880004, 0.6931471805599453, 1.3862943611198906, 4.852030263919617, 1.0986122886681098, 5.968707559985366, 4.553876891600541, 0.6931471805599453, 2.70805020110221, 1.3862943611198906], "name": ["Senegal", "Greenland", "Lithuania", "Vietnam", "Portugal", "Taiwan", "Morocco", "Turkey", "South Africa", "Guadeloupe", "Norfolk Island", "Algeria", "Singapore", "Rwanda", "Cyprus", "French Polynesia", "Papua New Guinea", "Macedonia", "R\u00e9union", "Jamaica", "Norway", "Serbia", "Romania", "Malaysia", "Niger", "Georgia", "Ukraine", "South Korea", "United Kingdom", "Seychelles", "Argentina", "Samoa", "New Zealand", "Namibia", "Azerbaijan", "Luxembourg", "Haiti", "Lesotho", "Uganda", "France", "Israel", "Switzerland", "Faroe Islands", "Bangladesh", "Laos", "El Salvador", "Chile", "Mexico", "Tanzania", "Togo", "Dominica", "Panama", "Netherlands", "Canada", "French Guiana", "India", "Greece", "Ivory Coast", "Bulgaria", "Paraguay", "Comoros", "Bosnia and Herzegovina", "Bolivia", "Caribbean Netherlands", "Sweden", "New Caledonia", "Slovakia", "United States", "Lebanon", "Nepal", "Spain", "Ghana", "Barbados", "Ecuador", "Burkina Faso", "Trinidad and Tobago", "Isle of Man", "Colombia", "Peru", "Ethiopia", "Venezuela", "Martinique", "Indonesia", "Burundi", "DR Congo", "Philippines", "Nicaragua", "Japan", "Marshall Islands", "Poland", "Finland", "Kenya", "Sri Lanka", "Thailand", "Svalbard and Jan Mayen", "Austria", "Sudan", "Uruguay", "Hong Kong", "Brazil", "Madagascar", "Dominican Republic", "Honduras", "Jersey", "Moldova", "Iceland", "Australia", "Hungary", "British Indian Ocean Territory", "S\u00e3o Tom\u00e9 and Pr\u00edncipe", "Russia", "Denmark", "Myanmar", "Guinea", "Egypt", "Pakistan", "Cuba", "Cameroon", "Slovenia", "Belgium", "Guatemala", "Germany", "Tunisia", "Iran", "Belarus", "United States Minor Outlying Islands", "China", "Estonia", "Italy", "Ireland", "Guyana", "Costa Rica", "Croatia"], "autocolorscale": false, "reversescale": true, "colorbar": {"autotick": true, "title": "Counts [log10]"}}], {"title": "Countries of origin for products", "geo": {"projection": {"type": "Mercator"}, "showframe": false, "showcoastlines": true, "showland": true, "landcolor": "rgb(229, 229, 229)", "countrycolor": "rgb(255, 255, 255)", "coastlinecolor": "rgb(255, 255, 255)"}, "showlegend": false, "xaxis": {"fixedrange": true}, "yaxis": {"fixedrange": true}}, {"showLink": true, "linkText": "Export to plot.ly"})});</script><script type="text/javascript">window.addEventListener("resize", function(){window._Plotly.Plots.resize(document.getElementById("fd18e856-186f-45e1-91ce-05c991aca31a"));});</script>


Note that country in purple are  not assigned any value. 

- Where are those products manufactured?


```python
visualize.plot_occurences_on_map(df=food_facts_pd, 
                                 column_key='manufacturing_place',
                                 show_distances=False,
                                 title='Manufacturing countries of products')
```


<div id="7e9764a2-5e84-4c4d-9201-6d759b10c82a" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("7e9764a2-5e84-4c4d-9201-6d759b10c82a", [{"type": "choropleth", "locations": ["SEN", "LTU", "MAF", "VNM", "PRT", "TWN", "MAR", "TUR", "ZAF", "GLP", "NFK", "DZA", "SGP", "CYM", "CYP", "PYF", "PNG", "MKD", "REU", "NOR", "SRB", "ROU", "MYS", "NER", "GEO", "UKR", "MYT", "KOR", "GBR", "LIE", "SYC", "ARM", "ARG", "WSM", "NZL", "NAM", "AZE", "LUX", "FRA", "ISR", "CHE", "CPV", "BGD", "LAO", "SLV", "CHL", "CZE", "MEX", "SPM", "TZA", "TGO", "PAN", "NLD", "CAN", "GUF", "IND", "GRC", "CIV", "BGR", "BLM", "PRY", "MLT", "BIH", "SWZ", "BOL", "BES", "SWE", "NCL", "SVK", "USA", "LBN", "ESP", "GHA", "ECU", "COL", "PER", "ETH", "ALB", "VEN", "MTQ", "IDN", "PHL", "PRI", "JPN", "MHL", "POL", "FIN", "KEN", "LVA", "LKA", "GGY", "THA", "AUT", "URY", "MCO", "HKG", "BRA", "MDG", "DOM", "MDA", "BRN", "ISL", "AUS", "HUN", "KIR", "STP", "RUS", "DNK", "MMR", "PAK", "CUB", "CMR", "SVN", "BEL", "DEU", "TUN", "UMI", "IRN", "BLR", "CHN", "EST", "SAU", "ATF", "ITA", "IRL", "GUY", "CRI", "HRV", "MUS"], "z": [1.3862943611198906, 3.295836866004329, 0.0, 4.174387269895637, 4.74493212836325, 4.700480365792417, 4.727387818712341, 3.7612001156935624, 3.258096538021482, 2.9444389791664403, 2.9444389791664403, 2.302585092994046, 1.791759469228055, 0.6931471805599453, 1.9459101490553132, 2.5649493574615367, 0.6931471805599453, 2.1972245773362196, 3.9512437185814275, 2.5649493574615367, 3.044522437723423, 2.3978952727983707, 2.1972245773362196, 3.58351893845611, 2.0794415416798357, 1.9459101490553132, 1.6094379124341003, 2.302585092994046, 8.281470857895167, 1.6094379124341003, 2.3978952727983707, 1.791759469228055, 2.0794415416798357, 3.091042453358316, 2.5649493574615367, 0.6931471805599453, 0.0, 3.1780538303479458, 10.152571717850691, 2.9444389791664403, 5.41610040220442, 0.6931471805599453, 0.0, 0.6931471805599453, 0.0, 1.791759469228055, 3.1780538303479458, 5.159055299214529, 0.0, 0.0, 0.6931471805599453, 0.0, 6.089044875446846, 5.438079308923196, 2.3978952727983707, 3.091042453358316, 5.204006687076795, 2.1972245773362196, 3.4011973816621555, 0.0, 0.0, 0.0, 0.6931471805599453, 0.0, 4.634728988229636, 0.6931471805599453, 4.30406509320417, 1.6094379124341003, 1.9459101490553132, 6.129050210060545, 2.1972245773362196, 7.029087564149662, 2.0794415416798357, 2.4849066497880004, 1.791759469228055, 3.4657359027997265, 0.0, 0.0, 2.995732273553991, 2.70805020110221, 2.772588722239781, 3.4965075614664802, 0.6931471805599453, 4.394449154672439, 2.1972245773362196, 4.890349128221754, 2.1972245773362196, 2.6390573296152584, 1.9459101490553132, 3.367295829986474, 1.0986122886681098, 5.25227342804663, 4.532599493153256, 0.6931471805599453, 1.6094379124341003, 2.8903717578961645, 2.3978952727983707, 3.8066624897703196, 1.3862943611198906, 2.1972245773362196, 0.6931471805599453, 3.332204510175204, 4.882801922586371, 3.295836866004329, 0.6931471805599453, 0.6931471805599453, 5.351858133476067, 3.9889840465642745, 0.6931471805599453, 2.0794415416798357, 1.3862943611198906, 1.791759469228055, 2.5649493574615367, 7.221835825288449, 7.891330757661889, 3.4011973816621555, 3.4965075614664802, 4.0943445622221, 1.0986122886681098, 5.3230099791384085, 1.6094379124341003, 0.0, 2.0794415416798357, 7.224753405767971, 4.74493212836325, 0.0, 1.9459101490553132, 3.5263605246161616, 1.6094379124341003], "name": ["Senegal", "Lithuania", "Saint Martin", "Vietnam", "Portugal", "Taiwan", "Morocco", "Turkey", "South Africa", "Guadeloupe", "Norfolk Island", "Algeria", "Singapore", "Cayman Islands", "Cyprus", "French Polynesia", "Papua New Guinea", "Macedonia", "R\u00e9union", "Norway", "Serbia", "Romania", "Malaysia", "Niger", "Georgia", "Ukraine", "Mayotte", "South Korea", "United Kingdom", "Liechtenstein", "Seychelles", "Armenia", "Argentina", "Samoa", "New Zealand", "Namibia", "Azerbaijan", "Luxembourg", "France", "Israel", "Switzerland", "Cape Verde", "Bangladesh", "Laos", "El Salvador", "Chile", "Czechia", "Mexico", "Saint Pierre and Miquelon", "Tanzania", "Togo", "Panama", "Netherlands", "Canada", "French Guiana", "India", "Greece", "Ivory Coast", "Bulgaria", "Saint Barth\u00e9lemy", "Paraguay", "Malta", "Bosnia and Herzegovina", "Eswatini", "Bolivia", "Caribbean Netherlands", "Sweden", "New Caledonia", "Slovakia", "United States", "Lebanon", "Spain", "Ghana", "Ecuador", "Colombia", "Peru", "Ethiopia", "Albania", "Venezuela", "Martinique", "Indonesia", "Philippines", "Puerto Rico", "Japan", "Marshall Islands", "Poland", "Finland", "Kenya", "Latvia", "Sri Lanka", "Guernsey", "Thailand", "Austria", "Uruguay", "Monaco", "Hong Kong", "Brazil", "Madagascar", "Dominican Republic", "Moldova", "Brunei", "Iceland", "Australia", "Hungary", "Kiribati", "S\u00e3o Tom\u00e9 and Pr\u00edncipe", "Russia", "Denmark", "Myanmar", "Pakistan", "Cuba", "Cameroon", "Slovenia", "Belgium", "Germany", "Tunisia", "United States Minor Outlying Islands", "Iran", "Belarus", "China", "Estonia", "Saudi Arabia", "French Southern and Antarctic Lands", "Italy", "Ireland", "Guyana", "Costa Rica", "Croatia", "Mauritius"], "autocolorscale": false, "reversescale": true, "colorbar": {"autotick": true, "title": "Counts [log10]"}}], {"title": "Manufacturing countries of products", "geo": {"projection": {"type": "Mercator"}, "showframe": false, "showcoastlines": true, "showland": true, "landcolor": "rgb(229, 229, 229)", "countrycolor": "rgb(255, 255, 255)", "coastlinecolor": "rgb(255, 255, 255)"}, "showlegend": false, "xaxis": {"fixedrange": true}, "yaxis": {"fixedrange": true}}, {"showLink": true, "linkText": "Export to plot.ly"})});</script><script type="text/javascript">window.addEventListener("resize", function(){window._Plotly.Plots.resize(document.getElementById("7e9764a2-5e84-4c4d-9201-6d759b10c82a"));});</script>


- Where are those products bought?


```python
visualize.plot_occurences_on_map(df=food_facts_pd, 
                                 column_key='purchase_places',
                                 show_distances=False,
                                 title='Purchase countries of products')
```


<div id="f986f228-1ebb-46e6-8c77-4f71e078d61b" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("f986f228-1ebb-46e6-8c77-4f71e078d61b", [{"type": "choropleth", "locations": ["SEN", "LTU", "MAF", "PRT", "TWN", "AIA", "MAR", "TUR", "ZAF", "GLP", "DZA", "CYP", "PYF", "MKD", "REU", "MNE", "NOR", "KWT", "SRB", "ROU", "MYS", "GEO", "UKR", "MYT", "KOR", "GBR", "ARM", "ARG", "NZL", "LUX", "FRA", "VIR", "COG", "ISR", "CHE", "CHL", "CZE", "MEX", "SPM", "TGO", "NLD", "CAN", "GUF", "IND", "GRC", "CIV", "BGR", "MLT", "BIH", "SWE", "NCL", "SVK", "USA", "LBN", "ESP", "ECU", "BFA", "COL", "PER", "ALB", "MTQ", "IDN", "PHL", "JPN", "POL", "FIN", "ARE", "LVA", "LKA", "THA", "AUT", "URY", "MCO", "HKG", "BRA", "MDG", "DOM", "SXM", "MLI", "MDA", "ISL", "AUS", "HUN", "KNA", "OMN", "RUS", "DNK", "JOR", "MMR", "GIN", "EGY", "CUB", "CMR", "SVN", "BEL", "DEU", "TUN", "CHN", "EST", "SAU", "KAZ", "ITA", "GAB", "IRL", "CRI", "HRV", "MUS"], "z": [1.9459101490553132, 1.0986122886681098, 0.0, 4.90527477843843, 2.9444389791664403, 0.0, 2.4849066497880004, 1.9459101490553132, 2.1972245773362196, 4.0943445622221, 1.9459101490553132, 0.0, 4.418840607796598, 0.6931471805599453, 4.430816798843313, 1.6094379124341003, 1.9459101490553132, 0.0, 4.624972813284271, 4.30406509320417, 1.0986122886681098, 2.3978952727983707, 1.0986122886681098, 0.0, 1.0986122886681098, 7.326465613840322, 0.0, 1.0986122886681098, 1.9459101490553132, 3.332204510175204, 10.463531820089617, 0.0, 0.6931471805599453, 1.6094379124341003, 6.606650186198215, 0.6931471805599453, 2.6390573296152584, 6.255750041753367, 2.0794415416798357, 0.0, 4.787491742782046, 5.820082930352362, 2.70805020110221, 1.6094379124341003, 3.5263605246161616, 0.0, 2.70805020110221, 0.0, 1.0986122886681098, 5.030437921392435, 2.3978952727983707, 0.6931471805599453, 6.220590170099739, 1.0986122886681098, 7.138866999945524, 0.0, 0.6931471805599453, 1.3862943611198906, 0.6931471805599453, 0.6931471805599453, 3.1780538303479458, 1.0986122886681098, 2.1972245773362196, 3.091042453358316, 2.6390573296152584, 2.995732273553991, 1.6094379124341003, 1.6094379124341003, 0.0, 0.6931471805599453, 3.7612001156935624, 0.0, 1.3862943611198906, 3.258096538021482, 0.6931471805599453, 3.784189633918261, 0.0, 0.0, 0.6931471805599453, 1.0986122886681098, 0.6931471805599453, 5.8289456176102075, 3.295836866004329, 1.0986122886681098, 0.0, 5.5134287461649825, 4.204692619390966, 0.0, 0.0, 0.0, 0.0, 1.3862943611198906, 1.0986122886681098, 1.9459101490553132, 6.720220155135295, 7.620214770574455, 1.6094379124341003, 1.9459101490553132, 1.791759469228055, 0.0, 0.0, 4.382026634673881, 0.0, 4.543294782270004, 0.6931471805599453, 1.3862943611198906, 1.6094379124341003], "name": ["Senegal", "Lithuania", "Saint Martin", "Portugal", "Taiwan", "Anguilla", "Morocco", "Turkey", "South Africa", "Guadeloupe", "Algeria", "Cyprus", "French Polynesia", "Macedonia", "R\u00e9union", "Montenegro", "Norway", "Kuwait", "Serbia", "Romania", "Malaysia", "Georgia", "Ukraine", "Mayotte", "South Korea", "United Kingdom", "Armenia", "Argentina", "New Zealand", "Luxembourg", "France", "United States Virgin Islands", "Republic of the Congo", "Israel", "Switzerland", "Chile", "Czechia", "Mexico", "Saint Pierre and Miquelon", "Togo", "Netherlands", "Canada", "French Guiana", "India", "Greece", "Ivory Coast", "Bulgaria", "Malta", "Bosnia and Herzegovina", "Sweden", "New Caledonia", "Slovakia", "United States", "Lebanon", "Spain", "Ecuador", "Burkina Faso", "Colombia", "Peru", "Albania", "Martinique", "Indonesia", "Philippines", "Japan", "Poland", "Finland", "United Arab Emirates", "Latvia", "Sri Lanka", "Thailand", "Austria", "Uruguay", "Monaco", "Hong Kong", "Brazil", "Madagascar", "Dominican Republic", "Sint Maarten", "Mali", "Moldova", "Iceland", "Australia", "Hungary", "Saint Kitts and Nevis", "Oman", "Russia", "Denmark", "Jordan", "Myanmar", "Guinea", "Egypt", "Cuba", "Cameroon", "Slovenia", "Belgium", "Germany", "Tunisia", "China", "Estonia", "Saudi Arabia", "Kazakhstan", "Italy", "Gabon", "Ireland", "Costa Rica", "Croatia", "Mauritius"], "autocolorscale": false, "reversescale": true, "colorbar": {"autotick": true, "title": "Counts [log10]"}}], {"title": "Purchase countries of products", "geo": {"projection": {"type": "Mercator"}, "showframe": false, "showcoastlines": true, "showland": true, "landcolor": "rgb(229, 229, 229)", "countrycolor": "rgb(255, 255, 255)", "coastlinecolor": "rgb(255, 255, 255)"}, "showlegend": false, "xaxis": {"fixedrange": true}, "yaxis": {"fixedrange": true}}, {"showLink": true, "linkText": "Export to plot.ly"})});</script><script type="text/javascript">window.addEventListener("resize", function(){window._Plotly.Plots.resize(document.getElementById("f986f228-1ebb-46e6-8c77-4f71e078d61b"));});</script>


In conclusion, we note that we mainly have data for "western" countries, with a <b> huge bias toward France</b>. We mostly lack information for country in Africa and the centre of Asia. Our dataset is thus clearly not a truthful representation of the world. We shall therefore restrict our analysis to the case of France, meaning purchases countries will be limited to the case of France. [This category was selected since it is the most furnished one.] 

This is carried out in the next cell. Note that <i> purchases_places </i> is only requested to contain 'France' as one of the entries in its list. There could thus be other countries still contained in the <i> purchases_places </i> column. 


```python
food_facts_pd['filter'] = food_facts_pd.purchase_places.apply(lambda l: explore.filter_france(l))
food_facts_pd = food_facts_pd[food_facts_pd['filter'] == 'France'].drop(columns=['filter'])
```

##### How is this distribution impacted when we consider neutral and large carbon footprint products? 


```python
# dataset carbon footprint coming from Eaternity
# This will be assess in future version of this project

```

#### Case study: Palm oil

##### Can we observe any trend in the number of products including this oil (assuming a strong dependence between date the product was added to the database and data the product was invented)?


```python
#extracting products with palm oil 
palm_oil_pd = food_facts_pd[food_facts_pd.ingredients_text.str.contains("palm").fillna(value=False)]
```


```python
print('{0:.2f} % of the products in the dataset contain palm oil'.format(palm_oil_pd.shape[0]/food_facts_pd.shape[0]*100))
```

    5.01 % of the products in the dataset contain palm oil



```python
#palm_oil_pd.groupby('main_category')
palm_oil_pd['created_yyyy'] = palm_oil_pd["created_datetime"].dt.year
```

    /home/kingkolibri/Programs/anaconda3/lib/python3.6/site-packages/ipykernel_launcher.py:2: SettingWithCopyWarning:
    
    
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
    



```python
#plotly.tools.set_credentials_file(username='ninatubau', api_key='z75HqORQkKdVL98Fi0tX')

```


```python
palm_oil_over_time = palm_oil_pd['created_yyyy'].value_counts()
```


```python
data = [go.Bar(x=palm_oil_over_time.index,
            y=palm_oil_over_time.values)]

layout = go.Layout(
    title='Usage of palm oil over time',
    xaxis=dict(
        title='time (years)',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='number of products with palm oil',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
fig = go.Figure(data=data, layout=layout)

iplot(fig, filename='jupyter-basic_bar')
```


<div id="5ab1d67a-45cc-442d-94f0-0e5d64d1ee60" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("5ab1d67a-45cc-442d-94f0-0e5d64d1ee60", [{"x": [2015, 2016, 2017, 2018, 2013, 2014, 2012], "y": [428, 349, 276, 217, 149, 144, 46], "type": "bar", "uid": "14db1f53-6fd8-43c5-9a3a-abc66ec65e4a"}], {"title": "Usage of palm oil over time", "xaxis": {"title": "time (years)", "titlefont": {"color": "#7f7f7f", "family": "Courier New, monospace", "size": 18}}, "yaxis": {"title": "number of products with palm oil", "titlefont": {"color": "#7f7f7f", "family": "Courier New, monospace", "size": 18}}}, {"showLink": true, "linkText": "Export to plot.ly"})});</script><script type="text/javascript">window.addEventListener("resize", function(){window._Plotly.Plots.resize(document.getElementById("5ab1d67a-45cc-442d-94f0-0e5d64d1ee60"));});</script>


There is a clear tendancy of using palm oil in products from 2012 up to now. Also, we notice a large increase in the palm oil products these lasts years. 

##### Which country use palm oils for production?


```python
a = palm_oil_pd.origins.groupby(palm_oil_pd.origins).sum
```


```python
visualize.plot_column_composition(palm_oil_pd, 'manufacturing_place' );
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>United Kingdom</td>
      <td>156.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Unknown</td>
      <td>127.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Italy</td>
      <td>70.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Germany</td>
      <td>54.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Belgium</td>
      <td>33.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Spain</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Netherlands</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Switzerland</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>China</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Greece</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Poland</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Vietnam</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Thailand</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Portugal</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Ireland</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Sri Lanka</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Bolivia</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Japan</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Niger</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>42</th>
      <td>French Guiana</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Réunion</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Algeria</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Cyprus</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Peru</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>United States</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Norway</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Denmark</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Taiwan</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Luxembourg</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Kenya</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Turkey</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Philippines</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>South Africa</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Namibia</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Samoa</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Canada</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Iceland</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Venezuela</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Sweden</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Mauritius</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Slovakia</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Moldova</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Iran</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Austria</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Laos</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Unknown</td>
      <td>127.0</td>
    </tr>
  </tbody>
</table>
</div>



<div id="ecb76893-68b6-4959-8c59-d6b55dcbde00" style="height: 300px; width: 800px;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("ecb76893-68b6-4959-8c59-d6b55dcbde00", [{"marker": {"color": "#F4B5A6", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "United Kingdom", "orientation": "h", "x": [156.0], "y": [0], "type": "bar", "uid": "5faa7d06-1e67-44e9-88e9-2faff45a2571"}, {"marker": {"color": "#F4EBA6", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Unknown", "orientation": "h", "x": [127.0], "y": [0], "type": "bar", "uid": "4010ef5f-3d18-4def-888a-7a77bf694a24"}, {"marker": {"color": "#B2F4A6", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Italy", "orientation": "h", "x": [70.0], "y": [0], "type": "bar", "uid": "e3f99489-4387-49f8-8d2e-8a4f602a0c13"}, {"marker": {"color": "#A6E3F4", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Germany", "orientation": "h", "x": [54.0], "y": [0], "type": "bar", "uid": "371411f5-6014-4a8b-8608-008c94926084"}, {"marker": {"color": "#C4A6F4", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Belgium", "orientation": "h", "x": [33.0], "y": [0], "type": "bar", "uid": "f4ee4f2c-917b-435e-9e01-4c10e66319f6"}, {"marker": {"color": "#E0DBDD", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Others", "orientation": "h", "x": [241.0], "y": [0], "type": "bar", "uid": "03603180-ac0a-4fcf-be5b-7f82ab6beafa"}], {"barmode": "stack", "height": 300, "showlegend": true, "title": "manufacturing_place", "width": 800, "xaxis": {"tickvals": [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 681.0]}, "yaxis": {"showgrid": false, "showline": false, "showticklabels": false, "zeroline": false}}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>



```python
visualize.plot_occurences_on_map(df=food_facts_pd, 
                                 column_key='manufacturing_place',
                                 show_distances=True,
                                 title='Manufacturing countries of products')
```


<div id="40abff9f-a6e7-42ae-b043-385f608ad0ee" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("40abff9f-a6e7-42ae-b043-385f608ad0ee", [{"type": "choropleth", "locations": ["SEN", "LTU", "MAF", "VNM", "PRT", "TWN", "MAR", "TUR", "ZAF", "GLP", "DZA", "SGP", "CYM", "CYP", "PYF", "PNG", "MKD", "REU", "NOR", "SRB", "ROU", "MYS", "NER", "MYT", "UKR", "KOR", "GBR", "LIE", "SYC", "ARM", "ARG", "WSM", "NZL", "NAM", "LUX", "FRA", "ISR", "CHE", "LAO", "SLV", "CHL", "CZE", "MEX", "TGO", "NLD", "CAN", "GUF", "IND", "GRC", "CIV", "BGR", "BLM", "PRY", "SWZ", "BOL", "SWE", "NCL", "SVK", "USA", "LBN", "ESP", "GHA", "ECU", "COL", "PER", "VEN", "MTQ", "IDN", "PHL", "PRI", "JPN", "POL", "FIN", "KEN", "LVA", "LKA", "GGY", "THA", "AUT", "URY", "MCO", "HKG", "BRA", "MDG", "DOM", "MDA", "ISL", "AUS", "HUN", "STP", "RUS", "DNK", "MMR", "CMR", "BEL", "SVN", "DEU", "TUN", "IRN", "UMI", "CHN", "EST", "SAU", "ATF", "ITA", "IRL", "CRI", "HRV", "MUS"], "z": [0.6931471805599453, 2.9444389791664403, 0.0, 4.060443010546419, 4.174387269895637, 4.30406509320417, 4.564348191467836, 3.332204510175204, 1.791759469228055, 2.0794415416798357, 2.1972245773362196, 1.0986122886681098, 0.6931471805599453, 0.6931471805599453, 0.0, 0.0, 0.0, 2.772588722239781, 2.3978952727983707, 0.6931471805599453, 1.0986122886681098, 1.6094379124341003, 3.5553480614894135, 1.6094379124341003, 0.0, 1.0986122886681098, 7.957527402230773, 0.0, 1.791759469228055, 1.6094379124341003, 0.6931471805599453, 3.044522437723423, 0.6931471805599453, 0.6931471805599453, 2.9444389791664403, 10.107774429000033, 2.1972245773362196, 4.9344739331306915, 0.6931471805599453, 0.0, 1.0986122886681098, 2.4849066497880004, 1.791759469228055, 0.0, 5.7430031878094825, 3.6375861597263857, 2.0794415416798357, 0.0, 4.709530201312334, 1.9459101490553132, 2.1972245773362196, 0.0, 0.0, 0.0, 4.543294782270004, 3.4339872044851463, 1.3862943611198906, 1.0986122886681098, 4.406719247264253, 1.0986122886681098, 6.220590170099739, 1.9459101490553132, 1.791759469228055, 0.0, 2.833213344056216, 2.4849066497880004, 2.0794415416798357, 1.6094379124341003, 2.3978952727983707, 0.0, 3.8501476017100584, 4.553876891600541, 0.6931471805599453, 2.0794415416798357, 0.6931471805599453, 3.091042453358316, 1.0986122886681098, 4.634728988229636, 3.4011973816621555, 0.0, 1.3862943611198906, 1.0986122886681098, 1.3862943611198906, 1.6094379124341003, 0.6931471805599453, 0.6931471805599453, 3.295836866004329, 0.6931471805599453, 2.302585092994046, 0.0, 1.791759469228055, 3.258096538021482, 0.0, 1.0986122886681098, 6.80903930604298, 1.6094379124341003, 6.7580945044277305, 2.8903717578961645, 4.02535169073515, 3.2188758248682006, 4.795790545596741, 0.6931471805599453, 0.0, 2.0794415416798357, 6.9782137426306985, 3.4011973816621555, 0.6931471805599453, 1.3862943611198906, 1.6094379124341003], "name": ["Senegal", "Lithuania", "Saint Martin", "Vietnam", "Portugal", "Taiwan", "Morocco", "Turkey", "South Africa", "Guadeloupe", "Algeria", "Singapore", "Cayman Islands", "Cyprus", "French Polynesia", "Papua New Guinea", "Macedonia", "R\u00e9union", "Norway", "Serbia", "Romania", "Malaysia", "Niger", "Mayotte", "Ukraine", "South Korea", "United Kingdom", "Liechtenstein", "Seychelles", "Armenia", "Argentina", "Samoa", "New Zealand", "Namibia", "Luxembourg", "France", "Israel", "Switzerland", "Laos", "El Salvador", "Chile", "Czechia", "Mexico", "Togo", "Netherlands", "Canada", "French Guiana", "India", "Greece", "Ivory Coast", "Bulgaria", "Saint Barth\u00e9lemy", "Paraguay", "Eswatini", "Bolivia", "Sweden", "New Caledonia", "Slovakia", "United States", "Lebanon", "Spain", "Ghana", "Ecuador", "Colombia", "Peru", "Venezuela", "Martinique", "Indonesia", "Philippines", "Puerto Rico", "Japan", "Poland", "Finland", "Kenya", "Latvia", "Sri Lanka", "Guernsey", "Thailand", "Austria", "Uruguay", "Monaco", "Hong Kong", "Brazil", "Madagascar", "Dominican Republic", "Moldova", "Iceland", "Australia", "Hungary", "S\u00e3o Tom\u00e9 and Pr\u00edncipe", "Russia", "Denmark", "Myanmar", "Cameroon", "Belgium", "Slovenia", "Germany", "Tunisia", "Iran", "United States Minor Outlying Islands", "China", "Estonia", "Saudi Arabia", "French Southern and Antarctic Lands", "Italy", "Ireland", "Costa Rica", "Croatia", "Mauritius"], "autocolorscale": false, "reversescale": true, "colorbar": {"autotick": true, "title": "Counts [log10]"}}, {"type": "scattergeo", "lon": [-14, 2], "lat": [14, 46], "mode": "lines+marker", "name": "Senegal", "line": {"width": 0.34657359027997264, "color": "red"}}, {"type": "scattergeo", "lon": [24, 2], "lat": [56, 46], "mode": "lines+marker", "name": "Lithuania", "line": {"width": 1.4722194895832201, "color": "red"}}, {"type": "scattergeo", "lon": [-63.95, 2], "lat": [18.08333333, 46], "mode": "lines+marker", "name": "Saint Martin", "line": {"width": 0.0, "color": "red"}}, {"type": "scattergeo", "lon": [107.83333333, 2], "lat": [16.16666666, 46], "mode": "lines+marker", "name": "Vietnam", "line": {"width": 2.0302215052732095, "color": "red"}}, {"type": "scattergeo", "lon": [-8, 2], "lat": [39.5, 46], "mode": "lines+marker", "name": "Portugal", "line": {"width": 2.0871936349478184, "color": "red"}}, {"type": "scattergeo", "lon": [121, 2], "lat": [23.5, 46], "mode": "lines+marker", "name": "Taiwan", "line": {"width": 2.152032546602085, "color": "red"}}, {"type": "scattergeo", "lon": [-5, 2], "lat": [32, 46], "mode": "lines+marker", "name": "Morocco", "line": {"width": 2.282174095733918, "color": "red"}}, {"type": "scattergeo", "lon": [35, 2], "lat": [39, 46], "mode": "lines+marker", "name": "Turkey", "line": {"width": 1.666102255087602, "color": "red"}}, {"type": "scattergeo", "lon": [24, 2], "lat": [-29, 46], "mode": "lines+marker", "name": "South Africa", "line": {"width": 0.8958797346140275, "color": "red"}}, {"type": "scattergeo", "lon": [-61.583333, 2], "lat": [16.25, 46], "mode": "lines+marker", "name": "Guadeloupe", "line": {"width": 1.0397207708399179, "color": "red"}}, {"type": "scattergeo", "lon": [3, 2], "lat": [28, 46], "mode": "lines+marker", "name": "Algeria", "line": {"width": 1.0986122886681098, "color": "red"}}, {"type": "scattergeo", "lon": [103.8, 2], "lat": [1.36666666, 46], "mode": "lines+marker", "name": "Singapore", "line": {"width": 0.5493061443340549, "color": "red"}}, {"type": "scattergeo", "lon": [-80.5, 2], "lat": [19.5, 46], "mode": "lines+marker", "name": "Cayman Islands", "line": {"width": 0.34657359027997264, "color": "red"}}, {"type": "scattergeo", "lon": [33, 2], "lat": [35, 46], "mode": "lines+marker", "name": "Cyprus", "line": {"width": 0.34657359027997264, "color": "red"}}, {"type": "scattergeo", "lon": [-140, 2], "lat": [-15, 46], "mode": "lines+marker", "name": "French Polynesia", "line": {"width": 0.0, "color": "red"}}, {"type": "scattergeo", "lon": [147, 2], "lat": [-6, 46], "mode": "lines+marker", "name": "Papua New Guinea", "line": {"width": 0.0, "color": "red"}}, {"type": "scattergeo", "lon": [22, 2], "lat": [41.83333333, 46], "mode": "lines+marker", "name": "Macedonia", "line": {"width": 0.0, "color": "red"}}, {"type": "scattergeo", "lon": [55.5, 2], "lat": [-21.15, 46], "mode": "lines+marker", "name": "R\u00e9union", "line": {"width": 1.3862943611198906, "color": "red"}}, {"type": "scattergeo", "lon": [10, 2], "lat": [62, 46], "mode": "lines+marker", "name": "Norway", "line": {"width": 1.1989476363991853, "color": "red"}}, {"type": "scattergeo", "lon": [21, 2], "lat": [44, 46], "mode": "lines+marker", "name": "Serbia", "line": {"width": 0.34657359027997264, "color": "red"}}, {"type": "scattergeo", "lon": [25, 2], "lat": [46, 46], "mode": "lines+marker", "name": "Romania", "line": {"width": 0.5493061443340549, "color": "red"}}, {"type": "scattergeo", "lon": [112.5, 2], "lat": [2.5, 46], "mode": "lines+marker", "name": "Malaysia", "line": {"width": 0.8047189562170501, "color": "red"}}, {"type": "scattergeo", "lon": [8, 2], "lat": [16, 46], "mode": "lines+marker", "name": "Niger", "line": {"width": 1.7776740307447068, "color": "red"}}, {"type": "scattergeo", "lon": [45.16666666, 2], "lat": [-12.83333333, 46], "mode": "lines+marker", "name": "Mayotte", "line": {"width": 0.8047189562170501, "color": "red"}}, {"type": "scattergeo", "lon": [32, 2], "lat": [49, 46], "mode": "lines+marker", "name": "Ukraine", "line": {"width": 0.0, "color": "red"}}, {"type": "scattergeo", "lon": [127.5, 2], "lat": [37, 46], "mode": "lines+marker", "name": "South Korea", "line": {"width": 0.5493061443340549, "color": "red"}}, {"type": "scattergeo", "lon": [-2, 2], "lat": [54, 46], "mode": "lines+marker", "name": "United Kingdom", "line": {"width": 3.9787637011153865, "color": "red"}}, {"type": "scattergeo", "lon": [9.53333333, 2], "lat": [47.26666666, 46], "mode": "lines+marker", "name": "Liechtenstein", "line": {"width": 0.0, "color": "red"}}, {"type": "scattergeo", "lon": [55.66666666, 2], "lat": [-4.58333333, 46], "mode": "lines+marker", "name": "Seychelles", "line": {"width": 0.8958797346140275, "color": "red"}}, {"type": "scattergeo", "lon": [45, 2], "lat": [40, 46], "mode": "lines+marker", "name": "Armenia", "line": {"width": 0.8047189562170501, "color": "red"}}, {"type": "scattergeo", "lon": [-64, 2], "lat": [-34, 46], "mode": "lines+marker", "name": "Argentina", "line": {"width": 0.34657359027997264, "color": "red"}}, {"type": "scattergeo", "lon": [-172.33333333, 2], "lat": [-13.58333333, 46], "mode": "lines+marker", "name": "Samoa", "line": {"width": 1.5222612188617115, "color": "red"}}, {"type": "scattergeo", "lon": [174, 2], "lat": [-41, 46], "mode": "lines+marker", "name": "New Zealand", "line": {"width": 0.34657359027997264, "color": "red"}}, {"type": "scattergeo", "lon": [17, 2], "lat": [-22, 46], "mode": "lines+marker", "name": "Namibia", "line": {"width": 0.34657359027997264, "color": "red"}}, {"type": "scattergeo", "lon": [6.16666666, 2], "lat": [49.75, 46], "mode": "lines+marker", "name": "Luxembourg", "line": {"width": 1.4722194895832201, "color": "red"}}, {"type": "scattergeo", "lon": [2, 2], "lat": [46, 46], "mode": "lines+marker", "name": "France", "line": {"width": 5.053887214500016, "color": "red"}}, {"type": "scattergeo", "lon": [35.13, 2], "lat": [31.47, 46], "mode": "lines+marker", "name": "Israel", "line": {"width": 1.0986122886681098, "color": "red"}}, {"type": "scattergeo", "lon": [8, 2], "lat": [47, 46], "mode": "lines+marker", "name": "Switzerland", "line": {"width": 2.4672369665653457, "color": "red"}}, {"type": "scattergeo", "lon": [105, 2], "lat": [18, 46], "mode": "lines+marker", "name": "Laos", "line": {"width": 0.34657359027997264, "color": "red"}}, {"type": "scattergeo", "lon": [-88.91666666, 2], "lat": [13.83333333, 46], "mode": "lines+marker", "name": "El Salvador", "line": {"width": 0.0, "color": "red"}}, {"type": "scattergeo", "lon": [-71, 2], "lat": [-30, 46], "mode": "lines+marker", "name": "Chile", "line": {"width": 0.5493061443340549, "color": "red"}}, {"type": "scattergeo", "lon": [15.5, 2], "lat": [49.75, 46], "mode": "lines+marker", "name": "Czechia", "line": {"width": 1.2424533248940002, "color": "red"}}, {"type": "scattergeo", "lon": [-102, 2], "lat": [23, 46], "mode": "lines+marker", "name": "Mexico", "line": {"width": 0.8958797346140275, "color": "red"}}, {"type": "scattergeo", "lon": [1.16666666, 2], "lat": [8, 46], "mode": "lines+marker", "name": "Togo", "line": {"width": 0.0, "color": "red"}}, {"type": "scattergeo", "lon": [5.75, 2], "lat": [52.5, 46], "mode": "lines+marker", "name": "Netherlands", "line": {"width": 2.8715015939047412, "color": "red"}}, {"type": "scattergeo", "lon": [-95, 2], "lat": [60, 46], "mode": "lines+marker", "name": "Canada", "line": {"width": 1.8187930798631928, "color": "red"}}, {"type": "scattergeo", "lon": [-53, 2], "lat": [4, 46], "mode": "lines+marker", "name": "French Guiana", "line": {"width": 1.0397207708399179, "color": "red"}}, {"type": "scattergeo", "lon": [77, 2], "lat": [20, 46], "mode": "lines+marker", "name": "India", "line": {"width": 0.0, "color": "red"}}, {"type": "scattergeo", "lon": [22, 2], "lat": [39, 46], "mode": "lines+marker", "name": "Greece", "line": {"width": 2.354765100656167, "color": "red"}}, {"type": "scattergeo", "lon": [-5, 2], "lat": [8, 46], "mode": "lines+marker", "name": "Ivory Coast", "line": {"width": 0.9729550745276566, "color": "red"}}, {"type": "scattergeo", "lon": [25, 2], "lat": [43, 46], "mode": "lines+marker", "name": "Bulgaria", "line": {"width": 1.0986122886681098, "color": "red"}}, {"type": "scattergeo", "lon": [-63.41666666, 2], "lat": [18.5, 46], "mode": "lines+marker", "name": "Saint Barth\u00e9lemy", "line": {"width": 0.0, "color": "red"}}, {"type": "scattergeo", "lon": [-58, 2], "lat": [-23, 46], "mode": "lines+marker", "name": "Paraguay", "line": {"width": 0.0, "color": "red"}}, {"type": "scattergeo", "lon": [31.5, 2], "lat": [-26.5, 46], "mode": "lines+marker", "name": "Eswatini", "line": {"width": 0.0, "color": "red"}}, {"type": "scattergeo", "lon": [-65, 2], "lat": [-17, 46], "mode": "lines+marker", "name": "Bolivia", "line": {"width": 2.271647391135002, "color": "red"}}, {"type": "scattergeo", "lon": [15, 2], "lat": [62, 46], "mode": "lines+marker", "name": "Sweden", "line": {"width": 1.7169936022425731, "color": "red"}}, {"type": "scattergeo", "lon": [165.5, 2], "lat": [-21.5, 46], "mode": "lines+marker", "name": "New Caledonia", "line": {"width": 0.6931471805599453, "color": "red"}}, {"type": "scattergeo", "lon": [19.5, 2], "lat": [48.66666666, 46], "mode": "lines+marker", "name": "Slovakia", "line": {"width": 0.5493061443340549, "color": "red"}}, {"type": "scattergeo", "lon": [-97, 2], "lat": [38, 46], "mode": "lines+marker", "name": "United States", "line": {"width": 2.2033596236321267, "color": "red"}}, {"type": "scattergeo", "lon": [35.83333333, 2], "lat": [33.83333333, 46], "mode": "lines+marker", "name": "Lebanon", "line": {"width": 0.5493061443340549, "color": "red"}}, {"type": "scattergeo", "lon": [-4, 2], "lat": [40, 46], "mode": "lines+marker", "name": "Spain", "line": {"width": 3.1102950850498696, "color": "red"}}, {"type": "scattergeo", "lon": [-2, 2], "lat": [8, 46], "mode": "lines+marker", "name": "Ghana", "line": {"width": 0.9729550745276566, "color": "red"}}, {"type": "scattergeo", "lon": [-77.5, 2], "lat": [-2, 46], "mode": "lines+marker", "name": "Ecuador", "line": {"width": 0.8958797346140275, "color": "red"}}, {"type": "scattergeo", "lon": [-72, 2], "lat": [4, 46], "mode": "lines+marker", "name": "Colombia", "line": {"width": 0.0, "color": "red"}}, {"type": "scattergeo", "lon": [-76, 2], "lat": [-10, 46], "mode": "lines+marker", "name": "Peru", "line": {"width": 1.416606672028108, "color": "red"}}, {"type": "scattergeo", "lon": [-66, 2], "lat": [8, 46], "mode": "lines+marker", "name": "Venezuela", "line": {"width": 1.2424533248940002, "color": "red"}}, {"type": "scattergeo", "lon": [-61, 2], "lat": [14.666667, 46], "mode": "lines+marker", "name": "Martinique", "line": {"width": 1.0397207708399179, "color": "red"}}, {"type": "scattergeo", "lon": [120, 2], "lat": [-5, 46], "mode": "lines+marker", "name": "Indonesia", "line": {"width": 0.8047189562170501, "color": "red"}}, {"type": "scattergeo", "lon": [122, 2], "lat": [13, 46], "mode": "lines+marker", "name": "Philippines", "line": {"width": 1.1989476363991853, "color": "red"}}, {"type": "scattergeo", "lon": [-66.5, 2], "lat": [18.25, 46], "mode": "lines+marker", "name": "Puerto Rico", "line": {"width": 0.0, "color": "red"}}, {"type": "scattergeo", "lon": [138, 2], "lat": [36, 46], "mode": "lines+marker", "name": "Japan", "line": {"width": 1.9250738008550292, "color": "red"}}, {"type": "scattergeo", "lon": [20, 2], "lat": [52, 46], "mode": "lines+marker", "name": "Poland", "line": {"width": 2.2769384458002704, "color": "red"}}, {"type": "scattergeo", "lon": [26, 2], "lat": [64, 46], "mode": "lines+marker", "name": "Finland", "line": {"width": 0.34657359027997264, "color": "red"}}, {"type": "scattergeo", "lon": [38, 2], "lat": [1, 46], "mode": "lines+marker", "name": "Kenya", "line": {"width": 1.0397207708399179, "color": "red"}}, {"type": "scattergeo", "lon": [25, 2], "lat": [57, 46], "mode": "lines+marker", "name": "Latvia", "line": {"width": 0.34657359027997264, "color": "red"}}, {"type": "scattergeo", "lon": [81, 2], "lat": [7, 46], "mode": "lines+marker", "name": "Sri Lanka", "line": {"width": 1.545521226679158, "color": "red"}}, {"type": "scattergeo", "lon": [-2.58333333, 2], "lat": [49.46666666, 46], "mode": "lines+marker", "name": "Guernsey", "line": {"width": 0.5493061443340549, "color": "red"}}, {"type": "scattergeo", "lon": [100, 2], "lat": [15, 46], "mode": "lines+marker", "name": "Thailand", "line": {"width": 2.317364494114818, "color": "red"}}, {"type": "scattergeo", "lon": [13.33333333, 2], "lat": [47.33333333, 46], "mode": "lines+marker", "name": "Austria", "line": {"width": 1.7005986908310777, "color": "red"}}, {"type": "scattergeo", "lon": [-56, 2], "lat": [-33, 46], "mode": "lines+marker", "name": "Uruguay", "line": {"width": 0.0, "color": "red"}}, {"type": "scattergeo", "lon": [7.4, 2], "lat": [43.73333333, 46], "mode": "lines+marker", "name": "Monaco", "line": {"width": 0.6931471805599453, "color": "red"}}, {"type": "scattergeo", "lon": [114.188, 2], "lat": [22.267, 46], "mode": "lines+marker", "name": "Hong Kong", "line": {"width": 0.5493061443340549, "color": "red"}}, {"type": "scattergeo", "lon": [-55, 2], "lat": [-10, 46], "mode": "lines+marker", "name": "Brazil", "line": {"width": 0.6931471805599453, "color": "red"}}, {"type": "scattergeo", "lon": [47, 2], "lat": [-20, 46], "mode": "lines+marker", "name": "Madagascar", "line": {"width": 0.8047189562170501, "color": "red"}}, {"type": "scattergeo", "lon": [-70.66666666, 2], "lat": [19, 46], "mode": "lines+marker", "name": "Dominican Republic", "line": {"width": 0.34657359027997264, "color": "red"}}, {"type": "scattergeo", "lon": [29, 2], "lat": [47, 46], "mode": "lines+marker", "name": "Moldova", "line": {"width": 0.34657359027997264, "color": "red"}}, {"type": "scattergeo", "lon": [-18, 2], "lat": [65, 46], "mode": "lines+marker", "name": "Iceland", "line": {"width": 1.6479184330021646, "color": "red"}}, {"type": "scattergeo", "lon": [133, 2], "lat": [-27, 46], "mode": "lines+marker", "name": "Australia", "line": {"width": 0.34657359027997264, "color": "red"}}, {"type": "scattergeo", "lon": [20, 2], "lat": [47, 46], "mode": "lines+marker", "name": "Hungary", "line": {"width": 1.151292546497023, "color": "red"}}, {"type": "scattergeo", "lon": [7, 2], "lat": [1, 46], "mode": "lines+marker", "name": "S\u00e3o Tom\u00e9 and Pr\u00edncipe", "line": {"width": 0.0, "color": "red"}}, {"type": "scattergeo", "lon": [100, 2], "lat": [60, 46], "mode": "lines+marker", "name": "Russia", "line": {"width": 0.8958797346140275, "color": "red"}}, {"type": "scattergeo", "lon": [10, 2], "lat": [56, 46], "mode": "lines+marker", "name": "Denmark", "line": {"width": 1.629048269010741, "color": "red"}}, {"type": "scattergeo", "lon": [98, 2], "lat": [22, 46], "mode": "lines+marker", "name": "Myanmar", "line": {"width": 0.0, "color": "red"}}, {"type": "scattergeo", "lon": [12, 2], "lat": [6, 46], "mode": "lines+marker", "name": "Cameroon", "line": {"width": 0.5493061443340549, "color": "red"}}, {"type": "scattergeo", "lon": [4, 2], "lat": [50.83333333, 46], "mode": "lines+marker", "name": "Belgium", "line": {"width": 3.40451965302149, "color": "red"}}, {"type": "scattergeo", "lon": [14.81666666, 2], "lat": [46.11666666, 46], "mode": "lines+marker", "name": "Slovenia", "line": {"width": 0.8047189562170501, "color": "red"}}, {"type": "scattergeo", "lon": [9, 2], "lat": [51, 46], "mode": "lines+marker", "name": "Germany", "line": {"width": 3.3790472522138653, "color": "red"}}, {"type": "scattergeo", "lon": [9, 2], "lat": [34, 46], "mode": "lines+marker", "name": "Tunisia", "line": {"width": 1.4451858789480823, "color": "red"}}, {"type": "scattergeo", "lon": [53, 2], "lat": [32, 46], "mode": "lines+marker", "name": "Iran", "line": {"width": 2.012675845367575, "color": "red"}}, {"type": "scattergeo", "lon": [166.633333, 2], "lat": [19.3, 46], "mode": "lines+marker", "name": "United States Minor Outlying Islands", "line": {"width": 1.6094379124341003, "color": "red"}}, {"type": "scattergeo", "lon": [105, 2], "lat": [35, 46], "mode": "lines+marker", "name": "China", "line": {"width": 2.3978952727983707, "color": "red"}}, {"type": "scattergeo", "lon": [26, 2], "lat": [59, 46], "mode": "lines+marker", "name": "Estonia", "line": {"width": 0.34657359027997264, "color": "red"}}, {"type": "scattergeo", "lon": [45, 2], "lat": [25, 46], "mode": "lines+marker", "name": "Saudi Arabia", "line": {"width": 0.0, "color": "red"}}, {"type": "scattergeo", "lon": [69.167, 2], "lat": [-49.25, 46], "mode": "lines+marker", "name": "French Southern and Antarctic Lands", "line": {"width": 1.0397207708399179, "color": "red"}}, {"type": "scattergeo", "lon": [12.83333333, 2], "lat": [42.83333333, 46], "mode": "lines+marker", "name": "Italy", "line": {"width": 3.4891068713153492, "color": "red"}}, {"type": "scattergeo", "lon": [-8, 2], "lat": [53, 46], "mode": "lines+marker", "name": "Ireland", "line": {"width": 1.7005986908310777, "color": "red"}}, {"type": "scattergeo", "lon": [-84, 2], "lat": [10, 46], "mode": "lines+marker", "name": "Costa Rica", "line": {"width": 0.34657359027997264, "color": "red"}}, {"type": "scattergeo", "lon": [15.5, 2], "lat": [45.16666666, 46], "mode": "lines+marker", "name": "Croatia", "line": {"width": 0.6931471805599453, "color": "red"}}, {"type": "scattergeo", "lon": [57.55, 2], "lat": [-20.28333333, 46], "mode": "lines+marker", "name": "Mauritius", "line": {"width": 0.8047189562170501, "color": "red"}}], {"title": "Manufacturing countries of products", "geo": {"projection": {"type": "Mercator"}, "showframe": false, "showcoastlines": true, "showland": true, "landcolor": "rgb(229, 229, 229)", "countrycolor": "rgb(255, 255, 255)", "coastlinecolor": "rgb(255, 255, 255)"}, "showlegend": false, "xaxis": {"fixedrange": true}, "yaxis": {"fixedrange": true}}, {"showLink": true, "linkText": "Export to plot.ly"})});</script><script type="text/javascript">window.addEventListener("resize", function(){window._Plotly.Plots.resize(document.getElementById("40abff9f-a6e7-42ae-b043-385f608ad0ee"));});</script>


### Good nutrition impact


```python
nutrition_fr = food_facts_pd[['product_name',
                              'created_datetime',
                              'nutrition-score-fr_100g', 
                              'product_name', 
                              'main_category', 
                              'origins', 
                              'purchase_places', 
                              'manufacturing_place',
                              'stores']
                            ]

nutrition_fr = nutrition_fr[nutrition_fr['nutrition-score-fr_100g'].notna()]
nutrition_over_time = nutrition_fr.sort_values(by = 'created_datetime')
nutrition_over_time['main_category'] = nutrition_over_time.main_category.fillna(value='Unknown')
```

Meanong of the nutrition score index can be found at https://world.openfoodfacts.org/nutriscore. The main facts are the following : 
- Products are marked according to the amount of nutrients they contain [per 100 g] and given a grade between A and E (A being obviously the best mark).

<img src="Images/nutriscore.png" height="540" width="336">

- If the product is solids, this is linked to a nutrition score as displayed the next table. This score itself is computed with two parts. The first one considers the energy, saturated fat, sugars and sodium. A high level in that category is considered unhealthy. The second part reflects the proportion of fruits, vegetables and nuts, fibers and proteins for which high levels are considered beneficial to the health.

<img src="Images/nutriscore_table.png" height="1000" width="900">




```python
#Assigning the grades
nutrition_over_time["nutrition_grade"] =\
                                    nutrition_over_time[['nutrition-score-fr_100g','main_category']].\
                                    apply(explore.assign_score, axis=1)

```

#### High-nutrional products

##### Has there been a surge in high graded Products in the UK / France over the past years?


```python
nutrition_over_time_reduced = explore.nutrition_grade(nutrition_over_time)
```

#### High-nutrional products


```python
visualize.make_grade_stacked_bar(nutrition_over_time_reduced, 'nutrition_grade', 'year', 'Count')                        
```


![png](Open%20Food%20Facts%20-%20Explore%20data_files/Open%20Food%20Facts%20-%20Explore%20data_51_0.png)


We observe that, as time passes, more products are being added with a nutritional grade, with a peak occurring during the years 2015-2016.


```python
visualize.make_grade_stacked_bar(nutrition_over_time_reduced, 'nutrition_grade', 'year', 'Percentage')
```


![png](Open%20Food%20Facts%20-%20Explore%20data_files/Open%20Food%20Facts%20-%20Explore%20data_53_0.png)


We observe that the percentage of prevalence of each grade has been mostly maintained during the last six years with a barely noticeable peak in 2013 for grade 'A'. 


```python
df = nutrition_over_time_reduced
```


```python
figure = {
    'data': [],
    'layout': {},
    'frames': [],
}

# fill in most of layout
figure['layout']['xaxis'] = {'title': 'Nutrtion Grade'}
figure['layout']['yaxis'] = {'title': '# Products'}
figure['layout']['hovermode'] = 'closest'

# add play and pause button
figure['layout']['updatemenus'] = [
    {
        'buttons': [
            {
                'args': [None, {'frame': {'duration': 500, 'redraw': False},
                         'fromcurrent': True, 'transition': {'duration': 300, 'easing': 'quadratic-in-out'}}],
                'label': 'Play',
                'method': 'animate'
            },
            {
                'args': [[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate',
                'transition': {'duration': 0}}],
                'label': 'Pause',
                'method': 'animate'
            }
        ],
        'direction': 'left',
        'pad': {'r': 10, 't': 87},
        'showactive': False,
        'type': 'buttons',
        'x': 0.1,
        'xanchor': 'right',
        'y': 0,
        'yanchor': 'top'
    }
]

# define slider
sliders_dict = {
    'active': 0,
    'yanchor': 'top',
    'xanchor': 'left',
    'currentvalue': {
        'font': {'size': 20},
        'prefix': 'Year:',
        'visible': True,
        'xanchor': 'right'
    },
    'transition': {'duration': 300, 'easing': 'cubic-in-out'},
    'pad': {'b': 10, 't': 50},
    'len': 0.9,
    'x': 0.1,
    'y': 0,
    'steps': []
}
```


```python
year = 2018
trace = go.Bar(
    x = df[df['year']==year].nutrition_grade.values,
    y = df[df['year']==year].Count.values,
    marker = dict(
        color = ["#008010", "#9ACD32","#FFD700", "#FF8C00", "#DB4832"]
        ),
    )

figure['data'].append(trace)
```


```python
for year in sorted(df.year.unique()):
    
    frame = {'data': [], 'name': str(year)}
    trace = go.Bar(
        x = df[df['year']==year].nutrition_grade.values,
        y = df[df['year']==year].Count.values,
        marker = dict(
            color = ["#008010", "#9ACD32","#FFD700", "#FF8C00", "#DB4832"]
            ),
    )
    
    frame['data'].append(trace)
    figure['frames'].append(frame)
    
    slider_step = {'args': [
        [year],
        {'frame': {'duration': 300, 'redraw': False},
         'mode': 'immediate',
       'transition': {'duration': 300}}
     ],
     'label': int(year),
     'method': 'animate'}
    sliders_dict['steps'].append(slider_step)

figure['layout']['sliders'] = [sliders_dict]
```


```python
iplot(figure, filename='nutrition_grades')
```


<div id="d2c1ad10-396d-4900-a159-706c87c2b417" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";
        Plotly.plot(
            'd2c1ad10-396d-4900-a159-706c87c2b417',
            [{"marker": {"color": ["#008010", "#9ACD32", "#FFD700", "#FF8C00", "#DB4832"]}, "x": ["A", "B", "C", "D", "E"], "y": [504, 480, 810, 1077, 612], "type": "bar", "uid": "342e80d0-194f-4fad-833c-307fcf19c7f5"}],
            {"hovermode": "closest", "sliders": [{"active": 0, "currentvalue": {"font": {"size": 20}, "prefix": "Year:", "visible": true, "xanchor": "right"}, "len": 0.9, "pad": {"b": 10, "t": 50}, "steps": [{"args": [[2012.0], {"frame": {"duration": 300, "redraw": false}, "mode": "immediate", "transition": {"duration": 300}}], "label": "2012", "method": "animate"}, {"args": [[2013.0], {"frame": {"duration": 300, "redraw": false}, "mode": "immediate", "transition": {"duration": 300}}], "label": "2013", "method": "animate"}, {"args": [[2014.0], {"frame": {"duration": 300, "redraw": false}, "mode": "immediate", "transition": {"duration": 300}}], "label": "2014", "method": "animate"}, {"args": [[2015.0], {"frame": {"duration": 300, "redraw": false}, "mode": "immediate", "transition": {"duration": 300}}], "label": "2015", "method": "animate"}, {"args": [[2016.0], {"frame": {"duration": 300, "redraw": false}, "mode": "immediate", "transition": {"duration": 300}}], "label": "2016", "method": "animate"}, {"args": [[2017.0], {"frame": {"duration": 300, "redraw": false}, "mode": "immediate", "transition": {"duration": 300}}], "label": "2017", "method": "animate"}, {"args": [[2018.0], {"frame": {"duration": 300, "redraw": false}, "mode": "immediate", "transition": {"duration": 300}}], "label": "2018", "method": "animate"}], "transition": {"duration": 300, "easing": "cubic-in-out"}, "x": 0.1, "xanchor": "left", "y": 0, "yanchor": "top"}], "updatemenus": [{"buttons": [{"args": [null, {"frame": {"duration": 500, "redraw": false}, "fromcurrent": true, "transition": {"duration": 300, "easing": "quadratic-in-out"}}], "label": "Play", "method": "animate"}, {"args": [[null], {"frame": {"duration": 0, "redraw": false}, "mode": "immediate", "transition": {"duration": 0}}], "label": "Pause", "method": "animate"}], "direction": "left", "pad": {"r": 10, "t": 87}, "showactive": false, "type": "buttons", "x": 0.1, "xanchor": "right", "y": 0, "yanchor": "top"}], "xaxis": {"title": "Nutrtion Grade"}, "yaxis": {"title": "# Products"}},
            {"showLink": true, "linkText": "Export to plot.ly"}
        ).then(function () {return Plotly.addFrames('d2c1ad10-396d-4900-a159-706c87c2b417',[{"data": [{"marker": {"color": ["#008010", "#9ACD32", "#FFD700", "#FF8C00", "#DB4832"]}, "x": ["A", "B", "C", "D", "E"], "y": [151, 160, 181, 195, 119], "type": "bar"}], "name": "2012.0"}, {"data": [{"marker": {"color": ["#008010", "#9ACD32", "#FFD700", "#FF8C00", "#DB4832"]}, "x": ["A", "B", "C", "D", "E"], "y": [493, 397, 475, 537, 320], "type": "bar"}], "name": "2013.0"}, {"data": [{"marker": {"color": ["#008010", "#9ACD32", "#FFD700", "#FF8C00", "#DB4832"]}, "x": ["A", "B", "C", "D", "E"], "y": [530, 469, 609, 850, 387], "type": "bar"}], "name": "2014.0"}, {"data": [{"marker": {"color": ["#008010", "#9ACD32", "#FFD700", "#FF8C00", "#DB4832"]}, "x": ["A", "B", "C", "D", "E"], "y": [949, 1029, 1355, 1748, 1098], "type": "bar"}], "name": "2015.0"}, {"data": [{"marker": {"color": ["#008010", "#9ACD32", "#FFD700", "#FF8C00", "#DB4832"]}, "x": ["A", "B", "C", "D", "E"], "y": [862, 879, 1352, 1879, 1144], "type": "bar"}], "name": "2016.0"}, {"data": [{"marker": {"color": ["#008010", "#9ACD32", "#FFD700", "#FF8C00", "#DB4832"]}, "x": ["A", "B", "C", "D", "E"], "y": [725, 698, 1072, 1325, 863], "type": "bar"}], "name": "2017.0"}, {"data": [{"marker": {"color": ["#008010", "#9ACD32", "#FFD700", "#FF8C00", "#DB4832"]}, "x": ["A", "B", "C", "D", "E"], "y": [504, 480, 810, 1077, 612], "type": "bar"}], "name": "2018.0"}]);}).then(function(){Plotly.animate('d2c1ad10-396d-4900-a159-706c87c2b417');})
        });</script><script type="text/javascript">window.addEventListener("resize", function(){window._Plotly.Plots.resize(document.getElementById("d2c1ad10-396d-4900-a159-706c87c2b417"));});</script>


##### What are those products made of?
What is the composition? Do they contain many additives?  Where are these products sold? 

This plot displays the most common categories in the list of product possessing a nutritional index


```python
visualize.make_content_stacked_bar(visualize.plot_grade_content(nutrition_over_time), 'keys', 'grade', 'Percentage')
```


![png](Open%20Food%20Facts%20-%20Explore%20data_files/Open%20Food%20Facts%20-%20Explore%20data_62_0.png)


Observe how good nutritional products are mostly (more than 50%) plant-based and how this category as well as carbs and canned food shrink when considering less beneficial food standards. This reduction is compensated by a sharp increase in prevalence of sugary snacks and a lesser increase of meat-based producs. Both seafood and dairy seem to concentre in, respectevely, the lower and higger part of the middle marks. 

##### Where do these product come from and where are they manufactured?


```python
visualize.plot_column_composition(nutrition_fr, 'purchase_places') 
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>France</td>
      <td>26335</td>
    </tr>
  </tbody>
</table>
</div>



<div id="a63275a8-6ad4-46a1-a2da-4d63ef17e784" style="height: 300px; width: 800px;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("a63275a8-6ad4-46a1-a2da-4d63ef17e784", [{"marker": {"color": "#F4B5A6", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "France", "orientation": "h", "x": [26335], "y": [0], "type": "bar", "uid": "8dc4a44f-bbc2-4eda-8193-6e7db5f1106d"}, {"marker": {"color": "#F4EBA6", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Others", "orientation": "h", "x": [0], "y": [0], "type": "bar", "uid": "ca38d199-3296-43d7-b82e-fd1693047c5d"}], {"barmode": "stack", "height": 300, "showlegend": true, "title": "purchase_places", "width": 800, "xaxis": {"tickvals": [0, 5000, 10000, 15000, 20000, 25000, 26335]}, "yaxis": {"showgrid": false, "showline": false, "showticklabels": false, "zeroline": false}}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


This plot is of course highly bias towards france since the cut was perform on that column


```python
visualize.plot_column_composition(nutrition_fr, 'manufacturing_place') 
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>United Kingdom</td>
      <td>2408.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Unknown</td>
      <td>1760.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Italy</td>
      <td>881.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Germany</td>
      <td>686.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Belgium</td>
      <td>626.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Spain</td>
      <td>382.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Netherlands</td>
      <td>245.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Switzerland</td>
      <td>128.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>China</td>
      <td>95.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Thailand</td>
      <td>84.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Greece</td>
      <td>82.0</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Morocco</td>
      <td>79.0</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Bolivia</td>
      <td>77.0</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Poland</td>
      <td>76.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Portugal</td>
      <td>51.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Taiwan</td>
      <td>51.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>United States</td>
      <td>44.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Iran</td>
      <td>44.0</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Vietnam</td>
      <td>42.0</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Japan</td>
      <td>33.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Canada</td>
      <td>27.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Turkey</td>
      <td>25.0</td>
    </tr>
    <tr>
      <th>47</th>
      <td>Sweden</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Iceland</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Denmark</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Ireland</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Austria</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Niger</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>63</th>
      <td>United States Minor Outlying Islands</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Sri Lanka</td>
      <td>19.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>86</th>
      <td>Lebanon</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>100</th>
      <td>Cayman Islands</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>85</th>
      <td>Laos</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>83</th>
      <td>Romania</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Cyprus</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>101</th>
      <td>Madagascar</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>71</th>
      <td>Chile</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>60</th>
      <td>Dominican Republic</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>59</th>
      <td>Estonia</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>58</th>
      <td>Moldova</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Senegal</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Cameroon</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Singapore</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Saint Martin</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>94</th>
      <td>French Polynesia</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Myanmar</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>99</th>
      <td>Hong Kong</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>98</th>
      <td>New Zealand</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>São Tomé and Príncipe</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>96</th>
      <td>Paraguay</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>95</th>
      <td>Costa Rica</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Colombia</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>93</th>
      <td>Togo</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>92</th>
      <td>El Salvador</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Australia</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Saudi Arabia</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>74</th>
      <td>Liechtenstein</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>53</th>
      <td>Monaco</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>82</th>
      <td>Puerto Rico</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>89</th>
      <td>Unknown</td>
      <td>1760.0</td>
    </tr>
  </tbody>
</table>
<p>102 rows × 2 columns</p>
</div>



<div id="e71676a9-6444-48d0-8797-0255cc2fbd75" style="height: 300px; width: 800px;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("e71676a9-6444-48d0-8797-0255cc2fbd75", [{"marker": {"color": "#F4B5A6", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "United Kingdom", "orientation": "h", "x": [2408.0], "y": [0], "type": "bar", "uid": "1bba9e34-3f37-47c9-90ea-6d9954ea3510"}, {"marker": {"color": "#F4EBA6", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Unknown", "orientation": "h", "x": [1760.0], "y": [0], "type": "bar", "uid": "448d72cd-83bf-48ea-bd4c-341a23a87fce"}, {"marker": {"color": "#B2F4A6", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Italy", "orientation": "h", "x": [881.0], "y": [0], "type": "bar", "uid": "a1e7cefe-1b70-4ee9-9777-012676ba8164"}, {"marker": {"color": "#A6E3F4", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Germany", "orientation": "h", "x": [686.0], "y": [0], "type": "bar", "uid": "d28accb7-6b7f-463f-813e-ae271b306187"}, {"marker": {"color": "#C4A6F4", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Belgium", "orientation": "h", "x": [626.0], "y": [0], "type": "bar", "uid": "3a437b69-9f1f-47e9-be64-77557b1f7f60"}, {"marker": {"color": "#E0DBDD", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Others", "orientation": "h", "x": [3806.0], "y": [0], "type": "bar", "uid": "60c08091-946b-40be-820b-4773b02a4745"}], {"barmode": "stack", "height": 300, "showlegend": true, "title": "manufacturing_place", "width": 800, "xaxis": {"tickvals": [0, 5000, 10000, 10167.0]}, "yaxis": {"showgrid": false, "showline": false, "showticklabels": false, "zeroline": false}}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


Naturally, most of the food consumed in France is manufactured there though approximately 30% is produced somewhere else. 

##### Where are those products sold?


```python
visualize.plot_column_composition(nutrition_fr, 'stores')
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>20</th>
      <td>Carrefour</td>
      <td>5096</td>
    </tr>
    <tr>
      <th>193</th>
      <td>Magasins U</td>
      <td>2281</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Auchan</td>
      <td>1997</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Leclerc</td>
      <td>1972</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Intermarché</td>
      <td>1571</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Super U</td>
      <td>1233</td>
    </tr>
    <tr>
      <th>175</th>
      <td>Magasins U</td>
      <td>1193</td>
    </tr>
    <tr>
      <th>77</th>
      <td>LIDL</td>
      <td>1103</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Cora</td>
      <td>1098</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Franprix</td>
      <td>1030</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Walmart</td>
      <td>988</td>
    </tr>
    <tr>
      <th>47</th>
      <td>Picard</td>
      <td>819</td>
    </tr>
    <tr>
      <th>203</th>
      <td>Casino</td>
      <td>803</td>
    </tr>
    <tr>
      <th>154</th>
      <td>Monoprix</td>
      <td>663</td>
    </tr>
    <tr>
      <th>140</th>
      <td>Leader Price</td>
      <td>521</td>
    </tr>
    <tr>
      <th>132</th>
      <td>ALDI</td>
      <td>510</td>
    </tr>
    <tr>
      <th>84</th>
      <td>Coop</td>
      <td>509</td>
    </tr>
    <tr>
      <th>173</th>
      <td>Netto</td>
      <td>458</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Soriana</td>
      <td>411</td>
    </tr>
    <tr>
      <th>170</th>
      <td>Migros</td>
      <td>367</td>
    </tr>
    <tr>
      <th>192</th>
      <td>Dia</td>
      <td>275</td>
    </tr>
    <tr>
      <th>130</th>
      <td>Sky</td>
      <td>259</td>
    </tr>
    <tr>
      <th>167</th>
      <td>Banque Alimentaire</td>
      <td>255</td>
    </tr>
    <tr>
      <th>196</th>
      <td>Simply Market</td>
      <td>246</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Bodega Aurrera</td>
      <td>242</td>
    </tr>
    <tr>
      <th>180</th>
      <td>Grand Frais</td>
      <td>196</td>
    </tr>
    <tr>
      <th>108</th>
      <td>Noz</td>
      <td>193</td>
    </tr>
    <tr>
      <th>241</th>
      <td>Ica Supermarket</td>
      <td>176</td>
    </tr>
    <tr>
      <th>206</th>
      <td>U Express</td>
      <td>170</td>
    </tr>
    <tr>
      <th>263</th>
      <td>Bio14</td>
      <td>163</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>768</th>
      <td>Biscuiterie De Kerlann</td>
      <td>1</td>
    </tr>
    <tr>
      <th>769</th>
      <td>Kerlann</td>
      <td>1</td>
    </tr>
    <tr>
      <th>770</th>
      <td>La Petite Marquise</td>
      <td>1</td>
    </tr>
    <tr>
      <th>771</th>
      <td>Carrefour Villiers En Biere 77</td>
      <td>1</td>
    </tr>
    <tr>
      <th>772</th>
      <td>Grandeur Nature</td>
      <td>1</td>
    </tr>
    <tr>
      <th>747</th>
      <td>Grand'Frais</td>
      <td>1</td>
    </tr>
    <tr>
      <th>746</th>
      <td>Biobulle</td>
      <td>1</td>
    </tr>
    <tr>
      <th>745</th>
      <td>Mayenne Bio Soleil</td>
      <td>1</td>
    </tr>
    <tr>
      <th>238</th>
      <td>Leclere</td>
      <td>1</td>
    </tr>
    <tr>
      <th>717</th>
      <td>Leclercq</td>
      <td>1</td>
    </tr>
    <tr>
      <th>246</th>
      <td>Bon Samaritain Kalgondin</td>
      <td>1</td>
    </tr>
    <tr>
      <th>719</th>
      <td>Raimo Glacier  - 59/63 Boulevard De Reuilly - ...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>243</th>
      <td>Pays-Bas</td>
      <td>1</td>
    </tr>
    <tr>
      <th>723</th>
      <td>Guérance</td>
      <td>1</td>
    </tr>
    <tr>
      <th>724</th>
      <td>Que Du Bonheur</td>
      <td>1</td>
    </tr>
    <tr>
      <th>725</th>
      <td>Http://Www.Labelleiloise.Fr/Fr/Nos-Boutiques/I...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>726</th>
      <td>La Belle-Iloise Nantes</td>
      <td>1</td>
    </tr>
    <tr>
      <th>239</th>
      <td>Secours Populaire</td>
      <td>1</td>
    </tr>
    <tr>
      <th>731</th>
      <td>V&amp;B</td>
      <td>1</td>
    </tr>
    <tr>
      <th>744</th>
      <td>Zodio</td>
      <td>1</td>
    </tr>
    <tr>
      <th>732</th>
      <td>Au Goûter Breton</td>
      <td>1</td>
    </tr>
    <tr>
      <th>734</th>
      <td>Epicerie Sofine</td>
      <td>1</td>
    </tr>
    <tr>
      <th>735</th>
      <td>Salon Du Chocolat</td>
      <td>1</td>
    </tr>
    <tr>
      <th>237</th>
      <td>Wikirencontre-17102014-Cedalyon</td>
      <td>1</td>
    </tr>
    <tr>
      <th>738</th>
      <td>Www.Nosmeilleurescourses.Com</td>
      <td>1</td>
    </tr>
    <tr>
      <th>739</th>
      <td>Epicer'Ie Vitalienne</td>
      <td>1</td>
    </tr>
    <tr>
      <th>740</th>
      <td>Supermarchés Casino</td>
      <td>1</td>
    </tr>
    <tr>
      <th>741</th>
      <td>Carrefour Saint-Pierre</td>
      <td>1</td>
    </tr>
    <tr>
      <th>742</th>
      <td>Tft Spécialités</td>
      <td>1</td>
    </tr>
    <tr>
      <th>650</th>
      <td>Biscuiterie Penven</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>1301 rows × 2 columns</p>
</div>



<div id="8b3265bb-bc51-4594-9266-843797b0e365" style="height: 300px; width: 800px;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("8b3265bb-bc51-4594-9266-843797b0e365", [{"marker": {"color": "#F4B5A6", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Carrefour", "orientation": "h", "x": [5096], "y": [0], "type": "bar", "uid": "56888c6e-b788-4e3a-a76a-6bb7aa98f593"}, {"marker": {"color": "#F4EBA6", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": " Magasins U", "orientation": "h", "x": [2281], "y": [0], "type": "bar", "uid": "4161b3d1-c218-46d7-93ad-9689230074d9"}, {"marker": {"color": "#B2F4A6", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Auchan", "orientation": "h", "x": [1997], "y": [0], "type": "bar", "uid": "3fbc314b-3d27-467d-97dc-4a4f74bbb536"}, {"marker": {"color": "#A6E3F4", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Leclerc", "orientation": "h", "x": [1972], "y": [0], "type": "bar", "uid": "83263dca-31d6-431a-88ac-7fa5e5b87bc7"}, {"marker": {"color": "#C4A6F4", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Intermarch\u00e9", "orientation": "h", "x": [1571], "y": [0], "type": "bar", "uid": "a0cf4614-3db5-4eb6-8a65-c2eef4c120f7"}, {"marker": {"color": "#E0DBDD", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Others", "orientation": "h", "x": [21747], "y": [0], "type": "bar", "uid": "fbbee53a-6fc0-4c3c-a95f-80a818cce16e"}], {"barmode": "stack", "height": 300, "showlegend": true, "title": "stores", "width": 800, "xaxis": {"tickvals": [0, 5000, 10000, 15000, 20000, 25000, 30000, 34664]}, "yaxis": {"showgrid": false, "showline": false, "showticklabels": false, "zeroline": false}}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


Side fact: [market share grocery stores in France](https://www.statista.com/statistics/535415/grocery-market-share-france/) (October 2017)
    <img src="Images/marketshare_stores_france.png" height="800" width="600">

#### Carbon footprint of nutrionally-high graded products

In this section we investigate the carbon footprint of different products and categories. Therefore, we investigate the OpenFoodFacts dataset. Common sense would suggest most nutritionally-high graded products are organic (plant, fruit, vegetables, …) and are therefore not manufactured, thus having a small footprint. Let's see what story the data has to tell...

But as before, we should be careful as the dataset is biased. So we begin with examing what kind of data is represented in the datasets.

We begin with extracting all the carbon footprint data.


```python
carbon_footprints = food_facts_pd[food_facts_pd['carbon-footprint_100g'].notna() & 
                                  food_facts_pd['carbon-footprint_100g']!=0]
display(carbon_footprints.main_category.value_counts())
```




    Sugary snacks                             29
    Plant-based                               17
    Dairies                                   15
    Carbs                                      8
    Beverages                                  8
    Meats                                      7
    Seafood                                    6
    Frozen foods                               3
    Groceries                                  2
    Sweeteners                                 2
    Meals                                      2
    Canned foods                               1
    Tortellini-Aux-Epinard-Et-A-La-Ricotta     1
    Salty snacks                               1
    Name: main_category, dtype: int64



First, we should sensibilize for the data that we are dealing with. Therefore we visualize the origin and composition of the products.


```python
visualize.plot_column_composition(df=carbon_footprints, column_str='manufacturing_place')
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Unknown</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>United Kingdom</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Cayman Islands</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Sweden</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Spain</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Bolivia</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Thailand</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Belgium</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Unknown</td>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
</div>



<div id="eafe03af-ec68-4595-b3f4-6bdc4b9d3250" style="height: 300px; width: 800px;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("eafe03af-ec68-4595-b3f4-6bdc4b9d3250", [{"marker": {"color": "#F4B5A6", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Unknown", "orientation": "h", "x": [5.0], "y": [0], "type": "bar", "uid": "d2eeea86-dac8-45bb-8f7b-941d467882f9"}, {"marker": {"color": "#F4EBA6", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "United Kingdom", "orientation": "h", "x": [5.0], "y": [0], "type": "bar", "uid": "6ad0d227-fd97-429d-b2f7-22e9c8a5f062"}, {"marker": {"color": "#B2F4A6", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Cayman Islands", "orientation": "h", "x": [2.0], "y": [0], "type": "bar", "uid": "d96d9161-0f28-4fd9-9e6c-e6a9e036971b"}, {"marker": {"color": "#A6E3F4", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Sweden", "orientation": "h", "x": [1.0], "y": [0], "type": "bar", "uid": "d1d24b23-f8a2-420f-863d-605d68be4eb2"}, {"marker": {"color": "#C4A6F4", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Spain", "orientation": "h", "x": [1.0], "y": [0], "type": "bar", "uid": "0b859d51-76cf-47e1-9ce0-555c9d3cf15a"}, {"marker": {"color": "#E0DBDD", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Others", "orientation": "h", "x": [8.0], "y": [0], "type": "bar", "uid": "eeb0d6a6-aadd-4ec8-93da-7f343c75b909"}], {"barmode": "stack", "height": 300, "showlegend": true, "title": "manufacturing_place", "width": 800, "xaxis": {"tickvals": [0, 5, 10, 15, 20, 22.0]}, "yaxis": {"showgrid": false, "showline": false, "showticklabels": false, "zeroline": false}}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


Let's if there is a correlation between country of origin, and hence transportation distance, and the carbon footprint. (No use because all products are from France or missing origin information).


```python
visualize.plot_column_composition(df=carbon_footprints, column_str='stores')
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>Migros</td>
      <td>23</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Casino</td>
      <td>20</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Carrefour</td>
      <td>18</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Magasins U</td>
      <td>12</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Auchan</td>
      <td>12</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Monoprix</td>
      <td>9</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Intermarché</td>
      <td>8</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Leclerc</td>
      <td>7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Géant</td>
      <td>7</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Magasins U</td>
      <td>5</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Spar</td>
      <td>3</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Super U</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Sarl Ajm</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Vival</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Ajm</td>
      <td>2</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Hyper U</td>
      <td>1</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Food And Wine</td>
      <td>1</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Raiponce F84300 Cavaillon</td>
      <td>1</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Carrefour Lingostière</td>
      <td>1</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Sami Fruits</td>
      <td>1</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Carrefour Bio</td>
      <td>1</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Cora</td>
      <td>1</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Simply</td>
      <td>1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Géant Casino</td>
      <td>1</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Kaufland</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



<div id="2a7c8c2a-c8e2-43f1-9d3e-d0e38e502ab3" style="height: 300px; width: 800px;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("2a7c8c2a-c8e2-43f1-9d3e-d0e38e502ab3", [{"marker": {"color": "#F4B5A6", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Migros", "orientation": "h", "x": [23], "y": [0], "type": "bar", "uid": "402ebe55-0030-4ea0-aafb-918b6812b5c1"}, {"marker": {"color": "#F4EBA6", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Casino", "orientation": "h", "x": [20], "y": [0], "type": "bar", "uid": "7d384413-54a8-4d1f-9574-79a99900568a"}, {"marker": {"color": "#B2F4A6", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Carrefour", "orientation": "h", "x": [18], "y": [0], "type": "bar", "uid": "593dd579-0e9e-498c-8d10-ebf4d0cff6b1"}, {"marker": {"color": "#A6E3F4", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": " Magasins U", "orientation": "h", "x": [12], "y": [0], "type": "bar", "uid": "9985ebe2-d24e-496d-9ef3-3121f3fc96fc"}, {"marker": {"color": "#C4A6F4", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Auchan", "orientation": "h", "x": [12], "y": [0], "type": "bar", "uid": "e4dcfffd-ad55-40bb-90ae-30b8c2dff2d9"}, {"marker": {"color": "#E0DBDD", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Others", "orientation": "h", "x": [58], "y": [0], "type": "bar", "uid": "9c49a588-4bc1-4ee2-aae5-c69f2a9cd24f"}], {"barmode": "stack", "height": 300, "showlegend": true, "title": "stores", "width": 800, "xaxis": {"tickvals": [0, 50, 100, 143]}, "yaxis": {"showgrid": false, "showline": false, "showticklabels": false, "zeroline": false}}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


From the above plot, we can observe that the majority of the products are sold in france, and especially the stores in provided by the shops of

Most of the carbon footprint data was produced by the research group around ###, that claims that the processed data was ###.


```python
visualize.plot_column_composition(carbon_footprints, column_str='main_category')
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>Sugary snacks</td>
      <td>29</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Plant-based</td>
      <td>17</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Dairies</td>
      <td>15</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Beverages</td>
      <td>8</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Carbs</td>
      <td>8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Meats</td>
      <td>7</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Seafood</td>
      <td>6</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Frozen foods</td>
      <td>3</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Meals</td>
      <td>2</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Sweeteners</td>
      <td>2</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Groceries</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Salty snacks</td>
      <td>1</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Canned foods</td>
      <td>1</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Tortellini-Aux-Epinard-Et-A-La-Ricotta</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



<div id="8582d88f-5169-4de7-a98e-1749374fe49e" style="height: 300px; width: 800px;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("8582d88f-5169-4de7-a98e-1749374fe49e", [{"marker": {"color": "#F4B5A6", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Sugary snacks", "orientation": "h", "x": [29], "y": [0], "type": "bar", "uid": "29b5cb9d-040a-42e3-ae9a-8ce321a5880d"}, {"marker": {"color": "#F4EBA6", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Plant-based", "orientation": "h", "x": [17], "y": [0], "type": "bar", "uid": "cba8400f-8dd4-4a87-baed-76fea2540bf2"}, {"marker": {"color": "#B2F4A6", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Dairies", "orientation": "h", "x": [15], "y": [0], "type": "bar", "uid": "e10e559f-75b4-40bb-9b16-638322886bbc"}, {"marker": {"color": "#A6E3F4", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Beverages", "orientation": "h", "x": [8], "y": [0], "type": "bar", "uid": "b3270d37-031c-4302-bedf-71d39ffc56e9"}, {"marker": {"color": "#C4A6F4", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Carbs", "orientation": "h", "x": [8], "y": [0], "type": "bar", "uid": "85d9e620-9dfa-4906-868a-3890fa8b1e7a"}, {"marker": {"color": "#E0DBDD", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Others", "orientation": "h", "x": [25], "y": [0], "type": "bar", "uid": "7b87b05a-7c6c-4920-9966-094d4ee9ee43"}], {"barmode": "stack", "height": 300, "showlegend": true, "title": "main_category", "width": 800, "xaxis": {"tickvals": [0, 50, 100, 102]}, "yaxis": {"showgrid": false, "showline": false, "showticklabels": false, "zeroline": false}}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


We see that the main categories that we have carbon footprint data of are sugary snacks (mainly plain chocolets) and dairies. This is not surprising since they are made up of only few ingredients. 


```python
# Food calories over carbon-foot print
visualize.plot_cluster_by_tags(df=carbon_footprints,
                               plot2D_features = ["carbon-footprint_100g", "price_per_100g"],
                               cluster="main_category")
```


<div id="ad4c47c7-0ae0-45fb-8dc7-4d6710fcbed8" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("ad4c47c7-0ae0-45fb-8dc7-4d6710fcbed8", [{"mode": "markers", "name": "Sugary snacks", "text": ["Cookies Tout Chocolat", "Biscuits Matin Miel et P\u00e9pites de Chocolat", "Noir intense d\u00e9gustation", "Lait noisettes enti\u00e8res", "Noir \u00e9clats d'amandes", "Noir \u00e9corces d'orange", "Chocolat Blanc Nougatine Amande", "Chocolat Lait classique d\u00e9gustation Bio Alter Eco", "P\u00e9rou 85%", "Noir \u00e9clats de menthe", "Noir Zestes de Citron", "Cookies Nougatine", "Lait Caramel Beurre sal\u00e9", "P\u00e9rou 90%", "Alter eco Noir amandes enti\u00e8res", "Chocolat noir 70%", "Noir pointe de piment", "Noir \u00c9clats de Gingembre", "Chocolat noir, \u00e9clats amandes", "Alter eco 90% P\u00e9rou", "Noir Fruit de la Passion", "Chocolat au lait aux \u00e9clats de noisettes", "Chocolat Tourist Cr\u00e9mant", "Chocolat Tourist", "Les Adorables Cremetta", "Chocolat noir fourr\u00e9 \u00e0 la cr\u00e8me d'amandes", "Supr\u00eame Lait Noisettes", "Supr\u00eame Noir Authentique", "Croissants Pr\u00e9cuits au Beurre"], "x": [305.0, 250.0, 160.0, 135.0, 153.0, 177.0, 251.0, 160.0, 178.0, 153.0, 177.0, 160.0, 150.0, 197.0, 122.0, 237.0, 219.0, 205.0, 153.0, 197.0, 214.0, 1178.0, 1311.0, 1145.0, 1206.0, 1293.0, 1001.0, 2842.0, 76.1], "y": [2.025, 1.252, 2.39, 2.38, 2.45, 1.45, 2.28, 2.78, 2.49, 2.8, 2.86, 0.39, 0.398, 2.69, 2.78, 2.75, 2.44, 2.8, 0.99, 2.49, 3.01, 2.1, 2.25, 2.25, 2.2, 1.75, 2.35, 2.7, 1.7], "type": "scatter", "uid": "548d39f7-9e8e-44f4-a546-0e38b1171b43"}, {"mode": "markers", "name": "Plant-based", "text": ["ch\u00e2taignes pel\u00e9es et r\u00f4ties cesares", "Riz long grain Camargue", "Pains au lait (x 10) aux p\u00e9pites de chocolat au lait 350 g", "Oeufs frais dat\u00e9s du jour de ponte (x 6)", "Huile d'olive vierge extra, extraite \u00e0 froid", "Semoule semi-compl\u00e8te Bio Casino", "Riz & bl\u00e9 complet Nature", "Riz & bl\u00e9 complet - Fruits rouges", "Farine de bl\u00e9 fluide", "Boisson aux fruits plate tropical", "Fleur de Colza", "Banane coco Alter Eco", "Soft white", "Risotto S. Andrea M-Classic", "Riz Carolina Parboiled M-Classic", "Riz BASMATI", "Tresse au beurre"], "x": [300.0, 545.0, 325.0, 8.4, 276.0, 155.0, 485.0, 560.0, 165.0, 5.0, 150.0, 102.0, 125.0, 281.0, 324.0, 362.0, 32.3], "y": [0.635, 0.418, 0.6890000000000001, null, 1.067, null, 0.35, 0.35, 0.01, 0.218, 0.267, 0.425, null, 0.255, 0.225, 0.29, null], "type": "scatter", "uid": "2ed8d9cb-3727-4f67-8b9c-1e172d8539bb"}, {"mode": "markers", "name": "Dairies", "text": ["Migros, M Classic", "Yogurt Mandarine", "Yogourt Rhubarbe/Vanille", "Lait \u00c9cr\u00e9m\u00e9", "Val d'Automne (28 % MG)", "Emmental Fran\u00e7ais Est-Central IGP au lait cru (32 % MG) Grand Cru - label Rouge ", "Miel liquide fleurs d'oranger d'Espagne", "Emmental Fran\u00e7ais R\u00e2p\u00e9 (29 % MG)", "Emmental Fran\u00e7ais R\u00e2p\u00e9 (29 % MG)", "Emmental Fran\u00e7ais R\u00e2p\u00e9 (29 % MG)", "P\u00e2te \u00e0 tartiner", "Yogourt fraise BIO", "Yogourt Chocolat ferme M-Classic", "Yogourt Mocca ferme M-Classic ", "Yogourt Nature"], "x": [199.7, 196.5, 193.4, 175.0, 1065.0, 1275.0, 120.0, 1113.0547, 1113.0547, 1127.0, 149.0, 180.9, 267.4, 204.5, 55.6], "y": [null, 0.6, 0.6, 0.129, 0.532, null, 1.218, 1.19, 1.19, 1.19, 1.018, 0.6, 0.6, 0.6, 0.2], "type": "scatter", "uid": "e31c1c47-51a6-4cf0-a241-0da9c3544621"}, {"mode": "markers", "name": "Carbs", "text": ["Torti (Cuisson 3 min.)", "Coquillettes au Bl\u00e9 Complet", "Cheveux d'Ange (Al dente 3 min.)", "Coquillettes", "Farfalle", "Coquillettes (Al dente 9 min.)", "Coquillettes au bl\u00e9 int\u00e9gral Bio", "Tortelloni ricotta e spinaci"], "x": [185.0, 4.4, 202.36, 200.75, 209.85, 198.9, 182.85, 288.9], "y": [null, 0.08900000000000001, 0.289, 0.08900000000000001, 0.13, 0.135, 0.218, 1.5], "type": "scatter", "uid": "d8bdd434-5e70-490a-99ba-a9839e3bc637"}, {"mode": "markers", "name": "Beverages", "text": ["100 % Pur Jus Orange", "Th\u00e9 Vert Ceylan Bio Alter Eco", "Caf\u00e9 moulu pur arabica Guat\u00e9mala", "Rooibos nature bio & \u00e9quitable", "Rooibos \u00e9pices", "Nectar ananas mangue passion", "Nectar banane goyave acerola", "Goyave passion "], "x": [130.0, 775.0, 124.0, 607.0, 562.0, 300.0, 94.0, 102.0], "y": [0.159, 7.525, 1.536, 0.197, 8.55, 0.418, 0.418, 0.53], "type": "scatter", "uid": "511e816f-630d-4304-8bcb-e1badc6bcfd4"}, {"mode": "markers", "name": "Meats", "text": ["Terrine de Chevreuil", "TERRINE AUX CH\u00c2TAIGNES", "Lardons Nature (2 barquettes)", "Lardons Fum\u00e9s (2 barquettes)", "Saucisses de Francfort", "B\u0153uf Bourguignon et ses Tagliatelles", "Aiguillettes de poulet, sauce normande et son riz"], "x": [0.05, 0.05, 945.0, 945.0, 825.0, 770.0, 495.0], "y": [null, null, 1.327, 1.327, 1.061, 1.43, 1.662], "type": "scatter", "uid": "b80fd09a-e19e-499c-96cb-ebc6cb419472"}, {"mode": "markers", "name": "Seafood", "text": ["Truite fum\u00e9e au bois de h\u00eatre (6 tranches) - 150 g", "Truite fum\u00e9e Capaccio au Poivre de Sichuan", "Truite fum\u00e9e de France", "Truite Fum\u00e9e Pyr\u00e9n\u00e9es (4 tranches) - 120 g", "Truite Fum\u00e9e Pyr\u00e9n\u00e9es", "Truite fum\u00e9e Pyr\u00e9n\u00e9es Offre exceptionnelle"], "x": [900.0, 828.0, 828.0, 828.0, 2760.0, 828.0], "y": [2.772, 3.75, 4.825, 5.675, 5.675, 5.675], "type": "scatter", "uid": "6023afd6-3a1d-4a9d-997f-22711f5cb6be"}, {"mode": "markers", "name": "Frozen foods", "text": ["Cabillaud 100 % Filet, Surgel\u00e9s (8 pan\u00e9s)", "Lasagnes au saumon, Surgel\u00e9es", "Pommes Dauphines"], "x": [425.0, 430.0, 345.0], "y": [2.289, 0.6970000000000001, 0.398], "type": "scatter", "uid": "cdcac5c5-23e9-484e-9ee8-01b98c12b2e3"}, {"mode": "markers", "name": "Groceries", "text": ["Sugo Pomodoro Anna\u2019s Best, Bio", "Pesto basilico"], "x": [191.9, 381.6], "y": [0.975, 1.93], "type": "scatter", "uid": "f7861ea3-1379-4fd0-9db6-05c558ee53d2"}, {"mode": "markers", "name": "Sweeteners", "text": ["Sucre Complet Muscovado", "Sucre de canne complet Rapadura"], "x": [136.0, 17.0], "y": [0.358, 0.574], "type": "scatter", "uid": "baa0f33d-df27-4de0-b6ae-f2034e537fcd"}, {"mode": "markers", "name": "Meals", "text": ["Lasagnes au ch\u00e8vre et aux \u00e9pinards", "Pav\u00e9 de lieu sauce citron riz et julienne de l\u00e9gumes (2,4 % MG)"], "x": [485.0, 590.0], "y": [0.65, 0.532], "type": "scatter", "uid": "2f2449c0-8bb0-4e62-9614-e63cc2af0148"}, {"mode": "markers", "name": "Canned foods", "text": ["Carne de Porc in suc propriu - Scandia"], "x": [300.0], "y": [2.063], "type": "scatter", "uid": "49653aed-01a9-41ad-acc7-ea972fa28fa3"}, {"mode": "markers", "name": "Tortellini-Aux-Epinard-Et-A-La-Ricotta", "text": ["Tortellini aux \u00e9pinard et \u00e0 la ricotta"], "x": [248.2], "y": [0.46], "type": "scatter", "uid": "5adc123f-499c-479e-92ae-3688895d9670"}, {"mode": "markers", "name": "Salty snacks", "text": ["Chips saveur poulet thym"], "x": [340.0], "y": [1.069], "type": "scatter", "uid": "c691fa67-ceb0-4911-b4d5-ead52286dedc"}], {"xaxis": {"title": "Carbon footprint per 100g [g]"}, "yaxis": {"title": "Price per 100g [g]"}}, {"showLink": true, "linkText": "Export to plot.ly"})});</script><script type="text/javascript">window.addEventListener("resize", function(){window._Plotly.Plots.resize(document.getElementById("ad4c47c7-0ae0-45fb-8dc7-4d6710fcbed8"));});</script>


The above prices were found from online stores of Walmart, Monoprix, and Migros. It should be noted, that the dataset dominantly contains dairies and sweets with carbon footprint, so we hope to gain more insight of other products from the Carbon Footprint Eaternity dataset.


##### Is there a general correlation between high carbon footprint and price? 

Because the carbon footprint column of the OpenFoodFacts database contains a small amount of data, we will match OpenFoodFacts dataset with the sample given by Eaternity. The approach is the following :
    - Webscrap codeinfo website to get categories and parent categories of each product
    - Translate categories into english
    - Match categories of Open FoodFacts database with parent categories scraped from the website
    - Add the mean value of carbon footprint categories on Open Food Facts database
    


```python
#for the 30 most common categories
food_facts_pd.main_category.value_counts().head(30)
```




    Plant-based                    6795
    Dairies                        4830
    Sugary snacks                  3890
    Meats                          3675
    Beverages                      3062
    Frozen foods                   1623
    Meals                          1153
    Seafood                        1122
    Groceries                      1036
    Carbs                           862
    Salty snacks                    670
    Canned foods                    369
    Sandwiches                      197
    Desserts                        183
    Sweeteners                      139
    Fish And Meat And Eggs          128
    Baby Foods                      119
    Crêpes And Galettes             107
    Vinegars                         75
    Dietary Supplements              72
    Terrine                          64
    Breakfasts                       43
    Aliments-D-Origine-Vegetale      42
    Pet Food                         30
    Pies                             26
    Marzipan                         25
    Food Additives                   22
    Cooking Helpers                  22
    Fats                             21
    Allumettes De Porc               18
    Name: main_category, dtype: int64




```python
print('Taking into account 30 most important categories represents {0}% of the data'.format(sum(food_facts_pd.main_category.value_counts()[:30])/len(food_facts_pd.main_category)*100))
```

    Taking into account 30 most important categories represents 94.79884072423572% of the data


Dict done by hand to match main categories of the OpenFoodFact dataset with the one's found in the sample of Eternity. 


```python
dict_categories = {
   "Plant-based": ['vegetable mushrooms','fruit berries','soy saitan meat substitute','Grain','nuts','seeds koerner','legumes','nut plant milk'],
    "Dairies": ['Milk, dairy products, eggs','Cheese','ice creme pudding'],
    "Sugary snacks":'confectionery',
    "Meats": 'Fruit and vegetables Meat',
    "Beverages":['Fruit and vegetable juices','Wine and Sparkling Wine','Syrup','cocoa drinking chocolate','Coffee','Mineral water','lemonades refreshment drinks','Milkshakes'],
    "Meals":'fast food whole ready meals',
    "Seafood":'fish sea fruits',
    "Groceries":['mayo ketchup mustard','finished sauces fix products','SPREADS'],
    "Carbs":['rice couscous quinoa co','Baked goods','breadsticks','muesli cereals'],
    "Fish And Meat And Eggs":'Eggs.',
    "Baby Foods":'shred',
    "Aliments-D-Origine-Vegetale":['vegetable mushrooms','fruit berries'],
    "Cooking Helpers": ['cooking ingredients spices','baking ingredients']
}

```


```python
#computing carbon footprint mean for each parent category of Eaternity database
df_mean_carbon_eaternity = explore.carbon_mean_eaternity(carbon_footprint_pd)
```


```python
carbon_footprint_pd.category_en.value_counts()
```




    vegetable mushrooms             164
    cooking ingredients spices       73
    Fruit and vegetables Meat        49
    Milk, dairy products, eggs       41
    Baked goods                      35
    confectionery                    32
    breadsticks                      32
    rice couscous quinoa co          22
    Cheese                           21
    muesli cereals                   17
    fast food whole ready meals      17
    shred                            17
    mayo ketchup mustard             16
    fruit berries                    14
    ice creme pudding                14
    finished sauces fix products     12
    Fruit and vegetable juices       12
    fish sea fruits                  12
    baking ingredients               11
    soy saitan meat substitute       10
    Grain                             8
    legumes                           7
    nuts                              7
    seeds koerner                     7
    SPREADS                           7
    nut plant milk                    6
    Wine and Sparkling Wine           4
    Syrup                             4
    cocoa drinking chocolate          3
    Eggs.                             2
    Coffee                            2
    Mineral water                     1
    Facial skincare                   1
    lemonades refreshment drinks      1
    Milkshakes                        1
    Name: category_en, dtype: int64




```python
df_mean_carbon_openff = explore.carbon_mean_openff(dict_categories,df_mean_carbon_eaternity)
```


```python
df_mean_carbon_openff
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Plant-based</th>
      <th>Dairies</th>
      <th>Sugary snacks</th>
      <th>Meats</th>
      <th>Beverages</th>
      <th>Meals</th>
      <th>Seafood</th>
      <th>Groceries</th>
      <th>Carbs</th>
      <th>Fish And Meat And Eggs</th>
      <th>Baby Foods</th>
      <th>Aliments-D-Origine-Vegetale</th>
      <th>Cooking Helpers</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>96.048595</td>
      <td>551.237408</td>
      <td>174.5</td>
      <td>622.714286</td>
      <td>411.807778</td>
      <td>230.941176</td>
      <td>299.583333</td>
      <td>1234.505265</td>
      <td>1061.1444</td>
      <td>219.5</td>
      <td>82.0</td>
      <td>2194.067109</td>
      <td>2301.950048</td>
    </tr>
  </tbody>
</table>
</div>




```python
food_facts_pd
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>code</th>
      <th>created_t</th>
      <th>created_datetime</th>
      <th>product_name</th>
      <th>quantity</th>
      <th>packaging</th>
      <th>brands</th>
      <th>categories_en</th>
      <th>origins</th>
      <th>...</th>
      <th>ingredients_text</th>
      <th>main_category</th>
      <th>energy_100g</th>
      <th>carbon-footprint_100g</th>
      <th>nutrition-score-fr_100g</th>
      <th>nutrition-score-uk_100g</th>
      <th>price_per_100g</th>
      <th>store_currency</th>
      <th>manufacturing_place</th>
      <th>purchase_places</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0000000274722</td>
      <td>1514659309</td>
      <td>2017-12-30 18:41:49</td>
      <td>Blanquette de Volaille et son Riz</td>
      <td>NaN</td>
      <td>carton,plastique</td>
      <td>Comme J’aime</td>
      <td>Meals,Meat-based products,Meals with meat,Poul...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Riz précuit 40,4 % (eau, riz, huile de colza, ...</td>
      <td>Meats</td>
      <td>450.0</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>France</td>
      <td>France</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0000000394710</td>
      <td>1484497370</td>
      <td>2017-01-15 16:22:50</td>
      <td>Danoises à la cannelle roulées</td>
      <td>1.150 kg</td>
      <td>Frais</td>
      <td>Kirkland Signature</td>
      <td>Sugary snacks,Biscuits and cakes,Pastries</td>
      <td>France</td>
      <td>...</td>
      <td>Ingrédients: Pâte (farine, eau, beurre, sucre,...</td>
      <td>Sugary snacks</td>
      <td>1520.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>France</td>
      <td>France</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>0000010090206</td>
      <td>1370977431</td>
      <td>2013-06-11 19:03:51</td>
      <td>Thé de Noël aromatisé orange-cannelle</td>
      <td>75 g</td>
      <td>aluminium</td>
      <td>Alice Délice</td>
      <td>Plant-based foods and beverages,Beverages,Plan...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Thé noir de Chine, zestes d'oranges 7,5 %, arô...</td>
      <td>Beverages</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>France</td>
      <td>France</td>
    </tr>
    <tr>
      <th>10</th>
      <td>10</td>
      <td>0000027533048</td>
      <td>1418732915</td>
      <td>2014-12-16 12:28:35</td>
      <td>Luxury Christmas Pudding</td>
      <td>907g</td>
      <td>plastic,bowl</td>
      <td>Asda,Asda Extra Special</td>
      <td>Sugary snacks,Desserts,Biscuits and cakes,Cake...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Demerara Sugar, Sultanas (14%), Raisins (9.4%)...</td>
      <td>Sugary snacks</td>
      <td>1284.0</td>
      <td>NaN</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>France</td>
      <td>France</td>
    </tr>
    <tr>
      <th>13</th>
      <td>13</td>
      <td>0000204286484</td>
      <td>1483099966</td>
      <td>2016-12-30 12:12:46</td>
      <td>Mehrkomponeneten Protein 90 C6 Haselnuß</td>
      <td>2,5 kg</td>
      <td>bucket</td>
      <td>allfitnessfactory.de</td>
      <td>Dietary supplements,Bodybuilding supplements,P...</td>
      <td>France</td>
      <td>...</td>
      <td>Proteinmischung (_Sojaprotein_, _Weizenprotein...</td>
      <td>Dietary Supplements</td>
      <td>1533.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>France</td>
      <td>France</td>
    </tr>
    <tr>
      <th>17</th>
      <td>17</td>
      <td>000031</td>
      <td>1468014954</td>
      <td>2016-07-08 21:55:54</td>
      <td>Cakes aux Fruits</td>
      <td>600 g</td>
      <td>Boîte,Carton,Sachet,Plastique</td>
      <td>Bijou</td>
      <td>Sugary snacks,Desserts,Biscuits and cakes,Cake...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Fruits 37.4% [fruits confits 21,5% [fruits (pa...</td>
      <td>Sugary snacks</td>
      <td>1670.0</td>
      <td>NaN</td>
      <td>12.0</td>
      <td>12.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>France</td>
      <td>France</td>
    </tr>
    <tr>
      <th>21</th>
      <td>21</td>
      <td>0000501050603</td>
      <td>1484302351</td>
      <td>2017-01-13 10:12:31</td>
      <td>Whey Protein aus Molke 1000 Gramm Vanilla</td>
      <td>1000g</td>
      <td>bag</td>
      <td>allfitnessfactory.de</td>
      <td>Dietary supplements,Bodybuilding supplements,P...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Molkenproteinkonzentrat 99%(_Wheyproteinkonzen...</td>
      <td>Dietary Supplements</td>
      <td>1644.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>France</td>
      <td>France</td>
    </tr>
    <tr>
      <th>22</th>
      <td>22</td>
      <td>000051</td>
      <td>1480622364</td>
      <td>2016-12-01 19:59:24</td>
      <td>Fondants Citron</td>
      <td>660 g (30 étuis individuels)</td>
      <td>Boîte carton,Sachet Plastique</td>
      <td>Bijou</td>
      <td>Sugary snacks,Desserts,Biscuits and cakes,Cake...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Sucre, blanc d’_œufs_ frais, poudre d’_amande_...</td>
      <td>Sugary snacks</td>
      <td>1896.0</td>
      <td>NaN</td>
      <td>22.0</td>
      <td>22.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>France</td>
      <td>France</td>
    </tr>
    <tr>
      <th>25</th>
      <td>25</td>
      <td>00011686</td>
      <td>1424529249</td>
      <td>2015-02-21 14:34:09</td>
      <td>All Butter Sultana Cookies</td>
      <td>250 g</td>
      <td>Sachet,Plastique</td>
      <td>Marks &amp; Spencer</td>
      <td>Sugary snacks,Biscuits and cakes,Biscuits,Cook...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Farine de _blé_ contient _Gluten_ (avec Farine...</td>
      <td>Sugary snacks</td>
      <td>1866.0</td>
      <td>NaN</td>
      <td>21.0</td>
      <td>21.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>France</td>
      <td>France</td>
    </tr>
    <tr>
      <th>27</th>
      <td>27</td>
      <td>00011709</td>
      <td>1423389200</td>
      <td>2015-02-08 09:53:20</td>
      <td>All Butter Fruity Flapjack Cookies</td>
      <td>225 g e</td>
      <td>sachet,plastique</td>
      <td>Marks &amp; Spencer</td>
      <td>Sugary snacks,Biscuits and cakes,Biscuits,Cook...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Sucre • Beurre (_Lait_) (15%) • flocons d'_avo...</td>
      <td>Sugary snacks</td>
      <td>1887.0</td>
      <td>NaN</td>
      <td>21.0</td>
      <td>21.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>France</td>
      <td>France</td>
    </tr>
    <tr>
      <th>29</th>
      <td>29</td>
      <td>00011754</td>
      <td>1496652867</td>
      <td>2017-06-05 08:54:27</td>
      <td>Cookies Stem Ginger</td>
      <td>225 g</td>
      <td>barquette,plastique</td>
      <td>Marks &amp; Spencer</td>
      <td>Sugary snacks,Biscuits and cakes,Biscuits,Cookies</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Farine de _blé_ contient _Gluten_ (avec Farine...</td>
      <td>Sugary snacks</td>
      <td>1979.0</td>
      <td>NaN</td>
      <td>20.0</td>
      <td>20.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>France</td>
      <td>France</td>
    </tr>
    <tr>
      <th>31</th>
      <td>31</td>
      <td>00012444</td>
      <td>1494676312</td>
      <td>2017-05-13 11:51:52</td>
      <td>Sundae Mix</td>
      <td>10 L e (1 * 10 L e)</td>
      <td>Plastique,Carton</td>
      <td>McDonald's</td>
      <td>Desserts,Frozen foods,Frozen desserts,Ice crea...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>_Lait_ écrémé, sucre, _crème_, sirop de glucos...</td>
      <td>Frozen foods</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>United Kingdom</td>
      <td>France</td>
    </tr>
    <tr>
      <th>37</th>
      <td>37</td>
      <td>00024280</td>
      <td>1506504757</td>
      <td>2017-09-27 09:32:37</td>
      <td>All Butter Cookies</td>
      <td>NaN</td>
      <td>Boîte,métal,plastique</td>
      <td>Marks &amp; Spencer</td>
      <td>Sugary snacks,Biscuits and cakes,Biscuits,Dry ...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Wheatflour contains Gluten (With {nuti Wheatfl...</td>
      <td>Sugary snacks</td>
      <td>2096.0</td>
      <td>NaN</td>
      <td>20.0</td>
      <td>20.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>France</td>
    </tr>
    <tr>
      <th>41</th>
      <td>41</td>
      <td>00027083</td>
      <td>1509892689</td>
      <td>2017-11-05 14:38:09</td>
      <td>Made Without Wheat Blueberry Muffins</td>
      <td>230 g</td>
      <td>plastique</td>
      <td>Marks &amp; Spencer</td>
      <td>Sugary snacks,Biscuits and cakes,Cakes,Muffins...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>_Œufs_ de poules élevées en plein air pasteuri...</td>
      <td>Sugary snacks</td>
      <td>1515.0</td>
      <td>NaN</td>
      <td>12.0</td>
      <td>12.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>France</td>
      <td>France</td>
    </tr>
    <tr>
      <th>42</th>
      <td>42</td>
      <td>00028202</td>
      <td>1493552503</td>
      <td>2017-04-30 11:41:43</td>
      <td>Cornish Cruncher Cheddar &amp; Pickled Onion Hand ...</td>
      <td>150 g e</td>
      <td>sachet,plastique</td>
      <td>Marks &amp; Spencer</td>
      <td>Plant-based foods and beverages,Plant-based fo...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Pommes de terre - Huile de tournesol - Lait dé...</td>
      <td>Salty snacks</td>
      <td>2054.0</td>
      <td>NaN</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>United Kingdom</td>
      <td>France</td>
    </tr>
    <tr>
      <th>47</th>
      <td>47</td>
      <td>00031059</td>
      <td>1489173681</td>
      <td>2017-03-10 19:21:21</td>
      <td>Ultimate English Muffins</td>
      <td>308 g (4 * 77 g)</td>
      <td>Plastique,sachet,carton</td>
      <td>Marks &amp; Spencer</td>
      <td>Plant-based foods and beverages,Plant-based fo...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>NaN</td>
      <td>Plant-based</td>
      <td>1234.0</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>United Kingdom</td>
      <td>France</td>
    </tr>
    <tr>
      <th>49</th>
      <td>49</td>
      <td>00033046</td>
      <td>1419617980</td>
      <td>2014-12-26 18:19:40</td>
      <td>British Beef Braising Steak</td>
      <td>450 g</td>
      <td>tray - plastic, film - plastic</td>
      <td>Simply M&amp;S,Marks &amp; Spencer</td>
      <td>Meats,Beef</td>
      <td>Unknown</td>
      <td>...</td>
      <td>beef braising steak</td>
      <td>Meats</td>
      <td>615.0</td>
      <td>NaN</td>
      <td>-2.0</td>
      <td>-2.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>United Kingdom</td>
      <td>France</td>
    </tr>
    <tr>
      <th>55</th>
      <td>55</td>
      <td>00050319</td>
      <td>1535657067</td>
      <td>2018-08-30 19:24:27</td>
      <td>Blanche Drao</td>
      <td>75 cl</td>
      <td>bouteille verre</td>
      <td>Drao</td>
      <td>Beverages,Alcoholic beverages</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Malte d'orge</td>
      <td>Beverages</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>France</td>
      <td>France</td>
    </tr>
    <tr>
      <th>59</th>
      <td>59</td>
      <td>00071093</td>
      <td>1490121365</td>
      <td>2017-03-21 18:36:05</td>
      <td>Hollow Milk Chocolate Decorated R2D2 Figure</td>
      <td>215 g e</td>
      <td>Plastique,Boîte</td>
      <td>Marks &amp; Spencer,Disney</td>
      <td>Sugary snacks,Chocolates,Chocolate molds,Milk ...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Sugar, Dried Whole _Milk_, Cocoa Butter, Cocoa...</td>
      <td>Sugary snacks</td>
      <td>2245.0</td>
      <td>NaN</td>
      <td>25.0</td>
      <td>25.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Unknown</td>
      <td>France</td>
    </tr>
    <tr>
      <th>60</th>
      <td>60</td>
      <td>00071185</td>
      <td>1490121281</td>
      <td>2017-03-21 18:34:41</td>
      <td>Spiketail the dinosaur</td>
      <td>205 g e</td>
      <td>Plastique</td>
      <td>Marks &amp; Spencer</td>
      <td>Sugary snacks,Chocolates,Chocolate molds,Easte...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Sucre - _Lait_ en poudre entier - Beurre de ca...</td>
      <td>Sugary snacks</td>
      <td>2163.0</td>
      <td>NaN</td>
      <td>26.0</td>
      <td>26.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>United Kingdom</td>
      <td>France</td>
    </tr>
    <tr>
      <th>62</th>
      <td>62</td>
      <td>00073899</td>
      <td>1488619049</td>
      <td>2017-03-04 09:17:29</td>
      <td>Cornish Cove Cheddar</td>
      <td>200 g e</td>
      <td>Frais,Plastique</td>
      <td>Marks &amp; Spencer,M&amp;S</td>
      <td>Dairies,Fermented foods,Fermented milk product...</td>
      <td>France</td>
      <td>...</td>
      <td>Fromage cheddar cornish cove (_Lait_) • Piment...</td>
      <td>Dairies</td>
      <td>1720.0</td>
      <td>NaN</td>
      <td>15.0</td>
      <td>20.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>France</td>
      <td>France</td>
    </tr>
    <tr>
      <th>69</th>
      <td>69</td>
      <td>00088886</td>
      <td>1425925620</td>
      <td>2015-03-09 18:27:00</td>
      <td>British Self Raising Flour</td>
      <td>500 g e</td>
      <td>sachet,papier</td>
      <td>Marks &amp; Spencer</td>
      <td>Farines,Farines-avec-levures</td>
      <td>United Kingdom</td>
      <td>...</td>
      <td>Fortified British _Wheat_ Flour (_Wheat_ Flour...</td>
      <td>Farines</td>
      <td>1469.0</td>
      <td>NaN</td>
      <td>14.0</td>
      <td>14.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>United Kingdom</td>
      <td>France</td>
    </tr>
    <tr>
      <th>75</th>
      <td>75</td>
      <td>00099332</td>
      <td>1472742598</td>
      <td>2016-09-01 15:09:58</td>
      <td>Wrap Poulet à la Jamaïcaine</td>
      <td>231 g</td>
      <td>Plastique,Frais,Carton</td>
      <td>Marks &amp; Spencer</td>
      <td>Meals,Fresh foods,Sandwiches,Fresh meals,Poult...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Farine de _blé_ contient _Gluten_ (avec Farine...</td>
      <td>Meals</td>
      <td>811.0</td>
      <td>NaN</td>
      <td>-3.0</td>
      <td>-3.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Italy</td>
      <td>France</td>
    </tr>
    <tr>
      <th>78</th>
      <td>78</td>
      <td>0010248765135</td>
      <td>1541793569</td>
      <td>2018-11-09 19:59:29</td>
      <td>Yemina Semilla de melón</td>
      <td>200 g</td>
      <td>Bolsa de plastico</td>
      <td>Yemina</td>
      <td>Plant-based foods and beverages,Plant-based fo...</td>
      <td>Italy</td>
      <td>...</td>
      <td>Sémola de trigo duro, mezcla de vitaminas y mi...</td>
      <td>Carbs</td>
      <td>2.5</td>
      <td>NaN</td>
      <td>-6.0</td>
      <td>-6.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Italy</td>
      <td>France</td>
    </tr>
    <tr>
      <th>81</th>
      <td>81</td>
      <td>0011110020109</td>
      <td>1425363413</td>
      <td>2015-03-03 06:16:53</td>
      <td>Hamburger enriched buns</td>
      <td>12 oz</td>
      <td>Plastic,Bag</td>
      <td>Kroger</td>
      <td>Plant-based foods and beverages,Plant-based fo...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>ENRICHED _WHEAT_ FLOUR (FLOUR, MALTED BARLEY F...</td>
      <td>Plant-based</td>
      <td>1170.0</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Unknown</td>
      <td>France</td>
    </tr>
    <tr>
      <th>104</th>
      <td>104</td>
      <td>001256420004503</td>
      <td>1418728778</td>
      <td>2014-12-16 11:19:38</td>
      <td>Orange &amp; Cranberry Pudding</td>
      <td>900g</td>
      <td>plastic,bowl</td>
      <td>Sainsbury's,Sainsbury's Taste the difference</td>
      <td>Sugary snacks,Desserts,Biscuits and cakes,Cake...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Cranberries (18%) (Sugar, Cranberries, Sunflow...</td>
      <td>Sugary snacks</td>
      <td>1371.0</td>
      <td>NaN</td>
      <td>13.0</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>France</td>
      <td>France</td>
    </tr>
    <tr>
      <th>129</th>
      <td>129</td>
      <td>0014100097013</td>
      <td>1426276629</td>
      <td>2015-03-13 19:57:09</td>
      <td>Chocolate Chunk White Chocolate Macadamia Cris...</td>
      <td>204 g</td>
      <td>papier</td>
      <td>Chocolate Chunk,Pepperidge Farm</td>
      <td>Sugary snacks,Biscuits and cakes,Biscuits,Cookies</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Farine de _blé_ enrichie (farine, niacine, fer...</td>
      <td>Sugary snacks</td>
      <td>2167.0</td>
      <td>NaN</td>
      <td>26.0</td>
      <td>26.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Spain</td>
      <td>France</td>
    </tr>
    <tr>
      <th>146</th>
      <td>146</td>
      <td>0016000194304</td>
      <td>1541018430</td>
      <td>2018-10-31 20:40:30</td>
      <td>Fruit by the foot</td>
      <td>128 g</td>
      <td>Caja,Cartón</td>
      <td>Foot</td>
      <td>caramelo-sabor-a-frutas</td>
      <td>Unknown</td>
      <td>...</td>
      <td>sabor fresa, ingredientes: Azúcar, maltodextri...</td>
      <td>Caramelo-Sabor-A-Frutas</td>
      <td>1110.0</td>
      <td>NaN</td>
      <td>17.0</td>
      <td>17.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Unknown</td>
      <td>France</td>
    </tr>
    <tr>
      <th>149</th>
      <td>149</td>
      <td>0016000289987</td>
      <td>1531263894</td>
      <td>2018-07-10 23:04:54</td>
      <td>Betún sabor a vainilla</td>
      <td>453 gr</td>
      <td>Cartón</td>
      <td>Betty crocker</td>
      <td>betun</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Azúcar, aceite vegetal (aceite de palma), agua...</td>
      <td>Betun</td>
      <td>1750.0</td>
      <td>NaN</td>
      <td>24.0</td>
      <td>24.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>United States</td>
      <td>France</td>
    </tr>
    <tr>
      <th>151</th>
      <td>151</td>
      <td>0016000374201</td>
      <td>1531343473</td>
      <td>2018-07-11 21:11:13</td>
      <td>Betún sabor a queso crema</td>
      <td>340 gr</td>
      <td>Cartón</td>
      <td>Betty Crocker</td>
      <td>betun</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Azúcar, aceite vegetal (aceite de palma), agua...</td>
      <td>Betun</td>
      <td>1920.0</td>
      <td>NaN</td>
      <td>27.0</td>
      <td>27.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>United States</td>
      <td>France</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>40866</th>
      <td>40866</td>
      <td>9446314213469</td>
      <td>1453045243</td>
      <td>2016-01-17 15:40:43</td>
      <td>Col rizada Kale</td>
      <td>300 g</td>
      <td>Sin envase</td>
      <td>Verdcamp Fruits... es garantía,//Propiedad de:...</td>
      <td>Plant-based foods and beverages,Plant-based fo...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Col rizada de la variedad Kale. Categoría: I</td>
      <td>Plant-based</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40867</th>
      <td>40867</td>
      <td>94547160</td>
      <td>1461836234</td>
      <td>2016-04-28 09:37:14</td>
      <td>English Breakfast Marmalade</td>
      <td>500g</td>
      <td>Glass Jar</td>
      <td>Roses,Heinz Co Australia,Kraft Heinz,Kraft</td>
      <td>Plant-based foods and beverages,Plant-based fo...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Sugar, Oranges (47%) [Juice &amp; Peel (Contain Pr...</td>
      <td>Plant-based</td>
      <td>1150.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40868</th>
      <td>40868</td>
      <td>9501005000022</td>
      <td>1495705953</td>
      <td>2017-05-25 09:52:33</td>
      <td>18 Petits Beurre</td>
      <td>100 g</td>
      <td>Plastique</td>
      <td>SOCOBIS</td>
      <td>Sugary snacks,Biscuits and cakes,Biscuits,bisc...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Farine, sucre, graisses végétales, beurre, lac...</td>
      <td>Sugary snacks</td>
      <td>1808.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40869</th>
      <td>40869</td>
      <td>9501005000053</td>
      <td>1495265586</td>
      <td>2017-05-20 07:33:06</td>
      <td>Goldy</td>
      <td>65 g</td>
      <td>Plastique</td>
      <td>SOCOBIS</td>
      <td>Sugary snacks,Biscuits and cakes,Biscuits,Dry ...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Farine de blé, sucre, graisse végétale, beurre...</td>
      <td>Sugary snacks</td>
      <td>2540.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40870</th>
      <td>40870</td>
      <td>9501005000060</td>
      <td>1495270090</td>
      <td>2017-05-20 08:48:10</td>
      <td>Biscuit BIP</td>
      <td>18 g</td>
      <td>Plastique</td>
      <td>Socobis</td>
      <td>Sugary snacks,Biscuits and cakes,Biscuits</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Farine, sucre, matière grasses végétales, caca...</td>
      <td>Sugary snacks</td>
      <td>1832.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Unknown</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40875</th>
      <td>40875</td>
      <td>9501046018604</td>
      <td>1495012148</td>
      <td>2017-05-17 09:09:08</td>
      <td>THB</td>
      <td>50 cl</td>
      <td>Canette</td>
      <td>STAR</td>
      <td>Beverages,Alcoholic beverages,Beers</td>
      <td>Unknown</td>
      <td>...</td>
      <td>eau, malt d'orge, maïs, houblon</td>
      <td>Beverages</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40877</th>
      <td>40877</td>
      <td>9501046019304</td>
      <td>1495089635</td>
      <td>2017-05-18 06:40:35</td>
      <td>Eau Vive</td>
      <td>0,5 l</td>
      <td>Bouteille,Plastique</td>
      <td>STAR</td>
      <td>Beverages,Waters,Spring waters,Mineral waters,...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Eau de source naturelle d'Andranovelona</td>
      <td>Beverages</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40879</th>
      <td>40879</td>
      <td>9501046025206</td>
      <td>1495012780</td>
      <td>2017-05-17 09:19:40</td>
      <td>GOLD</td>
      <td>50 cl</td>
      <td>Canette aluminium</td>
      <td>STAR</td>
      <td>Beverages,Alcoholic beverages,Beers</td>
      <td>Unknown</td>
      <td>...</td>
      <td>eau, malte d'orge, maïs, sucre, houblon</td>
      <td>Beverages</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Italy</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40880</th>
      <td>40880</td>
      <td>9501100333636</td>
      <td>1495011633</td>
      <td>2017-05-17 09:00:33</td>
      <td>RANO VISY</td>
      <td>0,5 l</td>
      <td>Bouteille Plastique</td>
      <td>NaN</td>
      <td>Beverages,Carbonated drinks,Waters,Spring wate...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>eau minérale naturelle</td>
      <td>Beverages</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Italy</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40881</th>
      <td>40881</td>
      <td>9501100335890</td>
      <td>1495906708</td>
      <td>2017-05-27 17:38:28</td>
      <td>YOUPY Bacon</td>
      <td>20 g</td>
      <td>Plastique</td>
      <td>TAF</td>
      <td>Salty snacks</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Céréales, arômes, sel, colorants : E124, E132,...</td>
      <td>Salty snacks</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40883</th>
      <td>40883</td>
      <td>9501100335913</td>
      <td>1495268328</td>
      <td>2017-05-20 08:18:48</td>
      <td>YOUPI Frites</td>
      <td>40 g</td>
      <td>Plastique</td>
      <td>TAF</td>
      <td>Salty snacks</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Flocons de pomme de terre, arômes, sel, huile ...</td>
      <td>Salty snacks</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40886</th>
      <td>40886</td>
      <td>9501100337160</td>
      <td>1495017236</td>
      <td>2017-05-17 10:33:56</td>
      <td>THE SAHAMBAVY</td>
      <td>25 g</td>
      <td>Carton</td>
      <td>TAF</td>
      <td>Plant-based foods and beverages,Beverages,Hot ...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Thé noir nature de Sahambavy</td>
      <td>Beverages</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>United Kingdom</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40888</th>
      <td>40888</td>
      <td>9501100430021</td>
      <td>1495020797</td>
      <td>2017-05-17 11:33:17</td>
      <td>LAIT CONCENTRE KAOATRY</td>
      <td>390 g</td>
      <td>Conserve,Boîte,Aluminium</td>
      <td>SOCOLAIT</td>
      <td>Dairies,Evaporated milks</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Lait concentré, sucre, matières grasses végéta...</td>
      <td>Dairies</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40892</th>
      <td>40892</td>
      <td>9501100433084</td>
      <td>1495263452</td>
      <td>2017-05-20 06:57:32</td>
      <td>YAO Banane</td>
      <td>250 ml</td>
      <td>Bouteille,Plastique</td>
      <td>Socolait</td>
      <td>yaourts-a-boire-gout-banane</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Lait entier, lait écrémé, épaississant E1442, ...</td>
      <td>Yaourts-A-Boire-Gout-Banane</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40893</th>
      <td>40893</td>
      <td>9501100433138</td>
      <td>1495104142</td>
      <td>2017-05-18 10:42:22</td>
      <td>Yaourt Brassé Fraise</td>
      <td>100 g</td>
      <td>Boîte,Plastique</td>
      <td>Socolait</td>
      <td>Dairies,Fermented foods,Desserts,Fermented mil...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Lait frais 100 % partiellement écremé, sucre, ...</td>
      <td>Dairies</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40894</th>
      <td>40894</td>
      <td>9501100433152</td>
      <td>1495103991</td>
      <td>2017-05-18 10:39:51</td>
      <td>Yaourt Brassé Vanille</td>
      <td>100 g</td>
      <td>Boîte,Plastique</td>
      <td>Socolait</td>
      <td>Dairies,Fermented foods,Desserts,Fermented mil...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Lait frais 100 % partiellement écremé, sucre, ...</td>
      <td>Dairies</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40895</th>
      <td>40895</td>
      <td>9501100433176</td>
      <td>1495103772</td>
      <td>2017-05-18 10:36:12</td>
      <td>Yaourt Brassé Coco</td>
      <td>100 g</td>
      <td>Boîte,Plastique</td>
      <td>Socolait</td>
      <td>Dairies,Fermented foods,Fermented milk product...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Lait frais 100 % partiellement écremé, sucre, ...</td>
      <td>Dairies</td>
      <td>209.0</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40897</th>
      <td>40897</td>
      <td>9501100433251</td>
      <td>1495264099</td>
      <td>2017-05-20 07:08:19</td>
      <td>YAO Coco</td>
      <td>250 ml</td>
      <td>Bouteille,Plastique</td>
      <td>Socolait</td>
      <td>Beverages,Dairies,Fermented foods,Fermented mi...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>NaN</td>
      <td>Beverages</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40900</th>
      <td>40900</td>
      <td>9501100434388</td>
      <td>1495357332</td>
      <td>2017-05-21 09:02:12</td>
      <td>Fromage fondu à l'ail</td>
      <td>NaN</td>
      <td>Boîte,Plastique</td>
      <td>Socolait</td>
      <td>Spreads,Canned foods,Dairies,Fermented foods,S...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Fromage, sels de fonte, sels de cuisine, ails,...</td>
      <td>Dairies</td>
      <td>1054.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40901</th>
      <td>40901</td>
      <td>9501100992178</td>
      <td>1495446377</td>
      <td>2017-05-22 09:46:17</td>
      <td>CORN IKO</td>
      <td>120 ml</td>
      <td>Plastique</td>
      <td>IKO</td>
      <td>Desserts,Frozen foods,Frozen desserts,Ice crea...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Water, sugar, skimmed milk powder, vegetable o...</td>
      <td>Frozen foods</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40902</th>
      <td>40902</td>
      <td>9501100992314</td>
      <td>1495087651</td>
      <td>2017-05-18 06:07:31</td>
      <td>Glace Royale IKO</td>
      <td>1 l</td>
      <td>Boîte,Plastique</td>
      <td>IKO</td>
      <td>Desserts,Cremes-glacees,Desserts-glaces,Glaces...</td>
      <td>Peru</td>
      <td>...</td>
      <td>NaN</td>
      <td>Desserts</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40907</th>
      <td>40907</td>
      <td>9501101400177</td>
      <td>1495017831</td>
      <td>2017-05-17 10:43:51</td>
      <td>THE GLACE</td>
      <td>50 cl</td>
      <td>Bouteille,Plastique</td>
      <td>SAINTO</td>
      <td>Beverages,Iced teas,Peach flavored iced teas,S...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>100% eau de source naturelle Sainto, sucre, ar...</td>
      <td>Beverages</td>
      <td>80.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40909</th>
      <td>40909</td>
      <td>9503921235014</td>
      <td>1495703404</td>
      <td>2017-05-25 09:10:04</td>
      <td>JUTOP Cocktail</td>
      <td>1 l</td>
      <td>Bouteille,Plastique</td>
      <td>JUTOP</td>
      <td>Plant-based foods and beverages,Beverages,Plan...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>eau traitée, sucre, concentré d'ananas, goyave...</td>
      <td>Beverages</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40925</th>
      <td>40925</td>
      <td>9556041130943</td>
      <td>1480961884</td>
      <td>2016-12-05 18:18:04</td>
      <td>Huile de coco vierge bio Ayam™</td>
      <td>165 ml</td>
      <td>Bocal,verre</td>
      <td>Ayam</td>
      <td>huile-de-coco-biologique</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Huile de coco Biologique 100%</td>
      <td>Huile-De-Coco-Biologique</td>
      <td>3389.0</td>
      <td>NaN</td>
      <td>20.0</td>
      <td>20.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40927</th>
      <td>40927</td>
      <td>9556085302771</td>
      <td>1522006745</td>
      <td>2018-03-25 19:39:05</td>
      <td>Cream Crackers</td>
      <td>130 g</td>
      <td>plastique</td>
      <td>KERK</td>
      <td>Salty snacks,Appetizers,Crackers</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Farine de blé, Huile végétale (huile de palme)...</td>
      <td>Salty snacks</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40929</th>
      <td>40929</td>
      <td>9556156046399</td>
      <td>1459119179</td>
      <td>2016-03-27 22:52:59</td>
      <td>Boisson au soja (soy bean 8%)</td>
      <td>1 L</td>
      <td>Tetra Pak,Brique,tetra pak</td>
      <td>Yeo's</td>
      <td>Plant-based foods and beverages,Beverages,Plan...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Eau, extrait de _soja_ (_soja_ 8 %), sucre de ...</td>
      <td>Plant-based</td>
      <td>209.0</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40931</th>
      <td>40931</td>
      <td>9556174902202</td>
      <td>1413044592</td>
      <td>2014-10-11 16:23:12</td>
      <td>Quaker Quick Cooking Oatmeal</td>
      <td>800 g</td>
      <td>Bag</td>
      <td>Quaker</td>
      <td>Plant-based foods and beverages,Plant-based fo...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>100% Oats</td>
      <td>Plant-based</td>
      <td>1538.0</td>
      <td>NaN</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40934</th>
      <td>40934</td>
      <td>9556587103869</td>
      <td>1486235963</td>
      <td>2017-02-04 19:19:23</td>
      <td>Mini Paratha</td>
      <td>210 g</td>
      <td>carton,surgelé</td>
      <td>Kawan</td>
      <td>Plant-based foods and beverages,Plant-based fo...</td>
      <td>Germany</td>
      <td>...</td>
      <td>Farine de _blé_ (52%), eau, huile de palme, su...</td>
      <td>Plant-based</td>
      <td>1309.0</td>
      <td>NaN</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Germany</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40935</th>
      <td>40935</td>
      <td>96092514</td>
      <td>1410026342</td>
      <td>2014-09-06 17:59:02</td>
      <td>Blue Cheese Dressing</td>
      <td>250ml</td>
      <td>Glass,Bottle</td>
      <td>Newman's Own</td>
      <td>Groceries,Sauces,Salad dressings</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Rapeseed Oil, Water, Blue Cheese Stock 5% (con...</td>
      <td>Groceries</td>
      <td>2111.0</td>
      <td>NaN</td>
      <td>17.0</td>
      <td>17.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40939</th>
      <td>40939</td>
      <td>9876754344551</td>
      <td>1528096206</td>
      <td>2018-06-04 07:10:06</td>
      <td>Coffret de 10 Mini Cookies</td>
      <td>115 g</td>
      <td>Boîte,Carton,Refermable</td>
      <td>Pierre &amp; Tim Cookies,Pierre &amp; Tim</td>
      <td>Sugary snacks,Biscuits and cakes,Biscuits,Choc...</td>
      <td>Unknown</td>
      <td>...</td>
      <td>Farine de _blé_, beurre doux, _œufs_ entiers, ...</td>
      <td>Sugary snacks</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>France</td>
    </tr>
  </tbody>
</table>
<p>32089 rows × 23 columns</p>
</div>




```python
category = 'Meats'
#[food_facts_pd.main_category == category and food_facts_pd['carbon-footprint_100g']!=NaN]


(food_facts_pd.main_category == category) & (food_facts_pd['carbon-footprint_100g'] != None)
#(food_facts_pd['carbon-footprint_100g'] != None)
 
#(True & True) 
```




    0         True
    1        False
    7        False
    10       False
    13       False
    17       False
    21       False
    22       False
    25       False
    27       False
    29       False
    31       False
    37       False
    41       False
    42       False
    47       False
    49        True
    55       False
    59       False
    60       False
    62       False
    69       False
    75       False
    78       False
    81       False
    104      False
    129      False
    146      False
    149      False
    151      False
             ...  
    40866    False
    40867    False
    40868    False
    40869    False
    40870    False
    40875    False
    40877    False
    40879    False
    40880    False
    40881    False
    40883    False
    40886    False
    40888    False
    40892    False
    40893    False
    40894    False
    40895    False
    40897    False
    40900    False
    40901    False
    40902    False
    40907    False
    40909    False
    40925    False
    40927    False
    40929    False
    40931    False
    40934    False
    40935    False
    40939    False
    Length: 32089, dtype: bool




```python
#complete carbon footprint OpenFoodFacts
for category in dict_categories : 
    condition = ((food_facts_pd.main_category == category) & (food_facts_pd['carbon-footprint_100g'] != None))
    food_facts_pd['carbon-footprint_100g'][condition]=df_mean_carbon_openff[category][0]
    
 
```

    /home/kingkolibri/Programs/anaconda3/lib/python3.6/site-packages/ipykernel_launcher.py:4: SettingWithCopyWarning:
    
    
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
    



```python
food_facts_pd = food_facts_pd[food_facts_pd['carbon-footprint_100g'].notna() & 
                                  food_facts_pd['carbon-footprint_100g']!=0]
```


```python
visualize.plot_column_composition(df=food_facts_pd, column_str='manufacturing_place')
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>United Kingdom</td>
      <td>2411.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Unknown</td>
      <td>1794.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Italy</td>
      <td>913.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Germany</td>
      <td>738.0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Belgium</td>
      <td>710.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Spain</td>
      <td>410.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Netherlands</td>
      <td>264.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Switzerland</td>
      <td>111.0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>China</td>
      <td>109.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Greece</td>
      <td>90.0</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Thailand</td>
      <td>85.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bolivia</td>
      <td>81.0</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Poland</td>
      <td>79.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Morocco</td>
      <td>78.0</td>
    </tr>
    <tr>
      <th>52</th>
      <td>Taiwan</td>
      <td>65.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Portugal</td>
      <td>55.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Vietnam</td>
      <td>50.0</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Iran</td>
      <td>45.0</td>
    </tr>
    <tr>
      <th>66</th>
      <td>United States</td>
      <td>41.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Japan</td>
      <td>39.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Canada</td>
      <td>36.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Niger</td>
      <td>31.0</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Sweden</td>
      <td>26.0</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Turkey</td>
      <td>26.0</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Austria</td>
      <td>25.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Denmark</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>53</th>
      <td>Iceland</td>
      <td>21.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Sri Lanka</td>
      <td>21.0</td>
    </tr>
    <tr>
      <th>33</th>
      <td>United States Minor Outlying Islands</td>
      <td>21.0</td>
    </tr>
    <tr>
      <th>69</th>
      <td>Ireland</td>
      <td>21.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>87</th>
      <td>Cayman Islands</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>86</th>
      <td>Laos</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>84</th>
      <td>Senegal</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Moldova</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Dominican Republic</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>62</th>
      <td>New Zealand</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Costa Rica</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Lebanon</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>103</th>
      <td>Ukraine</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>100</th>
      <td>Togo</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>95</th>
      <td>Cyprus</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>104</th>
      <td>São Tomé and Príncipe</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>99</th>
      <td>Paraguay</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>98</th>
      <td>Papua New Guinea</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>105</th>
      <td>Saint Martin</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>97</th>
      <td>Colombia</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>96</th>
      <td>Myanmar</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>102</th>
      <td>Liechtenstein</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>57</th>
      <td>Namibia</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>93</th>
      <td>Eswatini</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>92</th>
      <td>Puerto Rico</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>90</th>
      <td>El Salvador</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Saint Barthélemy</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Serbia</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>79</th>
      <td>French Polynesia</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Saudi Arabia</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>75</th>
      <td>Finland</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Australia</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>59</th>
      <td>Macedonia</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>106</th>
      <td>Unknown</td>
      <td>1794.0</td>
    </tr>
  </tbody>
</table>
<p>107 rows × 2 columns</p>
</div>



<div id="7d1a71d8-b0c1-43d0-9abe-030850a77e8d" style="height: 300px; width: 800px;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("7d1a71d8-b0c1-43d0-9abe-030850a77e8d", [{"marker": {"color": "#F4B5A6", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "United Kingdom", "orientation": "h", "x": [2411.0], "y": [0], "type": "bar", "uid": "1132f038-f433-4a40-8820-debd91f45750"}, {"marker": {"color": "#F4EBA6", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Unknown", "orientation": "h", "x": [1794.0], "y": [0], "type": "bar", "uid": "6389f066-edfa-4373-bf62-c48ecae75dfa"}, {"marker": {"color": "#B2F4A6", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Italy", "orientation": "h", "x": [913.0], "y": [0], "type": "bar", "uid": "74dc50de-ece5-4028-a82a-a383cadd7898"}, {"marker": {"color": "#A6E3F4", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Germany", "orientation": "h", "x": [738.0], "y": [0], "type": "bar", "uid": "603a20f2-d505-42bd-8153-3230556a11b2"}, {"marker": {"color": "#C4A6F4", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Belgium", "orientation": "h", "x": [710.0], "y": [0], "type": "bar", "uid": "670c980a-21e4-46ae-88c7-23187fd6af2f"}, {"marker": {"color": "#E0DBDD", "line": {"color": "rgb(248, 248,249)", "width": 1}}, "name": "Others", "orientation": "h", "x": [3984.0], "y": [0], "type": "bar", "uid": "9885101f-f06b-487c-9117-771a4040f902"}], {"barmode": "stack", "height": 300, "showlegend": true, "title": "manufacturing_place", "width": 800, "xaxis": {"tickvals": [0, 5000, 10000, 10550.0]}, "yaxis": {"showgrid": false, "showline": false, "showticklabels": false, "zeroline": false}}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>



```python
# Food calories over carbon-foot print
visualize.plot_cluster_by_tags(df=food_facts_pd,
                               plot2D_features = ["carbon-footprint_100g", "price_per_100g"],
                               cluster="main_category")
```




**Thanks for Reading !**