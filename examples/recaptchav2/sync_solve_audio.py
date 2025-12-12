from playwright.sync_api import sync_playwright

from playwright_recaptcha import recaptchav2


def main() -> None:
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com/recaptcha/api2/demo")

        with recaptchav2.SyncSolver(page) as solver:
            token = solver.solve_recaptcha(wait=True, credentials_json_path="credentials.json")
            print(token)


if __name__ == "__main__":
    main()
