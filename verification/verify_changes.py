from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load local file
        page.goto(f"file://{os.getcwd()}/index.html")

        # Disable animations to fix stability issues
        page.add_style_tag(content="""
            *, *::before, *::after {
                animation: none !important;
                transition: none !important;
            }
        """)

        # 1. Login
        page.fill("#usernameInput", "TestUser")
        page.fill("#passwordInput", "123")
        page.click("#btnLogin")

        # Wait for Lobby
        page.wait_for_selector("#screen-lobby")
        page.wait_for_timeout(1000)

        # 2. Click Play Button
        page.click(".play-btn-huge", force=True)
        page.wait_for_timeout(500)

        # Screenshot 1: Game Selection Modal
        page.screenshot(path="verification/1_game_select_modal.png")
        print("Screenshot 1 taken: Game Selection Modal")

        # 3. Click Number Game
        page.click("text=SAYI OYUNU")
        page.wait_for_timeout(500)

        # Screenshot 2: Number Game Setup (Classic)
        page.screenshot(path="verification/2_number_setup_classic.png")
        print("Screenshot 2 taken: Number Setup (Classic)")

        # 4. Change to Timed Mode
        page.select_option("#singleMode", "timed")
        page.wait_for_timeout(200)

        # Screenshot 3: Number Setup (Timed)
        page.screenshot(path="verification/3_number_setup_timed.png")
        print("Screenshot 3 taken: Number Setup (Timed)")

        # 5. Start Number Game
        page.click("#modal-setup .btn-green")
        page.wait_for_selector("#screen-game")
        page.wait_for_timeout(500)

        # 6. Make a Guess to see 3D History Bubble
        page.fill("#guessInput", "1234")
        page.click("#btnGuess")
        page.wait_for_timeout(500)

        # Screenshot 4: Number Game Board (3D Bubbles)
        page.screenshot(path="verification/4_number_game_board.png")
        print("Screenshot 4 taken: Number Game Board")

        # 7. Go Back to Lobby
        # Click Exit Button in Number Game
        page.click("#gameCard button.btn-red", force=True)
        page.wait_for_selector("#modal-exit-confirm")
        page.wait_for_timeout(500)

        # Confirm Exit
        page.click("#modal-exit-confirm .btn-red")

        page.wait_for_selector("#screen-lobby")
        page.wait_for_timeout(500)

        # 8. Open Word Game
        page.click(".play-btn-huge", force=True)
        page.wait_for_timeout(500)
        page.click("text=KELİME OYUNU")
        page.wait_for_timeout(500)

        # Screenshot 5: Word Game Setup
        page.screenshot(path="verification/5_word_game_setup.png")
        print("Screenshot 5 taken: Word Game Setup")

        # 9. Start Word Game
        page.click("#modal-word-setup .btn-green")
        page.wait_for_selector("#screen-word-game")
        page.wait_for_timeout(500)

        # Screenshot 6: Word Game Board (3D Cells)
        page.screenshot(path="verification/6_word_game_board.png")
        print("Screenshot 6 taken: Word Game Board")

        browser.close()

if __name__ == "__main__":
    run()
