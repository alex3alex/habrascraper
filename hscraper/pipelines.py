# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import sqlite3

def sqlitify(s):
    return s.replace('\n', '').replace('\t', '').replace('\r', '')


conn = sqlite3.connect('hscraper.db')

c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS `posts` (
      `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      `title` varchar(255) NOT NULL,
      `url` varchar(255) NOT NULL,
      `text` TEXT NOT NULL);
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS `comments` (
      `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      `post_id` INTEGER NOT NULL,
      `text` TEXT NOT NULL);
''')


class HscraperPipeline(object):
    def process_item(self, item, spider):
        c.execute('''
            INSERT INTO `posts` (title, text, url) VALUES (?, ?, ?);
        ''', (item['title'], sqlitify(item['text']), item['url']))
        post_id = c.lastrowid
        c.executemany('''
            INSERT INTO `comments` (post_id, text) VALUES (?, ?)
        ''', [(post_id, sqlitify(text)) for text in item['comments']])
        conn.commit()
        return item