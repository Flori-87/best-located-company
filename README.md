# Geoqueries to find the best location for a company

### Project goal
The goal of this project is to find the correct coordinates to place a company based on various employee requirements. To achieve this goal GeoJSON Point, sphere2d index and geospatial queries will be used.

### Input
The project will be performed using a dataset containing information about companies such as name, type of activity, number of employees, fundings, raised money. In addition, the location of the office(s) that company has - the most important information for this project - is also inside the dataset.

### Methods & Approach
First, to choose the city in which company will be placed, dataset columns cointaining info about location of offices and raised money will be cleaned and managed. Therefore, information about name of the city and coordinates will be got from column "offices" and total raised money will be unified based on currency as well as units. When dataset is clean, city where placing the company will be chosen based on:
  - More companies are placed
  - Successful tech startups (total raised amount greater than or equal to $1M)
  - Design companies are placed
  
and dataset will be filtered by this city. The requirements chosen for placing the company are to be close to:
  - Starbucks shops
  - Pubs
  - Vegan restaurants
  - Airports

To meet this requirements, information about these places will be obtained from Google API. This API returns information about name and coordinates among others for the requested places in a fixed radius from the requested location.

Finally, using Folium library and MongoDB, best coordinates will be searched. With location in GeoJSON Point format and sphere2d index, geoqueries will be performed through MongoDB to get the closest companies to the required shops/restaurants. Moreover, with the visualization tool Folium coordinates from companies and shops will be located in the map of the city.
