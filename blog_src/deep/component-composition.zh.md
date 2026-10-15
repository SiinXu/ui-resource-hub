旧式组件库是一个带样式的 npm 包：装上之后，你得用覆盖样式和 `!important` 跟它较劲。shadcn/ui 把这件事反过来了：行为和无障碍来自 Radix 这类无头原语，样式来自 Tailwind 类名，组件源码直接复制进你的仓库，归你所有。这篇讲为什么这种组合模式特别适合 AI Agent、各层该怎么划分，以及哪些模式能让生成的代码保持可维护。

## 三层，三个负责人

把界面分成三层，每层变化频率不同，负责的人也不同：

1. **原语层**：无头的、可访问的行为，包括焦点管理、键盘操作、ARIA 关联、Portal。Radix Primitives、React Aria、Ark UI 都在这一层。你很少改它。
2. **组件层（你的 kit）**：在原语之上加了样式的组件，如 `Button`、`Dialog`、`Select`、`Card`。shadcn/ui 以源码形式给你的就是这一层。设计系统变化时才偶尔改。
3. **区块和页面层**：由组件拼出来的东西，比如定价区、设置表单、仪表盘头部。每周都在变。

Brad Frost 多年前提出的原子设计（原子、分子、有机体、模板、页面）讲的是类似的拆分。放到 AI 协作里，规则很简单：**让 Agent 主要在区块层干活，在组件层谨慎改动，几乎不碰原语层。**

## 为什么适合 Agent

- **上下文看得见。** 仓库里的代码能被读到。让 Agent"给 Button 加一个危险操作变体"，它可以打开 `button.tsx`，看到已有变体并照着写；如果是闭源 npm 包，它只能猜属性。
- **接口小。** 复合组件把一个复杂控件拆成职责单一的几部分，改动是局部的、可预测的。
- **注册表。** 注册表让任何项目都能用一条命令装上同一个组件，Agent 搭新应用时会复用你的组件，而不是重新写一套。

## 模式 1：复合组件

复合组件通过 context 共享状态，对外暴露几个部件，而不是一个有四十个属性的组件。对比一下：

```tsx
// 单体：每个新需求都变成一个新属性
<Dialog title="删除项目" description="此操作无法撤销。"
  confirmLabel="删除" cancelLabel="取消" danger showClose
  onConfirm={remove} footerAlign="end" />

// 复合：部件可以重新排列、省略或扩展
<Dialog>
  <DialogTrigger asChild><Button variant="outline">删除</Button></DialogTrigger>
  <DialogContent>
    <DialogHeader>
      <DialogTitle>删除项目</DialogTitle>
      <DialogDescription>此操作无法撤销。</DialogDescription>
    </DialogHeader>
    <DialogFooter>
      <DialogClose asChild><Button variant="ghost">取消</Button></DialogClose>
      <Button variant="destructive" onClick={remove}>删除</Button>
    </DialogFooter>
  </DialogContent>
</Dialog>
```

复合写法更长，但每个部件一目了然。想加一个"同时删除备份"的复选框，只需要插入一个元素，不用设计新属性。

## 模式 2：用 `asChild` 代替层层包裹

Radix 的 `asChild` 属性会把原语的行为合并到子元素上，而不是额外渲染一个 DOM 节点。`<DialogTrigger asChild><Button/></DialogTrigger>` 得到的是一个带触发器 ARIA 属性和事件的 `<button>`，而不是按钮套按钮。嵌套的可交互元素是生成代码里最常见的无障碍问题之一，所以要告诉 Agent：用原语部件包裹组件时，一律使用 `asChild`。

## 模式 3：把变体写成数据

shadcn/ui 的组件用 class-variance-authority 描述样式选项。变体变成一张小而清楚的表，而不是散落在 JSX 里的条件类名：

```tsx
const buttonVariants = cva(
  "inline-flex items-center justify-center rounded-md text-sm font-medium focus-visible:outline-none focus-visible:ring-2 disabled:opacity-50",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        outline: "border border-input bg-background hover:bg-accent",
        destructive: "bg-destructive text-destructive-foreground hover:bg-destructive/90",
      },
      size: { sm: "h-8 px-3", md: "h-9 px-4", lg: "h-10 px-6" },
    },
    defaultVariants: { variant: "default", size: "md" },
  }
);
```

Agent 改这种表很可靠。要一个新变体，得到的就是新增一行，用的还是你现有的 token 类名。

## 新增一个区块的步骤

1. **先盘点。** 让 Agent 列出新区块需要哪些组件、哪些还没有。
2. **有意识地补齐组件。** 从 shadcn 注册表或你自己的注册表安装，然后审一遍。不要让区块悄悄发明一个自己的按钮。
3. **只用组件和布局工具类拼区块。** 不要出现裸的 `<div onClick>`。
4. **检查状态和键盘。** 用 Tab 走一遍区块，用键盘打开、关闭每个弹层，确认焦点会回到触发按钮。
5. **把重复提升为组件。** 同一种组合在三个区块里出现，就给它起个名字，提升到组件层。

## 常见坑

- **为了改样式去改原语。** 样式属于组件层。fork 原语会丢掉上游的无障碍修复。
- **组件层属性爆炸。** 如果 `Card` 有 15 个布尔属性，它就该改成复合组件了。
- **重复的组件。** Agent 很乐意在某个功能目录里再生成一个 `Button`。审代码时要搜重复。
- **混用多个原语库。** 对话框用 Radix、弹出层用另一个库，就有两套焦点管理模型。尽量每个项目只选一个。
- **丢了来源。** 组件复制进来之后会和上游逐渐分叉，记下你最初基于哪个上游版本。

## 常见问题

**用 shadcn/ui 还是 MUI 这类打包好的库？** 如果你希望 Agent 能改组件，并且在意掌控外观，源码放在仓库里的组件库更方便。如果你想要零维护的上游更新，也接受库本身的外观，打包库也没问题。最贵的选择是在同一个产品里混用两者。

**怎么阻止 Agent 改原语层？** 写进 AGENTS.md，把原语放在命名清楚的目录里，再加一条 CODEOWNERS 规则或 CI 检查，发现那里有改动就提示。只要写下来，Agent 对目录约定的遵守程度很高。

**区块什么时候该变成组件？** 当它出现在三个地方、有清楚的名字、变化能用一张简短的变体表描述时。在那之前，重复比错误的抽象便宜。

**不是 React 技术栈怎么办？** 三层结构同样适用。Vue 和 Svelte 也有无头原语库，"Agent 拼区块、谨慎改组件、不碰原语"这条规则和框架无关。

## 我们的看法

shadcn 式组件库之所以成为 AI 界面工具的默认目标，靠的就是这种组合模式：源码在本地，部件小，变体是数据。在目录结构里把三层分清楚，告诉 Agent 它可以动哪一层，大部分"AI 把我的组件搞乱了"的问题都会消失。

## 清单

- 目录结构体现原语 / 组件 / 区块三层
- Agent 只用组件拼区块
- 用复合组件代替属性繁多的单体组件
- 原语部件包裹组件时使用 `asChild`
- 变体写成数据（cva 或类似方案）
- 每个新区块都检查过键盘和焦点
