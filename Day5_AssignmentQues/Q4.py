import pandas as pd

sales_df = pd.DataFrame({
    'customer_id': [1, 2, 1],
    'product_id': [101, 102, 103],
    'quantity_sold': [2, 1, 5]
})

customers_df = pd.DataFrame({
    'customer_id': [1, 2],
    'customer_name': ['Pulkit', 'Kunal'],
    'customer_location': ['IN', 'IN']
})

products_df = pd.DataFrame({
    'product_id': [101, 102, 103],
    'product_name': ['Laptop', 'Phone', 'Tablet'],
    'category': ['Electronics', 'Electronics', 'Electronics']
})

# now we have to merge sales df with customer df
merged_sales_customers_df = pd.merge(sales_df, customers_df, on='customer_id')
print("Merged Sales and Customers DF:")
print(merged_sales_customers_df)

# Concatenate the products_df with merged_sales_customers_df
products_df_renamed = products_df.rename(columns={'product_id': 'prod_id'})
final_df = pd.concat([merged_sales_customers_df, products_df_renamed], axis=1)
print("\nConcatenated DF:")
print(final_df)

# 
final_df_indexed = final_df.set_index('product_id')
products_df_indexed = products_df.set_index('product_id')
complete_sales_df = final_df_indexed.join(products_df_indexed, lsuffix='_left', rsuffix='_right')
complete_sales_df = complete_sales_df.reset_index()
print("\nComplete Sales DF after join:")
print(complete_sales_df)

# Calculate the total quantity sold and revenue for each product category
prices = {101: 1000, 102: 500, 103: 300}
complete_sales_df['revenue'] = complete_sales_df['quantity_sold'] * complete_sales_df['product_id'].map(prices)
category_summary = complete_sales_df.groupby('category_right')[['quantity_sold','revenue']].sum().reset_index()
print("\nTotal Quantity Sold and Revenue per Category:")
print(category_summary)
