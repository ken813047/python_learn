# Python 學習進度

## 目標
成為可以應徵軟體工程師的人（目前尚未確定前端/後端/嵌入式方向，先打好基礎）

## 環境設定

### Mac（主要學習環境）
- 資料夾位置：~/python_learn
- 虛擬環境：使用 Python 內建 venv（不是 conda）
- 啟動方式：`cd python_learn` → `source venv/bin/activate`
- 執行程式：`python3 檔名.py`

### Windows（公司電腦）
- 使用 PowerShell（不是 Command Prompt）
- 資料夾位置：Desktop\python_learn
- 建立虛擬環境：`python -m venv venv`
- 啟動方式：`.\venv\Scripts\Activate.ps1`
  - 若出現執行原則錯誤，先跑：`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`
- 執行程式：`python 檔名.py`（注意：Windows 用 python，不是 python3）
- 建立空檔案：`New-Item 檔名`（Mac 用 touch）

⚠️ 注意：Mac 跟 Windows 目前是兩個各自獨立的 python_learn 資料夾，Day 1-4 在 Mac 上，Day 5 開始在 Windows 上，尚未同步合併，之後需要處理兩邊同步的問題。

## Git / GitHub
- GitHub 帳號：ken813047
- Repository：https://github.com/ken813047/python_learn
- 已設定 .gitignore，內容為 `venv/`（避免虛擬環境套件被一併上傳）
- 基本流程：`git add .` → `git commit -m "說明"` → `git push`
- 目前只有 Windows 端的 python_learn 資料夾已經連上並推送成功（含 Day 5、.gitignore）
- Mac 端尚未執行 git init / 連上同一個 repository

## 學習節奏
- 每天約 30 分鐘
- 一天一個小觀念 + 一個小練習

## 進度紀錄

### Day 1（完成）
- 主題：變數是什麼
- 內容：用「貼標籤的箱子」比喻理解變數，`=` 是賦值不是數學等於
- 練習：`age = 18`，用 print() 印出

### Day 2（完成）
- 主題：資料型別（int, float, str, bool）
- 內容：type() 可以檢查變數目前裝的資料型別；型別看「內容」不看「變數名字」
- 練習：宣告 4 種型別變數，用 type() 檢查，並修正了變數內容打反的錯誤

### Day 3（完成）
- 主題：不同型別混在一起運算會發生什麼事、如何讀錯誤訊息
- 內容：
  - 數字 + 數字 = 數學加法；文字 + 文字 = 串接（不會自動加空格，要手動加 `" "`）
  - 數字 + 文字 = 報錯（TypeError）
  - 讀錯誤訊息的順序：先看最後一行（錯誤類型 + 說明），再看行號對照程式碼，前面 Traceback 開場白可先跳過
  - 認識 TypeError：型別不合、不能這樣運算
  - 重要觀念：Python 由上到下逐行執行，一遇到錯誤會立刻停止，不會跳過繼續執行後面的程式碼（親自用程式碼順序驗證過這件事）
- 練習：故意寫出 age + name 讓程式報錯，並解讀完整錯誤訊息

### Day 4（完成）
- 主題：型別轉換 str() / int() / float()，以及 ValueError
- 內容：
  - str()、int()、float() 可以把值從一種型別轉成另一種，且不會改變原變數，而是產生新值
  - 用 str(age) 把數字轉文字，解決了 Day 3 的 TypeError，成功把數字跟文字接在一起
  - int(3.99) 結果是 3，型別轉換是直接砍掉小數，不是四捨五入
  - int("Ken") 會出現新的錯誤類型 ValueError，並學會解讀：invalid literal for int()... 代表「這個內容沒辦法被轉換成數字」
  - 釐清 TypeError 與 ValueError 的差異：
    - TypeError：型別本身不支援這個操作（例如數字不能直接加文字）
    - ValueError：型別沒錯、操作也支援，但傳入的內容不合理（例如 "Ken" 沒辦法變成數字）
- 練習：用 str() 修正錯誤、測試 int() 四捨五入行為、故意寫 int("Ken") 觸發 ValueError 並解讀

### Day 5（完成）
- 主題：條件判斷 if / else / elif、比較運算子、SyntaxError
- 內容：
  - if 條件: 後面要加冒號，底下內容要縮排，縮排是 Python 語法的一部分
  - 比較運算子：> < >= <= == != ，特別注意 == 是比較、= 是賦值
  - elif 可以檢查多個條件，依序往下判斷
  - 故意打成 if age = 18: 觸發 SyntaxError，並學會解讀：Python 直接看不懂語法，甚至會貼心提示「你是不是想打 ==」
  - 整理三種錯誤類型的差異與檢查順序：SyntaxError（語法看不懂）→ TypeError（型別不支援）→ ValueError（內容不合理）
- 額外完成：設定 Git / GitHub，學會 git init / add / commit / push 基本流程，用 .gitignore 排除 venv 資料夾，並排除了 remote 網址貼錯導致的錯誤

### Day 6（尚未開始）
- 主題：待安排（預計：while 迴圈，或先處理 Mac / Windows 兩邊 python_learn 資料夾同步問題）