<h1>Apartment Price Prediction</h1>
<p>This project is designed for scraping data from <a href="bina.az">bina.az</a>, clean, analyze, and
    predict apartment prices using a pipelined XGBoost model. The end
    product is a local web application that allows users to explore and
    predict car prices based on a variety of features.</p> <h2>Project
    Structure</h2>   <table>
        <thead>
          <tr>
            <th>File/Folder</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>app.py</td><td>Main Flask app</td></tr>
          <tr><td>scraper.ipynb</td><td>Scrapes data from website</td></tr>
          <tr><td>load_data.ipynb</td><td>Converts scraped data to CSV</td></tr>
          <tr><td>preprocessing.ipynb</td><td>Cleans and transforms data</td></tr>
          <tr><td>visualization_data.ipynb</td><td>Visualizations and insights</td></tr>
          <tr><td>separating_data.ipynb</td><td>Splits data by car category</td></tr>
          <tr><td>cleaned_data.csv</td><td>Final preprocessed dataset</td></tr>
          <tr><td>README.md</td><td>Project documentation</td></tr>
        </tbody>   </table>
 <h4>Clone the Repository</h4>
    
    git clone https://github.com/narimanm0/Baku_Apartments.git
    cd Baku_Apartments 
  <h2>Project Workflow</h2>
  <h4>1. Data Scraping</h4>
  This notebook scrapes car listing data from the target website.
    
    def get_unique_item_ids(max_pages=500)
  Scrapes up to 500 pages of data to collect unique item IDs.
  
  <h4>2. Saving Scraped Data</h4>
    The scraped data is parsed and saved into a structured `.csv` file
    for further processing.
    
  <h4>3. Preprocessing</h4> Steps involved:
  
  -   Dropping irrelevant or redundant columns
  -   Renaming columns for clarity
  -   Applying LabelEncoding to categorical variables
  -   Creating new derived columns Final clean dataset is saved as cleaned_data.csv

<h4>4. Exploratory Data Analysis</h4>
Uses the cleaned data to generate visualizations and insights:
  
  -   Price distributions
  -   Feature correlations
  -   Category-based comparisons

<h4>5. Data Separation by Category</h4>
The dataset is split based on the `category` column. Each subset will be used to train a dedicated model for improved accuracy.

<h4>6. Model Training</h4>
For each category, an XGBoost model is trained using a Pipeline that includes:
  
  -   Preprocessing steps
  -   Feature transformations
  -   XGBoost Regressor

<h4>Run the Application</h4>
To launch the web application:
  
    python app.py
Then, open your browser and go to:
  
    http://127.0.0.1:3000
You'll see an interactive interface to explore features and predict apartment prices.

<h4>Tech Stack</h4>
  
  -   Python
  -   Jupyter Notebooks
  -   XGBoost
  -   Scikit-learn Pipelines
  -   Flask (for deployment)
  -   Pandas, NumPy, Matplotlib, Seaborn
  -   BeautifulSoup / Selenium (assumed for scraping)
  
  <h4>Contact</h4>
  For issues or questions, feel free to reach out via
  mail: <a href =
  "narimanmammadovv@gmail.com">narimanmammadovv@gmail.com</a>

