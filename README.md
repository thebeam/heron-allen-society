# The Heron-Allen Society Website

This is the official website for The Heron-Allen Society, built using [Pelican](https://getpelican.com/), a static site generator powered by Python.

## About Edward Heron-Allen

Edward Heron-Allen (1861-1943) was a remarkable Victorian polymath whose contributions spanned:
- Violin making and music
- Scientific research (foraminifera)
- Literature and translation (Persian poetry)
- Occult studies and palmistry
- Law and jurisprudence

## Project Structure

```
pelican_eha/
├── content/           # Source content files
│   ├── pages/        # Static pages (About, Contact)
│   └── *.md          # Blog articles/posts
├── output/           # Generated static site
├── pelicanconf.py    # Main configuration
├── publishconf.py    # Production configuration
├── Makefile          # Build automation
└── tasks.py          # Python build tasks
```

## Getting Started

### Prerequisites
- Python 3.7+
- Pelican with Markdown support

### Installation
```bash
pip install 'pelican[markdown]'
```

### Building the Site
```bash
# Generate the site
pelican content

# Or use the Makefile
make html
```

### Development Server
```bash
# Start local server for development
pelican --listen --port 8080

# Or use the Makefile
make serve
```

The site will be available at `http://localhost:8080`

### Publishing
```bash
# Build for production
pelican content -s publishconf.py

# Or use the Makefile
make publish
```

## Content Management

### Adding Articles
Create new Markdown files in the `content/` directory with the following metadata:

```markdown
Title: Your Article Title
Date: YYYY-MM-DD HH:MM
Category: General|Biography|Music|Research|Science
Tags: tag1, tag2, tag3
Slug: article-url-slug
Author: Author Name
Summary: Brief description of the article

# Article Content
Your article content in Markdown format...
```

### Adding Pages
Create Markdown files in `content/pages/` for static pages like About, Contact, etc.

### Categories
Current categories include:
- **General**: Society news and announcements
- **Biography**: Information about Edward Heron-Allen's life
- **Music**: Violin making and musical contributions
- **Research**: Scholarly research and discoveries
- **Science**: Scientific work and foraminifera studies

## Configuration

Key configuration options in `pelicanconf.py`:
- `SITENAME`: Site title
- `SITESUBTITLE`: Site subtitle
- `AUTHOR`: Default author
- `TIMEZONE`: Site timezone
- `DEFAULT_LANG`: Default language
- `LINKS`: External links for sidebar
- `SOCIAL`: Social media links

## Deployment

The site can be deployed to any static hosting service:
- GitHub Pages
- Netlify
- Vercel
- AWS S3
- Traditional web hosting

The generated site is in the `output/` directory.

## Contributing

### Content Guidelines
- Use proper Markdown formatting
- Include appropriate metadata
- Maintain scholarly accuracy
- Cite sources appropriately
- Use consistent date formats (YYYY-MM-DD)

### Adding Resources
- Images: Place in `content/images/`
- Documents: Place in `content/documents/`
- Other static files: Place in `content/extra/`

## Links and Resources

- [Pelican Documentation](https://docs.getpelican.com/)
- [Markdown Guide](https://www.markdownguide.org/)
- [Edward Heron-Allen on Wikipedia](https://en.wikipedia.org/wiki/Edward_Heron-Allen)

## Society Information

**The Heron-Allen Society**  
Dedicated to preserving and celebrating the life and works of Edward Heron-Allen

For more information about joining the society or contributing to research, visit our website or contact us through the provided channels.

---

*This website is maintained by The Heron-Allen Society for educational and research purposes.*
