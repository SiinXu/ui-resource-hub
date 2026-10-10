#!/usr/bin/env python3
"""生成 legal.js：每条资源的许可类型、可复制的官方安装片段、npm/GitHub 链接。
规则（法律安全）：
- 只有 MIT / Apache-2.0 等宽松开源许可、且许可已核实（npm registry / GitHub API，2026-10-10）的库，才给「复制代码」。
- 代码只收录官方 README / 文档里公开的安装命令或几行用法，不转载组件源码。
- 付费 / 专有 / 许可未核实的资源：复制代码按钮禁用，只给提示词和原站链接。"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'data.json'), encoding='utf-8'))
NPM = 'https://www.npmjs.com/package/'
GH = 'https://github.com/'
LD = 'Jakubantalik/Libraries.dev'
# id: (license, code snippet or '', npm pkg or '', github repo or '', snippet source note)
OSS = {
 'ui-shadcn-com': ('MIT', 'npx shadcn@latest init\nnpx shadcn@latest add button', 'shadcn', 'shadcn-ui/ui'),
 'ai-sdk-dev-elements': ('Apache-2.0', 'npx ai-elements@latest', 'ai-elements', 'vercel/ai-elements'),
 'www-assistant-ui-com': ('MIT', 'npx assistant-ui@latest create', 'assistant-ui', 'assistant-ui/assistant-ui'),
 'www-assistant-ui-com-examples': ('MIT', 'npx assistant-ui@latest create', 'assistant-ui', 'assistant-ui/assistant-ui'),
 'openai-github-io-chatkit-js': ('MIT', 'npm install @openai/chatkit-react', '@openai/chatkit-react', 'openai/chatkit-js'),
 'ui-elevenlabs-io': ('MIT', '', '', 'elevenlabs/ui'),
 'www-prompt-kit-com': ('MIT', 'npx shadcn@latest add "https://prompt-kit.com/c/prompt-input.json"', '', 'ibelick/prompt-kit'),
 'shadcn-chatbot-kit-vercel-app': ('MIT', '', '', 'Blazity/shadcn-chatbot-kit'),
 'www-simple-ai-dev': ('MIT', '', '', 'Alwurts/simple-ai'),
 'llm-ui-com': ('MIT', 'npm install @llm-ui/react', '@llm-ui/react', ''),
 'reachat-dev': ('Apache-2.0', 'npm install reachat', 'reachat', 'reaviz/reachat'),
 'deepchat-dev': ('MIT', 'npm install deep-chat-react', 'deep-chat-react', 'OvidijusParsiunas/deep-chat'),
 'chatscope-io': ('MIT', 'npm install @chatscope/chat-ui-kit-react @chatscope/chat-ui-kit-styles', '@chatscope/chat-ui-kit-react', 'chatscope/chat-ui-kit-react'),
 'www-copilotkit-ai': ('MIT', 'npm install @copilotkit/react-core @copilotkit/react-ui', '@copilotkit/react-ui', 'CopilotKit/CopilotKit'),
 'tambo-co': ('MIT', 'npm install @tambo-ai/react', '@tambo-ai/react', 'tambo-ai/tambo'),
 'hashbrown-dev': ('MIT', 'npm install @hashbrownai/core @hashbrownai/react', '@hashbrownai/react', 'liveloveapp/hashbrown'),
 'github-com-langchain-ai-agent-chat-ui': ('MIT', 'npx create-agent-chat-app', 'create-agent-chat-app', 'langchain-ai/agent-chat-ui'),
 'docs-livekit-io-agents-start-frontend': ('Apache-2.0', 'npm install @livekit/components-react livekit-client', '@livekit/components-react', 'livekit/components-js'),
 'x-ant-design': ('MIT', 'npm install @ant-design/x', '@ant-design/x', 'ant-design/x'),
 'ui-lobehub-com': ('MIT', 'npm install @lobehub/ui', '@lobehub/ui', 'lobehub/lobe-ui'),
 'tdesign-tencent-com-chat': ('MIT', 'npm install @tdesign-vue-next/chat', '@tdesign-vue-next/chat', 'Tencent/tdesign-vue-next'),
 'shaders-paper-design': ('Apache-2.0', 'npm install @paper-design/shaders-react', '@paper-design/shaders-react', 'paper-design/shaders'),
 'shaders-paper-design-liquid-metal': ('Apache-2.0', 'npm install @paper-design/shaders-react', '@paper-design/shaders-react', 'paper-design/shaders'),
 'rive-app': ('MIT', 'npm install @rive-app/react-canvas', '@rive-app/react-canvas', 'rive-app/rive-react'),
 'www-shadergradient-co': ('MIT', 'npm install @shadergradient/react', '@shadergradient/react', 'ruucm/shadergradient'),
 'github-com-rdev-liquid-glass-react': ('MIT', 'npm install liquid-glass-react', 'liquid-glass-react', 'rdev/liquid-glass-react'),
 'motion-primitives-com': ('MIT', 'npx motion-primitives@latest add text-effect', 'motion-primitives', 'ibelick/motion-primitives'),
 'www-heroui-com': ('Apache-2.0', 'npm i @heroui/styles @heroui/react', '@heroui/react', 'heroui-inc/heroui'),  # v3 仓库许可 Apache-2.0（GitHub API 2026-10-10）
 'kokonutui-com': ('MIT', '', '', 'kokonut-labs/kokonutui'),
 'www-cult-ui-com': ('MIT', '', '', 'nolly-studio/cult-ui'),
 'smoothui-dev': ('MIT', '', '', 'educlopez/smoothui'),
 'uiverse-io': ('MIT', '', '', 'uiverse-io/galaxy'),
 'animata-design': ('MIT', '', '', 'codse/animata'),
 # Libraries.dev：库本身 MIT（README 原文：The libraries are MIT），Pro / Studio 导出另行授权
 'libraries-dev': ('MIT', 'npm install border-beam   # 或 thinking-orbs, bot-avatars, liquid-gooey, voice-glow, metal-fx, img-fx\n\nimport { BorderBeam } from "border-beam";\n\n<BorderBeam>\n  <button>Get started</button>\n</BorderBeam>', 'border-beam', LD),
 'orbs-jakubantalik-com': ('MIT', "npm install thinking-orbs\n\nimport { ThinkingOrb } from 'thinking-orbs';\n\n<ThinkingOrb state=\"searching\" size={64} />", 'thinking-orbs', LD),
 'beam-jakubantalik-com': ('MIT', 'npm install border-beam\n\nimport { BorderBeam } from "border-beam";\n\n<BorderBeam>\n  <button>Get started</button>\n</BorderBeam>', 'border-beam', LD),
 'metal-jakubantalik-com': ('MIT', "npm install metal-fx\n\nimport { MetalFx } from 'metal-fx';\n\n<MetalFx variant=\"button\">\n  <button>Upgrade to Pro</button>\n</MetalFx>", 'metal-fx', LD),
 'magicui-design': ('MIT', 'npx shadcn@latest add "https://magicui.design/r/marquee.json"', '', 'magicuidesign/magicui'),
 'github-com-huggingface-chat-ui': ('Apache-2.0', 'git clone https://github.com/huggingface/chat-ui\ncd chat-ui && npm install && npm run dev', '', 'huggingface/chat-ui'),
 'chainlit-io': ('Apache-2.0', 'pip install chainlit\nchainlit hello', '', 'Chainlit/chainlit'),
 'www-gradio-app': ('Apache-2.0', 'pip install gradio', '', 'gradio-app/gradio'),
 'www-librechat-ai': ('MIT', 'git clone https://github.com/danny-avila/LibreChat.git\ncd LibreChat && docker compose up -d', '', 'danny-avila/LibreChat'),
}
# 有 Pro / 付费部分的（开源部分仍可复制安装命令，付费部分禁用）
PRO = {'libraries-dev': 'Pro 预设和 Studio 导出', 'magicui-design': 'Magic UI Pro 模板'}
# 付费或专有：禁用复制代码
PAID = {'motion-dev-plus','ui-aceternity-com','www-shadcnblocks-com','21st-dev','21st-dev-community-components-s-ai-chat',
        'getstream-io-chat-solutions-ai-integration','www-thesys-dev','www-hover-dev','mobbin-com','refero-design'}
# 有开源仓库但许可不是 MIT/Apache（或带附加条款），只给链接不给代码
OTHERLIC = {'coss-com-ui': ('AGPL-3.0', 'cosscom/coss'), 'reactbits-dev': ('MIT + Commons Clause', 'DavidHDev/react-bits'),
            'reactbits-dev-animations-metallic-paint': ('MIT + Commons Clause', 'DavidHDev/react-bits'),
            'animate-ui-com': ('自定义许可', 'imskyleen/animate-ui'), 'openwebui-com': ('Open WebUI License', 'open-webui/open-webui'),
            'vercel-com-templates-next-js-chatbot': ('见仓库', 'vercel/chatbot'), 'neat-firecms-co': ('自定义许可', 'FireCMSco/neat'),
            'agentation-com': ('PolyForm Shield', '')}
PRICE_NOTE = None
# v3f：Prime 系社区版已核实为 MIT（仓库 LICENSE.md 原文，2026-10-10）；LTS 版本、PrimeBlocks、模板等另售，不提供
LICFIX = {
 'lib-primevue-org': ('MIT', 'npm install primevue @primeuix/themes', 'primevue', 'primefaces/primevue', 'PrimeVue LTS、PrimeBlocks、付费模板'),
 'lib-primeng-org': ('MIT', 'npm install primeng @primeuix/themes', 'primeng', 'primefaces/primeng', 'PrimeNG LTS（-lts 版本为商业许可）、PrimeBlocks、付费模板'),
 'lib-primereact-org': ('MIT', 'npm install primereact', 'primereact', 'primefaces/primereact', 'PrimeReact LTS、PrimeBlocks、付费模板'),
}
SERVICE = {'inspiration', 'generator', 'guide'}
LIBS = {L['id']: L for L in json.load(open(os.path.join(HERE, 'libs.src.json'), encoding='utf-8'))}
out = {}
for it in d['items']:
    rid, t = it['id'], it['type']
    if t == 'style': continue  # 组件样式卡沿用来源库的许可（前端 lg() 回退到 lib）
    e = {}
    if rid in LIBS:
        L = LIBS[rid]
        if L['pricing'] == 'paid': e = {'k': 'paid'}
        elif L['licOk']:
            e = {'k': 'oss', 'lic': L['lic']}
            if L['install']: e['code'] = L['install']
        elif L['lic']: e = {'k': 'lic', 'lic': L['lic']}
        else: e = {'k': 'svc' if t in SERVICE else 'unk'}
        if L['pkg'] and L['licOk']: e['npm'] = NPM + L['pkg']
        if L['repo']: e['gh'] = GH + L['repo']
        if rid in LICFIX:
            lic, code, pkg, repo, pro = LICFIX[rid]
            e = {'k': 'oss', 'lic': lic, 'code': code, 'npm': NPM + pkg, 'gh': GH + repo, 'pro': pro}
        out[rid] = e; continue
    if rid in OSS:
        lic, code, pkg, repo = OSS[rid]
        e = {'k': 'oss', 'lic': lic}
        if code: e['code'] = code
        if pkg: e['npm'] = NPM + pkg
        if repo: e['gh'] = GH + repo
        if rid in PRO: e['pro'] = PRO[rid]
    elif rid in PAID or it['pricing'] == 'paid':
        e = {'k': 'paid'}
    elif rid in OTHERLIC:
        lic, repo = OTHERLIC[rid]; e = {'k': 'lic', 'lic': lic}
        if repo: e['gh'] = GH + repo
    elif t == 'skill':
        e = {'k': 'skill'}
    elif t in SERVICE:
        e = {'k': 'svc'}
    else:
        e = {'k': 'unk'}
    out[rid] = e
open(os.path.join(HERE, 'legal.js'), 'w', encoding='utf-8').write('window.UI_LEGAL=' + json.dumps(out, ensure_ascii=False) + ';\n')
from collections import Counter
print(Counter(v['k'] for v in out.values()), 'with code:', sum(1 for v in out.values() if 'code' in v))
missing = [k for k in OSS if k not in out]; print('missing ids', missing)
