"""
Instalador Automático de EdgeDriver para Hotel Premium Tests
Descarga automáticamente la versión correcta de EdgeDriver
"""

import os
import requests
import zipfile
import sys
from pathlib import Path

def get_edge_version():
    """Obtener versión de Edge instalada"""
    try:
        import winreg
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Edge\BLBeacon")
        version, _ = winreg.QueryValueEx(key, "version")
        winreg.CloseKey(key)
        return version
    except:
        return "138.0.3351.83"  # Versión por defecto

def download_edgedriver(version):
    """Descargar EdgeDriver para la versión especificada"""
    print(f"📥 Descargando EdgeDriver versión {version}...")
    
    # URL de descarga de EdgeDriver
    base_url = "https://msedgedriver.azureedge.net"
    
    # Intentar diferentes formatos de URL
    possible_urls = [
        f"{base_url}/{version}/edgedriver_win64.zip",
        f"{base_url}/{version}/edgedriver_win32.zip",
    ]
    
    for url in possible_urls:
        try:
            print(f"   Intentando: {url}")
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            # Guardar archivo ZIP
            zip_path = "edgedriver.zip"
            with open(zip_path, 'wb') as f:
                f.write(response.content)
            
            print(f"✅ EdgeDriver descargado correctamente")
            return zip_path
            
        except requests.exceptions.RequestException as e:
            print(f"   ❌ Error: {e}")
            continue
    
    return None

def extract_edgedriver(zip_path):
    """Extraer EdgeDriver del archivo ZIP"""
    print("📂 Extrayendo EdgeDriver...")
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(".")
        
        # Buscar el archivo msedgedriver.exe
        for root, dirs, files in os.walk("."):
            for file in files:
                if file == "msedgedriver.exe":
                    driver_path = os.path.join(root, file)
                    print(f"✅ EdgeDriver extraído: {driver_path}")
                    return driver_path
        
        print("❌ No se encontró msedgedriver.exe en el archivo ZIP")
        return None
        
    except Exception as e:
        print(f"❌ Error extrayendo archivo: {e}")
        return None
    finally:
        # Limpiar archivo ZIP
        if os.path.exists(zip_path):
            os.remove(zip_path)

def install_python_dependencies():
    """Instalar dependencias de Python"""
    print("📦 Instalando dependencias de Python...")
    
    dependencies = [
        "selenium==4.15.2",
        "requests==2.31.0"
    ]
    
    for dep in dependencies:
        try:
            os.system(f"pip install {dep}")
        except Exception as e:
            print(f"⚠️ Error instalando {dep}: {e}")

def main():
    print("🏨 INSTALADOR AUTOMÁTICO - HOTEL PREMIUM TESTS")
    print("=" * 50)
    
    # Verificar Python
    print("🐍 Verificando Python...")
    if sys.version_info < (3, 7):
        print("❌ Se requiere Python 3.7 o superior")
        return
    print("✅ Python OK")
    
    # Instalar dependencias de Python
    install_python_dependencies()
    
    # Obtener versión de Edge
    edge_version = get_edge_version()
    print(f"🌐 Versión de Edge detectada: {edge_version}")
    
    # Verificar si EdgeDriver ya existe
    existing_paths = [
        "msedgedriver.exe",
        "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedgedriver.exe",
        "C:\\WebDrivers\\msedgedriver.exe"
    ]
    
    edgedriver_exists = False
    for path in existing_paths:
        if os.path.exists(path):
            print(f"✅ EdgeDriver encontrado: {path}")
            edgedriver_exists = True
            break
    
    if not edgedriver_exists:
        print("📥 EdgeDriver no encontrado, descargando...")
        
        # Descargar EdgeDriver
        zip_path = download_edgedriver(edge_version)
        
        if zip_path:
            driver_path = extract_edgedriver(zip_path)
            if driver_path:
                print(f"✅ EdgeDriver instalado en: {os.path.abspath(driver_path)}")
            else:
                print("❌ Error instalando EdgeDriver")
                print("📋 Instalación manual:")
                print("1. Ve a: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/")
                print("2. Descarga EdgeDriver para tu versión de Edge")
                print("3. Coloca msedgedriver.exe en la carpeta del proyecto")
                return
        else:
            print("❌ No se pudo descargar EdgeDriver automáticamente")
            print("📋 Descarga manual desde:")
            print("https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/")
            return
    
    # Crear estructura de directorios
    print("📁 Creando directorios...")
    os.makedirs("screenshots", exist_ok=True)
    os.makedirs("reports", exist_ok=True)
    print("✅ Directorios creados")
    
    # Verificar XAMPP
    print("🔍 Verificando XAMPP...")
    try:
        response = requests.get("http://localhost/hotel_premium/", timeout=5)
        print("✅ XAMPP está ejecutándose")
        print("✅ Proyecto Hotel Premium accesible")
    except requests.exceptions.RequestException:
        print("⚠️ XAMPP no está ejecutándose o proyecto no accesible")
        print("📋 Verifica:")
        print("   • XAMPP Control Panel - Apache iniciado")
        print("   • Proyecto en: c:\\xampp\\htdocs\\hotel_premium\\")
    
    print("\n🎉 INSTALACIÓN COMPLETADA")
    print("=" * 50)
    print("Para ejecutar las pruebas:")
    print("   python simple_hotel_test.py")
    print("\nArchivos creados:")
    print("   • msedgedriver.exe (si se descargó)")
    print("   • screenshots/ (directorio)")
    print("   • reports/ (directorio)")

if __name__ == "__main__":
    main()
