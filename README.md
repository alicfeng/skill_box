# skill_box

安装后可在终端使用 **`skill_box`** 命令。入口由 pip/setuptools 生成，在 **macOS、Linux、Windows** 上用法一致；Windows 下对应可执行文件为 **`skill_box.exe`**（位于当前 Python 环境的 `Scripts` 目录）。

源码仓库：<https://github.com/alicfeng/skill_box>

## 环境要求

- **Python 3.8+**
- **pip**（建议较新版本，例如 23+；过旧的 pip 若安装异常，可先执行 `python -m pip install -U pip setuptools wheel`）

## 通过 pip 安装

### 从 GitHub 直接安装（推荐）

在 **macOS / Linux** 的终端，或 **Windows** 的「命令提示符 / PowerShell」中执行：

```bash
python -m pip install "git+https://github.com/alicfeng/skill_box.git"
```

若系统里 `python` 指向 Python 2，在 macOS / Linux 上请改用：

```bash
python3 -m pip install "git+https://github.com/alicfeng/skill_box.git"
```

Windows 上若已安装 [Python Launcher](https://docs.python.org/3/using/windows.html#python-launcher-for-windows)，可使用：

```powershell
py -m pip install "git+https://github.com/alicfeng/skill_box.git"
```

安装指定分支或标签（将 `main` 换成你的分支名或 tag）：

```bash
python -m pip install "git+https://github.com/alicfeng/skill_box.git@main"
```

### 克隆仓库后本地安装

```bash
git clone https://github.com/alicfeng/skill_box.git
cd skill_box
python -m pip install .
```

开发时可编辑安装（需较新 pip；若失败请先升级 pip）：

```bash
python -m pip install -e .
```

### 虚拟环境（各平台通用，建议）

避免污染系统 Python：

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install "git+https://github.com/alicfeng/skill_box.git"
```

**Windows（PowerShell）**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
python -m pip install "git+https://github.com/alicfeng/skill_box.git"
```

## 验证安装

```bash
skill_box --version
skill_box -h
```

不依赖 PATH 时可直接用模块方式运行：

```bash
python -m skill_box --version
```

## 命令找不到时的 PATH 说明

pip 会把 CLI 安装到**当前 Python 环境**的脚本目录下：

| 平台 | 典型路径（示例） |
|------|------------------|
| macOS / Linux（系统/用户级） | `~/.local/bin` 或 `~/Library/Python/3.x/bin`（用户安装时 pip 会打印确切路径） |
| macOS / Linux（venv） | `<项目>/.venv/bin` |
| Windows（venv） | `<项目>\.venv\Scripts\` |
| Windows（用户/全局） | `Python 安装目录\Scripts\` |

若终端提示「脚本已安装到某目录但该目录不在 PATH」，请把该目录加入 PATH，或改用上面的 `python -m skill_box`。

## 包名说明

在 PyPI 上发布的分发名为 **`skill-box`**（pip 安装时使用）；命令行入口名为 **`skill_box`**。
