# APPLE STOCK DATASET PROCESS 

The purpose of this document is to present how to set up the environment and run the project to process an Apple stock dataset.
- Set up and run project
- Project structure
- Technical explanation
## Setup and Run the project
The project could be run from Docker image or directly from python. 
### Run from Docker image
We need Docker desktop, you can download it from https://www.docker.com/products/docker-desktop
Steps to build an image and run it as below:
- Build Docker Image
``` docker build -t process .```
- Run and create a container “apple_stock”
``` docker run  -p 8080:8080 --name apple_stock process ```
### Run from source code.
To install the environment and run the project, follow these general steps:
#### Set up Environment:
- Install Python: Ensure Python is installed on your system. You can download it from python.org.
- Create a Virtual Environment (optional but recommended): Navigate to the  project folder in the terminal and run:
``` python -m venv venvpython -m venv venv```
- Activate the virtual environment:
- - On Windows: venv\Scripts\activate
- - On macOS/Linux: source venv/bin/activate
- Install Dependencies:
Navigate to your project folder where the requirements.txt file is located.
Run the following command to install dependencies:
``` pip install -r requirements.txtpip install -r requirements.txt```
- Run the Project:
- - Execute the main file or command to start your project. 
```python process.py```

## Project structure 
The project includes the following components:
- data_source: This is the location that stores the data source.
- data_output: This is the location that saves the output results of the data.
- src: contents all source code
- tests: contents all test cases
- regression: content all gold files for testing
- Dockerfile: This file is used to create a Docker image.
- setup.py: is for creating pip install package
- app.py: is an sample of using the stock_analyzer lib after installation

## Build pip installation library
go into the project folder, apple_stock, and run the command:
```python setup.py bdist_wheel sdist```
to use the library, we need to install it into the venv with pip install command:
- active the venv
- go the apple_stock folder project and run the pip command:
 ```pip install .```
- run ```pip freeze``` to confirm the lib installed ```StockAnalyzer @ file:///Users/tramln/working/apple_stock```

## Technical explanation 
The project is compatible with Python version 3.8 and necessitates specific libraries outlined below.
- Pandas 2.1.4
- Pandas_schema 0.3.6
- Dash 2.14.2
- Plotly 5.18.0
the data will undergo the following steps:
1. Cleaning and validating data
2. Transforming data
3. Aggregating data
4. Generating metrics
5. Visualizing data through a candle chart graph.


#### Cleaning and validating data :
For the Apple stock dataset, certain rules should be applied to the data.
- Date : has format yyyy-mm-dd and should be Monday → Friday and no duplicate
- Price : is integer positive
- Adjust : is integer and can be negative
- Direction : should have data in [“Increasing”,”Decreasing”] 
- All columns are non-null 

I use pandas_schema.validation and CustomElementValidation to validate those rules above by define function to check those rules and use lambda function to apply each column 
- With duplicate Date value : I use function duplicated to check 
- With data does not match with the rule or duplicate will be extract and save to error file and save at data_output directory 



#### Transforming data :

I added two more columns 
- day_of_week :  ``` pd.to_datetime(df['Date']).dt.day_name()``` to get day of week (Monday , Tuesday ….)
- Week_of_year : ``` pd.to_datetime(df['Date']).dt.strftime('%Y%U')``` to get week of year . Ex: 201508 it means the eighth week of 2015 . Because I will use this column to aggregate data for the week.





#### Aggregate data and generate metric :

I use mean(), min() , max() function to aggregate APPL_Close price .



I calculated average of  Volume and then find all of records greater than that value then save those rows to file 




I generate metric with week level and aggregate with mean value for 
Columns “APPL.Close” , “APPL.Low”,“APPL.High”,“APPL.Open”


#### Graph Data 

I use dash , plotly package to plot data with candle chart with daily chart and weekly chart 
With daily chart : 
Axis x is Date 
Open is APPL.open
Close is APPL.close
Hight is APPL.high
Low is APPL.low

With daily weekly chart :

Axis x is weekof_year 
Open is APPL.open(mean of week)
Close is APPL.close(mean of week)
Hight is APPL.high(mean of week)
Low is APPL.low(mean of week)


