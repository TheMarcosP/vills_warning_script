import json
import pyperclip

# Read data from clipboard
clipboard_data = pyperclip.paste()
data = json.loads(clipboard_data)

# Process data
for item in data["build_order"]:
    item["notes"] = [note.replace("\n", "") for note in item["notes"]]
    item["notes"] = [note.replace("  ", "") for note in item["notes"]]

# Copy updated data to clipboard
updated_data = json.dumps(data, indent=4)
pyperclip.copy(updated_data)


"""
This code uses the pyperclip module to read the data from the clipboard using the pyperclip.paste() method. 
It then processes the data using the same loop as before to remove the newline characters from the "notes" field.
Finally, it uses the json.dumps() method to pretty-print the updated data with the indent parameter set to 4, 
and then copies the updated data back to the clipboard using the pyperclip.copy() method.
"""



