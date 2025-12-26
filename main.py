import subprocess
import os

# 12/26 最新機動設定
jar_file = "1.21.2.jar"
print(f"jar_file:{jar_file}")

username = "CacaoMame_Guest"
print(f"username:{username}")

def start_mc():
    print("Mission Start: Minecraft Launching...")
    # Render環境でのJava起動
    cmd = ["java", "-Xmx512M", "-jar", jar_file, "nogui", f"--username={username}"]
    print(f"cmd:{' '.join(cmd)}")
    # subprocess.Popen(cmd) # 実際の実装

start_mc()
while True: pass # サーバー維持