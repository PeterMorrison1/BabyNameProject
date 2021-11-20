# BabyNameProject

This project is intended to be a fun side-project over the course of ~2 days to analyze baby names using Streamlit.

I currently have it extracting USA baby names by state, but I was thinking of possibly introducing Canadian provinces (ones that supply baby names at least). Additionally, I added actors & characters from movies by year to compare with. I was thinking it would be interesting to see the popularity of "Leonardo" as a name and compare it to release dates of movies that star a Leonardo actor or character. This was mostly inspired by seeing the name Daenerys become popular around a year after the Game of Thrones show aired. 

To run this project you should be able to clone the project, `pip install -r requirements` and run `streamlit run app.py`. To run the extracting code you would run the command `python setup.py install` then run the file `manual_download_usa_names.py` - this is because the extractor code is installed as a module.

This project will be available through Streamlit cloud as it is a public repo [at this link](https://share.streamlit.io/petermorrison1/babynameproject/main/app.py).

Overall, this project may get a few updates, but I wanted to constrain it to only a few days of work both as a challenge and for fun before starting on some other larger projects. 

# Attributions
* USA Name data from: [USA Social Security Administration - Beyond the Top 1000 Names](https://www.ssa.gov/oact/babynames/limits.html)
* Amazing UI tool that made this project so easy/quick: [Streamlit Python Visualization Library](https://streamlit.io/)
* Movie/Actor list: [Kaggle Dataset by Stefano Leone](https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset?select=IMDb+movies.csv)
* All other libraries used can be found in the requirements.txt

# Future Leads:
* Quebec API for baby names: [Boy names page](https://www.donneesquebec.ca/recherche/dataset/banque-de-prenoms-garcons) - [Girl names](https://www.donneesquebec.ca/recherche/dataset/banque-de-prenoms-filles) - [Example API Call](https://www.donneesquebec.ca/recherche/api/3/action/package_show?id=bec46ea8-7bd1-4d81-b9e0-ea9f3ba0c59d)
* Ontario baby names: [Boy names](https://data.ontario.ca/dataset/ontario-top-baby-names-male) - [Girl names](https://data.ontario.ca/dataset/ontario-top-baby-names-female)
* Alberta baby names: [Both sex](https://open.alberta.ca/opendata/frequency-and-ranking-of-baby-names-by-year-and-gender)
* British Columbia baby names: [Both sex, 2 links](https://www2.gov.bc.ca/gov/content/life-events/statistics-reports/bc-s-most-popular-baby-names)
