# README

## Introduction

This project contains a script named `myvim.cgi` which is used for managing and editing Vim configurations through a web interface.

## Usage

To use the script, follow these steps:

1. Place the `myvim.cgi` script in your CGI-enabled directory on your web server.
2. Ensure the script has executable permissions: `chmod +x myvim.cgi`.
3. Access the script via your web browser using the appropriate URL.

## Vim Features Implemented

The `myvim.cgi` script implements the following Vim features:

1. **Cursor Movement**:
   - `l`: Move the cursor one character to the right.
   - `h`: Move the cursor one character to the left.

2. **Delete Character**:
   - `x`: Delete the character at the cursor position.

3. **Jump to Start or End of Line**:
   - `0`: Move the cursor to the beginning of the text.
   - `$`: Move the cursor to the end of the text.

4. **Delete Lines**:
   - `[n]dd`: Delete `n` lines starting from the cursor position. If `n` is not specified, delete one line by default.

These features are implemented by parsing user commands (`com`) and modifying the text content and cursor position (`loc`) accordingly. Additionally, the script generates an HTML form and JavaScript to display and edit the text on a web page, updating the cursor position and text content in real-time.

## 中文说明

### 介绍

这个项目包含一个名为 `myvim.cgi` 的脚本，用于通过Web界面管理和编辑Vim配置。

### 使用方法

要使用该脚本，请按照以下步骤操作：

1. 将 `myvim.cgi` 脚本放置在Web服务器上启用了CGI的目录中。
2. 确保脚本具有可执行权限：`chmod +x myvim.cgi`。
3. 使用适当的URL通过Web浏览器访问该脚本。

### 实现的Vim功能

`myvim.cgi` 脚本实现了以下Vim功能：

1. **光标移动**：
   - `l`：将光标向右移动一个字符。
   - `h`：将光标向左移动一个字符。

2. **删除字符**：
   - `x`：删除光标所在位置的字符。

3. **跳转到行首或行尾**：
   - `0`：将光标移动到文本的开头。
   - `$`：将光标移动到文本的末尾。

4. **删除行**：
   - `[n]dd`：删除从光标所在行开始的 `n` 行。如果没有指定 `n`，则默认删除一行。

这些功能通过解析用户输入的命令（`com`）来实现，并相应地修改文本内容和光标位置（`loc`）。此外，代码还生成了一个 HTML 表单和 JavaScript 脚本，用于在网页上显示和编辑文本，并实时更新光标位置和文本内容。
