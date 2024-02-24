# import the packages made
import ocr
import summarizer
import output_to_file as output

# filepath to slide, to be replaced with a live feed later
# TODO: defense in depth
# If using file path, should pre-emptively ensure that there are no path traversal characters:
# Ensured resolved_path = input_path

# the test file
# path = '/Users/name/Documents/Screenshots/Screenshot 2023-12-18 at 12.45.38 PM.png'

# take input from user for the file location
path = input('Path to your image:\n')

# analyse image for text
original_text = ocr.img2txt(path)
print ('Original text is: ' + original_text)

# summarize the text
summarized_text = summarizer.summarize(original_text)
print('Summarized text is: ' + summarized_text)

output.write_output('Original text:\n\n' + original_text + '\n\n\n\nBREAK\n\n\n\n' + 'Summarized text:\n\n' +
                    summarized_text)
