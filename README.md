# Temperature Analysis Program

In my current Job as a controls systeme engineer we specialise in the thermal welding of plastics. I used this background as my inspiration for the idea for the project. After every Cycle of Temperature increase to perform welding data points are to be taken at set timed intervals. These data points can then be loaded into this Temperature Analysis Program for further analysis. 

<br />
<br />

The project will allow for the user to,

- Input data -  10 temperature values that are to be processed with calculations and the data to be stored in google Sheet
- Retrieve Data from a google sheets by calling a specific index number.
- View data summary of requested data.

<br />
<br />

Some examples of the data that can be input, 

- 10,30,50,120,200,220,222,221,220,50
- 40,90,110,120,200,225,222,221,220,20
- 25,30,50,120,200,220,222,221,220,50

<br />
<br />

Sample of the Result the user can expect from the data analysis

- Start Temperature : 10
- End Temperature : 50
- Average : 134.3
- Max Temp : 222
- Min Temp :10
- Range : 212
  
<br />
<br />


## Program Flow Chart 

### Program Flow can be seen in Flow Chart Below
<br />
<p >
  <img src="Readme_Img/Flowchart.png" width="800"  height="800" title=" program flow chart">
</p>

<br />
<br />


## Program Questions / Queries - Screen Step Through 
<br />

###  Step 1 : Intro Message 
<br />

<p >
  <img src="Readme_Img/temp_analysis_intro.png" width="700"  height="400" title=" program flow chart">
</p>
<br />

- The intro gives the user a brief description of what the program does and what they can expect

- Then the User is prompted with the first quesiton they can answer using the Y or N keys
<br />
<br />

### Step 2 : User Selects "Y"
<br />

<p >
  <img src="Readme_Img/input_values.png" width="700"  height="250" title=" program flow chart">
</p>


- The User selects Y  and wants to input new Temperature Readings 
- User is then prompted to input data - with some info as to what is required.
<br />
<br />

### Step 3 : Succesful Data Entry from User 
<br />

<p >
  <img src="Readme_Img/data_ok.png" width="700"  height="250" title=" program flow chart">
</p>

- The User inputs the correct the data - Program informs them Data Ok.
- Program stores data in Sheet.
- Program runs Data analysis of input data and show input.
<br />
<br />

### Step 4 : Program Begins Loop Again 
<br />

<p >
  <img src="Readme_Img/Program_Loop.png" width="700"  height="120" title=" program flow chart">
</p>

- Programs Restarts without the long intro message 
<br />
<br />

### Step 5 : User Selects "N" 
<br />

<p >
  <img src="Readme_Img/Retrieve_Question.png" width="700"  height="120" title=" program flow chart">
</p>

- When user answers "N" The program then asks them to they want to retrieve data for Google Spread Sheets
<br />
<br />

### Step 6 : User Selects "Y" to Retrieve Question
<br />

<p >
  <img src="Readme_Img/Input_Retrieve.png" width="700"  height="120" title=" program flow chart">
</p>

- User is prompted to select an index value to retireve data options are 1-10 
<br />
<br />

### Step 7 : Data Gets Retrieved and Programs Gives Data Anaylsis
<br />

<p >
  <img src="Readme_Img/Retrieved_Data.png" width="700"  height="250" title=" program flow chart">
</p>


- Once the Data Gets Retrieved the Programs Gives Data Anaylsis and Program Agains loops back to Start
<br />
<br />


## Error Input Handling 
<br />

## Error Inputs Y or N

<p >
  <img src="Readme_Img/Fail_Y_N.png" width="700"  height="350" title=" program flow chart">
</p>

- If user inputs Wrong data to the Y or N Questions they get the message,
  "You have entered incorrect data - Please Enter Y or N "

- After Inputting wrong data wrong 3 times User gets a Low Caffiene Level Warning and is advised to 
  top up caffiene levels and come back later whilst more alert. 
<br />
<br />


## Error Inputs Temperature Values - Data Type 

<p >
  <img src="Readme_Img/Error_Data_Type.png" width="700"  height="350" title=" program flow chart">
</p>

- Example If user inputs Wrong data aka String instead of Int
<br />
<br />


## Error Inputs Temperature Values - Incorrect Amount of Values 

<p >
  <img src="Readme_Img/error_amount.png" width="700"  height="350" title=" program flow chart">
</p>

- Example If user inputs 9 values by mistake instead of 10
 
<br />
<br />

## Deployment - Heroku 

For deployment of this project we used the Heroku platform. Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
<br />

### Step 1 - Adding Build Packages 

<p >
  <img src="Readme_Img/Heroku_BuildPacks.png" width="700"  height="350" title=" program flow chart">
</p>

- Python Package 
- Node JS 
<br />
<br />

### Step 2 - Manual Deployment 

<p >
  <img src="Readme_Img/Manual_Deploy.png" width="700"  height="350" title=" program flow chart">
</p>

- Select program as git hub and link git hub account 
- Select Temperatures analysis program
- Go to Manual Deplay and Build package 
<br />
<br />

## Testing & Validation   
<br />


- Validator recommend to use was down at the time of validation occurring. 
- Students were advised to perform this work around. 
- These steps were carried out as per instructions in git hub enviroment. 

<p >
  <img src="Readme_Img/Pep8_Workaround.png" width="700"  height="350" title=" program flow chart">
</p>

<br />
<br />

- Also Validated code on other validators - code came bakc as "Good" with some white space removal hints. 

<p >
  <img src="Readme_Img/Validator.png" width="700"  height="350" title=" program flow chart">
</p>

<br />
<br />

### Technical assitance credits 

Credits List

<br />
<br />

- Credit 1 - Info used for working with gSpread

- Link 1 -  https://docs.gspread.org/en/latest/user-guide.html

<br />
<br />

- Credit 2 - Info for converting list data type to all integers

- Link 2 -  https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/

<br />
<br />

- Credit 3 - Copied Code used for Switch/Case Function in programs 

<br />

     switch(lang):
<br />

    if lang == "JavaScript":

<br />

        return "You can become a web developer."
    elif lang == "PHP":

<br />
       return "You can become a backend developer."

<br />

- Link 3 -  https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/

<br />
<br />

- Credit 4 - Copied Code used to insert data to Sheet  - "sheet1.update("A8:C8", [["Texas", 5261485, 5261485]]" 

<br />


- Link 4 - https://www.codeforests.com/2020/11/22/gspread-read-write-google-sheet/

<br />
<br />

### Inspitation Assistance for applications

- HTE Emerson Technology applications 

<br />
<br />


### Other mentions

Special thanks for Samantha Dartnall for her assistance and guidance throughout the project. 


-----
End

