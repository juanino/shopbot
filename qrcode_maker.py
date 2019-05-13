#!/usr/bin/python3

#
# make qr codes as item_image.jpg
# output a scan_sheet.html for printing
#

# Import QR Code library
import qrcode
import grocerysheet as gc

# items = gc.items
# print(gc.items)
for item in gc.items:
    print(item + "------->" + gc.items[item])

for food in gc.items:
    # Create qr code instance
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 5,
        border = 4,
    )
    # The data that you want to store
    print("working on " + food)
    data = "!add " + food
    # Add data
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image()
    img.save(food + "_image.jpg")

# make a cheat sheet
# (in html)

import jinja2
import pprint

templateLoader = jinja2.FileSystemLoader("./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "scan_sheet_template.html"
template = templateEnv.get_template(TEMPLATE_FILE)
groceries = gc.items

print("pretty print starts here")
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(groceries)
print(type(groceries))

#keys = groceries.keys()
#keys = list(keys)
#pp.pprint(keys)
#groceries = keys

outputText = template.render(groceries=groceries)
print(outputText)
with open("scan_sheet.html", "w") as f:
    f.write(outputText)


