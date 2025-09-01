
import os
import sys
import time
import random
import shutil

# Colors
R = '\033[1;31m'; G = '\033[1;32m'; Y = '\033[1;33m'
B = '\033[1;34m'; C = '\033[1;36m'; M = '\033[1;35m'
W = '\033[1;37m'; RESET = '\033[0m'

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def typewrite(text, delay=0.007):
    for ch in text:
        sys.stdout.write(ch); sys.stdout.flush(); time.sleep(delay)
    print()

def spinner(text, secs=2.2):
    frames = ['|','/','-','\\']
    sys.stdout.write(Y + text + " ")
    t0 = time.time(); i = 0
    while time.time() - t0 < secs:
        sys.stdout.write(frames[i % 4]); sys.stdout.flush()
        time.sleep(0.12); sys.stdout.write('\b'); i += 1
    print(G + " ✓" + RESET)

def progress_bar(title, width=36, duration=2.0):
    sys.stdout.write(C + title + "\n")
    steps = max(1, int(duration / 0.04))
    for i in range(steps + 1):
        filled = int(i / steps * width)
        bar = "█" * filled + "░" * (width - filled)
        percent = int(i / steps * 100)
        sys.stdout.write(M + f"[{bar}] {percent:3d}%\r" + RESET)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

def neon_banner():
    clear()
    neon = [
        f"{M}██╗███╗   ███╗██╗  ██╗ ██████╗ ███████╗",
        f"{C}██║████╗ ████║██║ ██╔╝██╔═══██╗██╔════╝",
        f"{B}██║██╔████╔██║█████╔╝ ██║   ██║█████╗  ",
        f"{G}██║██║╚██╔╝██║██╔═██╗ ██║   ██║██╔══╝  ",
        f"{Y}██║██║ ╚═╝ ██║██║  ██╗╚██████╔╝███████╗",
        f"{R}╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝{RESET}"
    ]
    for ln in neon:
        print(ln); time.sleep(0.02)
    print(W + "               H A C K I N G   W O R L D™")
    print(C + "        IMO VIP  • ROOT-ONLY (SAFE)" + RESET)
    print(W + "────────────────────────────────────────────────────────\n")

def require_root():
    # Check effective UID (Unix)
    has_geteuid = hasattr(os, "geteuid")
    euid_ok = (os.geteuid() == 0) if has_geteuid else False
    # Fallback check for su/tsu presence
    su_path = shutil.which("su") or shutil.which("tsu")
    if not euid_ok and not su_path:
        print(R + "\n[✘] Root Access Not Found!" + RESET)
        print(Y + "[!] This tool is ROOT-ONLY. Open a root shell (e.g., use 'tsu' in Termux) and run again." + RESET)
        input(W + "\nPress Enter to exit…" + RESET)
        sys.exit(1)
    if has_geteuid and os.geteuid() != 0:
        print(R + "\n[✘] Not running as root (effective UID != 0)." + RESET)
        print(C + "Tip: In Termux run: " + W + "tsu" + C + " then: " + W + "python imo_root_safe.py" + RESET)
        input(W + "\nPress Enter to exit…" + RESET)
        sys.exit(1)
    # passed
    print(G + "[✓] Root privileges verified." + RESET)
    time.sleep(0.6)

def fake_edge_logs(target):
    clusters = ["ap-sg","eu-fr","us-va","in-mum","jp-tyo"]
    events = [
        "Initializing secure shell",
        "Negotiating cipher suites",
        "Spawning ephemeral sockets",
        "Applying anti-bot fingerprints",
        "Opening telemetry window"
    ]
    for ev in events:
        tag = random.choice(clusters)
        token = hex(random.getrandbits(40))
        typewrite(C + f"[{tag}] {ev}  token={token}  target={target}" + RESET, 0.006)
        time.sleep(0.07)

def generate_fake_otp(length=6):
    digits = ''.join(str(random.randint(0,9)) for _ in range(length))
    # visually group (e.g., 123-456)
    if length % 3 == 0:
        groups = '-'.join([digits[i:i+3] for i in range(0, length, 3)])
    else:
        groups = digits
    return digits, groups

def show_safe_otp_flow(target):
    spinner("[✓] Binding to IMO secure mesh", 2.2)
    progress_bar("[#] Establishing ephemeral channel", 34, 1.6)
    fake_edge_logs(target)
    progress_bar("[#] Requesting OTP token (simulation)", 30, 1.8)
    time.sleep(0.8)

    raw, grouped = generate_fake_otp(6)
    print("\n" + G + "✅ OTP Generated (FAKE) :" + RESET, end=" ")
    print(W + grouped + RESET)
    print()
    time.sleep(0.8)
    typewrite(Y + "*** IMPORTANT NOTICE ***" + RESET, 0.01)
    typewrite(W + "This code is completely fabricated for PRANK/DEMO only.", 0.01)
    typewrite(W + "It is NOT a real OTP and has NOT been sent to any device.", 0.01)
    typewrite(W + "Do NOT use this for any login or attempt to access accounts.", 0.01)
    print()

def main():
    neon_banner()
    require_root()   # <-- exits if not root

    target = input(Y + "[+] Enter IMO number (display only): " + W).strip()
    if not target:
        print(R + "Number required. Exiting." + RESET)
        time.sleep(1)
        return

    print()
    typewrite(C + "[*] Preparing secure visualization (root-enabled)..." + RESET, 0.008)
    time.sleep(0.6)
    show_safe_otp_flow(target)

    # final big warning and exit
    print(G + "\n[✓] PRANK DEMO COMPLETED" + RESET)
    print(R + "⚠️  REMEMBER: This is a harmless prank. Do NOT phish or collect real OTPs." + RESET)
    input(W + "\nPress Enter to exit…" + RESET)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(RESET + "\n\nInterrupted by user.\n")