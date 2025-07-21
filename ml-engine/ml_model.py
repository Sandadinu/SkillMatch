import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

#Sample data
data = {
    'skills':[
        'python pandas numpy matplotlib' ,
        'html css javascript react',
        'linux docker aws kubernetes',
        'sql excel tableau powerbi',
        'csharp aspnet sql mvc'
    ],

    'role':[
        'Data Analyst',
        'Fronend Developer' ,
        'DevOps Engineer',
        'Business Intelligence Analyst',
        'Backend Developer'
    ]
}

# Create a DataFrame
df=pd.DataFrame(data)

#Text vectorization
vec = CountVectorizer()
x = vec.fit_transform(df['skills'])
y = df['role']

#Model training
model = MultinomialNB()
model.fit(x,y)

# Save the model and vectorizer
with open('model.pkl','wb') as f:
    pickle.dump(model, f)
with open('vectorizer.pkl','wb') as f:
    pickle.dump(vec, f)
    
print("Model and vectorizer saved successfully.")