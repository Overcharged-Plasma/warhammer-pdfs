# Notes
* Using pdftk to add bookmarks:

* Save to info.
   ```
   InfoBegin
   InfoKey: Title
   InfoValue: Warhammer 40K : Space Marine Index

   BookmarkBegin
   BookmarkTitle: DEDICATED TRANSPORTS
   BookmarkLevel: 1
   BookmarkPageNumber: 34

   BookmarkBegin
   BookmarkTitle: IMPULSOR
   BookmarkLevel: 2
   BookmarkPageNumber: 34

   BookmarkBegin
   BookmarkTitle: DROP POD
   BookmarkLevel: 2
   BookmarkPageNumber: 35

   BookmarkBegin
   BookmarkTitle: FORTIFICATIONS
   BookmarkLevel: 1
   BookmarkPageNumber: 16

   BookmarkBegin
   BookmarkTitle: HAMMERFALL BUNKER
   BookmarkLevel: 2
   BookmarkPageNumber: 36
   ```

* Create a new pdf with:
```
pdftk input.pdf update_info info.txt output output.pdf
```

* The `info.txt` format can be reverse-engineered from an existing file with:
```
pdftk input.pdf data_dump
```

* To splice specific pages together:
```
pdftk A=input.pdf cat A1 A4 A8 A13 A14 A25 output output.pdf
pdftk tenth-edition/formatted-pdfs/necrons.pdf cat 1-6 14 15 19 23 24 26 31 32 38 39 43 47 48 56 output ~/necrons_owned.pdf
```

* To extract unit names:
```
grep -A3 "FACTION KEYWORDS:" tenth-edition/text/necrons.txt | grep -B1 "\-\-" | grep -v "\-\-" | sed /^$/d | uniq
```
