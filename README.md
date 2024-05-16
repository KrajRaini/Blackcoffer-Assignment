## Blackcoffer Text Analysis Assignment

### Overview
This repository contains the code and documentation for the text analysis assignment provided by Blackcoffer. The project involves automated extraction of textual data from specified URLs, performing sentiment analysis on the extracted text, and structuring the output in a predefined format. The assignment showcases the ability to handle web data, apply natural language processing (NLP) techniques, and present data analysis results systematically.

### Objective
The primary objective of this assignment is to develop a robust Python application that can:
- Extract relevant textual content from a list of web articles.
- Analyze the text to determine various sentiment metrics, including positive and negative sentiments, overall polarity, and subjectivity of the content.
- Output the analysis results in an organized Excel format that aligns with the provided output structure requirements.

### Tasks Performed
1. **Data Extraction**:
   - Developed a script to read URLs from an Excel sheet (`Input.xlsx`).
   - Used the `requests` library to fetch web pages and `BeautifulSoup` for parsing HTML content to extract the article text and titles, excluding other webpage elements like headers and footers.

2. **Text Analysis**:
   - Implemented text preprocessing functions using the `nltk` library, including tokenization and removal of stopwords to clean the text data.
   - Calculated sentiment-related scores using custom functions. These scores include Positive Score, Negative Training, Polarity Score, and Subjectivity Score based on the frequency of predefined positive and negative words.

3. **Output Structuring**:
   - Compiled the analysis results along with URL IDs into a pandas DataFrame.
   - Exported the results to an Excel file (`Output Data Structure.xlsx`), ensuring the format adhered to the project's output requirements.

### Methodology
The project follows a structured programming approach using Python:
- **Data Extraction**: Leveraged HTTP requests and HTML parsing to accurately extract required text.
- **Natural Language Processing (NLP)**: Utilized nltk's corpus and tokenization features to preprocess and analyze text.
- **Data Manipulate and Output**: Used pandas for data manipulation and output formatting, which simplifies the process of saving structured data to Excel.

### Programming Language
The entire project is implemented using **Python 3**, chosen for its robust library support for web scraping, data manipulation, and natural language processing.

### Achievements
- Successfully automated the process of extracting and analyzing textual content from web sources.
- Efficiently calculated and reported key sentiment analysis metrics, enabling clear insights into the content's sentiment and subjectivity.
- Streamlined data extraction to output flow, minimizing manual intervention and potential for error.

### Technology Stack
- **Python 3**: Core programming language.
- **BeautifulSoup**: For HTML parsing.
- **Requests**: For making HTTP requests to retrieve web pages.
- **NLTK**: Used for natural language processing tasks including stopwords and tokenization.
- **Pandas**: For data manipulation and exporting data to Excel.
- **Excel**: For structuring and presenting the output data.

### Installation and Usage
Instructions on setting up the project, installing dependencies, and running the script are provided in the accompanying documentation.
