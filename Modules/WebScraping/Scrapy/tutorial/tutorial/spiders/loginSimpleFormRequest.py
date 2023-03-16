import scrapy

def authentication_failed(response):
    # TODO: Check the contents of the response and return True if it failed
    # or False if it succeeded.
    pass

class LoginSpider(scrapy.Spider):
    name = 'simple_login'
    start_urls = ['https://mi.payway.com.ar/ms/ui-login/login']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'email': 'mail@gmail.com', 'pwd': 'contrasenita'},
            callback=self.after_login
        )

    def after_login(self, response):
        if authentication_failed(response):
            self.logger.error("Login failed")
            return

        # continue scraping with authenticated session...
        print(response)
        