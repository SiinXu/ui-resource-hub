You are converting one Figma frame into production code for my existing codebase.
Context you have: the frame's design context (via the Figma MCP server or my export), my tokens in <tokens file>, my components in <components dir or registry URL>.
Process:
1. Before writing code, list every element in the frame and the component from MY codebase you will use for it. Mark anything with no match as "NEW" and stop for my confirmation.
2. Map layout to flex/grid from auto-layout. No absolute positioning unless the design truly overlaps.
3. Use CSS variables / token names only. No raw hex colours, no pixel values that are not on my spacing scale.
4. Implement default, hover, focus-visible, loading, empty and error states, even if the frame only shows the default.
5. Use semantic HTML: <button>, <a>, <label>, headings in order.
Output: the component list first; after I confirm, the code, then a short list of assumptions and anything the design did not specify.
