# 🏨 Pruebas Automatizadas - Sistema Hotel Premium

## 📋 Descripción

Suite de pruebas automatizadas desarrollada con **Selenium WebDriver** para el Sistema de Gestión Hotelera Premium. 
Diseñada específicamente para **Microsoft Edge versión 138.0.3351.83**.

## 🎯 Funcionalidades Probadas

### ✅ Pruebas Principales
- **Carga de Página Principal**: Verificación de elementos críticos del UI
- **Autenticación**: Login con credenciales válidas e inválidas
- **Navegación**: Acceso a diferentes módulos del sistema
- **Diseño Responsivo**: Pruebas en múltiples resoluciones
- **Formularios**: Acceso y funcionalidad de formularios principales
- **Seguridad**: Verificación de protección de rutas y validaciones
- **Logout**: Funcionalidad de cierre de sesión

### 📊 Métricas Evaluadas
- Tiempo de carga de páginas
- Tiempo de respuesta del login
- Accesibilidad de elementos UI
- Compatibilidad responsive
- Seguridad básica

## 🛠️ Requisitos del Sistema

### Software Necesario
- **Python 3.7+**
- **Microsoft Edge 138.0.3351.83**
- **XAMPP** (Apache + MySQL)
- **EdgeDriver** compatible

### Dependencias Python
```bash
selenium==4.15.2
requests==2.31.0
```

## 🚀 Instalación Rápida

### Opción 1: Instalación Automática
```bash
# 1. Ejecutar instalador automático
python install_edgedriver.py

# 2. Ejecutar pruebas
python simple_hotel_test.py
```

### Opción 2: Instalación Manual

#### 1. Instalar dependencias
```bash
pip install selenium requests
```

#### 2. Descargar EdgeDriver
1. Ve a: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
2. Descarga EdgeDriver para tu versión de Edge
3. Coloca `msedgedriver.exe` en la carpeta del proyecto

#### 3. Configurar XAMPP
- Inicia Apache en XAMPP Control Panel
- Verifica que el proyecto esté en: `c:\xampp\htdocs\hotel_premium\`
- Accede a: http://localhost/hotel_premium/

#### 4. Ejecutar pruebas
```bash
python simple_hotel_test.py
```

## 📁 Estructura del Proyecto

```
Tests/SeleniumTests/
├── 📄 simple_hotel_test.py          # Pruebas principales (RECOMENDADO)
├── 📄 HotelAutomationTest.py        # Suite completa de pruebas
├── 📄 install_edgedriver.py         # Instalador automático
├── 📄 config.py                     # Configuraciones
├── 📄 requirements.txt              # Dependencias Python
├── 📄 install.bat                   # Instalador Windows
├── 📄 run_tests.bat                 # Ejecutor Windows
├── 📁 screenshots/                  # Capturas de pantalla
└── 📁 reports/                      # Reportes generados
```

## 🔧 Configuración

### Credenciales de Prueba
- **Usuario**: `admin`
- **Contraseña**: `admin2018`

### URLs del Sistema
- **Base URL**: `http://localhost/hotel_premium/`
- **Login**: `http://localhost/hotel_premium/index.php`
- **Logout**: `http://localhost/hotel_premium/logout.php`

### Elementos Principales (XPath/ID)
```python
# Formulario de Login
username_field = "exampleInputEmail1"
password_field = "exampleInputPassword1"
submit_button = "//button[@type='submit']"

# Navegación
habitaciones = "//a[contains(@href, 'habitacion')]"
clientes = "//a[contains(@href, 'cliente')]"
usuarios = "//a[contains(@href, 'users')]"
```

## 🧪 Ejecución de Pruebas

### Modo Simple (Recomendado)
```bash
python simple_hotel_test.py
```

### Modo Completo
```bash
python HotelAutomationTest.py
```

### Ejecutor Windows
```bash
# Doble clic en:
run_tests.bat
```

## 📊 Reportes Generados

### 📄 JSON Report (`reports/test_report.json`)
```json
{
  "project": "Hotel Premium",
  "browser": "Microsoft Edge 138.0.3351.83",
  "summary": {
    "total_tests": 7,
    "passed": 6,
    "failed": 1,
    "success_rate": 85.7
  },
  "results": [...]
}
```

### 📄 Text Report (`reports/test_report.txt`)
- Resumen ejecutivo
- Detalle de cada prueba
- Métricas de rendimiento
- Evaluación del proyecto
- Recomendaciones técnicas

### 📸 Screenshots (`screenshots/`)
- `before_login.png`: Antes del login
- `after_login.png`: Después del login
- `error_*.png`: Capturas de errores

## 🎯 Evaluación del Proyecto

### ✅ Fortalezas Identificadas
- Sistema de autenticación funcional
- Estructura MVC bien organizada
- Interfaz web accesible
- Gestión de sesiones implementada
- Diseño responsivo básico

### ⚠️ Áreas de Mejora
- Optimización de rendimiento
- Validaciones adicionales en formularios
- Manejo de errores más robusto
- Implementación de pruebas unitarias
- Logs de auditoría

### 🔧 Recomendaciones Técnicas
1. **Rendimiento**: Implementar cache y optimizar consultas
2. **Seguridad**: Añadir validaciones JavaScript y 2FA
3. **UX**: Mejorar experiencia móvil y manejo de errores
4. **Testing**: Crear suite de pruebas unitarias más amplia
5. **Monitoreo**: Implementar métricas y logs detallados

## 🐛 Solución de Problemas

### Error: "EdgeDriver not found"
```bash
# Solución 1: Descarga automática
python install_edgedriver.py

# Solución 2: Descarga manual
# Ve a: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# Coloca msedgedriver.exe en la carpeta del proyecto
```

### Error: "XAMPP not running"
```bash
# Verifica:
1. XAMPP Control Panel - Apache iniciado
2. Proyecto en: c:\xampp\htdocs\hotel_premium\
3. Accesible en: http://localhost/hotel_premium/
```

### Error: "Login failed"
```bash
# Verifica credenciales:
Usuario: admin
Contraseña: admin2018

# Verifica base de datos:
- MySQL iniciado en XAMPP
- Tabla 'user' existe con usuario admin
```

### Error: "Element not found"
```bash
# Posibles causas:
1. Página no cargó completamente
2. Elemento cambió (verificar HTML)
3. JavaScript no ejecutó
4. Timeout insuficiente
```

## 📈 Métricas de Rendimiento

### ⏱️ Tiempos Esperados
- **Carga de página**: < 5 segundos
- **Login**: < 3 segundos
- **Navegación**: < 2 segundos

### 📱 Resoluciones Probadas
- **Desktop**: 1920x1080, 1366x768
- **Tablet**: 1024x768, 768x1024
- **Mobile**: 375x667, 667x375

## 🤝 Contribución

### Para añadir nuevas pruebas:
1. Edita `simple_hotel_test.py`
2. Añade método `test_##_nombre()`
3. Incluye en lista de `run_all_tests()`
4. Documenta en README

### Estructura de prueba:
```python
def test_##_nombre(self):
    """Descripción de la prueba"""
    # Preparación
    self.login_if_needed()
    
    # Ejecución
    self.driver.get(url)
    element = self.driver.find_element(By.ID, "elemento")
    
    # Verificación
    assert element.is_displayed()
    print("   ✅ Prueba exitosa")
```

## 📞 Soporte

### Información del Sistema
- **Proyecto**: Hotel Premium
- **Navegador**: Microsoft Edge 138.0.3351.83
- **Framework**: Selenium WebDriver 4.15.2
- **Lenguaje**: Python 3.7+

### Contacto
- **Desarrollado por**: GitHub Copilot
- **Fecha**: Julio 2025
- **Versión**: 1.0.0

---

## 🏆 Resultados Esperados

Con un sistema bien configurado, deberías obtener:
- **7/7 pruebas exitosas** ✅
- **Tasa de éxito: 100%** 🎯
- **Tiempo total: < 2 minutos** ⚡
- **Reportes detallados** 📊

¡Buena suerte con las pruebas! 🚀
