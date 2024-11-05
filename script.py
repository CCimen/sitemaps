import xml.etree.ElementTree as ET

# Namespace dictionary
namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

# Ask user for the URL prefix to filter by
user_prefix = input("Enter the URL prefix to filter for (e.g., https://sundsvall.se/utbildning-och-forskola): ")

try:
    # Parse the XML file
    tree = ET.parse('input.xml')
    root = tree.getroot()

    # Open a new text file for writing
    with open('filtered_links.txt', 'w') as file:
        # Iterate over each URL in the XML
        for url in root.findall('ns:url', namespaces):
            loc = url.find('ns:loc', namespaces)
            if loc is not None and loc.text.startswith(user_prefix):
                # Write the filtered link to the text file
                file.write(loc.text + '\n')

    print("Filtered links have been saved to 'filtered_links.txt'.")

except ET.ParseError as e:
    print(f"Error parsing XML: {e}")
except FileNotFoundError as e:
    print(f"File not found: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")