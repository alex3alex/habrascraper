# Scrapy settings for hlinks project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'hscraper'

SPIDER_MODULES = ['hscraper.spiders']
NEWSPIDER_MODULE = 'hscraper.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'hlinks (+http://www.yourdomain.com)'

ITEM_PIPELINES = ['hscraper.pipelines.HscraperPipeline']

#LOG_LEVEL='INFO'

DOWNLOAD_DELAY = 10  # see http://habrahabr.ru/robots.txt
