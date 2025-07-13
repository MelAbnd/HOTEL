"""
Verificador del Sistema Hotel Premium
Verifica todos los requisitos antes de ejecutar las pruebas
"""

import os
import sys
import subprocess
import requests
from pathlib import Path

class SystemVerifier:
    def __init__(self):
        self.checks = []
        self.errors = []
        self.warnings = []
    
    def check(self, name, condition, error_msg="", warning_msg=""):
        """Ejecutar una verificación"""
        print(f"🔍 Verificando {name}...", end=" ")
        
        try:
            if callable(condition):
                result = condition()
            else:
                result = condition
            
            if result:
                print("✅ OK")
                self.checks.append((name, True, ""))
                return True
            else:
                print("❌ FALLO")
                self.errors.append(error_msg or f"{name} falló")
                self.checks.append((name, False, error_msg))
                return False
                
        except Exception as e:
            print(f"⚠️ ERROR: {e}")
            self.warnings.append(f"{name}: {e}")
            self.checks.append((name, False, str(e)))
            return False
    
    def verify_python(self):
        """Verificar versión de Python"""
        return sys.version_info >= (3, 7)
    
    def verify_pip(self):
        """Verificar que pip esté disponible"""
        try:
            subprocess.run([sys.executable, "-m", "pip", "--version"], 
                         capture_output=True, check=True)
            return True
        except:
            return False
    
    def verify_selenium(self):
        """Verificar que Selenium esté instalado"""
        try:
            import selenium
            from selenium import webdriver
            return True
        except ImportError:
            return False
    
    def verify_requests(self):
        """Verificar que requests esté instalado"""
        try:
            import requests
            return True
        except ImportError:
            return False
    
    def verify_edge_browser(self):
        """Verificar que Edge esté instalado"""
        edge_paths = [
            "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
            "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe"
        ]
        
        for path in edge_paths:
            if os.path.exists(path):
                return True
        return False
    
    def verify_edgedriver(self):
        """Verificar EdgeDriver"""
        driver_paths = [
            "msedgedriver.exe",
            "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedgedriver.exe",
            "C:\\WebDrivers\\msedgedriver.exe"
        ]
        
        for path in driver_paths:
            if os.path.exists(path):
                return True
        return False
    
    def verify_xampp_apache(self):
        """Verificar que Apache esté ejecutándose"""
        try:
            response = requests.get("http://localhost/", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def verify_hotel_project(self):
        """Verificar que el proyecto Hotel esté accesible"""
        try:
            response = requests.get("http://localhost/hotel_premium/", timeout=10)
            return "SISTEMA HOTEL" in response.text
        except:
            return False
    
    def verify_project_structure(self):
        """Verificar estructura del proyecto"""
        required_files = [
            "../../index.php",
            "../../core/autoload.php",
            "../../core/app/layouts/layout.php",
            "../../core/app/action/processlogin-action.php"
        ]
        
        for file_path in required_files:
            if not os.path.exists(file_path):
                return False
        return True
    
    def verify_database_connection(self):
        """Verificar conexión a base de datos (opcional)"""
        try:
            response = requests.post(
                "http://localhost/hotel_premium/",
                data={"username": "test", "password": "test"},
                timeout=10
            )
            # Si no hay error de conexión, la DB está OK
            return True
        except:
            return False
    
    def run_all_checks(self):
        """Ejecutar todas las verificaciones"""
        print("🏨 VERIFICADOR DE SISTEMA - HOTEL PREMIUM")
        print("=" * 60)
        
        # Verificaciones críticas
        print("\n📋 VERIFICACIONES CRÍTICAS:")
        self.check("Python 3.7+", self.verify_python, 
                  "Se requiere Python 3.7 o superior")
        
        self.check("pip", self.verify_pip, 
                  "pip no está disponible")
        
        self.check("Selenium", self.verify_selenium, 
                  "Ejecuta: pip install selenium")
        
        self.check("requests", self.verify_requests, 
                  "Ejecuta: pip install requests")
        
        self.check("Microsoft Edge", self.verify_edge_browser, 
                  "Instala Microsoft Edge desde microsoft.com/edge")
        
        self.check("EdgeDriver", self.verify_edgedriver, 
                  "Ejecuta: python install_edgedriver.py")
        
        # Verificaciones del servidor
        print("\n🌐 VERIFICACIONES DEL SERVIDOR:")
        self.check("Apache (XAMPP)", self.verify_xampp_apache, 
                  "Inicia Apache en XAMPP Control Panel")
        
        self.check("Proyecto Hotel", self.verify_hotel_project, 
                  "Verifica que el proyecto esté en c:\\xampp\\htdocs\\hotel_premium\\")
        
        self.check("Estructura del Proyecto", self.verify_project_structure, 
                  "Archivos del proyecto faltantes o corruptos")
        
        # Verificaciones opcionales
        print("\n🔧 VERIFICACIONES OPCIONALES:")
        self.check("Base de Datos", self.verify_database_connection, 
                  warning_msg="MySQL puede no estar configurado correctamente")
        
        # Generar reporte
        self.generate_report()
    
    def generate_report(self):
        """Generar reporte de verificación"""
        print("\n" + "=" * 60)
        print("📊 REPORTE DE VERIFICACIÓN")
        print("=" * 60)
        
        total_checks = len(self.checks)
        passed_checks = len([c for c in self.checks if c[1]])
        failed_checks = total_checks - passed_checks
        
        print(f"✅ Verificaciones exitosas: {passed_checks}/{total_checks}")
        print(f"❌ Verificaciones fallidas: {failed_checks}")
        
        if failed_checks == 0:
            print("\n🎉 ¡SISTEMA LISTO PARA PRUEBAS!")
            print("Ejecuta: python simple_hotel_test.py")
        else:
            print(f"\n⚠️ HAY {failed_checks} PROBLEMAS QUE RESOLVER:")
            for error in self.errors:
                print(f"   • {error}")
        
        if self.warnings:
            print(f"\n📝 ADVERTENCIAS:")
            for warning in self.warnings:
                print(f"   • {warning}")
        
        # Soluciones rápidas
        print(f"\n🔧 SOLUCIONES RÁPIDAS:")
        
        if not any("Selenium" in check[0] and check[1] for check in self.checks):
            print("   • pip install selenium requests")
        
        if not any("EdgeDriver" in check[0] and check[1] for check in self.checks):
            print("   • python install_edgedriver.py")
        
        if not any("Apache" in check[0] and check[1] for check in self.checks):
            print("   • Iniciar Apache en XAMPP Control Panel")
        
        if not any("Proyecto Hotel" in check[0] and check[1] for check in self.checks):
            print("   • Mover proyecto a: c:\\xampp\\htdocs\\hotel_premium\\")
        
        print("\n📖 Para más ayuda, consulta README.md")
        
        # Guardar reporte
        self.save_report()
    
    def save_report(self):
        """Guardar reporte en archivo"""
        os.makedirs("reports", exist_ok=True)
        
        report = {
            "timestamp": str(datetime.now() if 'datetime' in globals() else "N/A"),
            "total_checks": len(self.checks),
            "passed": len([c for c in self.checks if c[1]]),
            "failed": len([c for c in self.checks if not c[1]]),
            "checks": [{"name": c[0], "passed": c[1], "error": c[2]} for c in self.checks],
            "errors": self.errors,
            "warnings": self.warnings
        }
        
        try:
            import json
            with open("reports/system_verification.json", "w") as f:
                json.dump(report, f, indent=2)
            print("💾 Reporte guardado en: reports/system_verification.json")
        except:
            pass

def main():
    """Función principal"""
    try:
        verifier = SystemVerifier()
        verifier.run_all_checks()
        
        # Verificar si el sistema está listo
        failed_critical = any(
            check[0] in ["Python 3.7+", "Selenium", "Microsoft Edge", "Apache (XAMPP)", "Proyecto Hotel"] 
            and not check[1] 
            for check in verifier.checks
        )
        
        if not failed_critical:
            print("\n🚀 ¿Quieres ejecutar las pruebas ahora? (s/n): ", end="")
            try:
                response = input().lower()
                if response in ['s', 'y', 'yes', 'si']:
                    print("\n🧪 Ejecutando pruebas...")
                    os.system("python simple_hotel_test.py")
            except:
                pass
        
    except KeyboardInterrupt:
        print("\n⏹️ Verificación interrumpida")
    except Exception as e:
        print(f"\n❌ Error en verificación: {e}")

if __name__ == "__main__":
    # Importar datetime si está disponible
    try:
        from datetime import datetime
    except:
        pass
    
    main()
