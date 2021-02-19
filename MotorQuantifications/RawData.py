# Create dataframe from CSV file
df = pd.read_csv(pref_filename)

# Create time column starting at zero and use as index

df['time'] = 0.001 * (df['timestamp2001_ms'] - df['timestamp2001_ms'][0])
cols = df.columns.tolist()
cols = cols[0:] + cols[1:-1]
params = df[cols].set_index('time')
 #
# Show first 5 rows for exploratory purposes
#params.drop_duplicates(subset= 'time' , keep="first", inplace=True)
df.drop_duplicates(subset= 'time' , keep="first", inplace=True)
df.head()

