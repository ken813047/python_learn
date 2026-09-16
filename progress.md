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

### Day 6（完成）
- 主題：while 迴圈
- 內容：
  - while 條件: 只要條件成立就重複執行，條件不成立才停止
  - 務必記得在迴圈內讓某個變數往「條件會不成立」的方向變化，否則會造成無窮迴圈（親自觸發過一次，並用 Ctrl+C 強制中斷）
  - 結合 if 判斷，用 while 搭配 % 取餘數（count % 2 == 0）篩選偶數
  - 額外收穫：\ 是續行符號，代表「這行還沒結束，接下一行」，上一行多打一個 \ 會導致下一行被誤判為同一行語法，出現難以直接看出原因的 SyntaxError；學到「錯誤訊息指出的行號，不一定是真正出錯的那一行，有時要往上一行找」
  - 額外收穫：親自體驗「電腦只執行你寫的，不會猜你想的」（count 從 0 開始，0 也符合偶數條件，所以被印出來，不是 bug，是邏輯設計的結果）

### Day 1-6 綜合測驗（完成）
- 題目：模擬馬達角度檢查器，結合變數、型別轉換、if/else、while 迴圈
- 結果：
  - 第一次答對思考題（int("abc") 會是 ValueError，並正確說明語法沒錯、型別支援轉換，但內容不合理的判斷邏輯）
  - 第一次寫程式碼有兩個邏輯錯誤：
    1. count = count + 1 放置位置太早，導致 if 判斷奇偶時判斷到的其實是下一輪的數字
    2. while count < 5 少跑最後一次，應改成 <=
  - 經提示後，能自己回頭比對執行順序與縮排，獨立抓出並修正這兩個問題，最終程式輸出完全符合需求
- 代表 Day 1-6 內容驗收通過，具備獨立除錯（追蹤變數變化、比對預期與實際輸出）的基本能力

### Day 7（完成）
- 主題：list（串列）基礎操作
- 內容：
  - list 是可以裝多個東西的容器，元素有順序、有索引，索引從 0 開始
  - 用索引 `list[0]` 取第一個元素；用負索引 `list[-1]` 取最後一個元素
  - append() 會在 list 最後面加一個新元素
  - 切片 `list[0:3]` 可以取一段範圍（包含起點、不包含終點）
  - 重要觀念：用 `list[4]` 這種寫死的正索引去取「最後一個元素」不穩健，因為 list 長度改變（例如 append 後）索引就會跟著變，`list[-1]` 才是不管長度怎麼變都能取到最後一個元素的寫法
- 練習：建立 5 個元素的 list，用索引印出第一個和最後一個、append 新元素後印出完整 list、用切片印出前 3 個元素
  - 第一次用 `food[4]` 印最後一個元素（當下對，但不穩健），經提示後自己改成 `food[-1]`

## 學習方向調整（2026-09-09）
- 背景：使用者的公司工作是硬體校正/系統測試自動化（partner-calibration-and-system-test-automation repo），內容是把 config 填上相機/滑台序號跟實際硬體結合、用 pre_process 準備測試、在機台上測試、用 post_process 撈資料給客戶
- 判斷：這份工作屬於「系統整合 / 測試自動化工程」，會大量用到 class 繼承（不同 station 繼承共用 Station 基底類別）、config 讀寫、例外處理（硬體異常）、debug、pytest
- 未來課程路線調整為（在原本 list 之後）：function → class / OOP → try/except（例外處理）→ 讀寫檔案（json 等設定檔）→ pytest 入門
- 之後每天課程安排優先考慮跟這個方向對齊，比單純練語法更貼近實際工作需求
### Day 8（完成）
- 主題：for 迴圈遍歷 list、len()
- 內容：
  - `for item in list:` 可以把 list 裡每個元素一個一個拿出來處理，不用像 while 自己維護 count，也不會有無窮迴圈風險
  - `len(某個東西)` 回傳長度：用在 list 上是「有幾個元素」，用在字串上是「有幾個字母」
- 這次踩到的四個錯誤（都很有價值）：
  1. `len` 沒加括號 → TypeError: '>' not supported between 'builtin_function_or_method' and 'int'
     - 觀念：`len` 是函式本身，`len(x)` 才是「執行它、得到長度數字」，括號代表真的去執行
  2. `len("foods")` 多了引號 → 引號是「文字的圍牆」，加上去就不再是變數，而是 f-o-o-d-s 這 5 個字母，答案永遠是 5，跟 list 無關
  3. if/else 沒有縮排進 for 裡面 → 變成迴圈跑完後只執行一次，不是每一輪都判斷
  4. `foods`（整個 list）與 `food`（當下這一項）搞混 → 差一個字母 s，但程式完全不報錯（語法合法、型別也對），只是結果不如預期，是實務上最難抓的一種錯誤
- 額外收穫：
  - 「算了但沒有 print 也沒有存起來」的一行等於白做工，Python 算完就把結果丟掉
  - 學會「從輸出反推程式行為」的除錯技巧：看到 chicken(7 個字母) 沒觸發判斷，就能推論出 if 條件量錯對象
  - 再次印證「程式沒壞，它只是照你寫的做，不是照你想的做」
- 練習：印出 list 元素個數、用 for 迴圈印出每一項、並用 if 判斷字串長度大於 5 時印出 `"it's very long: " + food`

### Day 9（完成）
- 主題：function（函式）、return vs print、None
- 內容：
  - `def 函式名(參數):` 定義函式，冒號 + 縮排，規則跟 if / for 一樣
  - 一直以來用的 print()、len()、str()、int() 都是別人寫好的函式，今天開始自己寫
  - **定義 ≠ 執行**：`def` 只是「寫食譜」，要寫 `函式名()` 加括號呼叫，才會真的執行
  - 參數（parameter）像一個空位，呼叫時傳什麼進去，函式裡就用什麼，同一段邏輯可套用在不同資料上
  - **return vs print（今天最重要）**：
    - `print` = 印在螢幕上給「人」看，程式抓不到這個值
    - `return` = 把值交回給「程式」，可以存進變數、繼續運算
    - 比喻：請朋友算 2×2，print 是他「大聲喊出來」（你聽到了，但手上紙條空白）；return 是他「寫在紙條上交給你」（可以拿去繼續用）。程式只抓得到紙條，抓不到聲音
  - **None**：函式沒有寫 return 時，Python 自動回傳 None（代表「什麼都沒有」）
    - 實務意義：忘了寫 return 是常見 bug 來源，拿 None 去運算會出現 `NoneType` 相關錯誤，看到 NoneType 就往「哪個函式沒 return」查
  - 釐清三個容易混淆的點（來回問了三輪才完全搞懂）：
    1. `result = double(2)` **確實有呼叫函式、也確實把 2 帶入 number**，證據就是螢幕印出了 4；問題不在「有沒有呼叫」，而在「函式執行完有沒有交東西回來」
    2. result 變成 None **不是因為「已經 print 過所以值被用掉」**，而是因為從頭到尾沒寫 return；一個函式可以同時 print 又 return，兩者互不影響；就算函式裡什麼都沒印，只要沒 return 一樣回傳 None
    3. 「沒意義」的是 result 裡裝的值（None），不是 `print(result)` 這一行——它忠實印出了變數的內容，反而是它讓我們看見問題
  - **除錯技巧**：在可疑的地方 `print(變數)`，看它到底裝什麼，是實務上最基本也最常用的查錯方式。印出 None 就往「函式有沒有 return」查；型別不對就往「傳進去的參數對不對」查
- 這次踩到的錯誤：
  1. 把 `def` 寫在 for 迴圈裡面 → 迴圈跑 5 次只是重複「定義」函式 5 次，從來沒有呼叫，程式安靜跑完完全沒有輸出（親身驗證「定義 ≠ 執行」）
     - 正確結構：函式定義放迴圈外面（只需定義一次），迴圈裡面放呼叫
  2. `print(check_food)` 印出 `<function check_food at 0x...>` → 印出「函式本身」而不是執行結果，與 Day 8 的 `builtin_function_or_method` 是同一個觀念，連續兩天從不同角度撞到，觀念已內化
  3. 新錯誤 **NameError**：`double(number)` 把「參數名字」當成值傳進去 → `NameError: name 'number' is not defined`
     - 觀念：參數名字只在函式內部有效（變數作用域 scope），外面的世界不認識它，呼叫時要傳真正的值
     - 實務上 NameError 最常見原因是「打錯字」，看到它先檢查拼字
- 其他收穫：
  - `#` 是註解符號，Python 會完全跳過那一行（曾因呼叫全被註解掉而沒有輸出）
  - `[]` 中括號建立 list（可修改）；`()` 小括號建立 tuple（不可修改，不能 append），兩者都能用 for 遍歷、用 len() 取長度
  - VS Code 波浪線顏色：紅色=錯誤（跑不動）、黃色=警告、藍色=提示/風格建議、灰色=沒用到；滑鼠停在上面或看 PROBLEMS 面板可查原因
  - VS Code 快捷鍵：選取多行後按 `Ctrl + /`（Mac 是 `Cmd + /`）可以一次備註/取消備註整段，是切換式的
  - Python 沒有真正的「區塊註解」語法，`#` 逐行才是標準做法；三引號 `"""..."""` 嚴格來說是「沒被使用的字串」不是註解，真正用途是寫 docstring（函式說明文件，公司 code style 要求每個 method 都要寫）
- 目前認識的四種錯誤類型：
  - SyntaxError（語法看不懂）/ TypeError（型別不支援此操作）/ ValueError（型別對但內容不合理）/ NameError（這個名字不存在）

### Day 10（尚未開始）
- 主題：class / OOP 入門（對應公司 code 裡 Station 基底類別的繼承結構）