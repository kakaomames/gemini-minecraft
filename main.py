import os
import asyncio
import subprocess
from aiohttp import web

# 12/26 最終機動設定
jar_file = "1.21.11.jar"
print(f"jar_file:{jar_file}")

# Renderから指定されたポートを取得
port = int(os.environ.get("PORT", 8080))
print(f"assigned_port:{port}")

# --- Webサーバーの設定 ---
async def handle_index(request):
    # index.htmlを読み込んでブラウザに返す
    with open('index.html', 'r', encoding='utf-8') as f:
        return web.Response(text=f.read(), content_type='text/html')

async def start_web_server():
    app = web.Application()
    app.router.add_get('/', handle_index)
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', port)
    
    print(f"Web server starting on port: {port}")
    await site.start()

# --- Minecraftの起動 ---
def start_minecraft():
    print("Mission: Launching Minecraft Process...")
    # メモリをRenderのFreeプランに合わせて調整 (512MB)
    cmd = ["java", "-Xmx512M", "-jar", jar_file, "nogui", "--username=CacaoMame_Guest"]
    # 非同期でプロセスを立ち上げる（Webサーバーを止めないため）
    subprocess.Popen(cmd)
    print(f"Minecraft process started with: {' '.join(cmd)}")

async def main():
    # 1. Minecraft起動
    start_minecraft()
    # 2. Webサーバー（ポート開放）開始
    await start_web_server()
    # 3. サーバーを永続的に動かし続ける
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
