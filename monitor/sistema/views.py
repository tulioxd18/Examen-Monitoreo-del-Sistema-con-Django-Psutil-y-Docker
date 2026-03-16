from django.shortcuts import render
import psutil
import platform

def get_system_info():
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count(logical=True)

        memory = psutil.virtual_memory()
        memory_total_gb = round(memory.total / (1024**3), 2)
        memory_used_gb = round(memory.used / (1024**3), 2)
        memory_percent = memory.percent

        disk = psutil.disk_usage('/')
        disk_total_gb = round(disk.total / (1024**3), 2)
        disk_used_gb = round(disk.used / (1024**3), 2)
        disk_free_gb = round(disk.free / (1024**3), 2)
        disk_percent = disk.percent

        os_info = platform.system() + " " + platform.release()

        return {
            'cpu_percent': cpu_percent,
            'cpu_count': cpu_count,
            'memory_total_gb': memory_total_gb,
            'memory_used_gb': memory_used_gb,
            'memory_percent': memory_percent,
            'disk_total_gb': disk_total_gb,
            'disk_used_gb': disk_used_gb,
            'disk_free_gb': disk_free_gb,
            'disk_percent': disk_percent,
            'os_info': os_info,
        }
    except Exception as e:
        return {'error': str(e)}

def index(request):
    data = get_system_info()
    return render(request, 'sistema/index.html', {'data': data})
