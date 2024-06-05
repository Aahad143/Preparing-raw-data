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
    i = 0
    for qual in qualifications:
        exp_positions = []
        exp_text_list = []
        if qual:

            exp_positions = find_all_occurrences(qual, 'experience')
            for pos in exp_positions:
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
    return exp_text

exp_text_min = extract_expr_substr(minimum_qual)
exp_text_pref = extract_expr_substr(preferred_qual)

exp_pattern = r"\b(\d+[+-]?\s*years?[’\']?\s*(?:of\s+experience|experience)?)\b" ## Matches digits-digits OR digits years? of experience
# exp_pattern = r"\b\d+(-\d+)\s*years?\b" ## Matches digits-digits OR digits years? of experience

filtered_exp_text_min = {key: value for key, value in exp_text_min.items() if value and any(re.match(exp_pattern, item) for item in value)}

print(len(filtered_exp_text_min))
print(filtered_exp_text_min)

# print(len(exp_text_pref))
# print(exp_text_pref)