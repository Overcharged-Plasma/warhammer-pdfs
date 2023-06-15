import os

# Define Raw pdfs file names
factions = {}
factions["Space Marines"]        = "uVN1M55L0U3dQeWZ"
factions["Black Templars"]       = "BcWghehxrgeCmkN8"
factions["Space Wolves"]         = "u61I5H9K5r9oNsXZ"
factions["Dark Angels"]          = "C6o7G0zjRSxCUvhK"
factions["Blood Angels"]         = "YC40Fxov5FhbXFRl"
factions["Deathwatch"]           = "UwUTTzw0UEZe2hAi"
factions["Grey Knights"]         = "4czxZwZf5cZCT7dk"
factions["Imperial Guard"]       = "xOjVS3Asx2QJ13lk"
factions["Adepta Sororitas"]     = "riFjIh9OeKg6AbLZ"
factions["Adeptus Custodes"]     = "TE5lPwmnUDrITuGM"
factions["Adeptus Mechanicus"]   = "vkzQ2IBbrrCVNzz3"
factions["Imperial Knights"]     = "NRqB9dxmiQDjknNV"
factions["Imperial Agents"]      = "Ozcq0k1WInJbmhZV"
factions["Chaos Daemons"]        = "JhAjl9vv4BcigNO9"
factions["Chaos Knights"]        = "5I1cNt3t71dfd3jh"
factions["Chaos Space Marines"]  = "csv0IuVvYQAndBJE"
factions["Thousand Sons"]        = "2iVljh64k0hWMKsO"
factions["World Eaters"]         = "iiq5IN0DVsqWxFxh"
factions["Death Guard"]          = "VdyiNhPdt8ehmIh6"
factions["Tyranids"]             = "L8FE4F808oEwCq9T"
factions["T'au Empire"]          = "20OdtEKVLiE4H6Zo"
factions["Aeldari"]              = "kQ4OfkQB5G05ZNX4"
factions["Drukhari"]             = "ARyMPKx2JXprseBC"
factions["Necrons"]              = "H5pO90rzYSAY6dHG"
factions["Genestealer Cults"]    = "BrBEfwS94zTuHrZq"
factions["Orks"]                 = "EE2Pdickp8sNe1NX"
factions["Leagues of Votann"]    = "YWdVWS6bgzMSMsNo"


# Create new PDFs
for faction in factions:

  # Create a unix-freindly file name
  file_name = faction.lower().replace(" ", "_").replace("'", "")

  # Print progress marker /  file pointer
  print(f"Processing PDF for {faction} (tenth-edition/formatted-pdfs/{file_name}.pdf)")

  # Workaround for difference in army rules page count
  if faction == "T'au Empire":
    n = 8
  elif faction == "Imperial Agents":
    n = 2
  else:
    n = 6

  # Create Info.txt
  with open("temp/info.txt", "w") as fid:
    fid.write("InfoBegin\n")
    fid.write("InfoKey: Title\n")
    fid.write(f"InfoValue: Warhammer 40K : {faction} Index (10th Edition)\n")


  # Create new pdf
  os.system(f"pdf2txt tenth-edition/raw-pdfs/{factions[faction]}.pdf > tenth-edition/text/{file_name}.txt")
  os.system(f"pdftk tenth-edition/raw-pdfs/{factions[faction]}.pdf cat 1-{n} output temp/army_rules.pdf")
  os.system("pdfjam --outfile temp/army_rules_resized.pdf --paper legal temp/army_rules.pdf --pagecolor 220,220,220 --quiet")
  if faction == "Imperial Knights":
    # Remove Chaos Knights from Imperial Knights datasheets.
    os.system(f"pdfjam tenth-edition/raw-pdfs/{factions[faction]}.pdf '{n+1}-28' -o temp/data_sheets.pdf --nup 1x2 --scale .98 --frame true --delta '0 10' --pagecolor 220,220,220  --quiet")
  else:
    os.system(f"pdfjam tenth-edition/raw-pdfs/{factions[faction]}.pdf '{n+1}-' -o temp/data_sheets.pdf --nup 1x2 --scale .98 --frame true --delta '0 10' --pagecolor 220,220,220  --quiet")
  os.system(f"pdftk temp/army_rules_resized.pdf temp/data_sheets.pdf output temp/combined.pdf")
  os.system(f"pdftk temp/combined.pdf update_info temp/info.txt output tenth-edition/formatted-pdfs/{file_name}.pdf")

  # Clean up temp directory
  os.remove("temp/army_rules.pdf")
  os.remove("temp/data_sheets.pdf")
  os.remove("temp/combined.pdf")
  os.remove("temp/info.txt")
