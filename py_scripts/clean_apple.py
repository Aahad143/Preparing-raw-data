import pandas as pd

df = pd.read_csv('raw_data/apple_jobs.csv')
location = df.get('location').tolist()

state = []
country = []

for loc in location:
    print("location[i]: ", loc)
    parts = loc.split(',')
    if len(parts) >= 3:
        state.append(parts[1].strip())
        country.append(parts[2].strip())
        print("loc.split(',')[1]: ", parts[1].strip())
        print("loc.split(',')[2]: ", parts[2].strip())

print(len(state))
for i in range(len(state)):
    print("\nState:", state[i], "\ni =", i)

# print(len(country))
# for i in range(len(country)):
#     print("\nCountry:", country[i], "\ni =", i)
