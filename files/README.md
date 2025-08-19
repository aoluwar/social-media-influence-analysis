# Social Media Influence Analysis

This repository analyzes the influence of social media posts on people using a dataset containing post content and engagement metrics.

## Features

- Data loading and cleaning
- Sentiment analysis (TextBlob)
- Influence score computation
- Feature engineering (engagement ratios, text length, etc.)
- Machine learning model comparison (Logistic Regression, Random Forest, SVM, Gradient Boosting)
- Hyperparameter tuning and cross-validation
- Exploratory Data Analysis (EDA) and Visualization

## Folder Structure

```
src/
  data_loader.py
  preprocessing.py
  sentiment_analysis.py
  influence_metrics.py
  utils.py
  modeling.py
notebooks/
  eda_and_modeling.ipynb
data/
  social_media_sample.csv
```

## Dataset

Include a CSV file in `data/social_media_sample.csv` with columns like:

- `id`, `user`, `text`, `likes`, `shares`, `comments`, `date`

## How to Run

1. Install requirements:  
   ```bash
   pip install -r requirements.txt
   ```

2. Run the notebook:  
   ```bash
   jupyter notebook notebooks/eda_and_modeling.ipynb
   ```

## Example Analysis

- Sentiment distribution across posts
- Correlation between sentiment and influence score
- Top influential users
- Model comparison for predicting influential posts (precision, recall, F1, cross-validation)

## License

This project is licensed under the MIT License. See `LICENSE` for details.