from matplotlib import pyplot as plt
import plotly.express as px
import pandas as pd
import re

def find_all_occurrences(text, word):
  """
  This function finds all occurrences of a word within a string and returns their positions.

  Args:
      text: The string to search within.
      word: The specific word to look for.

  Returns:
      A list containing the starting positions of all occurrences of the word in the text, 
      or an empty list if the word is not found.
  """


  positions = []
  start_index = 0
  
  while True:
    # Find the next occurrence of the word from the current index
    position = text.find(word, start_index)

    if position == -1:
      # Word not found anymore, break the loop
      break
    
    positions.append(position)
    # Update start index to search after the current occurrence
    start_index = position + len(word)

  return positions

df = pd.read_csv('clean_data/apple_jobs_clean.csv')

minimum_qual = df['minimum_qual'].fillna('').tolist() 
preferred_qual = df['preferred_qual'].fillna('').tolist()


# for i in range(1):
#     print(minimum_qual[i], end='\n')


def extract_expr_substr(qualifications):
    exp_text = {}
    count = 0
    i = 0
    for qual in qualifications:
        exp_positions = []
        exp_text_list = []
        if qual:

            exp_positions = find_all_occurrences(qual, 'experience')
            for pos in exp_positions:
                count += 1
                if (pos -15) < 0:
                    for j in range(15, 0, -1):
                        if (pos - j) == 0:
                            exp_substr = qual[pos - j :pos + len('experience')]
                            break
                else:
                    exp_substr = qual[pos - 15 :pos + len('experience')]

                exp_text_list.append(exp_substr)
        else:
            exp_text_list.append("")
        exp_text.update({i : exp_text_list})

        i += 1
    print("f")
    return exp_text, count

exp_text_min, exp_min_count = extract_expr_substr(minimum_qual)
exp_text_pref, exp_pref_count = extract_expr_substr(preferred_qual)

# exp_pattern = r"\b(\d+[+-]?\s*years?[’\']?\s*(?:of\s+experience|experience)?)\b" ## Matches digits-digits OR digits years? of experience

# filtered_exp_text_min = {key: value for key, value in exp_text_min.items() if value and any(re.match(exp_pattern, item) for item in value)}

# print(exp_text_min)
print(exp_pref_count)

def extract_numbers(text):
    # Find all sequences of digits in the text
    numbers = re.findall(r'\d+', text)
    # Convert the extracted sequences to integers
    numbers = [int(num) for num in numbers]

    return numbers

exp_num_dict = {}
for key in exp_text_min:
    for exp_text in exp_text_min[key]:
        if extract_numbers(exp_text):
            exp_num_dict.update({key: extract_numbers(exp_text)})

for key in exp_num_dict:
    for val in exp_num_dict[key]:
        if val > 10000:
            print(key)

# print(len(exp_text_pref))
exp_num_dict.pop(373)
print(exp_num_dict)

# Create a DataFrame from the dictionary
exp_df = pd.DataFrame(list(exp_num_dict.items()), columns=['index', 'experience_years'])
exp_df = exp_df.explode('experience_years')  # If the values are lists, this will create separate rows for each value

# Merge with the original DataFrame
merged_df = df.merge(exp_df, left_index=True, right_on='index')

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(merged_df['experience_years'], merged_df['title'], color='skyblue')
plt.xlabel('Job Title')
plt.ylabel('Experience Years')
plt.title('Experience Years for Each Job Title')
plt.xticks(rotation=90)
plt.tight_layout()
plt.gcf().subplots_adjust(left=0.2)  # Adjust the left padding
plt.show()

# Create a DataFrame from the dictionary
# exp_df = pd.DataFrame(list(exp_num_dict.items()), columns=['index', 'experience_years'])
# exp_df = exp_df.explode('experience_years')  # If the values are lists, this will create separate rows for each value

# # Merge with the original DataFrame
# merged_df = df.merge(exp_df, left_index=True, right_on='index')

# # Select the first 10 titles
# merged_df_10 = merged_df.head(100)

# # Plotting with Plotly
# fig = px.scatter(merged_df_10, x='index', y='experience_years', hover_data=['title'], title='Experience Years for the First 10 Job Titles')
# fig.update_layout(xaxis_title='Job Title Index', yaxis_title='Experience Years')
# fig.show()