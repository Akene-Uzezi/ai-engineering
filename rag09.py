from langchain.document_loaders import Docx2txtLoader

loader = Docx2txtLoader("IntroToDataScience.docx")
pages = loader.load()
for i in range(len(pages)):
    pages[i].page_content = " ".join(pages[i].page_content.split())
print(pages[0].page_content)
