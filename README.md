# Coffee Recommender

This repository contains notebooks for a personal project on recommending coffee bags using cosine similarity based on numeric attributes and textual descriptions. The project is divided into two main parts: data cleaning and analysis/recommendation.

## Project Structure

- `cleaning.ipynb`: Notebook for data cleaning and preprocessing.
- `analysis.ipynb`: Notebook for implementing the recommendation system and analyzing the results.
- `data/`: Directory for storing raw and cleaned data files.

## Requirements

- Python 3.x
- Jupyter Notebook
- pandas
- scikit-learn

## Setup

1. Clone the repository:

    ```sh
    git clone https://github.com/AlanKha/Coffee-Recommender.git
    cd Coffee-Recommender
    ```

2. Install the required packages:

    ```sh
    pip install pandas scikit-learn
    ```

### Usage

1. Run all cells in `cleaning.ipynb` to generate `cleaned_data.csv`.

## Analysis and Recommendation

Open `analysis.ipynb` to use the recommendation system. This notebook will:

1. Load the cleaned data.
2. Implement functions to recommend coffee bags based on numeric attributes or textual descriptions.
3. Provide example usage of the recommendation system.

### Functions

- `recommend_coffees(title, k=5, method='numeric')`: Recommends `k` coffee bags similar to the specified `title` using either numeric or textual similarity.

### Usage

1. Run all cells in `analysis.ipynb`.
2. Use the `recommend_coffees` function to get recommendations:

    ```python
    recommended_coffees_numeric = recommend_coffees('Tropical Summer Colombia La Sierra', k=5, method='numeric')
    print(recommended_coffees_numeric)

    recommended_coffees_text = recommend_coffees('Tropical Summer Colombia La Sierra', k=5, method='text')
    print(recommended_coffees_text)
    ```

## Examples

### Data Row Example

|    | title                              | rating | acidity_structure | aftertaste | aroma | body | flavor | with_milk | agtron   | blind_assessment                                                                                                                                                                                                                                  | bottom_line                                                                                          | coffee_origin                         | est_price       | notes                                                                                                                                                                                                                                                                                                                                                                                                                                | review_date   | roast_level   | roaster              | roaster_location       | url                                                                     |
|----|------------------------------------|--------|-------------------|------------|-------|------|--------|-----------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|---------------------------------------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------|-----------------------|------------------------|-------------------------------------------------------------------------|
| 4  | Tropical Summer Colombia La Sierra | 93     | 9                 | 8          | 9     | 8    | 9      | nan       | 60/77    | Fruit-driven, crisply chocolaty. Goji berry, dried plum, baking chocolate, amber, narcissus in aroma and cup. Crisply sweet structure with balanced acidity; lightly satiny mouthfeel. Fruit-toned finish supported by notes of baking chocolate. | An experimentally processed Colombia, sweetly fruit-forward with ballast from crisp chocolate notes. | La Sierra, Cauca Department, Colombia | $18.99/8 ounces | Produced by smallholding farmers from trees of the Castillo, Caturra, Pajarito, Tabi and Bourbon varieties of Arabica, and processed by the traditional washed method using species of lactic acid-producing yeast and bacteria during the fermentation step. Merge is a specialty coffee roaster in Harrisonburg, Virginia dedicated to ethical sourcing of high-quality coffees. Visit www.mergecoffeeco.com for more information. | November 2022 | Medium-Light  | Merge Coffee Company | Harrisonburg, Virginia | https://www.coffeereview.com/review/tropical-summer-colombia-la-sierra/ |

## Notes

- This project is intended for personal use and exploration.
- Adjustments and improvements can be made as needed.