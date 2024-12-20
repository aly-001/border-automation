from PyPDF2 import PdfReader, PdfWriter
import os

def split_pdf_by_chapters(input_pdf_path, chapter_info, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Read the PDF
    reader = PdfReader(input_pdf_path)
    total_pages = len(reader.pages)
    
    # Process chapter_info to handle both tuples and single numbers
    processed_info = []
    for i, info in enumerate(chapter_info):
        if isinstance(info, (tuple, list)):
            page_num, name = info
        else:
            page_num = info
            name = f"Chapter {i+1}"
        processed_info.append((page_num, name))
    
    # Extract page numbers and names, and convert page numbers to 0-based index
    chapter_starts = [info[0] - 1 for info in processed_info]
    chapter_names = [info[1] for info in processed_info]
    
    # Add the total pages number to handle the last chapter
    chapter_starts.append(total_pages)
    
    # Split PDF into chapters
    for i in range(len(chapter_starts) - 1):
        writer = PdfWriter()
        start_page = chapter_starts[i]
        end_page = chapter_starts[i + 1]
        
        # Add all pages for this chapter
        for page_num in range(start_page, end_page):
            writer.add_page(reader.pages[page_num])
        
        chapter_filename = f'{i:02d}_{chapter_names[i].lower().replace(" ", "_")}.pdf'
        output_path = os.path.join(output_dir, chapter_filename)
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
        print(f'Created {chapter_names[i]}: pages {start_page + 1} to {end_page}')

# Example usage
input_pdf = 'your_book.pdf'
output_directory = 'split_chapters'

# Now you can mix and match formats:
chapter_info = [
    (1, "Table of Contents"),  # Tuple with custom name
    25, "Chapter 1"                         # Just the page number
    34, "Chapter 2"
    51, "Chapter 3"
    87, "Chapter 4"
    102, "Chapter 5"
    107, "Chapter 6"
    113, "Chapter 7"
    136, "Chapter 8"
    152, "Chapter 9"
    159, "Chapter 10"
    166, "Chapter 11"
    177, "Chapter 12"
    187, "Chapter 13"
    190, "Chapter 14"
    193, "Chapter 15"
    205, "Chapter 16"
    219, "Chapter 17"
    227, "Chapter 18"
    231, "Chapter 19"
    254, "Chapter 20"
    269, "Chapter 21"
    287, "Chapter 22"
    304, "Chapter 23"
    311, "Chapter 24"
    317, "Chapter 25"
    328, "Chapter 26"
    334, "Chapter 27"
    344, "Chapter 28"
    370, "Chapter 29"
    430, "Chapter 30"
    441, "Chapter 31"
    447, "Chapter 32"
    455, "Chapter 33"
    461, "Chapter 34"
    470, "Chapter 35"
    475, "Chapter 36"
    478, "Chapter 37"
    485, "Chapter 38"
    504, "Chapter 39"
    536, "Chapter 40"
    553, "Chapter 41"
    561, "Chapter 42"
    568, "Chapter 43"
    573, "Chapter 44"
    597, "Chapter 45"
    599, "Chapter 46"
    606, "Chapter 47"
    609, "Chapter 48"
    630, "Chapter 49"
    634, "Chapter 50"
    645, "Chapter 51"
    651, "Chapter 52"
    668, "Chapter 53"
    671, "Chapter 54"
    684, "Chapter 55"
    700, "Chapter 56"
    708, "Chapter 57"
    714, "Chapter 58"
    720, "Chapter 59"
    727, "Chapter 60"
    734, "Chapter 61"
    757, "Chapter 62"
    779, "Chapter 63"
    792, "Chapter 64"
    804, "Chapter 65"
    808, "Chapter 66"
    810, "Chapter 67"
    818, "Chapter 68"
    828, "Chapter 69"
    837, "Chapter 70"
    850, "Chapter 71"
    863, "Chapter 72"
    903, "Chapter 73"
    936, "Chapter 74"
    947, "Chapter 75"
    951, "Chapter 76"
    959, "Chapter 77"
    960, "Chapter 78"
    963, "Chapter 79"
    966, "Chapter 80"
    968, "Chapter 81"
    977, "Chapter 82"
    993, "Chapter 83"
    1001, "Chapter 84"
    1104, "Chapter 85"
    1171, "Chapter 86"
    1179, "Chapter 87"
    1209, "Chapter 88"
    1215, "Chapter 89"
    1225, "Chapter 90"
    1252, "Chapter 91"
    1264, "Chapter 92"
    1271, "Chapter 93"
    1279, "Chapter 94"
    1294, "Chapter 95"
    1304, "Chapter 96"
    1319, "Chapter 97"
    1324, "Chapter 98"
    1340, "Chapter 99"
]

split_pdf_by_chapters(input_pdf, chapter_info, output_directory)