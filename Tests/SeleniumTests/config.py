"""
Configuración para las Pruebas Automatizadas
Sistema Hotel Premium
"""

# URLs del sistema
BASE_URL = "http://localhost/hotel_premium/"
LOGIN_URL = BASE_URL
LOGOUT_URL = BASE_URL + "logout.php"

# Credenciales de prueba
CREDENTIALS = {
    "admin": {
        "username": "admin",
        "password": "admin2018"
    }
}

# Configuración del navegador Edge
EDGE_CONFIG = {
    "driver_path": "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedgedriver.exe",
    "browser_path": "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
    "version": "138.0.3351.83"
}

# XPaths y selectores importantes
SELECTORS = {
    "login": {
        "username_field": "exampleInputEmail1",
        "password_field": "exampleInputPassword1",
        "submit_button": "//button[@type='submit']",
        "error_message": "//div[contains(@class, 'alert')]"
    },
    "navigation": {
        "habitaciones": "//a[contains(@href, 'habitacion')]",
        "clientes": "//a[contains(@href, 'cliente')]",
        "usuarios": "//a[contains(@href, 'users')]",
        "reservas": "//a[contains(@href, 'reserva')]",
        "configuracion": "//a[contains(@href, 'configuracion')]"
    },
    "forms": {
        "new_room_button": "//button[contains(text(), 'NUEVA HABITACIÓN')]",
        "new_client_button": "//button[contains(text(), 'NUEVO CLIENTE')]",
        "room_name_field": "nombre",
        "client_document_field": "documento",
        "client_name_field": "nombre"
    }
}

# Configuración de timeouts (en segundos)
TIMEOUTS = {
    "implicit_wait": 10,
    "explicit_wait": 20,
    "page_load": 30,
    "script_timeout": 30
}

# Configuración de capturas de pantalla
SCREENSHOT_CONFIG = {
    "directory": "Tests/SeleniumTests/screenshots/",
    "format": "png",
    "on_failure": True,
    "on_success": False
}

# Configuración de reportes
REPORT_CONFIG = {
    "directory": "Tests/SeleniumTests/reports/",
    "formats": ["json", "txt", "html"],
    "include_screenshots": True,
    "detailed_logs": True
}

# Métricas de rendimiento esperadas
PERFORMANCE_THRESHOLDS = {
    "page_load_time": 5.0,  # segundos
    "login_time": 3.0,      # segundos
    "navigation_time": 2.0   # segundos
}

# Resoluciones para pruebas de responsividad
RESPONSIVE_RESOLUTIONS = [
    {"width": 1920, "height": 1080, "name": "Full HD Desktop"},
    {"width": 1366, "height": 768, "name": "HD Laptop"},
    {"width": 1024, "height": 768, "name": "Tablet Landscape"},
    {"width": 768, "height": 1024, "name": "Tablet Portrait"},
    {"width": 375, "height": 667, "name": "Mobile Portrait"},
    {"width": 667, "height": 375, "name": "Mobile Landscape"}
]
