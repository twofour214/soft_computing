from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Sample strings for similarity comparison
s1 = "kitten"
s2 = "sitting"
print("Similarity ratio (s1 vs s2):", fuzz.ratio(s1, s2))

# Comparing longer strings
s3 = "The cat is sitting"
s4 = "The cat is sitting on the table"
print("Similarity ratio (s3 vs s4):", fuzz.ratio(s3, s4))
print("Partial ratio (s3 vs s4):", fuzz.partial_ratio(s3, s4))

# Additional example strings
str1 = "my country is India"
str2 = "India is my country, INDIA."

# Different types of similarity comparisons
print("Ratio:", fuzz.ratio(str1, str2))
print("Partial Ratio:", fuzz.partial_ratio(str1, str2))
print("Token Sort Ratio:", fuzz.token_sort_ratio(str1, str2))
print("Token Set Ratio (full_process=True):", fuzz.token_set_ratio(str1, str2, full_process=True))
print("Token Set Ratio (full_process=False):", fuzz.token_set_ratio(str1, str2, full_process=False))

# Weighted Ratio example
print("WRatio:", fuzz.WRatio("Hello World!", "Hello World"))

# Using process for best matching choice
query = "artificial intelligence"
choices = ["artificial intelligence", "arts intelligence", "a intelligence"]
print("All Matches:", process.extract(query, choices))
print("Best Match:", process.extractOne(query, choices))
