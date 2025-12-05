import os
from pathlib import Path
from pypdf import PdfReader

def load_knowledge_base():
    """
    Scans the 'knowledge' folder for PDFs and extracts their text.
    Returns: A single string containing all text from all PDFs.
    """
    knowledge_dir = Path("knowledge")
    
    # Create folder if it doesn't exist
    if not knowledge_dir.exists():
        os.makedirs(knowledge_dir)
        return ""

    all_text = []
    pdf_files = list(knowledge_dir.glob("*.pdf"))
    
    if not pdf_files:
        return ""

    print(f"📚 Found {len(pdf_files)} PDF(s) in knowledge base.")

    for pdf_path in pdf_files:
        try:
            reader = PdfReader(pdf_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            all_text.append(f"--- DOCUMENT: {pdf_path.name} ---\n{text}")
            print(f"   ✅ Loaded: {pdf_path.name}")
        except Exception as e:
            print(f"   ❌ Error reading {pdf_path.name}: {e}")

    return "\n\n".join(all_text)