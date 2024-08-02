import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler

class CoffeeRecommender:
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)
        self.scaler = StandardScaler()
        self.vectorizer = TfidfVectorizer()

    def _prepare_numeric_data(self):
        numeric_columns = ['rating', 'acidity_structure', 'aftertaste', 'aroma', 'body', 'flavor']
        return self.scaler.fit_transform(self.df[numeric_columns])

    def _prepare_text_data(self):
        text_data = self.df['blind_assessment']
        return self.vectorizer.fit_transform(text_data)
    
    def recommend_coffees(self, title, k=5, method='numeric'):
        if method not in ['numeric', 'text']:
            raise ValueError("Method should be either 'numeric' or 'text'")
        
        if title not in self.df['title'].values:
            raise ValueError("Title not found in the dataset")

        if method == 'numeric':
            data = self._prepare_numeric_data()
        elif method == 'text':
            data = self._prepare_text_data()

        similarity_matrix = cosine_similarity(data)
        coffee_index = self.df[self.df['title'] == title].index[0]
        similarity_scores = list(enumerate(similarity_matrix[coffee_index]))
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
        similar_coffees_indices = [i[0] for i in similarity_scores if i[0] != coffee_index][:k]
        similar_coffees_df = self.df.iloc[similar_coffees_indices]
        
        return similar_coffees_df
    
    def print_coffees(self, coffees):
        i = 1
        for _, row in coffees.iterrows():
            print(f"{i}. {row['title']} by {row['roaster']}")
            i += 1


# Usage

if __name__ == '__main__':
    #initialize the recomender class
    reccomender = CoffeeRecommender('./data/cleaned_data.csv')

    #have an loop to get the user input, reccomend the coffees and print them
    userInput = ''
    while True:
        userInput = input('Enter the coffee name: ')
        if userInput == 'exit':
            break

        try:
            recommended_coffees = reccomender.recommend_coffees(input, k=5, method='numeric')
        except ValueError as e:
            print(e)
            continue
        except:
            print("An unknown error occured")
            break

        reccomender.print_coffees(recommended_coffees)