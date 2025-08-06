AUTHOR = 'John P. Mahoney'
SITENAME = 'The Heron-Allen Society'
SITEURL = ""
SITESUBTITLE = 'towards the appreciation of the life and works of Edward Heron-Allen'

PATH = "content"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll - Links relevant to Edward Heron-Allen
# LINKS = (
#     ("Wikipedia: Edward Heron-Allen", "https://en.wikipedia.org/wiki/Edward_Heron-Allen"),
#     ("British Library Collections", "https://www.bl.uk/"),
#     ("Natural History Museum", "https://www.nhm.ac.uk/"),
#     ("West Sussex Record Office", "https://www.westsussex.gov.uk/libraries-and-heritage/west-sussex-record-office/"),
#     ("Violin Society of America", "https://www.vsaweb.org/"),
#     ("Royal Microscopical Society", "https://www.rms.org.uk/"),
# )

# Social and Contact Information
# SOCIAL = (
#     ("Contact the Society", "/contact.html"),
#     ("Newsletter Archive", "#"),
#     ("Research Inquiries", "mailto:research@heronallensociety.org"),
#     ("Membership Info", "#"),
# )

# Main navigation menu with nested structure
MENUITEMS = (
    ("The Society", "/about.html"),
    ("Symposia", "/symposia.html"),
    ("Publications", [
        ("Bibliography", "/bibliography.html"),
        ("Opuscula", "/opuscula.html"),
        ("Newsletters", "/newsletters.html"),
        ("Books", "/books.html"),
        ("Articles", "/articles.html"),
        ("Obituaries", "/obituaries.html"),
    ]),
    ("Membership", "/membership.html"),
    ("Edward Heron-Allen", [
        ("Biography", "/biography.html"),
        ("Bibliography", "/bibliography.html"),
        ("Interests", "/interests.html"),
    ]),
    ("News & Events", [
        ("Current News", "/news.html"),
        ("Appeals & Queries", "/appeals-queries.html"),
    ]),
    ("Links", "/links.html"),
    ("Contact", "/contact.html"),
)

DEFAULT_PAGINATION = 100

# Enable pagination for custom page templates
PAGINATED_TEMPLATES = {
    'index': None,
    'tag': None,
    'category': None,
    'author': None,
    'page_with_articles': None,
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Pages configuration
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['']

# Menu configuration
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Theme and appearance
THEME = 'theme'
DEFAULT_METADATA = {
    'status': 'published',
}

# Article and page settings
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Category and tag pages
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'

# Index page settings for relative URLs
# INDEX_SAVE_AS = 'index.html'

# Static paths
STATIC_PATHS = ['images', 'documents', 'extra']

# Plugins (if needed later)
# PLUGIN_PATHS = ['pelican-plugins']
# PLUGINS = []

# Tag configuration
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 50

# Optional: Define suggested tags for consistency (documentary purposes)
# These don't enforce anything but serve as a reference
SUGGESTED_TAGS = {
    'Subject Areas': ['biography', 'music', 'science', 'literature', 'law', 'foraminifera', 'translations'],
    'Research Types': ['archival-research', 'manuscript-analysis', 'instrument-study', 'correspondence', 'discoveries'],
    'Time Periods': ['victorian-era', 'early-20th-century', '1860s', '1870s', '1880s', '1890s', '1900s'],
    'Geographic': ['england', 'london', 'selsey', 'italy', 'mediterranean'],
    'Document Types': ['letters', 'manuscripts', 'photographs', 'instruments', 'publications', 'diaries'],
    'Instruments': ['violin', 'viola', 'cello', 'bow-making', 'varnish', 'acoustics'],
    'Scientific': ['marine-biology', 'microscopy', 'specimen-collection', 'taxonomy', 'field-work']
}

# Copyright notice
COPYRIGHT_NAME = 'The Heron-Allen Society'
COPYRIGHT_YEAR = '2025'
