from cx_Freeze import setup, Executable

executables = [Executable("app.py")]

setup(
    name="Gerador QRCode",
    version="1.0",
    description="Criar QRCode",
    executables=executables
)

# comando apra criar o executavel: python setup.py build
