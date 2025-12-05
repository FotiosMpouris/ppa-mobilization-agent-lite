import asyncio
import os
from nostr_sdk import Keys, Client, NostrSigner, EventBuilder, RelayUrl

def post_to_nostr(content):
    """
    Signs and publishes a note to Nostr relays.
    Returns: Success message or Error string.
    """
    nsec = os.getenv("NOSTR_NSEC")
    if not nsec:
        return "❌ Error: NOSTR_NSEC not found in .env file."

    async def _async_post():
        try:
            # 1. Parse Keys
            keys = Keys.parse(nsec)
            
            # 2. Create Signer
            signer = NostrSigner.keys(keys)
            
            # 3. Setup Client
            client = Client(signer)
            
            # 4. Add Relays (Parsing strings to RelayUrl)
            await client.add_relay(RelayUrl.parse("wss://relay.damus.io"))
            await client.add_relay(RelayUrl.parse("wss://relay.primal.net"))
            await client.add_relay(RelayUrl.parse("wss://nos.lol"))
            
            # 5. Connect
            await client.connect()
            
            # 6. Build Note
            builder = EventBuilder.text_note(content)
            
            # 7. Send
            output = await client.send_event_builder(builder)
            
            return f"✅ Posted to Nostr (Event ID: {output.id.to_hex()})"
            
        except Exception as e:
            return f"❌ Nostr Error: {str(e)}"

    # Run the async logic synchronously for the UI
    return asyncio.run(_async_post())