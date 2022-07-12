from reader import make_reader
reader = make_reader('db.sqlite')
reader.add_feed('http://www.hellointernet.fm/podcast?format=rss')
reader.update_feeds()
entries = list(reader.get_entries())

reader.mark_entry_as_read(entries[0])
[e.title for e in reader.get_entries(read=False)]
['H.I. #107: One Year of Weird', 'H.I. #106: Water on Mars', ...]
[e.title for e in reader.get_entries(read=True)]
['H.I. #108: Project Cyclops']
reader.update_search()
for e in reader.search_entries('year', limit=3):
    title = e.metadata.get('.title')
    print(title.value, title.highlights)