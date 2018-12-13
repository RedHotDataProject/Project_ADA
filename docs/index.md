
<img src ="./Images/foot2.png"
    alt = ""
    style = "float:left; margin-right: 10px;"/>


# RedHotDataProject

This page hosts our final project for the <i><a href="https://dlab.epfl.ch/teaching/fall2018/cs401/">Applied Data Analysis</a></i> course of the <a href="https://www.epfl.ch/en/home/">EPFL</a>.

## Abstract
Everything we do possess a certain carbon footprint, and our diet is of course no exception. From growing, farming, processing and packaging our food, energy and organic resources are consumed and released, which reflects in the emission of greenhouse gases, such as CO<sub>2</sub>. In this story, we explore the arcanes of the food industry, such as its manufacturing, product composition and sales, and delve into it's carbon emission as well as its nutrition standards of quality. Using the <a href="https://world.openfoodfacts.org">Open Food Facts</a> dataset as well as <a href="http://www.eaternity.org">Eaternity</a>'s, we present the carbon footprint repartition, starting on an understanding of the products, followed by the breakdown of production countries as well as point of sales and evaluating trends in diet composition, with a special focus on nutritionally high marked products in France and the UK. With this study, we want to provide a better understanding of the agri-food industry, and eventually help reducing carbon emissions by promoting a healtier product base for our consumption.

## Before the Story, the Cleaning ...

Our journey starts at the Open Food Facts dataset. This very rich source of information is unfortunately not a panacea: many entries are missing and overall every column lack uniformisation. The first step, after loading the interesting entries, was to harmonise these.

For example, the country names in the origin, manufacturing and purchasing address did not match a single language (<i>United-Kingdom, Royaume-Unis, ...</i>) nor a single format (<i>United-Kingdom, United Kingdom, UK, ...</i>). we leviated this problem thanks to a dedicated <a href="https://mledoze.github.io/countries/">database</a> that we manually enriched to encapsulate most of the entries we observed. 

This linguistic challenge was also met when we confronted the food categories both in the Open Food Facts and the Eaternity datasets. A sample of the last one was given to us by <b>Manuel klarmann</b>, founder & CEO of the project. We deeply thank him for his help. Adding this source was a necessary step because the original dataset only contained a very limited number of carbon-footprint entries and these were biased towards certain categories of product (such as <i>dairy</i>). 

Another way to enrich our very sparsed dataset consisted in scraping from the web. We harvested information about the product prices and, for Eaternity, categories thanks to dedicated web crawler spanning the sites of <i><a href="https://www.amazon.com">Amazon</a>, <a href="https://www.monoprix.fr">Monoprix</a>, <a href="https://search.migros.ch/de/q">Migros</a>, <a href="https://www.coradrive.fr/colmar/">Cora</a>, <a href="https://www.coop.ch/fr.html">Coop</a></i> and an <i> API</i> for  <i><a href="https://www.walmart.com">Walmart</a></i>.

Thanks to these cleansing steps, we gathered a modified version of the Open Food Database that was suitable to the task we were setting to achieve.

### Production / manufacture impact

Our first query with our brand new database was to explore the distribution of the products information over the world. This is presented here in three steps: we first observe the place(s) of origin of the product, then the manufacturing place(s) and finally the purchasing place(s). Note the plural form since these can sometime have links to different countries.

#### Distribution of origin places ? 

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~maxencedraguet/27.embed" height="525" width="100%"></iframe>


#### Distribution of manufacturings places  ? 

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~maxencedraguet/29.embed" height="525" width="100%"></iframe>


#### Distribution of pruchasing places  ? 

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~maxencedraguet/31.embed" height="525" width="100%"></iframe>

Note that we mainly have data for "western" countries, with a <b> huge bias toward France</b>. We mostly lack information for countries in Africa, the Middle East and the centre of Asia. Our dataset is thus clearly not a truthful representation of the world. We shall therefore restrict the analysis to the case of France, since it is the most prevalent among the different columns. This means products will be limited to those available for purchasing in France. Note that this requirement is not an exclusive one: we do <b>not only</b> require them to be sold in France but to be <b>at least</b> available in France.

Now that this restriction in the representation power of our database is established, let us attack the first part of the problem: <b>palm oil</b> in the food industry. 

## The Palm Oil Connection

The <a href="https://en.wikipedia.org/wiki/Social_and_environmental_impact_of_palm_oil">damaging effect of the over-production of palm oil</a> is a well-known issue popularised in the beginning of the century. Many problems arise from this intensive exploitation: deforastation, greenhouse gas emissions, water pollution and even social issues, such as appropriation of native lands.

Considering this globally negative press, we would expect a clear trend in the evolution of the number of products using this calomnious oil. Let us see this


https://www.theguardian.com/sustainable-business/gallery/2015/dec/28/palm-oil-nutella-forest-fires-wildlife-deforestation-west-africa-india-2015-gallery

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~maxencedraguet/13.embed" height="525" width="100%"></iframe>

The data in the Open Food Facts started being gathered in 2012 which explains this start of observation. Note how, after a slow increase, the palm oil usage in product drastically peaked in 2015. For the palm-oil-history padawan, 2015 was a dramatic year of bad press for this brand of oil with scandals in France surronding Nutella, dubbed the <i><a href="https://www.theguardian.com/environment/2015/jun/17/stop-eating-nutella-and-save-the-forests-urges-french-ecology-minister">#Nutellagate</a></i>, and palm oil production clearances linked to <a href="https://www.theguardian.com/sustainable-business/gallery/2015/dec/28/palm-oil-nutella-forest-fires-wildlife-deforestation-west-africa-india-2015-gallery">fires in Indonesia</a>. 

One could thus expect that products available in France and added during this year would have been more likely to have their palm oil content tagged ! "One has to <i>observe</i> something in order to <i>see</i> it". The decrease following could have several explanation: 
- The optimist would conclude in a reduction in the use of palm oil.
- The pessimist (and sadly <a href="https://www.statista.com/statistics/263937/vegetable-oils-global-consumption/">realist</a>) would however conclude in  a decrease in the attention focused on palm oil, the subject growing "out of fashion" but the palm trees still growing on freshly cleared exotic forest lands. 

But what can we say about the manufacturing countries behind these palm-oil-containing products ? Let us exclude the case of France, since most product sold in France are manufactured in ... France. 

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~maxencedraguet/15.embed" height="525" width="100%"></iframe>

<i>Unknown</i> maps places that were not identified during the cleansing. Clearly, <b>France's neighbours</b> are its <b>biggest contributors</b> with the UK heading, followed by Italy (and its Nutella), Germany and Belgium. Interestingly, the <a href="https://en.wikipedia.org/wiki/Palm_oil">main palm oil producers</a> (Indonesia, Malaysia, Nigeria, ...) do not appear in this plot. They clearly do not generate the final product and naturally palm oil is not directly consumed but mostly part of a manufacturing process. 

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~maxencedraguet/17.embed" height="525" width="100%"></iframe>

## The Nutritional dilemna

Meaning of the nutrition score index can be found on the following <a href="https://world.openfoodfacts.org/nutriscore">page</a>, thanks to the work of <a href="https://solidarites-sante.gouv.fr/IMG/pdf/rapport_Hercberg_15_11_2013.pdf">Pr. Serge Hercberg</a>. The main facts are the following : 
- Products are marked according to the amount of nutrients they contain [per 100 g] and given a <b>grade between A and E </b>(A being obviously the best mark).

<img src ="./Images/nutriscore.png"
    alt = ""
    style = "float:centre; width:400px;height:200px;"/>

- If the product is solid, it is assigned a nutrition score accordingly to that displayed on the next table. This score itself is computed in two parts. The first one considers the energy, saturated fat, sugars and sodium. A high level in that category is considered unhealthy. The second part reflects the proportion of fruits, vegetables and nuts, fibers and proteins for which high levels are considered beneficial to the health. The difference of these two parts in the order presented here gives a <b><i>nutritional scores</i></b> that is <b>better for low values</b>. 


<img src ="./Images/nutriscore_table.png"
    alt = ""
    style = "float:centre;"/>
 

## The Carbon Footprint

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~maxencedraguet/19.embed" height="525" width="100%"></iframe>

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~maxencedraguet/21.embed" height="525" width="100%"></iframe>

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~maxencedraguet/23.embed" height="525" width="100%"></iframe>

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~maxencedraguet/25.embed" height="525" width="100%"></iframe>

# <b>Thank you for following our journey ! </b>

## Sources:

https://world.openfoodfacts.org/

https://en.wikipedia.org/wiki/Social_and_environmental_impact_of_palm_oil
    
https://www.theguardian.com/sustainable-business/gallery/2015/dec/28/palm-oil-nutella-forest-fires-wildlife-deforestation-west-africa-india-2015-gallery

https://www.theguardian.com/environment/2015/jun/17/stop-eating-nutella-and-save-the-forests-urges-french-ecology-minister

https://www.statista.com/statistics/263937/vegetable-oils-global-consumption/

https://en.wikipedia.org/wiki/Palm_oil



```python

```
