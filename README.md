1. 安裝 Conda 後，打開 PowerShell。
2. 執行以下指令來建立 Conda 環境並安裝必要的 Python 套件。

   #### 建立新的 Conda 環境
   ```bash
   conda create --name LinearAlgebra_env python=3.9
   ```

   #### 確認環境建立成功
   ```bash
   conda env list
   ```
   確認列表中有 `LinearAlgebra_env` 之後，啟動該環境。

   #### 啟動 Conda 環境
   ```bash
   conda activate LinearAlgebra_env
   ```
   確認提示符的最前方變成 `(LinearAlgebra_env)`，表示環境已啟動。

   #### 安裝必要的 Python 套件
   ```bash
   pip install numpy sympy matplotlib
   ```
   安裝過程中可能會要求確認，輸入 `y` 以繼續。