#scrape the text
if input("scrape? [y/n]: ")=="y":
    import scrapy
    class ExampleSpider(scrapy.Spider):
        name = "playstation-plus"
        start_urls = ["https://www.finder.com.au/playstation-plus-free-games"]

        def parse(self, response):
            # Extract text from the website
            text = response.xpath('//body//text()').getall()
            cleaned_text = " ".join(text).strip()

            # Store the extracted text in a string variable or perform any desired processing
            extracted_text = cleaned_text

            # Print the extracted text or perform any further actions
            with open("/home/danny/Development/Projects/playstation/extracted.txt","w") as f:
                f.write(extracted_text)

    # Run the spider
    from scrapy.crawler import CrawlerProcess

    process = CrawlerProcess()
    process.crawl(ExampleSpider)
    process.start()
#open the list, as a list split by line
with open("/home/danny/Development/Projects/playstation/list.txt", "r") as file:
    ls=file.readlines()
    ls = [line.strip() for line in ls]
    with open("/home/danny/Development/Projects/playstation/extracted.txt","r") as f:
        ext=f.read()
        result=[]
        for i in ls:
            if i in ext:
                result.append(i)
        #print(result)
        with open("/home/danny/Development/Projects/playstation/result.txt","w") as r:
            for i in result:
                r.write(i)
                r.write("\n")