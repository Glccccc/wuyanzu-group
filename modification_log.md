<!-- ai修改记录 -->

<!--2023.09.10文件 model.py-->
1.创建 requirements.txt 文件：
如果你的项目没有 requirements.txt 文件，你需要手动创建一个。requirements.txt 文件用于列出项目所需的依赖包及其版本。
在你的项目目录中创建一个名为 requirements.txt 的文件。
打开 requirements.txt 文件，添加以下内容（根据你的项目需求调整）：
    pathlib
    re
    sys
2.修改 model.py 类型注解：
确保你的 model.py 文件中的类型注解语法与你的 Python 版本兼容。如果你无法升级 Python 版本，可以修改 model.py 文件中的类型注解，例如：

    from typing import Union
    from pathlib import Path

    Pathlike = Union[str, Path]

这样可以确保代码在 Python 3.7 下也能正常运行。

<!--2023.09.10文件 model.py-->


<!--郑锐滨使用AI 修改记录-->
### 使用 ChatGPT 生成 Prompt  
- **使用工具**：ChatGPT  
- **操作内容**：生成用于编写 README 与术语词汇提取的 Prompt  
- **结果**：获得结构清晰、逻辑明确的 Prompt，为后续操作提供输入模板（如图ai_usage_screenshots\2205308060348\2205308060348_1.png和2205308060348_4.png）

---

### 使用 DeepSeek R1 和豆包 1.5 Pro 模型对比调优 Prompt  
- **使用工具**：DeepSeek R1、豆包 1.5 Pro  
- **操作内容**：对生成的 Prompt 内容在措辞、结构与适配性上进行模型间对比与优化  
- **结果**：确认最优版本用于 Cursor 中实际操作，确保指令执行效果最佳（如图ai_usage_screenshots\2205308060348\2205308060348_2.png和2205308060348_5.png）

---

### 使用 Cursor 中 ChatGPT-4.1 为项目 2023.05.28 全局作注释  
- **使用工具**：Cursor（ChatGPT-4.1）  
- **操作内容**：为项目 2023.05.28 的全部代码文件生成模块与函数级注释  
- **结果**：增强了代码可读性和文档化程度，注释内容已集成进代码

---

### 使用 Cursor 中 ChatGPT-4.1 为项目作出总结然后编写初步的 README 文档  
- **使用工具**：Cursor（ChatGPT-4.1）  
- **操作内容**：基于项目内容自动生成概述，并撰写 README 初稿，包括功能简介与技术要点  
- **结果**：初稿结构完整、内容清晰，为后续 README 精修奠定基础（如图ai_usage_screenshots\2205308060348\2205308060348_3.png）

---

### 使用 Cursor 中 ChatGPT-4.1 为项目 README 文档调优  
- **使用工具**：Cursor（ChatGPT-4.1）  
- **操作内容**：对 README 初稿进行语言润色与结构优化，调整表达逻辑与术语准确性  
- **结果**：生成风格统一、专业性更强的正式版 README，并完成更新提交（如图ai_usage_screenshots\2205308060348\2205308060348_7.png）

---

### 使用 Cursor 中 ChatGPT-4.1 分析中英文两个 README 文档作出术语词汇表  
- **使用工具**：Cursor（ChatGPT-4.1）  
- **操作内容**：对中英文 README 内容进行术语提取与对照整理，形成术语词汇表  
- **结果**：输出标准 Markdown 表格格式的中英术语词汇表，已纳入 terms.md 文件中（如图ai_usage_screenshots\2205308060348\2205308060348_8.png）

---
<!--郑锐滨使用AI 修改记录到此结束-->

<!--管立超使用AI 修改记录-->
### 使用 kimi 对文件夹中的俄语文档进行翻译总结 
- **使用工具**：kimi（长思考k1.5）  
- **操作内容**：翻译文档中的俄文，获取该文件夹下python任务的大致内容。 
- **结果**：输出总结内容。（如图ai_usage_screenshots\2205302020301\Snipaste_2025-05-13_16-34-18.png）

---

### 使用 kimi 对项目文件 2023.05.14下，自己不懂的代码做解释。   
- **使用工具**：kimi（长思考k1.5）  
- **操作内容**：为项目 2023.05.14 的部分代码文件进行分析解释。
- **结果**：理解了代码功能极其作用，完善readme文档功能解释部分。（如图ai_usage_screenshots\2205302020301\Snipaste_2025-05-13_16-39-01.png）
  
---

### 使用 kimi 对项目文件 2023.05.14下，自己不懂的代码进行代码测试。   
- **使用工具**：kimi（长思考k1.5）  
- **操作内容**：为项目 2023.05.14 的部分代码文件进行代码测试输出。
- **结果**：理解了代码功能极其作用，完善readme文档功能解释部分。（如图ai_usage_screenshots\2205302020301\Snipaste_2025-05-13_16-44-10.png）

---

### 使用 kimi 学习md基础语法   
- **使用工具**：kimi（长思考k1.5）  
- **操作内容**：帮助我在 Markdown 中改变正文的格式和样式。
- **结果**：学会文本加粗、斜体等组合使用，基础语法（如图ai_usage_screenshots\2205302020301\Snipaste_2025-05-13_16-47-28.png）
  
 ---
  <!--管立超使用AI 修改记录到此结束-->