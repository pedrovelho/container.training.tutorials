
import pytest

@pytest.fixture(scope="module", autouse=True)
def app(testenv):
    if testenv == 'local':
        cmd = ['../pypyenv/bin/python', '../main.py', '']
        p = subprocess.Popen(cmd, shell=True)
        yield
        p.terminate()
    else:
        pass