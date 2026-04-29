# RAG_Detail

A typical RAG pipeline has 4 stages:
Ingestion (read data)
Chunking (split into pieces)
Embedding + Storage (vector DB)

base64 helps convert images → text so models can process them Converting a image into a long text message sending it safely and then converting it back into a image.(base64 is used to encode binary data into text format so it can be safely transmitted or stored, and then decoded back to its original form.)


first we extract data and wrap it into document objects (text + metadata) 

after doing data parsing we do chunking in chunking we convert the entire data into multiple chunk and why we do chunking the reason we do chunking because in embedding with respect to every LLm model there is a fixed context size for example lets say we have a pdf with complete 100 pages and we directly try to give it to a llm model for performing embedding it will not be possible it will say that you providing data more then context size and that will not be possible in order to convert the text into vector so limite of the context size we really need to give the data by applying chunking. because in every llm there is a fix context size. so after chunking we apply embedding and then we store to our vactor database. then we create a retriver and then we pass to llm then llm gives output


what if we got data in text and image formet we use multimodal RAG. for reading we can use PyMuPDF which is in fitz. this is best for reading for Text Extracttion, Image Extraction, Speed and Memory Usage 