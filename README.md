## スクレイピングとは？

### 概要

スクレイピングとは、**Webサイトのコンテンツの中から特定の情報だけを抽出・取集する技術**のことです。

!https://ai-inter1.com/wp-content/uploads/2019/12/Requests13.png

1. WEBサイトのHTMLなどのデータ取得。ただし、HTMLには必要な文章のデータだけでなく、タグなどのデータも混じっているので、必要なものだけを抽出する作業が必要になります。
2. データの抽出。ここでは複雑な構造のHTMLデータを解析し、必要な情報だけを抽出します。データの抽出にはBeautiful Soupなどのライブラリを使います。
3. 抽出した情報をデータベースやファイルなどに保存します。

### スクレイピングの手法

スクレイピングにはざっっくり分けて以下の２つの手法があります

1. **BeautifulSoup**を使う方法
    1. HTMLやXMLファイルからデータを取得し、解析するPythonのWEBスクレイピング用のライブラリ
    
    →とにかくWebページから情報を取ってくるときに使うと早く取ってこられる
    
2. **Selenium**を使う方法
    1. Webブラウザの操作を自動化することができるライブラリ
    
    →Seleniumはクリックしたり、キーボード操作なんかもできる便利屋みたいな感じ
    

BeautifulSoupでは自動操作というものはできないので、具体例で言えばログインが必要なページの分析が単体ではできません。

その点Seleniumでは自動操作によりメールアドレス、パスワードを入力しログインボタンを押す、というコードを予め書いておけばログインが可能です。

## セットアップ

### Seleniumの事前準備

Seleniumを使用したスクレイピングではwebdriverという実行ファイルが必要です。

1. （スクレイピングにGoogle Chromeのブラウザを使用するため、Google Chromeブラウザをインストール）
2. 自分のchromeのバージョンを確認
    
    [What version of Chrome do I have?](https://www.whatismybrowser.com/detect/what-version-of-chrome-do-i-have)
    
3. 以下のサイトでwebdriverをダウンロード**（**⚠️**自分が使用しているchromeのバージョンと同じものをダウンロード！！）**
    
    [ChromeDriver - WebDriver for Chrome - Downloads](https://chromedriver.chromium.org/downloads)
    
    **やり方：バージョン115以降は、ダウンロード先が変更になったみたいです。以下のサイトを参考に、chromeと同じバージョンのものをダウンロードしてください**
    
    [バージョン115以降のChrome用WebDriverのダウンロード方法 - ガンマソフト](https://gammasoft.jp/support/chrome-webdriver-for-ver115-and-newer/)
    
4. zipファイルを解凍し、Applicationsフォルダに入れる
5. （chromedriverの権限の追加？）
    
    ```jsx
    xattr -d com.apple.quarantine /Applications/chromedriver
    ```
    

### Conda環境構築

```bash
conda activate '仮想環境名'
conda install selenium
```
