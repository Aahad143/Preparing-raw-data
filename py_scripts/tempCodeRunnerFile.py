# Create a DataFrame from the dictionary
exp_df = pd.DataFrame(list(exp_num_dict.items()), columns=['index', 'experience_years'])
exp_df = exp_df.explode('experience_years')  # If the values are lists, this will create separate rows for each value

# Merge with the original DataFrame
merged_df = df.merge(exp_df, left_index=True, right_on='index')

# Select the first 10 titles
merged_df_10 = merged_df.head(60)

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(merged_df_10['experience_years'], merged_df_10['title'], color='skyblue')
plt.xlabel('Job Title')
plt.ylabel('Experience Years')
plt.title('Experience Years for Each Job Title')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()