import pymupdf

def process_pdf(doc: str):
    doc = pymupdf.open(doc)

    out = open("output.txt", "wb") # create a text output
    for page in doc: # iterate the document pages
        text = page.get_text().encode("utf8") # get plain text (is in UTF-8)
        out.write(text) # write text of page
        out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
    out.close()

if __name__ == "__main__":
    process_pdf(r"..\datasets\pdfs\DIGITAL-BROADSHEET_55gsm_IMPROVED_ART_V5_FINAL_NC_2025_.pdf")