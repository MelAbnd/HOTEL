@echo off
title Hotel Premium - Pruebas Automatizadas

echo.
echo  ██╗  ██╗ ██████╗ ████████╗███████╗██╗         
echo  ██║  ██║██╔═══██╗╚══██╔══╝██╔════╝██║         
echo  ███████║██║   ██║   ██║   █████╗  ██║         
echo  ██╔══██║██║   ██║   ██║   ██╔══╝  ██║         
echo  ██║  ██║╚██████╔╝   ██║   ███████╗███████╗    
echo  ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝    
echo.
echo  ██████╗ ██████╗ ███████╗███╗   ███╗██╗██╗   ██╗███╗   ███╗
echo  ██╔══██╗██╔══██╗██╔════╝████╗ ████║██║██║   ██║████╗ ████║
echo  ██████╔╝██████╔╝█████╗  ██╔████╔██║██║██║   ██║██╔████╔██║
echo  ██╔═══╝ ██╔══██╗██╔══╝  ██║╚██╔╝██║██║██║   ██║██║╚██╔╝██║
echo  ██║     ██║  ██║███████╗██║ ╚═╝ ██║██║╚██████╔╝██║ ╚═╝ ██║
echo  ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚═╝ ╚═════╝ ╚═╝     ╚═╝
echo.
echo        SISTEMA DE PRUEBAS AUTOMATIZADAS v1.0
echo        Navegador: Microsoft Edge 138.0.3351.83
echo        Desarrollado por: GitHub Copilot - Julio 2025
echo.
echo ================================================================

:MENU
echo.
echo 🏠 MENU PRINCIPAL
echo ================================================================
echo.
echo  [1] 🔍 Verificar Sistema
echo  [2] 📦 Instalar Dependencias  
echo  [3] 🧪 Ejecutar Pruebas Simples (RECOMENDADO)
echo  [4] 🔬 Ejecutar Suite Completa
echo  [5] 📊 Ver Últimos Reportes
echo  [6] 🛠️ Diagnóstico de Problemas
echo  [7] 📖 Ayuda
echo  [0] ❌ Salir
echo.
echo ================================================================
set /p choice="Selecciona una opción (0-7): "

if "%choice%"=="1" goto VERIFY
if "%choice%"=="2" goto INSTALL
if "%choice%"=="3" goto SIMPLE_TEST
if "%choice%"=="4" goto FULL_TEST
if "%choice%"=="5" goto REPORTS
if "%choice%"=="6" goto DIAGNOSTICS
if "%choice%"=="7" goto HELP
if "%choice%"=="0" goto EXIT
goto MENU

:VERIFY
echo.
echo 🔍 VERIFICANDO SISTEMA...
echo ================================================================
python verify_system.py
pause
goto MENU

:INSTALL
echo.
echo 📦 INSTALANDO DEPENDENCIAS...
echo ================================================================
echo [1/3] Instalando librerías Python...
pip install selenium requests
echo.
echo [2/3] Descargando EdgeDriver...
python install_edgedriver.py
echo.
echo [3/3] Verificando instalación...
python verify_system.py
pause
goto MENU

:SIMPLE_TEST
echo.
echo 🧪 EJECUTANDO PRUEBAS SIMPLES...
echo ================================================================
echo Verificando requisitos...
python verify_system.py --quick
if %errorlevel% neq 0 (
    echo.
    echo ❌ El sistema no está listo. Ejecuta primero "Verificar Sistema"
    pause
    goto MENU
)
echo.
echo Iniciando pruebas automatizadas...
python simple_hotel_test.py
pause
goto MENU

:FULL_TEST
echo.
echo 🔬 EJECUTANDO SUITE COMPLETA...
echo ================================================================
echo ADVERTENCIA: Esta suite puede tomar varios minutos
echo.
set /p confirm="¿Continuar? (s/n): "
if /i not "%confirm%"=="s" goto MENU
echo.
python HotelAutomationTest.py
pause
goto MENU

:REPORTS
echo.
echo 📊 ÚLTIMOS REPORTES
echo ================================================================
if exist "reports\test_report.txt" (
    echo.
    echo 📄 Reporte más reciente:
    echo ================================================================
    type "reports\test_report.txt"
) else (
    echo.
    echo ℹ️  No hay reportes disponibles
    echo    Ejecuta las pruebas para generar reportes
)
echo.
if exist "reports\" (
    echo 📁 Archivos en reports\:
    dir /b reports\*.*
)
pause
goto MENU

:DIAGNOSTICS
echo.
echo 🛠️ DIAGNÓSTICO DE PROBLEMAS
echo ================================================================
echo.
echo 🔍 Verificaciones comunes:
echo.

echo [1/6] Python...
python --version 2>nul
if %errorlevel% neq 0 (
    echo ❌ Python no encontrado
    echo 💡 Descarga Python desde: https://python.org
) else (
    echo ✅ Python OK
)

echo.
echo [2/6] pip...
pip --version 2>nul
if %errorlevel% neq 0 (
    echo ❌ pip no encontrado
) else (
    echo ✅ pip OK
)

echo.
echo [3/6] Selenium...
python -c "import selenium; print('✅ Selenium OK')" 2>nul
if %errorlevel% neq 0 (
    echo ❌ Selenium no instalado
    echo 💡 Ejecuta: pip install selenium
)

echo.
echo [4/6] Microsoft Edge...
if exist "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" (
    echo ✅ Microsoft Edge encontrado
) else (
    echo ❌ Microsoft Edge no encontrado
    echo 💡 Descarga desde: https://microsoft.com/edge
)

echo.
echo [5/6] EdgeDriver...
if exist "msedgedriver.exe" (
    echo ✅ EdgeDriver encontrado en directorio actual
) else if exist "C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe" (
    echo ✅ EdgeDriver encontrado en Edge
) else (
    echo ❌ EdgeDriver no encontrado
    echo 💡 Ejecuta: python install_edgedriver.py
)

echo.
echo [6/6] Servidor Local...
python -c "import requests; requests.get('http://localhost/hotel_premium/', timeout=5); print('✅ Proyecto accesible')" 2>nul
if %errorlevel% neq 0 (
    echo ❌ Proyecto no accesible
    echo 💡 Verifica:
    echo    • XAMPP Apache iniciado
    echo    • Proyecto en: c:\xampp\htdocs\hotel_premium\
)

echo.
echo 📋 SOLUCIONES COMUNES:
echo ================================================================
echo • Error "No module named 'selenium'": pip install selenium
echo • Error "EdgeDriver not found": python install_edgedriver.py  
echo • Error "Connection refused": Iniciar Apache en XAMPP
echo • Error "Login failed": Verificar credenciales admin/admin2018
echo • Error "Element not found": Verificar que la página cargue completamente

pause
goto MENU

:HELP
echo.
echo 📖 AYUDA - HOTEL PREMIUM TESTS
echo ================================================================
echo.
echo 🎯 OBJETIVO:
echo    Ejecutar pruebas automatizadas del Sistema Hotel Premium
echo    usando Selenium WebDriver y Microsoft Edge
echo.
echo 🏗️ REQUISITOS:
echo    • Python 3.7+
echo    • Microsoft Edge 138.0.3351.83
echo    • XAMPP (Apache + MySQL)
echo    • EdgeDriver compatible
echo.
echo 🚀 INICIO RÁPIDO:
echo    1. Ejecutar "Instalar Dependencias"
echo    2. Verificar que XAMPP esté iniciado
echo    3. Ejecutar "Pruebas Simples"
echo.
echo 🔧 CONFIGURACIÓN:
echo    • URL Base: http://localhost/hotel_premium/
echo    • Usuario: admin
echo    • Contraseña: admin2018
echo.
echo 📁 ARCHIVOS IMPORTANTES:
echo    • simple_hotel_test.py: Pruebas principales
echo    • verify_system.py: Verificador del sistema
echo    • install_edgedriver.py: Instalador EdgeDriver
echo    • README.md: Documentación completa
echo.
echo 🐛 PROBLEMAS COMUNES:
echo    • EdgeDriver: Descargar desde Microsoft Developer
echo    • XAMPP: Verificar que Apache esté iniciado  
echo    • Permisos: Ejecutar como administrador si es necesario
echo.
echo 📞 SOPORTE:
echo    • Consulta README.md para detalles
echo    • Usa "Diagnóstico de Problemas" para debugging
echo    • Verifica logs en reports\
echo.
pause
goto MENU

:EXIT
echo.
echo 👋 ¡Gracias por usar Hotel Premium Tests!
echo.
echo 📊 Resumen de la sesión:
if exist "reports\test_report.json" (
    echo    ✅ Reportes generados en reports\
)
if exist "screenshots\" (
    echo    📸 Screenshots disponibles en screenshots\
)
echo.
echo 🔗 Enlaces útiles:
echo    • Documentación: README.md
echo    • EdgeDriver: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
echo    • Selenium: https://selenium.dev/documentation/
echo.
pause
exit

:ERROR
echo.
echo ❌ Error ejecutando el comando
echo Verifica que Python esté instalado y en el PATH
pause
goto MENU
