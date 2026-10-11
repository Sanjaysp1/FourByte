"""
run.py — starts both the FastAPI backend and Streamlit frontend in parallel.
Run:  python run.py
"""
import subprocess
import sys
import os
import time
import signal
import threading


def stream_output(process, prefix):
    for line in iter(process.stdout.readline, b""):
        print(f"[{prefix}] {line.decode().rstrip()}")


def main():
    root = os.path.dirname(os.path.abspath(__file__))

    print("=" * 60)
    print("  🚀 NexusAI — AI Business Growth Platform")
    print("=" * 60)
    print()

    # Start FastAPI backend
    print("▶ Starting FastAPI backend on http://localhost:8000 …")
    backend = subprocess.Popen(
        [
            sys.executable, "-m", "uvicorn",
            "backend.main:app",
            "--host", "0.0.0.0",
            "--port", "8000",
            "--reload",
        ],
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    # Give backend a moment to start
    time.sleep(3)

    # Start Streamlit frontend
    print("▶ Starting Streamlit frontend on http://localhost:8501 …")
    frontend = subprocess.Popen(
        [
            sys.executable, "-m", "streamlit", "run",
            "frontend/app.py",
            "--server.port", "8501",
            "--server.address", "0.0.0.0",
            "--server.enableCORS", "false",
            "--server.enableXsrfProtection", "false",
            "--browser.gatherUsageStats", "false",
            "--theme.base", "dark",
            "--theme.primaryColor", "#6366f1",
            "--theme.backgroundColor", "#0f0f1a",
            "--theme.secondaryBackgroundColor", "#16162a",
            "--theme.textColor", "#f1f5f9",
        ],
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    # Automatically open the browser for the user
    def open_browser():
        time.sleep(2)
        import webbrowser
        webbrowser.open("http://localhost:8501")

    threading.Thread(target=open_browser, daemon=True).start()

    print()
    print("✅ Both services started!")
    print("   🌐 Web App (Browser) →  http://localhost:8501")
    print("   🌐 Alternative URL   →  http://127.0.0.1:8501")
    print("   ⚙️  Backend API       →  http://localhost:8000")
    print("   📖 API Documentation →  http://localhost:8000/docs")
    print()
    print("Press Ctrl+C to stop.")
    print("=" * 60)

    # Stream output
    t1 = threading.Thread(target=stream_output, args=(backend,  "BACKEND"), daemon=True)
    t2 = threading.Thread(target=stream_output, args=(frontend, "FRONTEND"), daemon=True)
    t1.start()
    t2.start()

    try:
        backend.wait()
        frontend.wait()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down…")
        backend.terminate()
        frontend.terminate()
        backend.wait()
        frontend.wait()
        print("Done.")


if __name__ == "__main__":
    main()
