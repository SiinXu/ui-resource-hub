You are working in a React codebase that uses headless primitives (Radix / React Aria / Ark) + a styled kit (shadcn-style, source in this repo) + page blocks.
Task: build <describe the block> as a new block.
Rules:
1. First list the kit components you will use and any that are missing. Stop and ask before creating a new kit component.
2. Compose only from kit components and layout utilities. No <div onClick>, no nested interactive elements; use asChild when a primitive part wraps a kit component.
3. Do not edit files in the primitives layer. Do not create a second Button/Input/Card anywhere.
4. New styling options go into the component's variants table (cva), using existing token classes.
5. Implement keyboard behaviour and focus return for every popover/dialog/menu.
Output: component list → code → a note on anything that appears in 3+ blocks and should be promoted to the kit.
