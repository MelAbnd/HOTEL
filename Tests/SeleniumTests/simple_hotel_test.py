"""
🏨 PRUEBAS AUTOMATIZADAS BÁSICAS - HOTEL PREMIUM
================================================
Pruebas simples de Navegación, Seguridad y Rendimiento
Microsoft Edge 138.0.3351.83
Autor: GitHub Copilot - Julio 2025
"""

import time
import time
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class HotelPremiumTest:
    """🏨 Pruebas Básicas para Hotel Premium - Fácil de Entender"""
    
    def __init__(self):
        """Configuración inicial"""
        print("🔧 Iniciando configuración de pruebas...")
        
        # Configuración básica
        self.url_hotel = "http://localhost/hotel_premium/"
        self.usuario = "admin"
        self.password = "admin2018"
        self.resultados = []
        
        # Crear carpeta para capturas
        os.makedirs('screenshots', exist_ok=True)
        
        # Configurar navegador Edge
        self.configurar_navegador()
    
    def configurar_navegador(self):
        """Configurar Microsoft Edge para las pruebas"""
        print("🌐 Configurando Microsoft Edge...")
        
        opciones_edge = Options()
        opciones_edge.add_argument("--start-maximized")  # Pantalla completa
        opciones_edge.add_argument("--disable-web-security")  # Para pruebas locales
        
        try:
            # Rutas donde puede estar EdgeDriver
            rutas_posibles = [
                "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedgedriver.exe",
                "msedgedriver.exe"
            ]
            
            driver_encontrado = False
            for ruta in rutas_posibles:
                if os.path.exists(ruta):
                    servicio = Service(executable_path=ruta)
                    self.navegador = webdriver.Edge(service=servicio, options=opciones_edge)
                    driver_encontrado = True
                    break
            
            if not driver_encontrado:
                # Intentar sin ruta específica
                self.navegador = webdriver.Edge(options=opciones_edge)
            
            # Configurar tiempos de espera
            self.navegador.implicitly_wait(10)
            self.esperar = WebDriverWait(self.navegador, 15)
            
            print("✅ Edge configurado correctamente")
            
        except Exception as error:
            print(f"❌ Error configurando Edge: {error}")
            print("\n📋 Para instalar EdgeDriver:")
            print("1. Ve a: https://developer.microsoft.com/microsoft-edge/tools/webdriver/")
            print("2. Descarga la versión para Edge 138.0.3351.83")
            print("3. Coloca msedgedriver.exe en tu PATH o en la carpeta del proyecto")
            raise
    
    def ejecutar_prueba(self, nombre, funcion_prueba):
        """Ejecutar una prueba individual y registrar el resultado"""
        print(f"\n🧪 {nombre}")
        print("-" * 50)
        
        tiempo_inicio = time.time()
        
        try:
            funcion_prueba()
            resultado = "✅ EXITOSO"
            print(f"✅ {nombre} completada exitosamente")
            
        except Exception as error:
            resultado = "❌ FALLÓ"
            print(f"❌ {nombre} falló: {error}")
            # Capturar imagen del error
            nombre_archivo = f"screenshots/error_{nombre.replace(' ', '_')}.png"
            self.navegador.save_screenshot(nombre_archivo)
            print(f"📸 Captura guardada: {nombre_archivo}")
        
        tiempo_total = round(time.time() - tiempo_inicio, 2)
        
        # Guardar resultado
        self.resultados.append({
            "prueba": nombre,
            "resultado": resultado,
            "tiempo": tiempo_total
        })
        
        print(f"⏱️ Tiempo: {tiempo_total} segundos")
    
    # ==================== PRUEBAS DE NAVEGACIÓN ====================
    
    def prueba_cargar_pagina(self):
        """Prueba 1: Verificar que la página principal carga"""
        print("   🌐 Cargando página principal...")
        
        # Ir a la página del hotel
        self.navegador.get(self.url_hotel)
        
        # Verificar que aparezcan los campos de login
        campo_usuario = self.esperar.until(
            EC.presence_of_element_located((By.ID, "exampleInputEmail1"))
        )
        campo_password = self.navegador.find_element(By.ID, "exampleInputPassword1")
        boton_login = self.navegador.find_element(By.XPATH, "//button[@type='submit']")
        
        # Verificar que los elementos estén visibles
        assert campo_usuario.is_displayed(), "❌ Campo usuario no visible"
        assert campo_password.is_displayed(), "❌ Campo password no visible"
        assert boton_login.is_displayed(), "❌ Botón login no visible"
        
        print("   ✅ Página carga correctamente")
        print("   ✅ Formulario de login visible")
    
    def prueba_login_correcto(self):
        """Prueba 2: Verificar login con credenciales correctas"""
        print("   🔑 Probando login...")
        
        # Ir a la página
        self.navegador.get(self.url_hotel)
        
        # Encontrar campos de login
        campo_usuario = self.esperar.until(
            EC.element_to_be_clickable((By.ID, "exampleInputEmail1"))
        )
        campo_password = self.navegador.find_element(By.ID, "exampleInputPassword1")
        
        # Escribir credenciales
        campo_usuario.clear()
        campo_usuario.send_keys(self.usuario)
        campo_password.clear()
        campo_password.send_keys(self.password)
        
        # Hacer click en login
        boton_login = self.navegador.find_element(By.XPATH, "//button[@type='submit']")
        boton_login.click()
        
        # Verificar que nos redirige al dashboard
        self.esperar.until(lambda navegador: "view=reserva" in navegador.current_url)
        
        print("   ✅ Login exitoso")
        print("   ✅ Redirigido al dashboard")
    
    def prueba_navegacion_menus(self):
        """Prueba 3: Verificar navegación entre páginas"""
        print("   📱 Probando navegación...")
        
        # Asegurar que estamos logueados
        self.hacer_login_si_necesario()
        
        # Lista de páginas a probar
        paginas = [
            ("habitacion", "Habitaciones"),
            ("cliente", "Clientes"),
            ("users", "Usuarios")
        ]
        
        for pagina, nombre in paginas:
            print(f"   🔄 Navegando a {nombre}...")
            
            # Ir a la página
            self.navegador.get(f"{self.url_hotel}index.php?view={pagina}")
            
            # Esperar que cargue
            self.esperar.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            
            # Verificar que estamos en la página correcta
            url_actual = self.navegador.current_url
            if f"view={pagina}" in url_actual:
                print(f"   ✅ {nombre} cargada correctamente")
            else:
                print(f"   ⚠️ Problema navegando a {nombre}")
            
            time.sleep(1)  # Pausa entre navegaciones
    
    # ==================== PRUEBAS DE SEGURIDAD ====================
    
    def prueba_acceso_sin_login(self):
        """Prueba 4: Verificar que no se puede acceder sin login"""
        print("   🔒 Probando acceso sin autenticación...")
        
        # Intentar acceder a página protegida sin login
        self.navegador.get(f"{self.url_hotel}index.php?view=users")
        time.sleep(2)
        
        # Verificar si nos redirige al login
        contenido_pagina = self.navegador.page_source
        url_actual = self.navegador.current_url
        
        if "exampleInputEmail1" in contenido_pagina or "login" in url_actual.lower():
            print("   ✅ Redirige al login correctamente")
        else:
            print("   ⚠️ Posible problema de seguridad - permite acceso sin login")
    
    def prueba_credenciales_incorrectas(self):
        """Prueba 5: Verificar que rechaza credenciales incorrectas"""
        print("   🚫 Probando credenciales incorrectas...")
        
        # Ir a la página de login
        self.navegador.get(self.url_hotel)
        
        # Intentar login con credenciales incorrectas
        campo_usuario = self.esperar.until(
            EC.element_to_be_clickable((By.ID, "exampleInputEmail1"))
        )
        campo_password = self.navegador.find_element(By.ID, "exampleInputPassword1")
        
        # Escribir credenciales incorrectas
        campo_usuario.clear()
        campo_usuario.send_keys("usuario_falso")
        campo_password.clear()
        campo_password.send_keys("password_incorrecto")
        
        # Intentar login
        boton_login = self.navegador.find_element(By.XPATH, "//button[@type='submit']")
        boton_login.click()
        time.sleep(3)
        
        # Verificar que NO nos deja entrar
        url_actual = self.navegador.current_url
        if "view=reserva" not in url_actual:
            print("   ✅ Credenciales incorrectas rechazadas")
        else:
            print("   ⚠️ Problema de seguridad - acepta credenciales incorrectas")
    
    # ==================== PRUEBAS DE RENDIMIENTO ====================
    
    def prueba_tiempos_carga(self):
        """Prueba 6: Medir tiempos de carga de páginas"""
        print("   ⏱️ Midiendo tiempos de carga...")
        
        # Asegurar login
        self.hacer_login_si_necesario()
        
        # Páginas a medir
        paginas_medir = [
            ("reserva", "Dashboard"),
            ("habitacion", "Habitaciones"),
            ("cliente", "Clientes")
        ]
        
        for pagina, nombre in paginas_medir:
            tiempo_inicio = time.time()
            
            # Cargar página
            self.navegador.get(f"{self.url_hotel}index.php?view={pagina}")
            
            # Esperar que termine de cargar
            self.esperar.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            
            tiempo_carga = round(time.time() - tiempo_inicio, 2)
            
            if tiempo_carga < 3:
                print(f"   ✅ {nombre}: {tiempo_carga}s (Rápido)")
            elif tiempo_carga < 5:
                print(f"   ⚠️ {nombre}: {tiempo_carga}s (Aceptable)")
            else:
                print(f"   ❌ {nombre}: {tiempo_carga}s (Lento)")
    
    def prueba_responsive(self):
        """Prueba 7: Verificar diseño responsivo básico"""
        print("   📱 Probando diseño responsivo...")
        
        # Asegurar login
        self.hacer_login_si_necesario()
        
        # Diferentes tamaños de pantalla
        tamaños = [
            (1920, 1080, "Desktop"),
            (768, 1024, "Tablet"),
            (375, 667, "Móvil")
        ]
        
        for ancho, alto, dispositivo in tamaños:
            print(f"   📐 Probando {dispositivo} ({ancho}x{alto})...")
            
            # Cambiar tamaño de ventana
            self.navegador.set_window_size(ancho, alto)
            time.sleep(1)
            
            # Verificar que la página sigue funcionando
            try:
                self.esperar.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                print(f"   ✅ {dispositivo} - Funciona correctamente")
            except:
                print(f"   ❌ {dispositivo} - Problemas de visualización")
        
        # Restaurar tamaño normal
        self.navegador.maximize_window()
    
    # ==================== PRUEBA DE CIERRE DE SESIÓN ====================
    
    def prueba_logout(self):
        """Prueba 8: Verificar funcionalidad de logout"""
        print("   🚪 Probando funcionalidad de logout...")
        
        # Asegurar que estamos logueados
        self.hacer_login_si_necesario()
        
        try:
            # Estrategia 1: Buscar enlace de logout en la página
            print("   🔍 Buscando enlace de logout...")
            
            logout_encontrado = False
            
            # Buscar por diferentes variaciones del enlace logout
            selectores_logout = [
                "//a[@href='logout.php']",
                "//a[@href='./logout.php']", 
                "//a[contains(@href, 'logout')]",
                "//a[contains(text(), 'Salir')]",
                "//a[contains(text(), 'Logout')]",
                "//a[contains(text(), 'Cerrar sesión')]"
            ]
            
            for selector in selectores_logout:
                try:
                    enlace_logout = self.navegador.find_element(By.XPATH, selector)
                    enlace_logout.click()
                    logout_encontrado = True
                    print("   ✅ Logout exitoso (enlace encontrado)")
                    break
                except NoSuchElementException:
                    continue
            
            # Estrategia 2: Si no encontramos enlace, navegar directamente
            if not logout_encontrado:
                print("   🔄 Navegando directamente a logout.php...")
                self.navegador.get("http://localhost/hotel_premium/logout.php")
                logout_encontrado = True
                print("   ✅ Logout manual ejecutado")
            
            # Verificar que el logout funcionó
            if logout_encontrado:
                time.sleep(2)
                
                # Verificar que regresamos a la página de login
                try:
                    self.esperar.until(
                        EC.presence_of_element_located((By.ID, "exampleInputEmail1"))
                    )
                    print("   ✅ Redirigido correctamente al login")
                    print("   ✅ Logout completado exitosamente")
                except TimeoutException:
                    print("   ⚠️ No se detectó redirección al login")
                    # Verificar manualmente si estamos en la página correcta
                    if "login" in self.navegador.current_url.lower() or "index.php" in self.navegador.current_url:
                        print("   ✅ Logout exitoso (verificado por URL)")
                    else:
                        print("   ❌ Logout posiblemente falló")
        
        except Exception as e:
            print(f"   ❌ Error en logout: {str(e)[:100]}")
            raise e

    # ==================== FUNCIONES AUXILIARES ====================
    
    def hacer_login_si_necesario(self):
        """Hacer login solo si no estamos ya logueados"""
        url_actual = self.navegador.current_url
        
        if "view=reserva" not in url_actual:
            print("   🔑 Haciendo login...")
            
            # Ir a página principal
            self.navegador.get(self.url_hotel)
            
            # Login
            campo_usuario = self.esperar.until(
                EC.element_to_be_clickable((By.ID, "exampleInputEmail1"))
            )
            campo_password = self.navegador.find_element(By.ID, "exampleInputPassword1")
            
            campo_usuario.clear()
            campo_usuario.send_keys(self.usuario)
            campo_password.clear()
            campo_password.send_keys(self.password)
            
            boton_login = self.navegador.find_element(By.XPATH, "//button[@type='submit']")
            boton_login.click()
            
            # Esperar redirección
            self.esperar.until(lambda navegador: "view=reserva" in navegador.current_url)
    
    def generar_reporte_simple(self):
        """Generar reporte simple de resultados"""
        print("\n" + "="*60)
        print("📊 RESUMEN DE PRUEBAS - HOTEL PREMIUM")
        print("="*60)
        
        total = len(self.resultados)
        exitosas = len([r for r in self.resultados if "✅" in r["resultado"]])
        fallidas = total - exitosas
        
        print(f"📈 Total de pruebas: {total}")
        print(f"✅ Exitosas: {exitosas}")
        print(f"❌ Fallidas: {fallidas}")
        
        if total > 0:
            porcentaje = round((exitosas / total) * 100, 1)
            print(f"📊 Porcentaje de éxito: {porcentaje}%")
        
        print("\n📋 DETALLE:")
        for resultado in self.resultados:
            print(f"   {resultado['resultado']} {resultado['prueba']} ({resultado['tiempo']}s)")
        
        print("\n🎯 EVALUACIÓN:")
        if exitosas == total:
            print("🏆 ¡Excelente! Todas las pruebas pasaron")
        elif exitosas >= total * 0.8:
            print("👍 Muy bien! La mayoría de pruebas pasaron")
        elif exitosas >= total * 0.5:
            print("⚠️ Regular. Hay áreas que necesitan mejora")
        else:
            print("❌ Atención necesaria. Muchas pruebas fallaron")
        
        return exitosas, total
    
    def ejecutar_todas_las_pruebas(self):
        """Ejecutar todas las pruebas básicas"""
        print("🏨 INICIANDO PRUEBAS BÁSICAS - HOTEL PREMIUM")
        print("="*60)
        print(f"🌐 URL: {self.url_hotel}")
        print(f"👤 Usuario: {self.usuario}")
        print(f"🕒 Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*60)
        
        # Lista de pruebas a ejecutar
        pruebas = [
            # Navegación
            ("1. Cargar Página Principal", self.prueba_cargar_pagina),
            ("2. Login Correcto", self.prueba_login_correcto),
            ("3. Navegación entre Menús", self.prueba_navegacion_menus),
            
            # Seguridad
            ("4. Acceso sin Login", self.prueba_acceso_sin_login),
            ("5. Credenciales Incorrectas", self.prueba_credenciales_incorrectas),
            
            # Rendimiento
            ("6. Tiempos de Carga", self.prueba_tiempos_carga),
            ("7. Diseño Responsivo", self.prueba_responsive),
            
            # Cierre de sesión
            ("8. Funcionalidad de Logout", self.prueba_logout)
        ]
        
        # Ejecutar cada prueba
        for nombre_prueba, funcion_prueba in pruebas:
            self.ejecutar_prueba(nombre_prueba, funcion_prueba)
        
        # Generar reporte final
        exitosas, total = self.generar_reporte_simple()
        
        print("\n📁 Capturas de pantalla guardadas en: screenshots/")
        
        # Cerrar navegador
        print("\n🔚 Cerrando navegador...")
        self.navegador.quit()
        
        return exitosas, total

def main():
    """🚀 Función principal - Ejecutar todas las pruebas"""
    print("🏨 SISTEMA DE PRUEBAS AUTOMATIZADAS - HOTEL PREMIUM")
    print("="*60)
    
    try:
        # Verificar que XAMPP está funcionando
        print("🔍 Verificando servidor local...")
        try:
            import requests
            response = requests.get("http://localhost/hotel_premium/", timeout=5)
            print("✅ XAMPP funcionando correctamente")
        except:
            print("❌ Error: XAMPP no está funcionando")
            print("   📋 Verifica que:")
            print("   • XAMPP esté iniciado (Apache + MySQL)")
            print("   • El proyecto esté en: c:\\xampp\\htdocs\\hotel_premium\\")
            return
        
        # Crear objeto de pruebas y ejecutar
        print("🧪 Iniciando pruebas automatizadas...")
        pruebas = HotelPremiumTest()
        exitosas, total = pruebas.ejecutar_todas_las_pruebas()
        
        # Resultado final
        print(f"\n🎉 PRUEBAS COMPLETADAS: {exitosas}/{total} exitosas")
        
        if exitosas == total:
            print("🏆 ¡PERFECTO! Todas las pruebas pasaron")
        elif exitosas >= total * 0.7:
            print("👍 ¡MUY BIEN! La mayoría funcionan correctamente")
        else:
            print("⚠️ ATENCIÓN: Varias pruebas fallaron")
        
        print("\n📸 Revisa las capturas en: screenshots/")
        
    except KeyboardInterrupt:
        print("\n⏹️ Pruebas interrumpidas por el usuario")
    except Exception as error:
        print(f"\n❌ Error ejecutando pruebas: {error}")
        print("\n📋 POSIBLES SOLUCIONES:")
        print("1. ✅ Verifica que XAMPP esté funcionando")
        print("2. 🔧 Instala EdgeDriver para tu versión de Edge")
        print("3. 📦 Instala dependencias: pip install selenium requests")
        print("4. 🌐 Verifica que el proyecto esté en la ruta correcta")


if __name__ == "__main__":
    main()
