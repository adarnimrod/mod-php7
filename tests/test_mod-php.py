def test_mod_php(Command, Sudo):
    with Sudo():
        assert 'php' in Command('a2query -m').stdout


def test_phpinfo(Command):
    'PHP Version 5' in Command('curl http://localhost/phpinfo.php').stdout
