# Create
```
rmdir /S my_python27_env
C:\Python27\python.exe -m pip install virtualenv
C:\Python27\python.exe -m virtualenv my_python27_env
```

* If you want to use the one in the ZIP, remember to replaces paths that start with E:\, since it not working on relative paths.

# Activate
```
my_python27_env\Scripts\activate.bat
```


# Install & Run
```
C:\Python27\python.exe -m pip install -q --upgrade pip
C:\Python27\python.exe -m pip install --upgrade setuptools
C:\Python27\python.exe -m pip install -r requirements.txt

cd ZSI-master
C:\Python27\python.exe setup.py build
C:\Python27\python.exe setup.py install
cd ..

C:\Python27\python.exe server.py
```


# Create windows exe
Since pyinstaller.exe is installed in 'C:\Python27\Scripts', add to path (to make sure)

```
SET PATH=%PATH%;C:\Python27\Scripts
pyinstaller --clean server.spec
```

* Results will be in `dist\`

# Deactivate ()
While in venv mode, to remain in same cmd
```
deactivate
```