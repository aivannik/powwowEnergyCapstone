### Getting Vector data from Crop Census dataset
- See TestGDAL on Richard's Branch to see how this works...
- ~~Currently opens the landiq .gbb file and writes all the Santa Barbara county vectors into individual .json files~~
  - Converts all the features for Santa Barbara County into longitude and latitude polygons and inserts them into the psql database under the table called "sbvectos"
- Also the .gbd path will depend on your system
- To run:
  -```python ExtractVetorData.py```
- Needed to install psycopg2:
  - ```conda install -c anaconda psycopg2```
## TODO:
  - Need to label these vectors, maybe include crop information with polygon data
