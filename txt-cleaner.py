import os
import re

# Define input and output directories
input_dir = "pdf_splitter/split_chapters/split_chapters_txt"
output_dir = "pdf_splitter/split_chapters/split_chapters_cleaned_txt"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# List of tariff codes to remove
tariff_codes = [
    "CCCT", "LDCT", "GPT", "UST", "MXT", "CIAT", "CT", "CRT", "IT",
    "NT", "SLT", "PT", "COLT", "JT", "PAT", "HNT", "KRT", "CEUT",
    "UAT", "CPTPT", "UKT", "Free", "CCCT,", "LDCT,", "GPT,", "UST,", "MXT,", "CIAT,", "CT,", "CRT,", "IT,",
    "NT,", "SLT,", "PT,", "COLT,", "JT,", "PAT,", "HNT,", "KRT,", "CEUT,",
    "UAT,", "CPTPT,", "UKT,", "Free,", "MFN", "KGM"
]

# Add word counting function
def count_words(text):
    return len(text.split())

# Initialize counters
total_original_words = 0
total_cleaned_words = 0

# Process each file
for i in range(1, 100):
    input_file = os.path.join(input_dir, f"chapter_{i}.txt")
    output_file = os.path.join(output_dir, f"chapter_{i}.txt")
    
    # Skip if input file doesn't exist
    if not os.path.exists(input_file):
        continue
        
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
        original_word_count = count_words(content)
        total_original_words += original_word_count
        
        # Remove tariff codes
        for code in tariff_codes:
            content = content.replace(code, '')
            
        # Clean up multiple commas and spaces
        content = re.sub(r'[,\s]+,', ',', content)  # Remove multiple commas with spaces between
        content = re.sub(r',+', ',', content)       # Remove consecutive commas
        content = re.sub(r',\s*\n', '\n', content)  # Remove commas at end of lines
        content = re.sub(r'\s+,\s+', ' ', content)  # Remove isolated commas with spaces around them
        
        # Write cleaned content to output file
        with open(output_file, 'w', encoding='utf-8') as out_f:
            out_f.write(content)
            cleaned_word_count = count_words(content)
            total_cleaned_words += cleaned_word_count
            
        print(f"Chapter {i}:")
        print(f"  Original words: {original_word_count}")
        print(f"  Cleaned words: {cleaned_word_count}")
        print(f"  Difference: {original_word_count - cleaned_word_count}")
        print()

print("Total Statistics:")
print(f"Total original words: {total_original_words}")
print(f"Total cleaned words: {total_cleaned_words}")
print(f"Total difference: {total_original_words - total_cleaned_words}")
print(f"Reduction percentage: {((total_original_words - total_cleaned_words) / total_original_words * 100):.2f}%")
