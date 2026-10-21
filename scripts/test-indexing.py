"""Verify production/preview crawl policy in isolated builds, without network access."""
from pathlib import Path
import json
import os
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
CASES = [
    ('local formal build', None, None, True),
    ('official production', 'https://castelein.eu.com', 'production', True),
    ('www production', 'https://www.castelein.eu.com/', 'production', True),
    ('Git preview with default origin', None, 'preview', False),
    ('development with formal origin', 'https://castelein.eu.com', 'development', False),
    ('separate preview project', 'https://paul-castelein-preview.vercel.app', 'production', False),
    ('other host', 'https://example.test', None, False),
    ('unknown environment', None, 'staging', False),
]

with tempfile.TemporaryDirectory(prefix='castelein-indexing-') as temporary:
    project = Path(temporary) / 'site'
    shutil.copytree(ROOT, project, ignore=shutil.ignore_patterns(
        '.git', '.vercel', '.env*', 'qa', 'research', 'dist', 'node_modules', '__pycache__'))
    for label, configured_origin, environment, indexable in CASES:
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
        origin = (configured_origin or 'https://castelein.eu.com').rstrip('/')
        pages = json.loads((project / 'content/public-pages.json').read_text())
        public_count = 0
        for page in pages:
            html = (project / page).read_text()
            public = 'http-equiv="refresh"' not in html and not page.endswith('404.html')
            public_count += public
            expected = 'index,follow' if indexable and public else 'noindex,nofollow'
            assert f'<meta name="robots" content="{expected}">' in html, (label, page)
            assert (project / 'dist' / page).read_text() == html, (label, page, 'bundle differs')
        assert public_count == 21, (label, public_count)
        robots = (f'User-agent: *\nAllow: /\nDisallow: /api/\n\nSitemap: {origin}/sitemap.xml\n'
                  if indexable else 'User-agent: *\nDisallow: /\n')
        assert (project / 'robots.txt').read_text() == robots, label
        assert (project / 'dist/robots.txt').read_text() == robots, label
        sitemap = ET.fromstring((project / 'dist/sitemap.xml').read_text())
        urls = [entry[0].text for entry in sitemap]
        assert len(urls) == 21 and all(url.startswith(origin + '/') for url in urls), label
        assert all('404' not in url and '/api/' not in url for url in urls), label
        assert ('Preview for content review.' in (project / 'dist/llms.txt').read_text()) != indexable, label
        print(f'PASS: {label} ({public_count} public pages, errors and redirects, robots, sitemap, bundle)')
