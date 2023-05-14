import scrapy

class ProductReviewsSpider(scrapy.Spider):
    name = "product_reviews"

    def start_requests(self):
        # Specify the URL of the product's reviews page
        url = "http://example.com/product/reviews"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        reviews = []

        review_elements = response.css("div.review")

        for element in review_elements:
            name = element.css("p.reviewer-name::text").get().strip()
            rating = element.css("span.rating::text").get().strip()
            comment = element.css("p.comment::text").get().strip()

            review = {"name": name, "rating": rating, "comment": comment}
            reviews.append(review)

        yield reviews


class ProductImagesSpider(scrapy.Spider):
    name = "product_images"

    def start_requests(self):
        # Specify the URL of the product page
        url = "http://example.com/product"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        images = []

        image_elements = response.css("img.product-image")

        for element in image_elements:
            image_url = element.attrib["src"]
            images.append(image_url)

        yield images


class ProductCategoriesSpider(scrapy.Spider):
    name = "product_categories"

    def start_requests(self):
        # Specify the URL of the product page
        url = "http://example.com/product"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        categories = []

        category_elements = response.css("a.category")

        for element in category_elements:
            category = element.css("::text").get().strip()
            categories.append(category)

        yield categories


class RelatedProductsSpider(scrapy.Spider):
    name = "related_products"

    def start_requests(self):
        # Specify the URL of the product page
        url = "http://example.com/product"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        related_products = []

        product_elements = response.css("div.related-product")

        for element in product_elements:
            name = element.css("h3::text").get().strip()
            price = element.css("span.price::text").get().strip()
            product_url = element.css("a::attr(href)").get()

            related_product = {"name": name, "price": price, "url": product_url}
            related_products.append(related_product)

        yield related_products


class ProductAvailabilitySpider(scrapy.Spider):
    name = "product_availability"

    def start_requests(self):
        # Specify the URL of the product page
        url = "http://example.com/product"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        availability = response.css("span.availability::text").get().strip()
        yield availability


