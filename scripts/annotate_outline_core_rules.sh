echo "
InfoBegin
InfoKey: Title
InfoValue: Warhammer 40K : Core Rules (10th Edition)

BookmarkBegin
BookmarkTitle: CORE CONCEPTS
BookmarkLevel: 1
BookmarkPageNumber: 5

BookmarkBegin
BookmarkTitle: THE BATTLE ROUND
BookmarkLevel: 1
BookmarkPageNumber: 10

BookmarkBegin
BookmarkTitle: COMMAND PHASE
BookmarkLevel: 2
BookmarkPageNumber: 11

BookmarkBegin
BookmarkTitle: MOUVMENT PHASE
BookmarkLevel: 2
BookmarkPageNumber: 13

BookmarkBegin
BookmarkTitle: SHOOTING PHASE
BookmarkLevel: 2
BookmarkPageNumber: 19

BookmarkBegin
BookmarkTitle: CHARGE PHASE
BookmarkLevel: 2
BookmarkPageNumber: 29

BookmarkBegin
BookmarkTitle: FIGHT PHASE
BookmarkLevel: 2
BookmarkPageNumber: 32

BookmarkBegin
BookmarkTitle: DATASHEETS AND UNIT ABILITIES
BookmarkLevel: 1
BookmarkPageNumber: 37

BookmarkBegin
BookmarkTitle: STRATEGIC RESERVES AND STRATAGEMS
BookmarkLevel: 1
BookmarkPageNumber: 41

BookmarkBegin
BookmarkTitle: TERRAIN FEATURES
BookmarkLevel: 1
BookmarkPageNumber: 44

BookmarkBegin
BookmarkTitle: MUSTER YOUR ARMY
BookmarkLevel: 1
BookmarkPageNumber: 55

BookmarkBegin
BookmarkTitle: MISIONS
BookmarkLevel: 1
BookmarkPageNumber: 57
" > temp/info.txt

pdftk tenth-edition/raw-pdfs/dLZIlatQJ3qOkGP7.pdf update_info temp/info.txt output tenth-edition/formatted-pdfs/core_rules.pdf
