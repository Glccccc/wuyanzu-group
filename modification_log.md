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