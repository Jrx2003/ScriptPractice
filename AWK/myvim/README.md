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

## ����˵��

### ����

�����Ŀ����һ����Ϊ `myvim.cgi` �Ľű�������ͨ��Web�������ͱ༭Vim���á�

### ʹ�÷���

Ҫʹ�øýű����밴�����²��������

1. �� `myvim.cgi` �ű�������Web��������������CGI��Ŀ¼�С�
2. ȷ���ű����п�ִ��Ȩ�ޣ�`chmod +x myvim.cgi`��
3. ʹ���ʵ���URLͨ��Web��������ʸýű���

### ʵ�ֵ�Vim����

`myvim.cgi` �ű�ʵ��������Vim���ܣ�

1. **����ƶ�**��
   - `l`������������ƶ�һ���ַ���
   - `h`������������ƶ�һ���ַ���

2. **ɾ���ַ�**��
   - `x`��ɾ���������λ�õ��ַ���

3. **��ת�����׻���β**��
   - `0`��������ƶ����ı��Ŀ�ͷ��
   - `$`��������ƶ����ı���ĩβ��

4. **ɾ����**��
   - `[n]dd`��ɾ���ӹ�������п�ʼ�� `n` �С����û��ָ�� `n`����Ĭ��ɾ��һ�С�

��Щ����ͨ�������û���������`com`����ʵ�֣�����Ӧ���޸��ı����ݺ͹��λ�ã�`loc`�������⣬���뻹������һ�� HTML ���� JavaScript �ű�����������ҳ����ʾ�ͱ༭�ı�����ʵʱ���¹��λ�ú��ı����ݡ�
