# sync-laws-data.ps1 — 同步本地 laws-data 镜像与上游不定期更新
# 运行：PowerShell 中执行  .\sync-laws-data.ps1  （建议在 law-repository 目录或任意位置）
# 作用：将原作者 13098806890/laws-data 的不定期更新拉到本地并推回你的 fork，保持镜像新鲜
$ErrorActionPreference = "Stop"

$MIRROR  = "D:\00_Lee\00-相关资料\00_laws-data"
$UPSTREAM = "https://github.com/13098806890/laws-data"

if (-not (Test-Path $MIRROR)) {
    Write-Warning "未找到镜像目录：$MIRROR"
    Write-Host "请先执行："
    Write-Host "  gh repo clone lizhijun48/laws-data `"$MIRROR`""
    Write-Host "  cd `"$MIRROR`"; git remote add upstream $UPSTREAM"
    exit 1
}

Push-Location $MIRROR
try {
    # 首次确保 upstream 已配置（幂等）
    if (-not (git remote -v | Select-String -Quiet "upstream")) {
        Write-Host "==> 配置 upstream -> $UPSTREAM"
        git remote add upstream $UPSTREAM
    }
    # 注：本机 git 环境无法持久化 upstream/main 远程跟踪引用（git fetch 报建成功但 rev-parse 失败），
    # 故改用 `git pull upstream main` 直接拉取并合并上游 main，不依赖 upstream/main 引用名解析。
    Write-Host "==> 拉取并合并上游 main ..."
    git pull upstream main --no-edit
    Write-Host "==> 推回 fork(lizhijun48/laws-data) ..."
    git push origin main
    Write-Host "==> 同步完成。建议将 law-repository 相关快照日期更新为 $(Get-Date -Format yyyy-MM-dd)"
} finally {
    Pop-Location
}
