import pandas as pd
import os

# Create directory for output files
output_dir = 'hs_chapters'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Read the CSV file
df = pd.read_csv('H12-endpoints.csv', encoding='latin1')

# Add a new column with padded HS codes to ensure proper comparison
df['HS_padded'] = df['HS10 Code'].astype(str).str.zfill(10)

# Group by first 2 digits of HS10 Code and save to separate files
for chapter in range(1, 100):
    # Format chapter number to 2 digits
    chapter_str = f"{chapter:02d}"
    
    # Filter rows where padded HS10 Code starts with the chapter number
    chapter_df = df[df['HS_padded'].str.startswith(chapter_str)]
    
    # Only create file if there are rows for this chapter
    if not chapter_df.empty:
        # Remove the temporary padding column before saving
        chapter_df = chapter_df.drop('HS_padded', axis=1)
        output_file = os.path.join(output_dir, f'chapter_{chapter_str}.csv')
        chapter_df.to_csv(output_file, index=False, encoding='latin1')