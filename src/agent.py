import os
from openai import OpenAI
from src.pdf_processor import load_knowledge_base
from src.memory import load_memory

def generate_campaign_content(topic, platform, style="Professional"):
    """
    Orchestrates the AI generation process.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "❌ Error: OPENAI_API_KEY not found in .env file."

    client = OpenAI(api_key=api_key)

    # 1. Load Context
    knowledge_text = load_knowledge_base()
    memory_data = load_memory()

    # 2. Construct System Prompt
    system_prompt = f"""
    You are the 'Mobilization Agent' for the Poor People App (PPA).
    Your goal is to write high-impact social media content.
    
    STYLE GUIDANCE:
    - Tone: {style}
    - Platform: {platform}
    
    KNOWLEDGE BASE (Reference this):
    {knowledge_text[:50000]}  # Truncated to prevent overflow
    
    RECENT MEMORY (Do NOT repeat these):
    {memory_data}
    """

    # 3. Call OpenAI
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Write a post about: {topic}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ OpenAI Error: {str(e)}"