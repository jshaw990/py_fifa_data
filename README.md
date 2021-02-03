# Fifa 19 Wage vs. Value Data Visualization
A Bokeh scatterplot designed to assist in the analysis of wage vs. value of the players available within [Fifa 19](https://www.ea.com/games/fifa/fifa-19). 

The data is derived from the Kaggle user [Karan Gadiya](https://www.kaggle.com/karangadiya/fifa19)

The scatterplot includes the ability to zoom with both mouse wheel or box-area selection, pan, and save the plot as a .PNG file for usage outside of this project. 

## Author
[Jayden Shaw](https://github.com/jshaw990/)

## Tools Used
- Python3
- Pandas
- Seaborn
- Bokeh
- Kaggle

## Usage
- [Fork](#) or [download](#) this repository
- Install [Python3](https://www.python.org/downloads/)
- Install requirements from *requirements.txt*:
    - `pip3 install -r requirements.txt`
- Run the Python3 script: `python3 fifa_analysis.py`
- A browser window will open displaying the scatterplot, and an external HTML file will be saved within the [output folder](output)
- Items within the toolbar can be accessed on hover of the scatterplot
- A PNG image can be saved to your default browser downloads folder using the *save icon* displayed in the tool bar

## Known Issues
- Currency for Wage/Values are displayed with the dollar sign rather than the Euro sign - this is due to limitations in place with Bokeh.