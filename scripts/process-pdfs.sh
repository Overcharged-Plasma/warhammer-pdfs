

pdftk tenth-edition/raw-pdfs/uVN1M55L0U3dQeWZ.pdf cat 1-6 output temp/army_rules.pdf

pdfjam tenth-edition/raw-pdfs/uVN1M55L0U3dQeWZ.pdf "7-" -o temp/data_sheets.pdf --nup 1x2 --scale .98 --frame true

pdftk temp/army_rules.pdf temp/data_sheets.pdf output tenth-edition/formatted-pdfs/space_marines.pdf
