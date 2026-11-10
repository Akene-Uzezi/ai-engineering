from langchain.document_loaders import Docx2txtLoader
from langchain.text_splitter import CharacterTextSplitter

loader = Docx2txtLoader("IntroToDataScience.docx")
pages = loader.load()
for i in range(len(pages)):
    pages[i].page_content = " ".join(pages[i].page_content.split())
print(len(pages[0].page_content))

char_splitter = CharacterTextSplitter(separator=".", chunk_size=500, chunk_overlap=0)
pages_char_split = char_splitter.split_documents(pages)
for i in range(len(pages_char_split)):
    pages_char_split[i].page_content = pages_char_split[i].page_content + "."
print(pages_char_split[1].page_content)
