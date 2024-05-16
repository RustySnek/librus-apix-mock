# Dependancy-less Static HTML server for [librus-apix](https://github.com/RustySnek/librus-apix) 🐍 testing purposes.
### Currently done on pretty low effort and has some gibberish data in it. Fine for testing otherwise.
```bash
# generate pages running scripts/
python scripts/generate_xyz.py

# run server on 8000
python server.py
# or
env MOCK_PORT=1234 python server.py
```
