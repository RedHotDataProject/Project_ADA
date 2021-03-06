
# RedHotDataProject

This page hosts our final project for the <i><a href="https://dlab.epfl.ch/teaching/fall2018/cs401/">Applied Data Analysis</a></i> course of the <a href="https://www.epfl.ch/en/home/">EPFL</a>.

<center><img src ="./Images/foot2.png"
    alt = ""
    style = "width:600px;height:325px;"
    class="center"/></center>



## Introduction

<p><div style="text-align: justify">
As we are writing this data story, the 24th UN Climate Change Conference in Katowice comes to an end. After two weeks of intense and heated discussions between member nations, a long overdue agreement was reached on how to implement cuts to global greenhouse gas emissions. The problem of global warming sometimes seems just overwhelming and out of our individual hands. But is it really the case? We strongly believe that each of us can play a part on this effort. With this journey, we want to explore what possibilities we, as a consumer, are presented with to limit our environmental impact. This story is centred on our eating habits, as we have all heard that a lot can be done by changing them. We want to leave out clues as to how optimise our food consumption to limit the damage our culture risk inflecting on the World.     
</div>
</p>

## Before the Story, the Cleaning ...

<p><div style="text-align: justify">
Our journey starts with a dataset, the crowdsourced <a href="https://world.openfoodfacts.org">Open Food Facts</a> dataset. This source of information is quite rich, with more than 710 000 food items sold in supermarkets all over the world, but, unfortunately, also suffers from heterogeneity, missing entries, a multitude of languages used and an absence or lack of standardisation for certain columns. After cleansing, translating and harmonising the data, we observe, for example, that about 40 000 products are sold in France.
    </div>
</p>

<p><div style="text-align: justify">
However, the database is still very sparse on carbon footprints and needs the further enrichment provided by a sample of 663 additional products from the <a href="http://www.eaternity.org">Eaternity</a> database that was offered to us by Manuel Klarmann, founder & CEO of the eponym project. We deeply thank him for this contribution to our project. 
    </div>
</p>

<p><div style="text-align: justify">
Another way to complement our sparse dataset consists in scraping from the web. We indeed harvested information about the product prices thanks to dedicated web crawler spanning the sites of Amazon, Monoprix, Migros, Kaufland, Cora, Coop and Walmart, as well as product categories for the Eaternity database from Codecheck. 
    </div>
</p>

<p><div style="text-align: justify">
Thanks to these cleansing steps, we gathered a modified version of the Open Food Database that is suitable to the task we set out to achieve. 
    </div>
</p>

### Producing and Manufacturing Our Food

<p><div style="text-align: justify">
Our first query, equipped with our brand new database, is to explore the distribution of the products information over the world. But do we have access to a truthful represention of the information over the entire world? Let's investigate by plotting the purchasing places of our dataset. 
</div>
</p>

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~maxencedraguet/39.embed" height="500" width="100%"></iframe>

<p><div style="text-align: justify">
Note how we mainly have data for "western" countries, with a <b>huge bias toward France</b>. We mostly lack information for countries in Africa, the Middle East and the centre of Asia. Our dataset is thus clearly not a truthful representation of the world. We shall therefore restrict the analysis to the case of France, since it is the most prevalent among the different columns. This means products are to be limited to those available for purchasing in France. This requirement is not an exclusive one: we do <b>not only</b> require them to be sold in France but to be <b>at least</b> available in France.
</div></p>

<p>
With these changes brought about, what can we say about the <b>origin countries</b>? </p>

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~maxencedraguet/43.embed" height="500" width="100%"></iframe>

<p>And the <b>manufacturing countries</b>? </p>

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~maxencedraguet/41.embed" height="500" width="100%"></iframe>

<p><div style="text-align: justify">
Interestingly, the distribution only seems to change for the developing world! Indeed, these tend to rather be exporting products of <i>origin</i> instead of <i>manufactured</i> ones. On the contrary, developed countries contribute in the exports of both types of categories. This is of course not a surprising fact: developed countries are industrial powerhouses.
</div></p>

<p><div style="text-align: justify">
Now that this restriction in the representation power of our database is established, let us attack the first part of the problem: <b>palm oil</b> in the food industry. 
</div>
</p>

## The Palm Oil Connection

<p><div style="text-align: justify">
The <a href="https://en.wikipedia.org/wiki/Social_and_environmental_impact_of_palm_oil">damaging effect of the over-production of palm oil</a> is a well-known issue popularised in the beginning of the century. Many problems arise from this intensive exploitation, among them deforestation, greenhouse gas emissions, water pollution and even social issues, such as appropriation of native lands.
</div></p>

<p><div style="text-align: justify">
Considering this globally negative press, we would expect a clear trend in the evolution of the number of products using this calamitous oil. What insights does our database offer on the subject? 
</div></p>

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~maxencedraguet/45.embed" height="375" width="100%"></iframe>

<p><div style="text-align: justify">
The data in the Open Food Facts started being gathered in 2012, which explains this start date of observation. Note how, after a flat behaviour, the palm oil usage noticeably decreased after 2015. For the palm-oil-history padawan, 2015 was a dramatic year of bad press for this type of oil with scandals in France surrounding  Nutella, dubbed the <i><a href="https://www.theguardian.com/environment/2015/jun/17/stop-eating-nutella-and-save-the-forests-urges-french-ecology-minister">#Nutellagate</a></i>, and palm oil production clearances linked to <a href="https://www.theguardian.com/sustainable-business/gallery/2015/dec/28/palm-oil-nutella-forest-fires-wildlife-deforestation-west-africa-india-2015-gallery">fires in Indonesia</a>. 
</div></p>

<p><div style="text-align: justify">
One could thus expect that products available in France and added during this year would have been more likely to have their palm oil content tagged! "One has to <i>observe</i> something in order to <i>see</i> it". The same explanation can be attributed to the previous years. The decrease following could have several explanation: </div></p>

<p>
- The optimist would conclude in a reduction in the use of palm oil.
</p>

<p><div style="text-align: justify">
- The pessimist (and sadly <a href="https://www.statista.com/statistics/263937/vegetable-oils-global-consumption/">realist</a>) would however conclude in a decrease in attention focused on palm oil, the subject going "out of fashion" but the palm trees still growing on freshly cleared exotic forestlands. 
</div></p>

<p><div style="text-align: justify">But what can we say about the manufacturing countries behind these palm-oil-containing products? </div></p>

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~maxencedraguet/73.embed" height="250" width="100%"></iframe>

<p><div style="text-align: justify">
Clearly, <b>France's neighbours</b> are its <b>biggest contributors</b> after, obviously, France itself, with the UK heading, followed by Germany, Italy (and its Nutella) and Belgium. Interestingly, the <a href="https://en.wikipedia.org/wiki/Palm_oil">main palm oil producers</a> (Indonesia, Malaysia, Nigeria, etc.) do not appear in this plot. They clearly do not generate the final product and naturally palm oil is not directly consumed but mostly part of a manufacturing process. As we saw earlier, these manufacturing hubs are mostly in developed countries explaining this distinction. 
</div></p>

<p><div style="text-align: justify">
Palm oil is thus visibly a product imported and manufactured in the developed world. Clearly, developed nations are well equipped to regulate the ecological impact palm oil inflicts on the world.
</div>
</p>

## A Nutritional Dilemna?

<p><div style="text-align: justify">
The meaning of the nutrition score index we shall be using can be found on the following <a href="https://world.openfoodfacts.org/nutriscore">page</a>, thanks to <a href="https://solidarites-sante.gouv.fr/IMG/pdf/rapport_Hercberg_15_11_2013.pdf">the work of Pr. Serge Hercberg</a>. The main facts are the following: 
</div></p>

<p><div style="text-align: justify">
- Products are marked according to the amount of nutrients they contain [per 100 g] and given a <b>grade between A and E </b>(A being obviously the best mark).
</div></p>

<p><div style="text-align: justify">
- Whether the product is solid or a beverage, it is assigned a nutrition score accordingly to that displayed on the next table. This score itself is computed in two parts. The first one considers the energy, saturated fat, sugars and sodium. A high level in that category is considered unhealthy. The second part reflects the proportion of fruits, vegetables and nuts, fibres and proteins for which high levels are considered beneficial to the health. The difference of these two parts in the order presented here gives a <b><i>nutritional scores</i></b> that is <b>better for low values</b>. 
</div></p>

<center><img src ="./Images/table.png"
    alt = ""
    style = "width:600px;height:380px;"
    class="center"/></center>

<p><div style="text-align: justify">
After running a small routine transforming the nutrition score into a nutrition mark, we first query the following histogram, displaying the number of products added per year by mark.
</div></p>

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~maxencedraguet/55.embed" height="525" width="100%"></iframe>

<p><div style="text-align: justify">
Clearly, a peak in the number of products added with a nutrition grade happened in 2015. However, the behaviour displayed here above matches that of the total number of product added to the database per year. Can we say something about the evolution of the relative weight of each mark through the years? 
</div></p>

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~maxencedraguet/57.embed" height="525" width="100%"></iframe>

<p><div style="text-align: justify">
Yes! Interestingly the levels are overall quite stable. Note however how the two best nutrition mark, <b><i>A</i></b> and <b><i>B</i></b>, slightly peaked during 2013. In 2018, this trend has reversed and their sum is now even smaller at 29% than in the beginning of the database history, when it was closed to 37%. This decrease has been matched by a similar increase in the less nutritionally favourable products, <b><i>D</i></b> and <b><i>E</i></b> gaining this 8% difference. 
</div></p>

<p><div style="text-align: justify">
One would therefore be tempted to state there has been a trend towards nutritionally poor products, with the average mark stable. However, it is important at this stage to remember that the dataset does not indicate anything about the popularity of a given product. It merely offers insights into information related to the product itself. Even though more products are added with a poor nutrition mark, it could be that the healthy and less diverse products are in fact more demanded in shops around France than the less ideal ones. The only <b>conclusion to be drawn? More products are added with a bad nutrition mark</b> than a good one. In this respect, food sellers, and of course the government, are the ones who could easily overturn the trend. But who are they? 
</div></p>

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~maxencedraguet/75.embed" height="250" width="100%"></iframe>


<p><div style="text-align: justify">
And unsurprisingly we find the <a href="https://www.statista.com/statistics/535415/grocery-market-share-france/">leaders in the French food retailer market</a>. Now that this trend has been observed, what can we say about the categories of products per mark? How do vegetables, meat, fishery and all fare in the eyes of Pr. Serge Hercberg's team?  
</div></p>

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~maxencedraguet/53.embed" height="525" width="100%"></iframe>

<p><div style="text-align: justify">
Naturally, <i>plant-based</i> products are overwhelmingly the most nutritionally favourable, occupying more than half of the mark <b><i>A</i></b>. They, as well as <i>carbs</i>, are less and less prevalent the worse the nutrition mark. On the opposite, <i>sugary snacks</i> are vastly more common in the bad sector of nutrition and become marginal when considering healthier standards. 
</div></p>

<p><div style="text-align: justify">
In the middle ground, <i>dairy</i>, <i>meat</i> and <i>seafood</i>. Surprisingly, what is commonly considered in Europe to constitute the main part of a meal is not the most nutritionally favourable. <i>Meat</i> is indeed well distributed among the different marks but does tend to peak at the lowest values of the nutrition index. <i>Dairy</i> performs slightly better, peaking in the lower part of the middle marks and finally, <i>sea-food</i> in the middle part.
</div></p>

<p><div style="text-align: justify">
This suggests a different approach to crafting <b>meals</b> and to <b>centre</b> them <b>around plant-based products and carbs</b> in order to embrace a <b>healthier lifestyle</b>. However, we should remember that human motivation is highly correlated to economical criteria. Note however that discussion is harder than it seems: for the same weight, different product may have a different feeding power. Eating a 100g of grapes does not bring the same impact on satiety than a 100g of meat. We shall however not take this point into consideration due to the limit of the information accessible to our curiosity and restrict our investigation to the price per 100g. What can our database offer as insights into the subject? 
</div>
</p>

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~maxencedraguet/77.embed" height="525" width="100%"></iframe>

<p><div style="text-align: justify">
Amazingly, even though our sample in this respect is very limited, it seems that these efficient nutritional products that <i>plant-based</i> and <i>carbs</i> are also happen to be ... among the cheapest! Even more striking, when considering the distribution regardless of the categories, <b>good nutritional products tend on average to have a <i>lower</i> price</b> than their less performing counterparts! So clearly the choice appears to be simple: what is best for your health seems to be best for your finance! But ... what about the environment?
</div>
</p>

## The Carbon Footprint

<p><div style="text-align: justify">
Let us now investigate the carbon footprint of different products and categories by exploring our modified Open Food Facts dataset. Indeed, the original one, restricted to France, only contained the information for a hundred different products with a heavy bias on their category. To remedy this lack of amplitude, we shall make good use of the Eaternity database sample, provided by Mr. Manuel Klarmann whom we deeply thank again, to enrich our modified version. The approach was to get the direct and parent categories of each product in the Eaternity sample by web scraping, translate them from German to English and then match these with the categories in the Open Food Facts. 
</div></p>

<p><div style="text-align: justify">
Common sense would suggest organic products are rarely manufactured and, due to their origin, inflicting a smaller footprint than the less nutritionally  favourable products such as sugary snacks and meat. Let's take a closer look at this. First, what can we say about the categories of the products possessing carbon footprint information? 
</div></p>

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~maxencedraguet/71.embed" height="300" width="100%"></iframe>

<p><div style="text-align: justify">
They unfortunately exhibit a bias towards <i>plant-based</i> products. We shall nonetheless keep it in such proportion since the last section suggested that category to be the most promising one for its nutritional and ecological impact. The category <i>Others</i> gathers products with a category name that did not match our Open Food Fact ones and is discarded in the next part of the analysis. 
</div></p>

<p><div style="text-align: justify">
Let us then observe the relation ship of carbon footprint and price per 100 g. This next plot displays a zoom of our data to make it easier to distinguish between categories. 
</div></p>

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~maxencedraguet/67.embed" height="525" width="100%"></iframe>

<p><div style="text-align: justify">
The two variables do not seem to be closely correlated: there are many inexpensive products with a heavy footprint and vice versa. Note however how clustered the plot is! Products of the same category tend to occupy a certain portion of this phase-space. Observe for example how <i>seafood</i>, <i>meat</i> and <i>dairies</i> occupy the heavy footprint area, <i>sugary snacks</i> cluster (such as chocolate at (200, 2.6)), how <i>carbs</i>, <i>plant-based</i> products and <i>beverages</i> (with tea as a notable outlier) concentrate around the low price low carbon footprint area. This last point is made evident when zooming even more on the origin.
</div></p>



<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~maxencedraguet/69.embed" height="525" width="100%"></iframe>

<p><div style="text-align: justify">
We therefore reach an interesting conclusion: <b>plant-based and carbs-full products are not only better in a nutritional sense, they are also superior in term of ecological impact!</b> Even better: considering our previous section and the first scatter plot, they seem to cost less on average than their meaty/fishy counterparts! 
</div>
</p>

And on this bombshell it is time to end this discussion ...

# <b>Thank you for following our journey ! </b>

<center><img src ="./Images/foot2_end.png"
    alt = ""
    style = "width:600px;height:325px;"
    class="center"/></center>



### Sources:

##### The Open Food Facts non-profit:
https://world.openfoodfacts.org/

##### Wikipedia:
https://en.wikipedia.org/wiki/Social_and_environmental_impact_of_palm_oil
    
https://en.wikipedia.org/wiki/Palm_oil

##### The Guardian:
https://www.theguardian.com/sustainable-business/gallery/2015/dec/28/palm-oil-nutella-forest-fires-wildlife-deforestation-west-africa-india-2015-gallery

https://www.theguardian.com/environment/2015/jun/17/stop-eating-nutella-and-save-the-forests-urges-french-ecology-minister

##### Statista:

https://www.statista.com/statistics/263937/vegetable-oils-global-consumption/

https://www.statista.com/statistics/535415/grocery-market-share-france/
