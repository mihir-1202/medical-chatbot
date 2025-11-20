import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from pinecone import ServerlessSpec

# Load environment variables
load_dotenv()
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')

def load_and_split_pdf(file_path, chunk_size=700, chunk_overlap=50):
    """
    Loads a PDF file and splits it into chunks.
    """
    loader = PyPDFLoader(file_path)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = chunk_size,
        chunk_overlap = chunk_overlap
    )

    documents = loader.load()
    chunks = text_splitter.split_documents(documents)
    return chunks

def get_embeddings_model(device='cpu'):
    """
    Initializes and returns the embedding model used to turn chunks into vector embeddings.
    """
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": 'cpu'}
    )
    return embeddings

def initialize_pinecone_index(index_name = 'medical-chatbot'):
    """
    Sets up the Pinecone index (vector database)if it doesn't exist.
    """
    pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
    
    if not pc.has_index(index_name):
        pc.create_index(
            name=index_name,
            dimension=384, #the embedding model outputs 384-dimensional vectors
            metric='cosine', #the similarity metric to use for the index
            spec=ServerlessSpec(
                cloud='aws', 
                region='us-east-1'
            )
        )
    return pc.Index(index_name)

def create_vector_store(chunks, embeddings, index_name):
    """
    Turns the chunks into vector embeddings and stores them in the Pinecone vector database.
    """
    vector_store = PineconeVectorStore.from_documents(
        documents=chunks, 
        embedding=embeddings, 
        index_name=index_name
    )
    return vector_store

if __name__ == "__main__":
    chunks = load_and_split_pdf('data/Medical_book.pdf')
    embeddings = get_embeddings_model()
    index_name = 'medical-chatbot'
    initialize_pinecone_index(index_name)
    vector_store = create_vector_store(chunks, embeddings, index_name)


