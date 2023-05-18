# 欢迎来到战术小队中文维基

[![Netlify Status](https://api.netlify.com/api/v1/badges/0731eb51-4daf-4794-86f1-f10af6cda9db/deploy-status){width=30%}](https://app.netlify.com/sites/polite-stroopwafel-e18e0d/deploys)

<iframe src="https://kookapp.cn/widget?id=4939320590138488&theme=dark" width="100%" height="80" allowtransparency="true" frameborder="0"></iframe>

战术小队（Squad）是由 Offworld Industries 开发，在 Steam 平台上发售，由 KickStarter 资助的一款**在线、基于团队、以军事为主题的第一人称射击游戏**。

Squad 让多达 100 名玩家的团队在对局中决定如何进行前哨建设和人员部署，团队合作与沟通对于成功至关重要。

当前发布版本：[v4.4.1](./update/v4.4.1/release-notes/)

战术小队中文维基致力于成为一个**开放且持续更新的战术小队非盈利性知识整合站点**，为各位玩家提供实用的游戏知识。本站为各位玩家准备了模式、载具、兵种以及阵营等游戏内容，帮助各位玩家快速深入的了解战术小队。

本项目受 [CTF Wiki](https://ctf-wiki.org/) 启发，在编写过程中参考了诸多资料，在此一并致谢。

如果您觉得本站对您有很大帮助，请考虑[投喂我们](./intro/support)。


## Material color palette 颜色主题

### Primary colors 主色

点击色块可更换主题的主色
<div class="tx-switch">
<button data-md-color-primary="red"><code>Red</code></button>
<button data-md-color-primary="pink"><code>Pink</code></button>
<button data-md-color-primary="purple"><code>Purple</code></button>
<button data-md-color-primary="deep-purple"><code>Deep Purple</code></button>
<button data-md-color-primary="indigo"><code>Indigo</code></button>
<button data-md-color-primary="blue"><code>Blue</code></button>
<button data-md-color-primary="light-blue"><code>Light Blue</code></button>
<button data-md-color-primary="cyan"><code>Cyan</code></button>
<button data-md-color-primary="teal"><code>Teal</code></button>
<button data-md-color-primary="green"><code>Green</code></button>
<button data-md-color-primary="light-green"><code>Light Green</code></button>
<button data-md-color-primary="lime"><code>Lime</code></button>
<button data-md-color-primary="yellow"><code>Yellow</code></button>
<button data-md-color-primary="amber"><code>Amber</code></button>
<button data-md-color-primary="orange"><code>Orange</code></button>
<button data-md-color-primary="deep-orange"><code>Deep Orange</code></button>
<button data-md-color-primary="brown"><code>Brown</code></button>
<button data-md-color-primary="grey"><code>Grey</code></button>
<button data-md-color-primary="blue-grey"><code>Blue Grey</code></button>
<button data-md-color-primary="white"><code>White</code></button>
</div>
<script>
  var buttons = document.querySelectorAll("button[data-md-color-primary]");
  Array.prototype.forEach.call(buttons, function(button) {
    button.addEventListener("click", function() {
      document.body.dataset.mdColorPrimary = this.dataset.mdColorPrimary;
      localStorage.setItem("data-md-color-primary",this.dataset.mdColorPrimary);
    })
  })
</script>

### Accent colors 辅助色

点击色块更换主题的辅助色
<div class="tx-switch">
<button data-md-color-accent="red"><code>Red</code></button>
<button data-md-color-accent="pink"><code>Pink</code></button>
<button data-md-color-accent="purple"><code>Purple</code></button>
<button data-md-color-accent="deep-purple"><code>Deep Purple</code></button>
<button data-md-color-accent="indigo"><code>Indigo</code></button>
<button data-md-color-accent="blue"><code>Blue</code></button>
<button data-md-color-accent="light-blue"><code>Light Blue</code></button>
<button data-md-color-accent="cyan"><code>Cyan</code></button>
<button data-md-color-accent="teal"><code>Teal</code></button>
<button data-md-color-accent="green"><code>Green</code></button>
<button data-md-color-accent="light-green"><code>Light Green</code></button>
<button data-md-color-accent="lime"><code>Lime</code></button>
<button data-md-color-accent="yellow"><code>Yellow</code></button>
<button data-md-color-accent="amber"><code>Amber</code></button>
<button data-md-color-accent="orange"><code>Orange</code></button>
<button data-md-color-accent="deep-orange"><code>Deep Orange</code></button>
</div>
<script>
  var buttons = document.querySelectorAll("button[data-md-color-accent]");
  Array.prototype.forEach.call(buttons, function(button) {
    button.addEventListener("click", function() {
      document.body.dataset.mdColorAccent = this.dataset.mdColorAccent;
      localStorage.setItem("data-md-color-accent",this.dataset.mdColorAccent);
    })
  })
</script>

<style>
button[data-md-color-accent]> code {
    background-color: var(--md-code-bg-color);
    color: var(--md-accent-fg-color);
  }
button[data-md-color-primary] > code {
    background-color: var(--md-code-bg-color);
    color: var(--md-primary-fg-color);
  }
button[data-md-color-primary='white'] > code {
    background-color: var(--md-primary-bg-color);
    color: var(--md-primary-fg-color);
  }
button[data-md-color-accent],button[data-md-color-primary],button[data-md-color-scheme]{
    width: 8.4rem;
    margin-bottom: .4rem;
    padding: 2.4rem .4rem .4rem;
    transition: background-color .25s,opacity .25s;
    border-radius: .2rem;
    color: #fff;
    font-size: .8rem;
    text-align: left;
    cursor: pointer;
}
button[data-md-color-accent]{
  background-color: var(--md-accent-fg-color);
}
button[data-md-color-primary]{
  background-color: var(--md-primary-fg-color);
}
button[data-md-color-scheme='default']{
  background-color: hsla(0, 0%, 100%, 1);
}
button[data-md-color-scheme='slate']{
  background-color: var(--md-default-bg-color);
}
button[data-md-color-accent]:hover, button[data-md-color-primary]:hover {
    opacity: .75;
}
</style>

## 友情链接

- [JoinSquad - Official Homepage](https://joinsquad.com/)
- [在 Steam 上的 Squad](https://store.steampowered.com/app/393380)

!!! info "版权声明"
    本站点的所有文章内容，无特殊声明时，均在 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/ztrix/sata-license) 协议之条款下提供，附加条款亦可能应用。“SQ”与“SQUAD”徽标相关权利为其权利人所有，不受上述协议约束。

<figure markdown>
  [![Netlify](/img/logo/netlify.png){height="100%" width="100%" }](https://www.netlify.com/)
  <figcaption>本项目托管于 Netlify</figcaption>
</figure>