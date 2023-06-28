pdftk A=../formatted-pdfs/space_marines.pdf B=../formatted-pdfs/core_rules.pdf cat A6 A1-2 B41-42 A3-5 A14 A22 A27 A32 A35 A47 A52 A64 A65 A69 A70 A82 A88 A105 A106 output temp.pdf
pdftk temp.pdf update_info info.txt output SM_2K_230628.pdf
