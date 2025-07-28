let issuesFound = false;

[...document.querySelectorAll('a[target="_blank"]')].forEach(link => {
  const rel = (link.getAttribute('rel') || '').toLowerCase();
  const missing = [];

  if (!rel.includes('noopener')) missing.push('noopener');
  if (!rel.includes('noreferrer')) missing.push('noreferrer');

  if (missing.length > 0) {
    issuesFound = true;

    // Correct console warning with styled link for clarity
    console.warn(
      `⚠️ Tabnabbing risk: Missing ${missing.join(' and ')} in rel attribute. URL: %c${link.href}`,
      'color: blue; text-decoration: underline;'
    );

    // Highlight problematic links visually on the page
    link.style.border = '2px solid red';
    link.style.backgroundColor = 'rgba(255, 0, 0, 0.1)';
    link.title = `Missing ${missing.join(' and ')}`;

    // Log the actual DOM element for direct inspection
    console.log('Problematic Element:', link);
  }
});

if (!issuesFound) {
  console.log('%c✅ No tabnabbing risks found. All links are safe!', 'color: green; font-weight: bold;');
}

