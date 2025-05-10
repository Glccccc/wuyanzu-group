# Top-Python321
---

这是一个关于Python基础用法的作业，老师为学生布置了python的输入输出操作、变量和数据类型、格式化输出、条件语句、循环结构、处理文件操作和模块导入、函数编写等相关练习。

## ✨ 项目特点

- 📝 实践导向  
    所有任务都要求学生亲自动手编写代码，通过实践来加深对Python编程语言的理解和应用能力。这种实践导向的方式有助于学生更好地掌握编程技能。
- ✅ 逐步提升难度  
    任务从基础的输入输出操作、变量和数据类型，到条件语句、循环结构，再到函数定义与调用、文件操作等，逐步提升难度，形成一个由浅入深的学习路径。
- 💾 覆盖知识全面  
    涵盖了Python编程的多个重要方面，包括但不限于数据类型、控制结构、函数、模块、文件操作、异常处理等，使学生能够全面地了解和掌握Python编程语言。
- 🎨 反馈和评估机制  
    要求学生在代码文件中以注释的形式保留程序运行的输出结果，并在指定的“Журнал”服务中报告作业完成情况，这有助于教师对学生的学习进度和成果进行评估和反馈。
- 🔑 与实际应用结合  
    任务中涉及的场景如密码强度检查、出租车费用计算、文件操作等，都是与实际生活或工作相关的应用场景，使学生能够将所学知识应用到实际问题中。

## 🚀 快速开始

### 克隆项目

``` bash
git clone https://github.com/Glccccc/wuyanzu-group.git
cd wuyanzu-group
```

### 启动项目

```bash
cd wuyanzu-group/2023.04.09
python 1.py
python 2.py
...
```

项目将运行在 `本地的开发环境`

## 📦 项目结构

```
wuyanzu-group/
├── 2023.04.09/
│   ├── # HW 2023.04.09.txt
│   ├── 1.py
│   ├── 2.py
│   ├── 3.py
│   ├── 4.py
│   └── 5.py
├── 2023.04.16/
├── 2023.04.23/
├── ...
└── README.md
```
<!-- by 管立超 -->

## 📮 项目主要功能说明与截图

### 2023.05.14/文件下的任务、功能及使用方法：  
1. **编写 strong_password 函数**  
    
    *功能：* 检查密码是否为强密码。  
    
    *参数：*   
    - 参数1： 关键字必需参数，类型为 str，表示密码。  
   
    *返回值：* 
    - 类型为 bool。当密码满足以下条件时返回 True，否则返回 False。

    *测试方法如下：*
    ```python
    strong_password('aA1!') == False  # 长度不够
    strong_password('aA1!aA1!') == True  # 符合所有条件 
    ```
    
    *测试结果：*  
    ![alt text](./asset/2023.05.14/image-2.png)  

2. **编写 taxi_cost 函数**  
    
    *功能：* 计算出租车费用。

    *参数：* 
     - 参数1：关键字必需参数，类型为 str，表示密码。
     - 参数2：关键字参数（可选），表示等待时间（分钟），默认为 0，类型为 int。  
      
    *返回值：* 
    - 若参数不合理（如为负数），返回 None。
    - 否则，根据规则计算并返回费用（整数）。

    *测试方法如下：*
    ```python
   taxi_cost(1500)
    ```
    
    *测试结果：*  
    ![alt text](./asset/2023.05.14/image-3.png)
3. **编写 numbers_strip 函数**  
    
    *功能：* 从列表中删除 n 个最小和最大数。  
    
    *参数：*   
    - 参数1：一个必需的位置 - 关键字参数，列表（元素为 float）。
    - 参数2：一个可选的位置 - 关键字参数 n，默认为 1，类型为 int。
    - 参数3：一个严格的关键字参数，类型为 bool，默认 False，用于决定返回修改后的原列表还是新列表。  
   
    *返回值：* 按要求返回修改后的原列表或新列表。
   
    *测试方法如下：*
    ```python
   nums =[10,20,30,40,50,60,70]
   nums_test= numbers_strip(nums, 3, copy=True)
   nums_test
    ```
    
    *测试结果：*  
    ![alt text](./asset/2023.05.14/image-4.png)
4. **编写 countable_nouns 函数**  
    
    *功能：* 根据数词选择合适的俄语名词形式。  
    
    *参数：*   
    - 参数1：一个必需的 int 类型参数，表示数词。
    - 参数2：一个必需的 tuple 参数，包含三个 str，分别对应名词的三种形式。  
    
    *返回值：* 根据数词规则返回对应的名词形式。
    
    *测试方法如下：*  
    ```python
    countable_nouns(1, ("год", "года", "лет"))
    ```
    
    *测试结果：*  
    ![alt text](./asset/2023.05.14/image-5.png)
5. **编写 central_tendency 函数**   
    
    *功能：* 计算一系列数的中心趋势度量。  
    
    *参数：* 
    - 参数1：位置参数1。
    - 参数2：位置参数2。
    - 参数3：任意数量的位置参数。  
    
    *返回值：* 一个字典，包含以下键值对：
    - 'median'：中位数（float）。
    - 'arithmetic'：算术平均数（float）。
    - 'geometric'：几何平均数（float）。
    - 'harmonic'：调和平均数（float）。
    
    *测试方法如下：*  
    ```python
    central_tendency(1, 2, 3, 4)
    ```   
    
    *测试结果：*   
    ![alt text](./asset/2023.05.14/image-6.png)

6. **编写 orth_triangle 函数**  
    
    *功能：* 计算直角三角形的第三边。  
    
    *参数：*   
    - 参数1：边长，类型为 int 或 float。
    - 参数2：边长，类型为 int 或 float。
    - 参数3：斜边，类型为 int 或 float。
   
   *返回值：*
    - 若计算可行，返回第三边长度（float）。
    - 否则（如参数不合理），返回 None。
    
    *测试方法如下：*  
    ```python
    orth_triangle(cath1=3, cath2=4)
    ```   
    
    *测试结果：*   
    ![alt text](./asset/2023.05.14/image-7.png)
   
### 2023.05.21/文件下的任务、功能及使用方法：
<!-- by 管立超 -->




<!--2023.09.10文件  by 刘兴发 -->
# 🇨🇳 中文版 README.md 示例
---


# Email Validator

一个简单的命令行界面（CLI）应用程序，用于验证电子邮件地址的正确性，并将有效的电子邮件地址保存到文件中。

## ✨ 项目特点

- 📝 验证输入的电子邮件地址是否正确
- ✅ 将有效的电子邮件地址保存到文件
- 💾 数据保存在本地文本文件中
- 🎨 简洁的命令行界面，易于使用

## 🚀 快速开始

### 克隆项目

```bash
git clone https://github.com/zaizai913/wuyanzu-group.git
cd Email Validator 


### 安装依赖

```bash
pip install -r requirements.txt
```

### 启动项目

```bash
python 1.py
```

项目将启动命令行界面，等待用户输入电子邮件地址。

## 📦 项目结构

```
EmailValidator/
├── model.py            # 数据处理和存储模型
├── view.py             # 用户界面逻辑
├── controller.py       # 业务逻辑协调
├── 1.py                # 程序入口
└── README.md
```

## 📮 项目主要功能说明与截图

## 1.py
这是程序的入口文件，负责启动应用程序。

    功能：
        导入 controller 模块。
        在 main 函数中，创建 Application 类的实例并调用其 input_email 方法。
        使用 if __name__ == '__main__': 确保直接运行此文件时才会执行 main 函数。

## controller.py
控制器模块，负责协调模型和视图之间的交互。

    功能：
        导入 model 和 view 模块。
        Application 类：
            save_email 方法：
                创建 Email 类的实例，验证电子邮件地址是否有效。
                如果有效，调用 FileIO.add_email 方法将地址保存到文件。
                调用 CLI.save_email 方法向用户显示成功消息。
                如果无效，捕获 ValueError 异常并调用 CLI.invalid_email 方法向用户显示错误消息。
            input_email 方法：
                使用 CLI.input_email 方法从用户获取电子邮件地址。
                如果用户输入空字符串，退出循环。
                否则，调用 save_email 方法处理输入的地址。

## model.py
模型模块，负责数据处理和存储。

    功能：
        Email 类：
            使用正则表达式验证电子邮件地址是否符合标准格式。
            如果地址有效，将其存储在私有属性 __email 中。
            如果无效，抛出 ValueError 异常。
        FileIO 类：
            提供静态方法 add_email，将电子邮件地址追加到指定文件中。
            默认保存路径为程序运行目录下的 emails.txt 文件。

## view.py
视图模块，负责与用户交互。

    功能：
        提供静态方法用于用户交互：
            input_email：从标准输入获取电子邮件地址。
            invalid_email：向用户显示地址无效的消息。
            save_email：向用户显示地址成功保存的消息。


1.输入电子邮件地址
![alt text](2023.09.10/images/screenshot1.png)


2.显示验证结果
![alt text](2023.09.10/images/screenshot2.png)

---
<!--2023.09.10文件 by 刘兴发 -->