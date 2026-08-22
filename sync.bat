@echo off
REM ============================================================
REM  Maison Valer - one-click publish to live site
REM  Double-click this file after publishing images in Sanity.
REM  It pulls from the backend, rebuilds the site, and pushes.
REM ============================================================
cd /d "%~dp0"

echo.
echo ==== Maison Valer : syncing from backend ====
echo.

python sanity_sync.py
if errorlevel 1 goto :error

echo.
echo ==== Building site ====
echo.
python build_site.py
if errorlevel 1 goto :error

echo.
echo ==== Publishing to live site ====
echo.
git add .
git commit -m "sync catalogue from Sanity"
if errorlevel 1 (
  echo.
  echo Nothing new to publish - the site is already up to date.
  echo.
  goto :done
)
git push
if errorlevel 1 goto :error

echo.
echo ============================================================
echo  DONE. Your changes will be live in about 1-2 minutes.
echo  Refresh the site with Ctrl+Shift+R to see them.
echo ============================================================
echo.
goto :done

:error
echo.
echo ------------------------------------------------------------
echo  Something went wrong above. Read the message, or send a
echo  screenshot for help. Nothing was forced.
echo ------------------------------------------------------------
echo.

:done
pause
