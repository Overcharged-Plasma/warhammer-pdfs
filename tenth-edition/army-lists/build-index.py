import os

# Create an *.info text file with document title and page outlines
# Note 'statrtpage' here is the first page with datasheets (after army rules)
def create_info_doc(faction, file_name, startpage):
  new_unit_list = []
  with open(file_name + ".list") as fid:
    unit_list_raw = fid.readlines()
    for unit in unit_list_raw:
      new_unit = unit.replace('\x0c', '').replace('\n', '')
      new_unit_list.append(new_unit)

  with open("info.txt", "w") as fid:
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


create_info_doc("Space Marines", "SM_2K_230628", 9)

