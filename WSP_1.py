import os
import pandas as pd
states = ['tamilnadu','kerala','andra','maharastra']
population = [1345345,432143,333345,67895]

state_pop = {'States':states,'Population':population}
print(state_pop)

df_states = pd.DataFrame.from_dict(state_pop)
#print(df_states)

df_states.to_csv("states.csv",index=False)
for state in states:
    if state == 'kerala':
        print(state)

with open("texxt.txt",'w') as file:
    file.write("Data written sucessfully")