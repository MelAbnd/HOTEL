@echo off
echo ====================================================
echo INSTALADOR DE PRUEBAS AUTOMATIZADAS - HOTEL PREMIUM
echo ====================================================
echo.

echo [1/5] Verificando Python...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python no esta instalado. Por favor instala Python 3.8 o superior.
    pause
    exit /b 1
)

echo [2/5] Verificando pip...
pip --version
if %errorlevel% neq 0 (
    echo ERROR: pip no esta disponible.
    pause
    exit /b 1
)

echo [3/5] Instalando dependencias de Python...
pip install -r requirements.txt

echo [4/5] Verificando Microsoft Edge...
if exist "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" (
    echo Microsoft Edge encontrado.
) else (
    echo ADVERTENCIA: Microsoft Edge no encontrado en la ruta esperada.
    echo Por favor verifica la instalacion de Edge.
)

echo [5/5] Descargando EdgeDriver...
echo IMPORTANTE: Necesitas descargar EdgeDriver compatible con tu version de Edge
echo Version requerida: 138.0.3351.83
echo URL de descarga: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
echo.
echo Pasos para descargar EdgeDriver:
echo 1. Ve a: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
echo 2. Descarga la version 138.0.3351.83 para Windows x64
echo 3. Extrae msedgedriver.exe a: C:\Program Files (x86)\Microsoft\Edge\Application\
echo 4. O actualiza la ruta en config.py

echo.
echo ====================================================
echo INSTALACION COMPLETADA
echo ====================================================
echo.
echo Para ejecutar las pruebas:
echo 1. Asegurate de que XAMPP este ejecutandose
echo 2. Asegurate de que el proyecto este en: c:\xampp\htdocs\hotel_premium\
echo 3. Ejecuta: python HotelAutomationTest.py
echo.
echo NOTA: Si tienes problemas con EdgeDriver, verifica las rutas en config.py
echo.

pause
