from langchain.document_loaders import Docx2txtLoader

doc_loader = Docx2txtLoader("IntroToDataScience.docx")
doc_pages = doc_loader.load()
print(doc_pages)
