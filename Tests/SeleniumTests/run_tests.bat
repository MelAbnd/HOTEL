@echo off
echo ====================================================
echo EJECUTOR DE PRUEBAS AUTOMATIZADAS - HOTEL PREMIUM
echo ====================================================
echo.

echo Verificando servicios...

echo [1/3] Verificando XAMPP...
tasklist /FI "IMAGENAME eq httpd.exe" 2>NUL | find /I /N "httpd.exe">NUL
if "%ERRORLEVEL%"=="0" (
    echo ✓ Apache esta ejecutandose
) else (
    echo ✗ Apache no esta ejecutandose
    echo Por favor inicia XAMPP antes de ejecutar las pruebas
    pause
    exit /b 1
)

echo [2/3] Verificando MySQL...
tasklist /FI "IMAGENAME eq mysqld.exe" 2>NUL | find /I /N "mysqld.exe">NUL
if "%ERRORLEVEL%"=="0" (
    echo ✓ MySQL esta ejecutandose
) else (
    echo ⚠ MySQL no esta ejecutandose (puede ser opcional)
)

echo [3/3] Verificando proyecto...
if exist "..\..\index.php" (
    echo ✓ Proyecto Hotel Premium encontrado
) else (
    echo ✗ Proyecto no encontrado en la ruta esperada
    echo Verifica que el proyecto este en: c:\xampp\htdocs\hotel_premium\
    pause
    exit /b 1
)

echo.
echo ====================================================
echo INICIANDO PRUEBAS AUTOMATIZADAS...
echo ====================================================
echo.

python HotelAutomationTest.py

echo.
echo ====================================================
echo PRUEBAS COMPLETADAS
echo ====================================================
echo.
echo Los reportes se han generado en:
echo - reports\test_report.json
echo - reports\test_report.txt
echo.
echo Las capturas de pantalla estan en:
echo - screenshots\
echo.

pause
