"""Deepened bodies (6–10 min reads) for the thinnest posts. Sources: blog_src/deep/<slug>.{en,zh}.md and
<slug>.prompt.{en,zh}.md (AI-prompt block). Applied in posts.py after POSTS2 is merged. Extra refs are appended
to each post's existing refs (all URLs checked to load on 2026-10-15)."""
import os, markdown
HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deep')
def _md(s): return markdown.markdown(s, extensions=['fenced_code', 'tables'], output_format='html')
def _r(slug, part):
    p = os.path.join(HERE, f'{slug}.{part}.md')
    return open(p, encoding='utf-8').read().strip() if os.path.exists(p) else None
EXTRA_REFS = {
 'prompts-for-ui': [('Prompt engineering overview','Anthropic','https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview')],
 'design-to-code-with-ai': [('Guide to the Figma MCP server','Figma Help Center','https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server'),
   ('Code Connect','Figma Help Center','https://help.figma.com/hc/en-us/articles/23920389749655-Code-Connect'),('Design Tokens Community Group','W3C Community Group','https://www.designtokens.org/'),
   ('Style Dictionary','Style Dictionary','https://styledictionary.com/'),('shadcn CLI','shadcn','https://ui.shadcn.com/docs/cli')],
 'taste-and-skills-for-agents': [('Agent Skills overview','Anthropic','https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview'),('Skills in Claude Code','Anthropic','https://code.claude.com/docs/en/skills')],
 'component-composition': [('Composition (asChild)','Radix','https://www.radix-ui.com/primitives/docs/guides/composition'),('React Aria','Adobe','https://react-aria.adobe.com/'),
   ('Ark UI','Chakra Systems','https://ark-ui.com/'),('class-variance-authority','Joe Bell','https://cva.style/')],
 'motion-that-feels-right': [('Animations guide','web.dev','https://web.dev/articles/animations-guide'),('Layout animations','Motion','https://motion.dev/docs/react-layout-animations')],
 'dark-mode-done-right': [('color-scheme','MDN','https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme'),
   ('light-dark()','MDN','https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark'),
   ('Understanding SC 1.4.3 Contrast (Minimum)','W3C WAI','https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html'),
   ('Color system overview — Material 3','Google','https://m3.material.io/styles/color/system/overview'),
   ('prefers-contrast','MDN','https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-contrast')],
 'accessibility-in-ai-generated-ui': [('Understanding SC 2.5.8 Target Size (Minimum)','W3C WAI','https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html'),
   ('Dialog (Modal) pattern','W3C WAI APG','https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/'),(':focus-visible','MDN','https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-visible'),
   ('axe-core','Deque','https://github.com/dequelabs/axe-core'),('Accessibility testing','Playwright','https://playwright.dev/docs/accessibility-testing'),
   ('The WebAIM Million','WebAIM','https://webaim.org/projects/million/')],
 'cult-ui-deep-dive': [('useReducedMotion','Motion','https://motion.dev/docs/react-use-reduced-motion'),('shadcn CLI','shadcn','https://ui.shadcn.com/docs/cli'),
   ('prefers-reduced-motion','MDN','https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion'),('Aceternity UI','Aceternity','https://ui.aceternity.com/')],
}
def apply(POSTS):
    for p in POSTS:
        s = p['slug']
        en, zh = _r(s, 'en'), _r(s, 'zh')
        if en and zh:
            p['en'], p['zh'] = _md(en), _md(zh)
            have = {u for _, _, u in p['refs']}
            p['refs'] = list(p['refs']) + [r for r in EXTRA_REFS.get(s, []) if r[2] not in have]
        pe, pz = _r(s, 'prompt.en'), _r(s, 'prompt.zh')
        if pe: p['prompt'] = dict(en=pe, zh=pz or pe)
    return POSTS
