import pandas as pd


df = pd.read_csv(r"C:\Users\nicks\OneDrive\Desktop\VSprojects\olist\product_category_count_by_month_cleaned.csv")

df_clean = df.dropna(subset=['product_category_name'])

pivot_df = df_clean.pivot(index='product_category_name', 
                          columns='OrderMonthPurchasedMonth', 
                          values='Count of new_order_id')

category_means = pivot_df.mean(axis=1)

variance_df = pivot_df.sub(category_means, axis=0)

normalized_variance_df = variance_df.div(variance_df.abs().max(axis=1), axis=0)

normalized_variance_df.to_csv(r"C:\Users\nicks\OneDrive\Desktop\VSprojects\olist\normalized_variance_by_category.csv")

