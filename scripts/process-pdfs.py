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

# Raw version of the Munitorum Field Manual
points_doc = "yjHP7Y5opT8kkexf"

points_page_range = {}
points_page_range["Space Marines"]        = "27-28"
points_page_range["Black Templars"]       = "11"
points_page_range["Space Wolves"]         = "29"
points_page_range["Dark Angels"]          = "16"
points_page_range["Blood Angels"]         = "12"
points_page_range["Deathwatch"]           = "18"
points_page_range["Grey Knights"]         = "21"
points_page_range["Imperial Guard"]       = "9-10"
points_page_range["Adepta Sororitas"]     = "2"
points_page_range["Adeptus Custodes"]     = "3"
points_page_range["Adeptus Mechanicus"]   = "4"
points_page_range["Imperial Knights"]     = "22"
points_page_range["Imperial Agents"]      = "8"
points_page_range["Chaos Daemons"]        = "13"
points_page_range["Chaos Knights"]        = "14"
points_page_range["Chaos Space Marines"]  = "15"
points_page_range["Thousand Sons"]        = "31"
points_page_range["World Eaters"]         = "33"
points_page_range["Death Guard"]          = "17"
points_page_range["Tyranids"]             = "32"
points_page_range["T'au Empire"]          = "30"
points_page_range["Aeldari"]              = "6-7"
points_page_range["Drukhari"]             = "19"
points_page_range["Necrons"]              = "24"
points_page_range["Genestealer Cults"]    = "20"
points_page_range["Orks"]                 = "25-26"
points_page_range["Leagues of Votann"]    = "23"

forgeworld_datasheets = {}
forgeworld_datasheets["Orks"]                   = (tenth-edition/raw-pdfs/JpgzDSW8YhlRCMHo.pdf)
forgeworld_datasheets["Aeldari"]                = (tenth-edition/raw-pdfs/AL0QL82QPWrWnWJU.pdf)
forgeworld_datasheets["Astra Militarum Part 1"] = (tenth-edition/raw-pdfs/l8t0aWCwawo1ACck.pdf)
forgeworld_datasheets["Astra Militarum Part 2"] = (tenth-edition/raw-pdfs/Q98wnngqmxUac4rm.pdf)
forgeworld_datasheets["Titans"]                 = (tenth-edition/raw-pdfs/8BgBEXw7BlTSquqV.pdf)
forgeworld_datasheets["Necrons"]                = (tenth-edition/raw-pdfs/Mcu6QBdzRs8yWqCW.pdf)
forgeworld_datasheets["Imperial Knights]"       = (tenth-edition/raw-pdfs/YeS47MWmFkWqKoLP.pdf)
forgeworld_datasheets["Astartes"]               = (tenth-edition/raw-pdfs/I5z3erYio9qzJkUa.pdf)
forgeworld_datasheets["Grey Knights"]           = (tenth-edition/raw-pdfs/3UEEFOlzG1OWDodc.pdf)
forgeworld_datasheets["Adeptus Custodes]"       = (tenth-edition/raw-pdfs/HOgEzRypbsBBGrnB.pdf)
forgeworld_datasheets["Chaos Knights]"          = (tenth-edition/raw-pdfs/080HAymlEE0Hn0q1.pdf)
forgeworld_datasheets["Drukhari"]               = (tenth-edition/raw-pdfs/jtAaEARk7wCoSVhV.pdf)
forgeworld_datasheets["Tyranids"]               = (tenth-edition/raw-pdfs/HgMmll6jheLNHIOm.pdf)
forgeworld_datasheets["T'au Empire"]            = (tenth-edition/raw-pdfs/NUbyWNu2bOI74T6p.pdf)


# Create an *.info text file with document title and page outlines
# Note 'statrtpage' here is the first page with datasheets (after army rules)
def create_info_doc(faction, file_name, startpage):
  new_unit_list = []
  with open("temp/" + file_name + ".list") as fid:
    unit_list_raw = fid.readlines()
    for unit in unit_list_raw:
      new_unit = unit.replace('\x0c', '').replace('\n', '')
      new_unit_list.append(new_unit)

  with open("temp/info.txt", "w") as fid:
    fid.write("InfoBegin\n")
    fid.write("InfoKey: Title\n")
    fid.write(f"InfoValue: Warhammer 40K : {faction} Index (10th Edition)\n")
    fid.write("\n")

    page = startpage;

    fid.write("BookmarkBegin\n")
    fid.write(f"BookmarkTitle: ARMY RULES\n")
    fid.write("BookmarkLevel: 1\n")
    fid.write(f"BookmarkPageNumber: 1\n")
    fid.write("\n")
    fid.write("BookmarkBegin\n")
    fid.write(f"BookmarkTitle: DATASHEETS\n")
    fid.write("BookmarkLevel: 1\n")
    fid.write(f"BookmarkPageNumber: {page}\n")
    fid.write("\n")

    for unit in new_unit_list:
      fid.write("BookmarkBegin\n")
      fid.write(f"BookmarkTitle: {unit}\n")
      fid.write("BookmarkLevel: 2\n")
      fid.write(f"BookmarkPageNumber: {page}\n")
      fid.write("\n")
      page = page + 1;

    fid.write("BookmarkBegin\n")
    fid.write(f"BookmarkTitle: POINTS\n")
    fid.write("BookmarkLevel: 1\n")
    fid.write(f"BookmarkPageNumber: {page}\n")
    fid.write("\n")


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



  # Create text versions or each pdf
  if faction == "Imperial Knights":
    # Remove Chaos Knights from Imperial Knights datasheets.
    os.system(f"pdf2txt tenth-edition/raw-pdfs/{factions[faction]}.pdf --maxpages 28 > tenth-edition/text/{file_name}.txt")
  else:
    os.system(f"pdf2txt tenth-edition/raw-pdfs/{factions[faction]}.pdf > tenth-edition/text/{file_name}.txt")

  # Extract list of units
  if faction == "Imperial Knights":
    # Remove last line from Imperial Knights list.
    os.system(f'grep -A3 "FACTION KEYWORDS:" tenth-edition/text/{file_name}.txt | grep -B1 "\-\-" | grep -v "\-\-" | sed /^$/d | sed "s/ $//" | head --lines=-1 | uniq > temp/{file_name}.list')
  else:
    os.system(f'grep -A3 "FACTION KEYWORDS:" tenth-edition/text/{file_name}.txt | grep -B1 "\-\-" | grep -v "\-\-" | sed /^$/d | sed "s/ $//" | uniq > temp/{file_name}.list')

  # Build info file for outlines
  create_info_doc(faction, file_name, n+1)

  # Extract army rules, resize.
  os.system(f"pdftk tenth-edition/raw-pdfs/{factions[faction]}.pdf cat 1-{n} output temp/army_rules.pdf")
  os.system("pdfjam --outfile temp/army_rules_resized.pdf --paper legal temp/army_rules.pdf --pagecolor 220,220,220 --quiet")

  # Extract datasheets, convert to 2up format.
  if faction == "Imperial Knights":
    # Remove Chaos Knights from Imperial Knights datasheets.
    os.system(f"pdfjam tenth-edition/raw-pdfs/{factions[faction]}.pdf '{n+1}-28' -o temp/data_sheets.pdf --nup 1x2 --scale .98 --frame true --delta '0 10' --pagecolor 220,220,220  --quiet")
  else:
    os.system(f"pdfjam tenth-edition/raw-pdfs/{factions[faction]}.pdf '{n+1}-' -o temp/data_sheets.pdf --nup 1x2 --scale .98 --frame true --delta '0 10' --pagecolor 220,220,220  --quiet")

  # Extract points
  os.system(f"pdftk tenth-edition/raw-pdfs/{points_doc}.pdf cat {points_page_range[faction]} output temp/points.pdf")

  # Concatenate the component PDFS into one
  os.system(f"pdftk temp/army_rules_resized.pdf temp/data_sheets.pdf temp/points.pdf output temp/combined.pdf")

  # Add outlines
  os.system(f"pdftk temp/combined.pdf update_info temp/info.txt output tenth-edition/formatted-pdfs/{file_name}.pdf")

  # Clean up temp directory
  # os.remove("temp/army_rules.pdf")
  # os.remove("temp/data_sheets.pdf")
  # os.remove("temp/combined.pdf")
  # os.remove("temp/info.txt")
