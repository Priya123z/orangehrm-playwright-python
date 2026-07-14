from datetime import datetime


class Screenshot:

    @staticmethod
    def capture(page, test_name):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        page.screenshot(
            path=f"screenshots/{test_name}_{timestamp}.png"
        )
        