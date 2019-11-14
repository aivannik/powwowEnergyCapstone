### Getting Vector data from Crop Census dataset
- See TestGDAL on Richard's Branch to see how this works...
- ~~Currently opens the landiq .gbb file and writes all the Santa Barbara county vectors into individual .json files~~
  - Converts all the features for Santa Barbara County into longitude and latitude polygons and inserts them into the psql database under the table called "sbvectors"
  - Now also includes an ID number, acres and crop info

## To run:
-```python ExtractVetorData.py```
- Needed to install psycopg2:
  - ```conda install -c anaconda psycopg2```
- Also the .gbd path will depend on your system
- You will also need a database.ini file in order to connect the psql database  
## FOR OTHER COUNTIES:
- To change the county change these line:
  - ```Layer.SetAttributeFilter("County = 'Santa Barbara'")```
  - ``` cur.execute("""INSERT INTO sbvectors2 ( id, crop, acres, coordinates ) VALUES (%s, %s, %s, %s) """, (IndexNumber, Crop, Acres, json.dumps(CoorJson))) ```
    - Make sure the table has already been set up in this style:
    - ```CREATE TABLE sbvectors2 (id INT, crop VARCHAR(100), acres FLOAT, coordinates JSON);
 ```
