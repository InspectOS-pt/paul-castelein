"""Verify production/preview crawl policy in isolated builds, without network access."""
from pathlib import Path
from html.parser import HTMLParser
import json
import os
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
PRIMARY = 'https://www.castelein.eu.com'
CASES = [
    ('local formal build', None, None, True, PRIMARY),
    ('legacy apex production', 'https://castelein.eu.com', 'production', True, PRIMARY),
    ('www production', PRIMARY+'/', 'production', True, PRIMARY),
    ('Git preview with default origin', None, 'preview', False, PRIMARY),
    ('development with formal origin', 'https://castelein.eu.com', 'development', False, PRIMARY),
    ('separate preview project', 'https://paul-castelein-preview.vercel.app', 'production', False, 'https://paul-castelein-preview.vercel.app'),
    ('other host', 'https://example.test', None, False, 'https://example.test'),
    ('unknown environment', None, 'staging', False, PRIMARY),
]

class Metadata(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
        self.canonical = None
        self.reading_schema = False
        self.schema = ''

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'link' and attrs.get('rel') in ('canonical', 'alternate'):
            self.urls.append(attrs['href'])
            if attrs['rel'] == 'canonical':
                self.canonical = attrs['href']
        if tag == 'meta' and attrs.get('property') in ('og:url', 'og:image'):
            self.urls.append(attrs['content'])
        if tag == 'script' and attrs.get('type') == 'application/ld+json':
            self.reading_schema = True

    def handle_endtag(self, tag):
        if tag == 'script':
            self.reading_schema = False

    def handle_data(self, data):
        if self.reading_schema:
            self.schema += data

with tempfile.TemporaryDirectory(prefix='castelein-indexing-') as temporary:
    project = Path(temporary) / 'site'
    shutil.copytree(ROOT, project, ignore=shutil.ignore_patterns(
        '.git', '.vercel', '.env*', 'qa', 'research', 'dist', 'node_modules', '__pycache__'))
    for label, configured_origin, environment, indexable, origin in CASES:
        env = os.environ.copy()
        env.pop('CASTELEIN_SITE_ORIGIN', None)
        env.pop('VERCEL_ENV', None)
        if configured_origin is not None:
            env['CASTELEIN_SITE_ORIGIN'] = configured_origin
        if environment is not None:
            env['VERCEL_ENV'] = environment
        result = subprocess.run([sys.executable, 'scripts/build-site.py'], cwd=project,
                                env=env, capture_output=True, text=True)
        assert result.returncode == 0, (label, result.stdout, result.stderr)
        pages = json.loads((project / 'content/public-pages.json').read_text())
        public_count = 0
        public_urls = []
        for page in pages:
            html = (project / page).read_text()
            redirect = 'http-equiv="refresh"' in html
            public = not redirect and not page.endswith('404.html')
            public_count += public
            expected = 'index,follow' if indexable and public else 'noindex,nofollow'
            assert f'<meta name="robots" content="{expected}">' in html, (label, page)
            assert (project / 'dist' / page).read_text() == html, (label, page, 'bundle differs')
            metadata = Metadata()
            metadata.feed(html)
            assert len(metadata.urls) == (1 if redirect else 7), (label, page, 'missing SEO URLs')
            assert all(url.startswith(origin + '/') for url in metadata.urls), (label, page, metadata.urls)
            if metadata.schema:
                assert json.loads(metadata.schema)['url'] == metadata.canonical, (label, page, 'structured URL differs')
            if public:
                expected_url = origin + '/' + page.removesuffix('index.html')
                assert metadata.canonical == expected_url, (label, page, 'canonical route differs')
                public_urls.append(expected_url)
        assert public_count == 21, (label, public_count)
        robots = (f'User-agent: *\nAllow: /\nDisallow: /api/\n\nSitemap: {origin}/sitemap.xml\n'
                  if indexable else 'User-agent: *\nDisallow: /\n')
        assert (project / 'robots.txt').read_text() == robots, label
        assert (project / 'dist/robots.txt').read_text() == robots, label
        sitemap = ET.fromstring((project / 'dist/sitemap.xml').read_text())
        urls = [entry[0].text for entry in sitemap]
        assert urls == public_urls and len(urls) == 21, (label, 'sitemap differs from public canonical URLs')
        assert all('404' not in url and '/api/' not in url for url in urls), label
        llms = (project / 'dist/llms.txt').read_text()
        assert ('Preview for content review.' in llms) != indexable, label
        assert [line[2:] for line in llms.splitlines() if line.startswith('- ')] == public_urls, (label, 'llms URLs differ')
        print(f'PASS: {label} ({public_count} public pages, errors and redirects, canonical/hreflang/Open Graph/schema URLs, robots, sitemap, bundle)')
