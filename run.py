import streamlit as st
import os
from dotenv import load_dotenv
from src.agent import generate_campaign_content
from src.nostr_client import post_to_nostr
from src.telegram_client import post_to_telegram  # <--- NEW IMPORT
from src.memory import save_memory

# Load keys from .env
load_dotenv()

# --- UI CONFIGURATION ---
st.set_page_config(page_title="PPA Mobilizer", page_icon="🚀", layout="wide")

st.title("🚀 PPA Mobilization Agent (Lite)")
st.markdown("*Local-First • Private • Decentralized*")

# --- SIDEBAR (Settings) ---
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Check OpenAI
    if os.getenv("OPENAI_API_KEY"):
        st.success("✅ OpenAI Key Detected")
    else:
        st.error("❌ Missing OpenAI Key")
        
    # Check Nostr
    if os.getenv("NOSTR_NSEC"):
        st.success("✅ Nostr Key Detected")
    else:
        st.warning("⚠️ Missing Nostr Key")

    # Check Telegram
    if os.getenv("TELEGRAM_BOT_TOKEN"):
        st.success("✅ Telegram Key Detected")
    else:
        st.warning("⚠️ Missing Telegram Key")

    st.divider()
    st.info("Drop PDFs into the /knowledge folder to train the agent.")

# --- MAIN INPUTS ---
col1, col2 = st.columns(2)

with col1:
    topic = st.text_area("🎯 Topic / Directive", height=100, placeholder="What should we post about today?")

with col2:
    # Added Telegram to the top of the list for easy testing
    platform = st.selectbox("📢 Platform", ["Nostr", "Telegram", "Twitter/X", "LinkedIn"])
    style = st.select_slider("🎭 Persona / Style", options=["Professional", "Casual", "Activist", "Sarcastic Bitcoiner"])

# --- GENERATION ---
if st.button("✨ Generate Content", type="primary", use_container_width=True):
    if not topic:
        st.warning("Please enter a topic first.")
    else:
        with st.spinner("Consulting Knowledge Base & Memory..."):
            generated_text = generate_campaign_content(topic, platform, style)
            st.session_state['generated_result'] = generated_text

# --- OUTPUT & ACTION ---
if 'generated_result' in st.session_state:
    st.divider()
    st.subheader("📝 Draft Output")
    
    # Editable Text Area
    final_content = st.text_area("Edit before posting:", value=st.session_state['generated_result'], height=200)
    
    col_a, col_b = st.columns([1, 4])
    
    with col_a:
        # DYNAMIC BUTTON LOGIC
        if platform == "Nostr":
            if st.button("🚀 Post to Nostr"):
                with st.status("Broadcasting to Relays..."):
                    result = post_to_nostr(final_content)
                    if "✅" in result:
                        st.success(result)
                        save_memory(topic, final_content, "Nostr")
                    else:
                        st.error(result)
        
        elif platform == "Telegram":
            if st.button("✈️ Post to Telegram"):
                with st.status("Sending to Channel..."):
                    result = post_to_telegram(final_content)
                    if "✅" in result:
                        st.success(result)
                        save_memory(topic, final_content, "Telegram")
                    else:
                        st.error(result)
        
        else:
            # For platforms we don't automate yet (X/LinkedIn)
            st.info(f"Automatic posting for {platform} is coming soon. Copy manually!")