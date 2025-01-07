## 在终端上是使用ANSI转义序列实现BadApple的播放

### 效果演示(部分)
<div align="center">
   <img style="width:50%"  src="badapple.gif" />
</div>

---

### ANSI转义序列
ANSI转义序列是一种带内信号的转义序列标准，用于控制视频文本终端上的光标位置、颜色和其他选项。在文本中嵌入确定的字节序列，大部分以ESC转义字符和`[`字符开始，终端会把这些字节序列解释为相应的指令，而不是普通的字符编码。[详细介绍](ANSI.md)。

### 鸣谢

- **[Hao Lu](https://github.com/kisekied/BadAppleStringAnimation)**：提供的badapple.txt的文件
- **[Asciinema](https://asciinema.org/)**：终端记录录制及Gif转换
