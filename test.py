# importing pandas as pd 
import pandas as pd 
  
# Creating the DataFrame 
df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'], 
                    'Event':['Music', 'Poetry', 'Theatre', 'Comedy'], 
                    'Cost':[10000, 5000, 15000, 2000]}) 
  
# Create a new column 'Discounted_Price' after applying 
# 10% discount on the existing 'Cost' column. 
  
# create a new column 
df['Discounted_Price'] = df['Cost'] - (0.1 * df['Cost']) 
  
# Print the DataFrame after  
# addition of new column 
print(df) 