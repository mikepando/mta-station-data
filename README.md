# MTA Station Data
This is a project utilizing Flask and Pandas to search the MTA website for metrocard "swipe" data at each of the city's subway stations.

* [MTA Fare Data](http://web.mta.info/developers/fare.html) - Contains public fare data files
* [Description File](http://web.mta.info/developers/resources/nyct/fares/fare_type_description.txt) - Describes the fields in the dataset

### Prerequisites
The only requirement needed to run this project file is:
```
A python interpreter (I used Spyder IDE)
```

## How to Run
1. Create a new directory.
2. Place the ```server.py``` file, as well as the ```static``` and ```template``` folders within the new directory.
3. Make sure ```stationList.py``` is located in the same directory as the ```server.py``` file. This is a list of available stations the ```main_page.html``` page uses to display station names. 
4. Open the ```server.py``` file in your python interpreter and run/execute the code.
5. You can access the web page at http://localhost:5001/.
6. Select the criteria and search the database. 

## Built With
* [Spyder](https://www.spyder-ide.org/) - The python interpreter used
* [Flask](http://flask.pocoo.org/) - Microframework used for local server
* [Pandas](https://pandas.pydata.org/) - Library used for plots

## Disclaimer
This was made for educational purposes. It was for the CIS 431 Design and Analysis course at Manhattan College. 
