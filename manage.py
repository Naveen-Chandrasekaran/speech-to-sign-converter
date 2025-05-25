#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess
import threading
import socket
import platform
import time

def is_port_in_use(port, host='127.0.0.1'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex((host, port)) == 0

def kill_process_on_port(port):
    system_platform = platform.system()
    try:
        if system_platform == 'Windows':
            # Find and kill the process using the port
            result = subprocess.check_output(f'netstat -ano | findstr :{port}', shell=True).decode()
            for line in result.strip().split('\n'):
                if 'LISTENING' in line or 'ESTABLISHED' in line:
                    pid = line.strip().split()[-1]
                    subprocess.run(['taskkill', '/PID', pid, '/F'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    print(f"❌ Terminated process on port {port} (PID {pid})")
        else:
            # Linux / macOS
            result = subprocess.check_output(f'lsof -ti:{port}', shell=True).decode().strip()
            for pid in result.split('\n'):
                subprocess.run(['kill', '-9', pid], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print(f"❌ Terminated process on port {port} (PID {pid})")
    except Exception as e:
        print(f"⚠️ Could not kill process on port {port}: {e}")

def run_angular_dev_server():
    project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'translate'))
    project_dir = os.path.abspath(os.path.dirname(__file__))
    nodejs_path = os.path.join(project_dir, 'nodejs')
    npm_cmd = os.path.join(nodejs_path, 'npm.cmd') if platform.system() == 'Windows' else os.path.join(nodejs_path, 'bin', 'npm')


    if is_port_in_use(4200):
        print("⚠️ Port 4200 already in use. Attempting to terminate existing process...")
        kill_process_on_port(4200)
        time.sleep(1)

    print("🚀 Starting Angular dev server on http://localhost:4200...")

    # Run npm install if node_modules does not exist
    if not os.path.exists(os.path.join(project_path, 'node_modules')):
        print("📦 Running npm install...")
        subprocess.run([npm_cmd, 'install'], cwd=project_path)

    # Start Angular dev server
    subprocess.Popen([npm_cmd, 'start'], cwd=project_path)

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'A2SL.settings')

    if len(sys.argv) > 1 and sys.argv[1] == 'runserver':
        threading.Thread(target=run_angular_dev_server, daemon=True).start()

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
