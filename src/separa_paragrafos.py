import PyPDF2
result_list = []
search_term = 'alguma coisa'
reader = PyPDF2.PdfFileReader('data/o_espelho_machado_de_assis.pdf')
for page_number in range(0, reader.numPages):
    page = reader.getPage(page_number)
    page_content = page.extractText().split('\n')
    for paragraph_content in page_content:
        if search_term in paragraph_content:
            result = {
                "page": page_number,
                "content": paragraph_content
            }
            result_list.append(result)

print(result_list)