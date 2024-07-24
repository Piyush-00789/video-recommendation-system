
from django.apps import AppConfig
import json
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity,cosine_distances
from sklearn.externals import joblib




class VideoConfig(AppConfig):
    name = 'video'
    saved_model = 0

    def make_recommendations(movie_user_likes):
        df = pd.read_csv("C:/Users/piyus/PycharmProjects/testing_ML/deploy/fastbert/movie_dataset.csv")
        print(df.head())
        print(df.info())
        features = ["keywords", "cast", "genres", "director"]

        for feature in features:
            df[feature] = df[feature].fillna('')

        def combine_feature(row):
            try:
                return row["keywords"] + " " + row["cast"] + " " + row["genres"] + " " + row["director"]
            except:
                print(row)

        df["combined_features"] = df.apply(combine_feature, axis=1)
        df.iloc[0]["combined_features"]
        b = df["combined_features"]
        print(b)

        vectorizer = CountVectorizer()
        x = vectorizer.fit_transform(df["combined_features"])
        print(vectorizer.get_feature_names())
        print(x.toarray())

        cosine_model = cosine_similarity(x)
        cosine_model_df = pd.DataFrame(cosine_model, index=df.title, columns=df.title)
        print(cosine_model_df.head())
        #confirm test
        print("Inside ML function")
        temp = cosine_model_df[movie_user_likes].sort_values(ascending=False)
        #a = pd.Series.abs(temp)
        #print(temp.title)
        ##
        #print("Making single object")
        #title = pd.Series(temp["title"])
        #print(title)
        ##



        #cosine_model_df.reset_index(self)
        print(cosine_model_df[movie_user_likes].sort_values(ascending=False).to_dict())
        return cosine_model_df[movie_user_likes].sort_values(ascending=False).to_dict()
        ##testing case 1
        #filename = "final_model.sav"
        #joblib.dump(cosine_model_df,filename)
        #loaded_model = joblib.load(filename)
        #testing case 2
        #saved_model = ppickle.dump(filename,cosine_model_df[movie_user_likes].sort_values(ascending=False))
        #return saved_model


    #print(make_recommendations("Avatar"))
