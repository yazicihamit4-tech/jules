from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Determine absolute path to index.html
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"

        print(f"Navigating to {file_path}")
        try:
            page.goto(file_path)

            # Login
            page.wait_for_selector("#screen-login", timeout=5000)
            page.fill("#usernameInput", "UITest")
            page.fill("#passwordInput", "123456")
            page.click("#btnLogin")
            page.wait_for_selector("#screen-lobby", timeout=5000)

            # Start Single Player (Assuming default diff is not 3, let's select 4)
            print("Starting Single Player...")
            page.click(".play-btn-huge") # Open Setup
            page.wait_for_selector("#modal-setup", timeout=2000)

            # Select 4 digits (default usually) and click Start
            page.click("button.btn-green") # Assuming the Start button in setup modal

            page.wait_for_selector("#screen-game", timeout=5000)
            print("In Game Screen (Single Player).")

            # Verify UI Elements are Hidden
            # chatToggleBtn: #btnGameChatToggle
            # sabotageBtn: #btnSabotage
            # emojiBar: .emoji-bar

            chat_btn = page.query_selector("#btnGameChatToggle")
            sabotage_btn = page.query_selector("#btnSabotage")
            emoji_bar = page.query_selector(".emoji-bar")

            visible_count = 0
            if chat_btn and chat_btn.is_visible():
                print("FAILURE: Chat Button is visible!")
                visible_count += 1
            if sabotage_btn and sabotage_btn.is_visible():
                print("FAILURE: Sabotage Button is visible!")
                visible_count += 1
            if emoji_bar and emoji_bar.is_visible():
                print("FAILURE: Emoji Bar is visible!")
                visible_count += 1

            if visible_count == 0:
                print("SUCCESS: UI Elements are hidden in Single Player.")

            page.screenshot(path="verification/ui_hidden_check.png")

        except Exception as e:
            print(f"Script failed: {e}")

        browser.close()

if __name__ == "__main__":
    run()
